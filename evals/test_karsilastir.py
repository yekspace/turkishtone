"""Kelime sınırı ve API karşılaştırma aracının çevrimdışı kontrolleri."""

import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import karsilastir as eval_araci
import editor_api
from kelime_say import kelime_say
from kaynak_kontrolu import bulgulari_kontrol_et, denetim_istegi, inceleme_adaylari, kaynak_alintisini_coz


def api_yaniti(metin: str) -> dict:
    return {
        "id": "resp_test",
        "model": "test-model",
        "status": "completed",
        "output": [
            {"type": "reasoning"},
            {"type": "message", "content": [{
                "type": "output_text",
                "text": json.dumps({
                    "baslik": "Sayıma katılmayacak başlık",
                    "govde": metin,
                    "editor_notu": "Sayıma katılmayacak editör notu.",
                }),
            }]},
        ],
    }


class KarsilastirmaTesti(unittest.TestCase):
    def test_kaynak_alintisi_sirali_tam_cumlelerin_ozgun_araligini_korur(self):
        brief = "Metin hazır. Kapüşon ayarlanabilir. Süre belirtilmedi."
        self.assertEqual(kaynak_alintisini_coz("Metin hazır. Süre belirtilmedi.", brief), brief)
        ters = "Süre belirtilmedi. Metin hazır."
        self.assertEqual(kaynak_alintisini_coz(ters, brief), ters)
        uydurma = "Metin hazır. Süre iki saattir."
        self.assertEqual(kaynak_alintisini_coz(uydurma, brief), uydurma)
        eksik = "hazır. Süre belirtilmedi."
        self.assertEqual(kaynak_alintisini_coz(eksik, brief), eksik)
        yinelenen = f"{brief} Metin hazır."
        birlesik = "Metin hazır. Süre belirtilmedi."
        self.assertEqual(kaynak_alintisini_coz(birlesik, yinelenen), birlesik)

    def test_kesinlik_bulgularinda_iki_odak_ayri_kalir(self):
        brief = "Atölye planlanıyor. Cuma günü başlaması öngörülüyor."
        cikti = {"baslik": "Atölye", "govde": "Atölye düzenlenecek. Cuma günü başlayacak."}
        bulgular = [
            {"kategori": "degisen_kesinlik", "odak": "etkinligin_gerceklesmesi",
             "kaynak_alintisi": "Atölye planlanıyor.", "metin_alintisi": "Atölye düzenlenecek.",
             "aciklama": "Plan kesinleşmiş gibi."},
            {"kategori": "degisen_kesinlik", "odak": "baslangic_tarihi",
             "kaynak_alintisi": "Cuma günü başlaması öngörülüyor.",
             "metin_alintisi": "Cuma günü başlayacak.", "aciklama": "Tahmin kesin tarih olmuş."},
        ]
        sonuc = bulgulari_kontrol_et({"bulgular": bulgular}, brief, cikti)
        self.assertEqual([b["odak"] for b in sonuc], ["etkinligin_gerceklesmesi", "baslangic_tarihi"])
        self.assertTrue(all(b["alinti_eslesti"] for b in sonuc))

    def test_kaynak_denetimi_adaylari_baglami_ve_tam_cumleyi_korur(self):
        brief = "Reklam metni yaz. Askısı ayarlanabilir. Tanıtımın açılması planlanıyor."
        cikti = {"baslik": "Tanıtım açılacak", "govde":
                 "Askıyı ayarlayabilirsiniz. Gün boyu konfor sağlar. Açılışın yapılacağı öngörülüyor."}
        self.assertEqual(inceleme_adaylari(brief, cikti),
                         ["Tanıtım açılacak", "Gün boyu konfor sağlar."])
        istek = denetim_istegi("test-model", brief, cikti)
        self.assertEqual(json.loads(istek["input"])["govde"], cikti["govde"])

    def test_kapsam_adaylari_tur_ipucu_olmadan_denetime_gider(self):
        brief = "İçerik taslağı. Kapağı vidalıdır. Kayıt yöntemi henüz açıklanmadı."
        cikti = {"baslik": "Mağaza raflarına uygundur",
                 "govde": "Kapağı vidalıdır. Kayıt yöntemi açıklanmadı. Kurum diğer bilgileri de yayımlamadı."}
        veri = json.loads(denetim_istegi("test-model", brief, cikti)["input"])
        self.assertEqual(veri["inceleme_adaylari"], [
            "Mağaza raflarına uygundur",
            "Kayıt yöntemi açıklanmadı.",
            "Kurum diğer bilgileri de yayımlamadı.",
        ])
        self.assertEqual(veri["brief"], brief)
        self.assertEqual(veri["govde"], cikti["govde"])

    def test_odakli_duzeltme_olculen_acigi_ve_briefi_gonderir(self):
        brief = {"input": "Atölye ücretsiz.", "alt": 15, "ust": 25}
        ilk = {"kelime": 8, "cikti": {"baslik": "Atölye", "govde": "Taslak", "editor_notu": ""}}
        istek = eval_araci.duzeltme_istegi("test-model", brief, ilk, "Talimat", "low")
        self.assertIn("alt sınırdan 7 kelime kısa", istek["input"])
        self.assertIn(brief["input"], istek["input"])
        self.assertEqual(istek["reasoning"], {"effort": "low"})
        self.assertNotIn("reasoning", eval_araci.duzeltme_istegi("test-model", brief, ilk, "Talimat"))

    def test_varsayilan_yalnizca_cekirdegi_yukler(self):
        varsayilan = eval_araci.talimatlari_oku()
        self.assertEqual(varsayilan, eval_araci.oku(eval_araci.ROOT / "SKILL.md").split("---", 2)[2].strip())
        secili = eval_araci.talimatlari_oku("Basın bülteni", soz_varligi=True)
        self.assertIn("## Basın bülteni\n", secili)
        self.assertIn("# Söz varlığı ve bağlama göre sözcük seçimi", secili)
        self.assertNotIn("# Üslup profilleri", secili)

    def test_yeni_turler_kendi_rehber_bolumunu_yukler(self):
        self.assertEqual(tuple(eval_araci.briefleri_oku(True)), eval_araci.YENI_TURLER)
        talimat = eval_araci.talimatlari_oku("Seslendirme")
        self.assertIn("## Seslendirme metni", talimat)
        self.assertNotIn("## Sosyal medya", talimat)

    def test_kaynak_kontrolu_kaniti_metne_gore_denetler(self):
        brief = "Etkinlik planlanıyor. Yağmur yağarsa iptal edilecek."
        cikti = {"baslik": "Duyuru", "govde": "Etkinlik yapılacak. Giriş 100 lira.",
                 "editor_notu": "Dahili not"}
        denetim = {"bulgular": [
            {"kategori": "degisen_kesinlik", "kaynak_alintisi": "Etkinlik planlanıyor.",
             "metin_alintisi": "Etkinlik yapılacak.", "aciklama": "Plan kesinleşmiş."},
            {"kategori": "atlanan_kosul", "kaynak_alintisi": "Yağmur yağarsa iptal edilecek.",
             "metin_alintisi": "", "aciklama": "İptal koşulu eksik."},
            {"kategori": "uydurulan_iddia", "kaynak_alintisi": "",
             "metin_alintisi": "Giriş 200 lira.", "aciklama": "Ücret verilmemiş."},
        ]}
        sonuc = bulgulari_kontrol_et(denetim, brief, cikti)
        self.assertEqual([b["alinti_eslesti"] for b in sonuc], [True, True, False])
        istek = denetim_istegi("test-model", brief, cikti)
        self.assertEqual(json.loads(istek["input"]),
                         {"brief": brief, "baslik": "Duyuru", "govde": cikti["govde"],
                          "inceleme_adaylari": ["Etkinlik yapılacak."]})

    def test_kaynak_kontrolu_dis_tirnagi_cozer_ve_ayni_alintiyi_eler(self):
        brief = "Yağmur yağarsa iptal edilecek."
        cikti = {"baslik": "Duyuru", "govde": "Yağmur yağarsa iptal edilecek. Giriş 100 lira."}
        denetim = {"bulgular": [
            {"kategori": "degisen_kesinlik", "kaynak_alintisi": brief,
             "metin_alintisi": brief, "aciklama": "Fark görünmüyor."},
            {"kategori": "uydurulan_iddia", "kaynak_alintisi": "",
             "metin_alintisi": "“Giriş 100 lira.”", "aciklama": "Ücret verilmemiş."},
        ]}
        bulgu, = bulgulari_kontrol_et(denetim, brief, cikti)
        self.assertTrue(bulgu["alinti_eslesti"])
        self.assertEqual(bulgu["metin_alintisi"], "Giriş 100 lira.")

    def test_turkce_govde_sayimi(self):
        self.assertEqual(kelime_say("Saat 10.00’da başlar. —\nÖn kayıt yok."), 6)
        self.assertEqual(kelime_say("… ---"), 0)

    def test_yarim_api_yaniti_reddedilir(self):
        yanit = {"status": "incomplete", "incomplete_details": {"reason": "max_output_tokens"}}
        with self.assertRaisesRegex(ValueError, "max_output_tokens"):
            eval_araci.yaniti_oku(yanit)

    def test_kosullar_ayni_briefle_calisir_ve_govdeyi_olcer(self):
        briefler = eval_araci.briefleri_oku()
        talimat = eval_araci.talimatlari_oku()
        yanitlar = [
            api_yaniti(" ".join(["örnek"] * sayi))
            for brief in briefler.values()
            for sayi in (brief["alt"], brief["ust"])
        ]
        with tempfile.TemporaryDirectory() as dizin:
            with (
                patch.object(eval_araci, "ROOT", Path(dizin)),
                patch.object(eval_araci, "briefleri_oku", return_value=briefler),
                patch.object(eval_araci, "talimatlari_oku", return_value=talimat),
                patch.object(editor_api, "api_cagir", side_effect=yanitlar) as api,
                patch.dict("os.environ", OPENAI_API_KEY="test"),
                patch("sys.argv", ["karsilastir.py", "--model", "test-model"]),
            ):
                self.assertEqual(eval_araci.main(), 0)
            dosya, = Path(dizin).glob("evals/runs/*/sonuclar.json")
            kosu = json.loads(dosya.read_text(encoding="utf-8"))
            self.assertTrue(kosu["tamamlandi"])
            self.assertTrue(dosya.with_name("karsilastirma.md").is_file())
        self.assertEqual(api.call_count, 6)
        self.assertTrue(all(r["aralikta"] and not r["duzeltildi"] for r in kosu["sonuclar"]))
        for i, brief in enumerate(briefler.values()):
            skillsiz = api.call_args_list[2 * i].args[1]
            skilli = api.call_args_list[2 * i + 1].args[1].copy()
            self.assertEqual(skilli.pop("instructions"), talimat)
            self.assertEqual(skillsiz, skilli)
            self.assertEqual(skillsiz["input"], brief["input"])

    def test_kota_hatasi_ilk_sonucu_silmez(self):
        briefler = eval_araci.briefleri_oku()
        with tempfile.TemporaryDirectory() as dizin:
            with (
                patch.object(eval_araci, "ROOT", Path(dizin)),
                patch.object(eval_araci, "briefleri_oku", return_value=briefler),
                patch.object(eval_araci, "talimatlari_oku", return_value="Skill talimatı"),
                patch.object(
                    editor_api, "api_cagir",
                    side_effect=[api_yaniti(" ".join(["örnek"] * 45)), RuntimeError("HTTP 429")],
                ) as api,
                patch.dict("os.environ", OPENAI_API_KEY="test"),
                patch("sys.argv", ["karsilastir.py", "--model", "test-model"]),
            ):
                self.assertEqual(eval_araci.main(), 1)
            dosya, = Path(dizin).glob("evals/runs/*/sonuclar.json")
            kosu = json.loads(dosya.read_text(encoding="utf-8"))
            self.assertTrue(dosya.with_name("01.json").is_file())
        self.assertEqual(api.call_count, 2)
        self.assertFalse(kosu["tamamlandi"])
        self.assertEqual(len(kosu["sonuclar"]), 1)
        self.assertEqual(kosu["hata"]["kosul"], "skill-li")

    def test_sinir_disi_taslak_bir_kez_duzeltilir(self):
        brief = {"input": "Etkinlik ücretsiz. Başlık ve gövde yaz.", "alt": 5, "ust": 8}
        with tempfile.TemporaryDirectory() as dizin:
            with (
                patch.object(eval_araci, "ROOT", Path(dizin)),
                patch.object(eval_araci, "briefleri_oku", return_value={"Haber": brief}),
                patch.object(eval_araci, "talimatlari_oku", return_value="Skill talimatı"),
                patch.object(
                    editor_api, "api_cagir",
                    side_effect=[api_yaniti("Etkinlik ücretsiz."), api_yaniti("Ücretsiz etkinlik."),
                                 api_yaniti(" ".join(["örnek"] * 9)),
                                 api_yaniti("Herkes bu etkinliğe ücretsiz olarak katılabilir.")],
                ) as api,
                patch.dict("os.environ", OPENAI_API_KEY="test"),
                patch("sys.argv", ["karsilastir.py", "--model", "test-model"]),
            ):
                self.assertEqual(eval_araci.main(), 0)
            dosya, = Path(dizin).glob("evals/runs/*/sonuclar.json")
            skillsiz, skilli = json.loads(dosya.read_text(encoding="utf-8"))["sonuclar"]
        self.assertEqual(api.call_count, 4)
        self.assertTrue(skillsiz["editor_incelemesi"])
        self.assertFalse(skilli["editor_incelemesi"])
        self.assertEqual(skilli["ilk_taslak"]["kelime"], 9)
        self.assertEqual(skilli["kelime"], 6)
        ikinci_istek = api.call_args_list[1].args[1]
        self.assertIn(brief["input"], ikinci_istek["input"])
        self.assertIn("Etkinlik ücretsiz.", ikinci_istek["input"])
        self.assertNotIn("instructions", ikinci_istek)
        self.assertEqual(api.call_args_list[3].args[1]["instructions"], "Skill talimatı")


if __name__ == "__main__":
    unittest.main()
