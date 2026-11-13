import io
import json
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import editor
import editor_api
from markdown_bolum import bolumu_sec


def yanit(icerik):
    return {"status": "completed", "output": [
        {"type": "message", "content": [{"type": "output_text", "text": json.dumps(icerik)}]}
    ]}


class EditorTesti(unittest.TestCase):
    def test_proje_dili_yazim_ve_duzeltmeye_gider_denetim_briefle_sinirli_kalir(self):
        brief = "Etkinlik için başvuru açıldı."
        proje_dili = "# Hitap\n\nSiz diye yaz. Kıyı Atölyesi adını koru."
        ilk = {"baslik": "Başvuru", "govde": "Başvurabilirsiniz.", "editor_notu": ""}
        son = {**ilk, "govde": "Etkinliğe katılmak için başvurabilirsiniz."}
        with tempfile.TemporaryDirectory() as dizin:
            kaynak = Path(dizin) / "brief.md"
            tercih = Path(dizin) / "proje.md"
            kaynak.write_text(brief, encoding="utf-8")
            tercih.write_text(proje_dili, encoding="utf-8-sig")
            with (patch.dict("os.environ", OPENAI_API_KEY="test"),
                  patch.object(editor_api, "api_cagir", side_effect=[
                      yanit(ilk), yanit(son), yanit({"bulgular": []}),
                  ]) as api, redirect_stdout(io.StringIO())):
                self.assertEqual(editor.main([
                    "--brief", str(kaynak), "--proje-dili", str(tercih),
                    "--kelime", "3", "5", "--kaynak-kontrolu",
                ]), 0)
        self.assertEqual(api.call_count, 3)
        for cagri in api.call_args_list[:2]:
            self.assertIn("Kıyı Atölyesi adını koru", cagri.args[1]["input"])
        denetim = json.loads(api.call_args_list[2].args[1]["input"])
        self.assertEqual(denetim["brief"], brief)
        self.assertNotIn("Kıyı Atölyesi", api.call_args_list[2].args[1]["input"])

    def test_bolum_revizyonu_komsulari_ve_satir_sonlarini_korur(self):
        once = "\ufeff# Dosya\r\n\r\n```md\r\n## Giriş\r\n```\r\n\r\nÖnceki paragraf.\r\n\r\n## Giriş ##\r\n\r\n"
        sonra = "\r\n\r\n## Sonuç\r\n\r\nSonraki paragraf.  \r\n"
        taslak = once + "Eski giriş.\r\n\r\n### Ayrıntı\r\n\r\nEski alt bölüm." + sonra
        cikti = {"baslik": "Model başlığı", "govde": "Yeni giriş.\n\n### Ayrıntı\n\nYeni alt bölüm.",
                 "editor_notu": ""}
        with tempfile.TemporaryDirectory() as dizin:
            dosya = Path(dizin) / "taslak.md"
            dosya.write_bytes(taslak.encode("utf-8"))
            cikis = io.StringIO()
            with (patch.dict("os.environ", OPENAI_API_KEY="test"),
                  patch.object(editor_api, "api_cagir", return_value=yanit(cikti)) as api,
                  redirect_stdout(cikis)):
                self.assertEqual(editor.main([
                    "--taslak", str(dosya), "--bolum", "Giriş", "--istek", "Girişi düzenle.",
                ]), 0)
            self.assertEqual(dosya.read_bytes(), taslak.encode("utf-8"))
        self.assertEqual(api.call_count, 1)
        girdi = api.call_args.args[1]["input"]
        self.assertIn("Önceki paragraf.", girdi)
        self.assertIn("Eski alt bölüm.", girdi)
        self.assertIn("## Sonuç", girdi)
        self.assertIn("Sonraki paragraf.", girdi)
        self.assertNotIn("```md", girdi)
        sonuc = json.loads(cikis.getvalue())
        self.assertEqual(sonuc["cikti"]["baslik"], "Giriş")
        self.assertEqual(sonuc["taslak_guncel"], once + cikti["govde"].replace("\n", "\r\n") + sonra)

    def test_bolum_birlesimi_komsu_basliklari_ve_kod_citini_gozetir(self):
        taslak = "Giriş\n-----\n\nEski paragraf.\n\nUzun sonuç\nbaşlığı\n------------\n\nKapanış."
        bolum = bolumu_sec(taslak, "Giriş")
        self.assertEqual(bolum.birlestir("Yeni paragraf."),
                         taslak.replace("Eski paragraf.", "Yeni paragraf."))
        for gecersiz in ("Yeni paragraf.\n\n## Ek başlık\nDışarı taşan metin.", "```\nAçık blok"):
            with self.subTest(govde=gecersiz), self.assertRaises(ValueError):
                bolum.birlestir(gecersiz)
        with self.assertRaisesRegex(ValueError, "birden fazla"):
            bolumu_sec("## Giriş\nBir.\n\n## Giriş\nİki.", "Giriş")

    def test_tek_duzeltme_kaynak_bulgu_ve_kelime_acigini_birlikte_isler(self):
        brief = "Kütüphane bir atölye düzenlemeyi planlıyor. 16 Mart öngörülüyor."
        ilk = {"baslik": "Atölye kesinleşti", "govde": "Etkinlik yapılacak.", "editor_notu": ""}
        son = {"baslik": "Kütüphane atölye planlıyor",
               "govde": "Kütüphane bir atölye düzenlemeyi planlıyor. Başlangıç için 16 Mart öngörülüyor.",
               "editor_notu": "Onay bekleniyor"}
        bulgu = {"kategori": "degisen_kesinlik", "odak": "etkinligin_gerceklesmesi",
                 "kaynak_alintisi": "düzenlemeyi planlıyor", "metin_alintisi": "Atölye kesinleşti",
                 "aciklama": "Plan kesinleşmiş gibi verilmiş."}
        with tempfile.TemporaryDirectory() as dizin:
            kaynak = Path(dizin) / "brief.md"
            kaynak.write_text(brief, encoding="utf-8-sig")
            cikis = io.StringIO()
            with (patch.dict("os.environ", OPENAI_API_KEY="test"),
                  patch.object(editor_api, "api_cagir", side_effect=[
                      yanit(ilk), yanit({"bulgular": [bulgu]}), yanit(son), yanit({"bulgular": []})
                  ]) as api, redirect_stdout(cikis)):
                self.assertEqual(editor.main([
                    "--model", "test", "--brief", str(kaynak), "--tur", "Basın bülteni",
                    "--kelime", "10", "15", "--kaynak-duzelt"
                ]), 0)
        self.assertEqual(api.call_count, 4)
        duzeltme = api.call_args_list[2].args[1]["input"]
        self.assertIn(bulgu["aciklama"], duzeltme)
        self.assertIn("10–15", duzeltme)
        self.assertIn(brief, duzeltme)
        sonuc = json.loads(cikis.getvalue())
        self.assertEqual(sonuc["cikti"], son)
        self.assertEqual(sonuc["kelime"], 10)
        self.assertTrue(sonuc["aralikta"])
        self.assertEqual(sonuc["kaynak_kontrolu"], [])
        self.assertFalse(sonuc["editor_incelemesi"])

    def test_kaynaksiz_revizyon_sayimi_gosterir_ve_taslagi_duzenler(self):
        with tempfile.TemporaryDirectory() as dizin:
            dosya = Path(dizin) / "taslak.md"
            dosya.write_text("## Eski başlık\n\nBir taslak.", encoding="utf-8")
            cikis = io.StringIO()
            with (patch.dict("os.environ", OPENAI_API_KEY="test"),
                  patch.object(editor_api, "api_cagir", return_value=yanit({
                      "baslik": "Yeni başlık", "govde": "Kısa bir gövde.", "editor_notu": ""
                  })) as api, redirect_stdout(cikis)):
                self.assertEqual(editor.main([
                    "--model", "test", "--taslak", str(dosya), "--istek", "Başlığı sadeleştir."
                ]), 0)
        self.assertEqual(api.call_count, 1)
        girdi = api.call_args.args[1]["input"]
        self.assertIn("Bir taslak.", girdi)
        self.assertIn("Başlığı sadeleştir.", girdi)
        sonuc = json.loads(cikis.getvalue())
        self.assertEqual(sonuc["kelime"], 3)
        self.assertIsNone(sonuc["aralikta"])
        self.assertIsNone(sonuc["kaynak_kontrolu"])

    def test_son_denetim_hatasinda_duzeltilen_metin_korunur(self):
        ilk = {"baslik": "Başlık", "govde": "Tek.", "editor_notu": ""}
        son = {**ilk, "govde": "Üç kelimelik gövde."}
        with patch.object(editor_api, "api_cagir", side_effect=[
            yanit(ilk), yanit({"bulgular": []}), yanit(son), RuntimeError("Denetim başarısız.")
        ]) as api:
            sonuc = editor.calistir(
                "test", "test-model", "Brief.", "İstek.", "Talimat.", 3, 5,
                kaynak_kontrolu=False, kaynak_duzelt=True
            )
        self.assertEqual(api.call_count, 4)
        self.assertEqual(sonuc["cikti"], son)
        self.assertEqual(sonuc["ilk_kaynak_kontrolu"], [])
        self.assertIsNone(sonuc["kaynak_kontrolu"])
        self.assertTrue(sonuc["editor_incelemesi"])
        self.assertEqual(sonuc["hatalar"][0]["asama"], "son_kaynak_kontrolu")

    def test_alintisi_eslesmeyen_bulgu_otomatik_duzeltilmez(self):
        taslak = {"baslik": "Atölye", "govde": "Atölye planlanıyor.", "editor_notu": ""}
        bulgu = {"kategori": "degisen_kesinlik", "odak": "etkinligin_gerceklesmesi",
                 "kaynak_alintisi": "planlanıyor", "metin_alintisi": "Atölye yapılacak.",
                 "aciklama": "Plan kesinleştirilmiş."}
        with patch.object(editor_api, "api_cagir", side_effect=[
            yanit(taslak), yanit({"bulgular": [bulgu]})
        ]) as api:
            sonuc = editor.calistir(
                "test", "test-model", "Atölye planlanıyor.", "İstek.", "Talimat.", None, None,
                kaynak_kontrolu=False, kaynak_duzelt=True
            )
        self.assertEqual(api.call_count, 2)
        self.assertFalse(sonuc["duzeltildi"])
        self.assertFalse(sonuc["kaynak_kontrolu"][0]["alinti_eslesti"])
        self.assertTrue(sonuc["editor_incelemesi"])
