# Kaynak denetimi için canlı kör karşılaştırma

Konuşma, reklam, kampanya ve basın bülteni için önceki dört brief ve sekiz son metin kullanıldı. Eski ve güncel denetim aynı başlık ve gövdeyi, aynı brief’i ve aynı `gpt-5.4-mini-2026-03-17` ayarını aldı. Yazılar sabit tutuldu. Karşılaştırma tablosunda iki koşuldan sekizer canlı denetim yer alır.

İlk değişiklik bültendeki kesinlik sorununu yakaladı, ancak dolaylı reklam güvencesini yine kaçırdı. Son sürümde süre veya kesinlik belirteci taşıyan cümleler modelin incelemesine ayrıca sunuldu. Bunlar tek başına hata kararı sayılmadı. Kör değerlendirici brief, yayın metni ve rastgele sıralanmış iki bulgu listesini gördü. Koşullar değerlendirme kaydedildikten sonra eşleştirildi.

| Metin | Önceki geçerli / yanlış veya yinelenen | Güncel geçerli / yanlış veya yinelenen | Editör gözlemi |
|---|---:|---:|---|
| 1 · Konuşma | 0 / 0 | 0 / 0 | Kaynak bilgileri korunuyor. |
| 2 · Konuşma | 0 / 0 | 0 / 0 | Kaynak bilgileri korunuyor. |
| 3 · Reklam | 1 / 0 | 1 / 1 | Sağanakta kullanım önerisi iki denetimde de yakalandı. Güncel denetim kapüşonun olağan işlevini de ayrı sorun saydı. |
| 4 · Reklam | 0 / 0 | 1 / 0 | Güncel denetim “yol boyunca hazırlıklı kalmanızı sağlar” ifadesindeki süreli güvenceyi yakaladı. |
| 5 · Kampanya | 0 / 0 | 0 / 0 | Katılım koşulları korunuyor. |
| 6 · Kampanya | 0 / 0 | 0 / 0 | Katılım koşulları korunuyor. |
| 7 · Basın bülteni | 0 / 0 | 1 / 0 | Güncel denetim brief’te belirtilmeyen kurumsal amacı yakaladı. |
| 8 · Basın bülteni | 0 / 0 | 1 / 1 | Başvuru başlangıç tarihinin açıklanmamasını tüm takvime genişletme sorunu yakalandı. Kesinlik bulgusunun gerekçesi yeterince ayrıştırılmadı. |
| **Toplam** | **1 / 0** | **4 / 2** | |

Reklamdaki “hazırlıklı kalmanızı sağlar” ifadesi, ayarlanabilir kapüşonun etkisini bütün yolculuğa yayıyor. Kör değerlendirici bulguyu geçerli saydı ve “hazırlıklı” sözcüğünün yağmurluğu yanında bulundurma anlamında da okunabileceğini belirtti.

Bültende güncel denetim “düzenlenecek” ve “başlaması öngörülen” ifadelerini aynı alıntıya aldı. Kör değerlendirici, başlangıç tarihinin ihtiyatlı kaldığını ve gerekçenin hangi iddiadaki kesinlik değişimini kastettiğini yeterince açıklamadığını belirtti. “Düzenlenecek” sözcüğü etkinliğin gerçekleşmesini kendi cümlesinde kesinleştiriyor diye okunursa bu bulgu savunulabilir. Tabloda muhafazakâr sayım kullanıldı. Başvuru takvimi bulgusu geçerli bir kapsam farkı olsa da model bunu eksik koşul diye etiketledi.

Kör değerlendirme sekiz metin ve tek bağımsız model değerlendiricisine dayanıyor. Son talimat bu testte gözlenen hatalardan yararlanılarak geliştirildi. Bu karşılaştırma yeni metinlerdeki hata oranını ölçmez.

Ek canlı sınamada bir müze atölyesi için başlangıç tarihinin “öngörülüyor” ifadesini iki metinde de korudum. Denetim, atölyenin “düzenlenmesinin planlandığı” metinde bulgu vermedi. Başlık ve gövde “düzenleyecek” diye değiştirildiğinde iki yerdeki kesinlik artışını ayrı ayrı işaretledi. İki alıntı da eşleşti. Bunlar aynı iddianın iki yerde geçmesiydi.
