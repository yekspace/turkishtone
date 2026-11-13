<img src="assets/turkishtone-logo.png" alt="TurkishTone tırnaklı logosu" width="240">

# TurkishTone

**An Agent Skill for natural Turkish writing, editing, and localization in Codex and Claude.**

Draft from a brief or revise an existing text while preserving the author’s voice and source facts. TurkishTone includes Turkish usage guides and a template for project-specific tone and terminology.

TurkishTone, Türkiye Türkçesiyle doğal ve özgün metin yazmak, düzenlemek ve yerelleştirmek için bir Agent Skill. Sözcükleri anlamına ve çağrışımına göre seçer. Cümlelerin ritmini metnin türüne ve yazarın sesine uyarlar. Haber, rehber, ürün içeriği, makale, konuşma, seslendirme, sosyal medya, reklam, kampanya ve basın bülteni için ayrı yazım ölçütleri sunar. [Türe göre yazım](references/icerik-turleri.md) · [Söz varlığı](references/soz-varligi.md)

## Install / Kurulum

Download `turkishtone.zip` from **Releases**. For Codex or Claude Code, extract it and copy the `turkishtone` folder to one of the paths below. For Claude chat, upload the ZIP under **Customize → Skills → + → Create skill → Upload a skill** and enable it. [Agent Skills specification](https://agentskills.io/specification) · [Claude chat setup](https://support.claude.com/en/articles/12512180-use-skills-in-claude)

**Releases** bölümünden `turkishtone.zip` dosyasını indir. Codex veya Claude Code için arşivi açıp içindeki `turkishtone` klasörünü aşağıdaki konumlardan birine kopyala. Depoyu indirdiysen `SKILL.md` ve yanındaki klasörleri `turkishtone` adlı klasöre koy. `~` kullanıcı klasörünü gösterir.

| Platform | Project / Proje | User / Kullanıcı | Invoke / Çağrı |
|---|---|---|---|
| Codex | `.agents/skills/turkishtone` | `~/.agents/skills/turkishtone` | `$turkishtone` |
| Claude Code | `.claude/skills/turkishtone` | `~/.claude/skills/turkishtone` | `/turkishtone` |

Skill’i doğrudan çağırmak için tablodaki ifadeyi isteğinin başına ekle. İki uygulama da uygun bir yazım isteğinde skill’i kendiliğinden seçebilir. [Codex skill belgeleri](https://learn.chatgpt.com/docs/build-skills) · [Claude Code skill belgeleri](https://code.claude.com/docs/en/skills)

### Claude sohbetine kurulum

Claude’da **Customize → Skills → + → Create skill → Upload a skill** yolunu izle. `turkishtone.zip` dosyasını olduğu gibi yükle ve skill’i etkinleştir. Ardından “TurkishTone’u kullanarak…” diye başlayabilirsin. Codex ve Claude sohbetlerinde yazım ve revizyon için ayrı bir OpenAI API anahtarı gerekmez. [Claude yükleme adımları](https://support.claude.com/en/articles/12512180-use-skills-in-claude)

### Örnek istek

> Bu duyuru metnini mahalle haber sitesi için 60–80 kelimelik bir habere dönüştür. Sınır gövde için. Tarihi, kayıt koşulunu ve verilen özel adları koru. Eksik yer bilgisini editör notuna yaz.

Brief’te okuru, yayın türünü, yanıtlanacak soruyu, kaynak notlarını ve varsa uzunluk sınırını belirt. Marka sesi için beğendiğin bir örnek, tekrarları azaltmak için benzer eski yayınları ekleyebilirsin. [Üç örnek brief](evals/briefler.md)

Kaynak vermeden de yazım isteği gönderebilirsin. “Yağmurdan sonra boş bir vapur iskelesinde geçen iki paragraflık kısa bir öykü yaz” doğrudan üretim isteğidir. Genel açıklama, slogan, taslak ve başka yaratıcı işlerde de konu, tür ve ton yeterli olabilir. Güncel veya doğrulama gerektiren olgular kullanılacaksa bunların kaynağını kontrol et.

Projeye özel hitap, terim ve ad tercihleri için [proje dili şablonunu](templates/proje-dili.md) doldur. Dosyayı sohbete ekle veya proje içindeki yolunu belirt ve yazarken uygulamasını iste.

## OpenAI API’de kullan

`scripts/editor.py`, sohbet dışında ve kendi uygulamanda kullanabileceğin isteğe bağlı bir komuttur. Metin üretimi, revizyon ve kaynak denetimi için OpenAI Responses API’yi kullanır. Python 3.10 veya üstüyle `OPENAI_API_KEY` ortam değişkenini ayarla. Paket klasöründe kendi UTF-8 brief’inden metin üretmek için şu komutu çalıştır.

```sh
python scripts/editor.py --brief brief.md --tur "Basın bülteni" --kelime 60 80 --kaynak-kontrolu
```

Aynı komuta taslak ve düzenleme isteği eklediğinde mevcut metin revize edilir.

```sh
python scripts/editor.py --brief brief.md --taslak taslak.md --istek "Başlığı kaynağa göre düzelt ve tekrarları çıkar." --tur "Basın bülteni" --kelime 60 80 --kaynak-duzelt
```

Kaynağa bağlı olmayan bir yazım isteğini de brief dosyasına koyabilirsin. Kaynaksız revizyonda `--taslak` ve `--istek` yeterlidir. Kaynak denetimini kullanmak için olguları içeren bir `--brief` dosyası ver. `--tur` seçtiğinde komut ilgili rehberi yükler. `--model` ile varsayılan model kimliğini değiştirebilirsin.

Brief’te istediğin sesi somut tarif edebilirsin. Örneğin “Birinci tekil kişiyle yaz. Sıcak ve ölçülü bir dil kullan. Duyguyu küçük hareketlerden sezdir.” Üslup ve bölüm akışı rehberini `--uslup-profili`, sözcük seçimi rehberini `--soz-varligi` ile ekleyebilirsin. `--dil-bilgisi` cümle, bağlaç ve soru rehberinin yanı sıra anlam ve anlatım denetimi rehberini de yükler. Bu seçenekleri birlikte kullanabilirsin.

### Proje dilini yeniden kullan

[Proje dili şablonunu](templates/proje-dili.md) kopyala. Hitabı, terimleri, korunacak adları ve üslup örneklerini kendi projen için düzenle. Komut dosyayı hem yazım hem revizyon sırasında kullanır. Bu işe özel hitap ve terim tercihlerini brief’te veya `--istek` ile belirtebilirsin.

```sh
python scripts/editor.py --brief brief.md --proje-dili proje-dili.md --tur "Yerelleştirme"
```

Çeviri veya uyarlama için `--tur "Yerelleştirme"`, karakter konuşmaları için `--tur "Diyalog"`, sesli okunacak metinler için `--tur "Seslendirme"` ilgili rehberi yükler. Çevrilecek metni brief’e ya da düzenlenecek taslağa koy.

### Bir bölümü düzenle

Markdown taslağındaki başlığı `#` işaretleri olmadan, metinde geçtiği biçimiyle yaz. Seçilen başlık taslakta bir kez geçmeli ve altında düzenlenecek metin bulunmalı.

```sh
python scripts/editor.py --taslak taslak.md --bolum "Giriş" --istek "İlk paragrafı kısalt ve son cümleyi sonraki bölüme bağla." --proje-dili proje-dili.md
```

`cikti` seçilen bölümü, `taslak_guncel` birleştirilmiş Markdown metnini verir. Başlık ve komşu bölümler olduğu gibi korunur. Sayım ve varsa kaynak denetimi seçilen bölüme uygulanır. Bu kullanımda kaynak denetimi için brief’e bölümün ele alması gereken olguları yaz.

Komut standart çıktıya JSON yazar. `cikti` alanında başlık, gövde ve editör notu, `kelime` alanında son gövdenin sayımı bulunur. `--kelime ALT UST` verirsen `aralikta` sonucu da hesaplanır. `kaynak_kontrolu` son metindeki bulguları gösterir. Denetim kapalıysa alan `null`, denetim bulgu üretmediyse boş listedir. Başlık ve editör notu sayılmaz.

`--kaynak-kontrolu` yalnızca son metni denetler. `--kaynak-duzelt` seçeneği ilk metni de denetler. Alıntı eşleşmesi doğrulanan bulgular ve varsa kelime sınırı sapması aynı ek revizyonda ele alınır. Komut yeni metni yeniden sayar ve denetler. Bu akış en fazla dört API çağrısı yapar. Kalan bulgular veya sınır sapması `editor_incelemesi` alanını etkinleştirir. İlk metin üretildikten sonra bir API adımı aksarsa eldeki metin JSON çıktısında korunur, sorun `hatalar` alanına yazılır ve komut sıfırdan farklı bir kodla çıkar.

### Kendi uygulamana bağla

Responses API’de `instructions` alanına `SKILL.md` gövdesini, `input` alanına yazım isteğini veya brief’i ver. Değerlendirme aracındaki `talimatlari_oku()` yalnızca çekirdeği yükler. Brief’in türü belliyse `talimatlari_oku(tur)` ilgili tür rehberini ekler. Dil bilgisi ve anlatım denetimi, ayrıntılı ton veya dönem dili gerekiyorsa sırasıyla `dil_bilgisi=True`, `uslup_profili=True` veya `soz_varligi=True` seç. Yerel Markdown bağlantılarını uygulaman çözmeli. Başlık, gövde ve editör notunu ayrı alanlarda almak için Structured Outputs kullanılabilir. [Responses API](https://developers.openai.com/api/reference/resources/responses/methods/create) · [Structured Outputs](https://developers.openai.com/api/docs/guides/structured-outputs)

Sözcük seçimi, dönem dili veya marka sesi önemliyse söz varlığı rehberini de ekle. `talimatlari_oku("Konuşma metni", soz_varligi=True, uslup_profili=True)` konuşma bölümünü, söz varlığını ve üslup profillerini birlikte yükler. Brief’te dinleyiciyi, vesileyi, süreyi, tonu ve aynen kalacak ad veya terimleri belirt. “Anma konuşması, ölçülü ve sıcak bir hitap, ‘istiklal’ terimini koru” gibi bir tarif yaz. [Üslup profilleri](references/uslup-profilleri.md)

Uygulamada kesin uzunluk sınırı varsa son gövdeyi sunucuda ölç. Bu deponun sayacı, boşlukla ayrılan ve en az bir harf veya rakam içeren düz metin parçalarını sayar. Başlık ve editör notunu ölçüme verme. Yayın sisteminin kendi sayım kuralı varsa onu kullan.

```sh
python scripts/kelime_say.py --min 45 --max 75 govde.txt
```

Komut kelime sayısını yazdırır. Aralık içindeyse çıkış kodu `0`, dışındaysa `1`, girdi geçersizse `2` döner. Dosya verilmezse UTF-8 metni standart girdiden okur.

`scripts/govde_dogrula.py` içindeki `olc()` ve `duzeltme_girdisi()` işlevlerini API uygulamana alabilirsin. İlk taslağı ölç. Sınır dışındaysa orijinal brief’i, taslağı, gerçek kelime sayısını ve aralığı içeren tek bir düzeltme isteği gönder. Aynı modeli, çıktı şemasını ve başlangıç talimatlarını kullan. Yeni gövdeyi tekrar ölç. Sınırı hâlâ kaçırıyorsa sonucu editör incelemesine işaretle. Kaynak sadakatini ayrıca kontrol et. Kelime sayacı yalnızca uzunluğu doğrular.

## Karşılaştırmayı çalıştır

Arşivdeki karşılaştırmalar, geliştirme sırasında kullanılan farklı talimat sürümlerini içerir. Önceki talimatlar ve raporlar o dönemdeki Türkçe Editör adını taşır.

Python 3.10 veya üstü yeterli. Canlı çalışma için `OPENAI_API_KEY` ortam değişkeni ve seçilen modele erişimi olan bir API projesi gerekir. Model kimliği sabitlenirse sonraki denemelerde aynı model sürümü kullanılabilir. Aşağıdaki örnek Responses API ve Structured Outputs destekleyen bir model sürümü kullanır. [Model bilgisi](https://developers.openai.com/api/docs/models/gpt-5.4-mini)

```sh
python evals/karsilastir.py --model gpt-5.4-mini-2026-03-17 --hazirlik
python evals/karsilastir.py --model gpt-5.4-mini-2026-03-17
```

İlk komut istekleri yerelde oluşturur. İkinci komut üç brief’i iki koşulda çalıştırır. Altı ilk taslağa, gerektiğinde en fazla altı düzeltme çağrısı eklenir. Model, brief, çıktı şeması, token sınırı ve düzeltme kuralı iki koşulda da aynıdır. Skill’li koşula yazım talimatları eklenir. Başarılı yanıtlar geldikçe `evals/runs/` altında kaydedilir. Koşu bittiğinde `sonuclar.json` ve `karsilastirma.md` ilk ve son metinleri, gövde sayımını ve inceleme durumunu gösterir. API bir aşamada hata verirse o ana kadar alınan taslaklar korunur.

| API yanıtı | Kontrol edilecek yer |
|---|---|
| `401` | API anahtarı ve ait olduğu proje |
| `403` veya `404` | Proje yetkisi ve model erişimi |
| `429` ve `credit_balance_exhausted` veya `insufficient_quota` | API kuruluşunun bakiyesi ve kullanım sınırı |
| `429` ve `rate_limit_exceeded` | İstek veya token hızı sınırı |

```sh
python -m unittest discover -s evals -v
```

Bu testler kelime sayımını ve karşılaştırma aracını temsili yanıtlarla ağ bağlantısı kurmadan denetler.

## Kaynak kontrolü

`--kaynak-kontrolu` seçeneği her son metnin başlığını ve gövdesini orijinal brief’le ayrı bir API çağrısında karşılaştırır. Aynı denetim iki koşula da uygulanır. Model, bulguyu üç türden biriyle işaretler.

| Bulgu | Örnek |
|---|---|
| `uydurulan_iddia` | Brief’te ücret yokken “Giriş 100 lira” yazılması |
| `atlanan_kosul` | Yağmurda iptal koşulunun metinde yer almaması |
| `degisen_kesinlik` | “Etkinlik planlanıyor” bilgisinin “Etkinlik yapılacak” diye verilmesi |

Bulgular, varsa kaynak ve metin alıntısıyla döner. Uygulama alıntıların ilgili metinde bire bir geçtiğini denetler ve bulgulu çıktıyı editör incelemesine işaretler. Model, brief’te aynı sırada ve birer kez geçen tam cümleleri aradaki metni atlayarak birleştirirse uygulama kaynaktaki kesintisiz bölümü gösterir. Alıntının eşleşmesi, modelin yorumunun doğru olduğunu tek başına göstermez. Boş bulgu listesi de yayıma uygunluk kararı değildir. Denetim brief’le sınırlıdır. Uygulama editör notunu, metnin üslubunu ve dış kaynakları ayrıca değerlendirebilir.

Reklam denetimi dolaylı performans, süre ve güvence vaatlerini de kapsar. Örneğin ayarlanabilir bir askı, tek başına gün boyu konfor vaadini desteklemez. Basın bülteninde planın statüsü başlık ve gövdedeki her ayrı iddiada denetlenir. Planı kesinleştiren bir cümle, başka bir cümledeki ihtiyatlı ifadeyle kendiliğinden düzelmiş sayılmaz. Uygulama süre, güvence veya kesinleşme belirteci içeren cümleleri ayrıca denetleyiciye gösterir. Model bu cümleleri tüm metin ve brief bağlamında değerlendirir.

Denetim, yayın mecrası veya hedef okur bilgisinden çıkarılan ürün uygunluğu iddialarını da inceler. Ayrıca açıklanmayan bilginin kapsamını korur. Örneğin kayıt yönteminin açıklanmadığını belirten brief, bütün başvuru bilgilerinin paylaşılmadığı iddiasına dayanak vermez. Bu tür kapsam kaymaları `uydurulan_iddia` olarak işaretlenir. [Kapsam denetimi örnekleri](evals/kaynak-kapsami-ornekleri.json)

Parçanın olağan işlevi belirtilen kullanım sınırı içinde kaldığında desteklenebilir. Örneğin hafif yağmurda başı örtmeye yardımcı olan kapüşon ile gün boyu kuru kalma vaadi farklı iddialardır. Etkinlik bulgularındaki `odak` alanı gerçekleşmenin kesinliğini `etkinligin_gerceklesmesi`, başlangıç gününün veya saatinin kesinliğini `baslangic_tarihi` olarak kaydeder. Diğer bulgularda `genel` kullanılır. [Sekiz yeni denetim örneği](evals/kaynak-ayrim-ornekleri.json)

[Kapüşon ve etkinlik kesinliği için canlı kör karşılaştırma](evals/canli-kaynak-ayrimi-rapor.md) · [Kör değerlendirme dosyası](evals/canli-kaynak-ayrimi-kor.md)

[Önceki kaynak denetimi karşılaştırması](evals/canli-kaynak-denetimi-rapor.md) · [Kör değerlendirme dosyası](evals/canli-kaynak-denetimi-kor.md)

```sh
python evals/karsilastir.py --model gpt-5.4-mini-2026-03-17 --yeni-turler --kaynak-kontrolu --denetim-caba low
```

Komut makale, duygusal içerik, seslendirme ve sosyal medya için sekiz ilk taslak ile sekiz kaynak denetimi çalıştırır. Gövde sınırını kaçıran ilk taslağa bir düzeltme çağrısı eklenir. `--denetim-caba low` yalnızca denetim isteğine uygulanır. Bu seçeneği, akıl yürütme düzeyini destekleyen modellerle kullan. [Dört tür için brief’ler](evals/yeni-tur-briefleri.md)

Canlı denemede sekiz son gövdenin altısı kelime aralığına girdi. Denetim kaynakta olmayan bir çalışma günü iddiasını buldu. Ayrıca üç bilinen hatanın yer aldığı kontrollü örnekte üç kategoriyi de işaretledi. Makale karşılaştırmasında kaçan bulgular da raporda gösteriliyor. [Canlı metinler ve editör karşılaştırması](evals/canli-yeni-turler.md)

Editör değerlendirmesinde önce kaynakla çelişen ve uydurulan iddiaları işaretle. Ardından gövde uzunluğunu, aynı bilginin kaç kez söylendiğini, okurun yanıtı nerede aldığını ve doğal Türkçe için hangi cümlelerin düzeltilmesi gerektiğini kaydet. Mümkünse metinleri A ve B olarak gösterip koşul etiketlerini inceleme sonrasına kadar gizle. Birden fazla koşuda sonuçları karşılaştır. Üç brief belirli hataları yakalamak için kullanılır. [Önceki Codex denemesi](evals/codex-karsilastirmasi.md)

Tek düzeltmeli canlı denemede altı ilk taslağın hiçbiri hedef aralıkta değildi. Bir düzeltme aralığa girdi ve diğer beşi editör incelemesine işaretlendi. [Canlı deneme ve 12 yanıt](evals/canli-duzeltme-denemesi.md)

Katkı gönderirken hatayı gösteren bir brief, model çıktısı ve beklediğin düzeltmeyi ekle. Düzeltme bir yazım kuralına dayanıyorsa TDK bağlantısını, üslup tercihi ise örnek cümleyi paylaş.

## Kör editör değerlendirmesi

Konuşma, reklam, kampanya ve basın bülteni için aynı brief’leri iki koşulda çalıştır. Komut, skill’li koşula ilgili tür, üslup ve söz varlığı rehberlerini yükler. [Dört üslup brief’i](evals/uslup-briefleri.md)

```sh
python evals/karsilastir.py --model gpt-5.4-mini-2026-03-17 --uslup-turleri
python evals/kor_degerlendirme.py evals/runs/KOSU/sonuclar.json --metin inceleme.md --anahtar kosullar.json
```

İkinci komut her çiftin A ve B sırasını ayrı ayrı karıştırır. Editöre yalnızca `inceleme.md` dosyasını ver. Editör brief’leri ve son metinleri kaynak sadakati, üslup uyumu, doğallık, mecra ve amaç açısından puanlar. Puanlama bittikten sonra koşulları aç. Kelime sınırını uygulamanın ölçtüğü sayımla ayrıca raporla.

[Kör okuma için A/B metinleri](evals/canli-uslup-metinleri.md) · [Puanlar, koşullar ve editör notları](evals/canli-uslup-karsilastirmasi.md)

Üslup profilleriyle söz varlığı rehberini ayrı ayrı ölçmek için aynı dört brief’i `--rehber-etkisi` seçeneğiyle çalıştır. Her brief için sade çekirdek ve tür rehberi, bunlara üslup profili eklenmiş sürüm, söz varlığı eklenmiş sürüm ve iki rehberin birlikte eklendiği sürüm üretilir. Aynı kör değerlendirme aracı dört metni A–D olarak karıştırır. Kelime kontrolü ve gerekirse tek düzeltme bütün koşullara aynı biçimde uygulanır.

[Dört koşulun kör editör sonuçları](evals/canli-rehber-karsilastirmasi.md) · [Kör okuma metinleri](evals/canli-rehber-metinleri.md) · [Canlı kaynaksız yazım örnekleri](evals/kaynaksiz-ornekler.md)

Aynı dört brief’le eski sürümü, sade çekirdeği ve skillsiz koşulu karşılaştırmak için `--surum-karsilastirmasi` kullan. Eski sürüm önceki ana talimatı ve o koşuda yüklenen rehberleri içerir. Sade sürüm çekirdek ve brief’in tür rehberini kullanır. Kör değerlendirme aracı bu koşuda A–C metinleri üretir.

[Üç sürümün kör editör sonuçları](evals/canli-surum-karsilastirmasi.md) · [Kör okuma metinleri](evals/canli-surum-metinleri.md)

Önceki sade sürümle güncel sade sürümü karşılaştırmak için `--sade-karsilastirmasi` kullan. Önceki talimatlar `evals/onceki-sade-talimatlar.json` dosyasında arşivlenir. İki koşul aynı brief’leri, kelime kontrolünü ve en fazla bir düzeltmeyi kullanır. `--kaynak-kontrolu` ile iki koşulun son metinleri aynı kaynak denetiminden geçer.

```sh
python evals/karsilastir.py --model gpt-5.4-mini-2026-03-17 --sade-karsilastirmasi --duzeltme-caba low --kaynak-kontrolu --denetim-caba low
```

`--duzeltme-caba low`, destekleyen modellerde düzeltme isteğine ölçülen kelime farkını ve cümleleri yeniden sayma adımını ekler. Bu karşılaştırmada yalnızca güncel sürüm bu düzeltmeyi kullanır. İlk taslak isteğinin ayarları iki koşulda aynıdır. Uygulama düzeltilen gövdeyi kendi sayacıyla ölçer. Kaynak denetimi ve kelime sınırı, editör incelemesi için ayrı gerekçelerdir.

[Sade sürümlerin kör editör sonuçları](evals/canli-sade-karsilastirmasi.md) · [Kör okuma metinleri](evals/canli-sade-metinleri.md)

## License / Lisans

TurkishTone is available under the [MIT License](LICENSE).
