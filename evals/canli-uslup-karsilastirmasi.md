# Canlı API ve kör editör karşılaştırması

Dört kurgusal brief, aynı `gpt-5.4-mini-2026-03-17` model sürümü ve aynı çıktı şemasıyla iki koşulda çalıştırıldı. Skill’li koşula Türkçe Editör, tür rehberi, üslup profilleri ve söz varlığı rehberi eklendi. Her iki koşulda da uygulama ilk gövdeyi ölçtü. Sınırı kaçıran beş taslak birer kez yeniden yazdırıldı. Sekiz ilk taslak ve beş düzeltme için toplam 13 canlı API yanıtı alındı.

Bağımsız değerlendirici yalnızca brief’leri ve her tür için ayrı ayrı karıştırılan A/B son metinlerini gördü. Her metne kaynak sadakati, üslup uyumu, doğallık, mecra ve amaç sırasıyla 0–2 puan verdi. Kelime sınırı ayrı ölçüldü. Koşullar değerlendirme tamamlandıktan sonra eşleştirildi.

| Tür | Metin A ve puanları | Metin B ve puanları | Editör tercihi | Hedef | Son gövde skillsiz / skill’li |
|---|---|---|---|---:|---:|
| Konuşma | Skill’li · 1 / 1 / 1 / 1 = **4** | Skillsiz · 1 / 2 / 2 / 2 = **7** | B, skillsiz | 55–105 | 56 / 49 |
| Reklam | Skillsiz · 2 / 2 / 1 / 2 = **7** | Skill’li · 1 / 2 / 2 / 2 = **7** | A, skillsiz | 35–75 | 40 / 36 |
| Kampanya | Skill’li · 2 / 1 / 1 / 2 = **6** | Skillsiz · 2 / 2 / 2 / 2 = **8** | B, skillsiz | 40–85 | 41 / 41 |
| Basın bülteni | Skill’li · 1 / 2 / 1 / 2 = **6** | Skillsiz · 1 / 2 / 1 / 2 = **6** | A, skill’li | 65–125 | 58 / 57 |

Puan toplamı skillsiz koşulda 28/32, skill’li koşulda 23/32. Reklam ve basın bülteninde puan eşitliğine rağmen değerlendirici kaynak sadakati açısından bir metni tercih etti. Skillsiz metin dört türün üçünde, skill’li metin birinde tercih edildi. Skillsiz üç, skill’li iki gövde kelime sınırını karşıladı.

- **Konuşma.** Skillsiz metnin “sergimize hoş geldiniz” girişi açılış anını ve hitabı kuruyor. Skill’li metindeki “ilk kez bir arada” bilgisi brief’te yok ve tıpkıbasım bilgisi tekrarlanıyor. Skillsiz metin “bugün” diyerek açılış anına uyuyor, ancak cumartesi bilgisini açıkça vermiyor.
- **Reklam.** Skill’li metin daha akıcı bulundu. “Yer kaplamadan” ifadesi kaynakta ölçülmemiş bir üstünlük bildiriyor, “yağmurlu günlerde” ifadesi hafif yağmur kapsamını gevşetiyor. Skillsiz metin kullanım anını ve katlanabilirlik faydasını somutlaştırıyor. Bazı ifadeleri akışı aksatıyor.
- **Kampanya.** İki metin de saat, yer, ücret, kayıt ve kitap koşullarını aktarıyor. Skillsiz metnin “Yanınızda … getirin” ve “Sizi bekliyoruz” çağrısı daha sıcak. Skill’li metin mekânı tekrarlıyor ve “belirtilen saatte” ifadesiyle resmileşiyor. Buna karşılık, kitap değişiminin nasıl gerçekleşeceğini daha açık söylüyor.
- **Basın bülteni.** Skill’li metin “öngörülüyor” ifadesiyle açılışın kesinleşmediğini koruyor. “Kurumlar … bekliyor” ifadesi brief’te yok. Skillsiz metin “düzenlenecek” diyerek planı kesinleştiriyor ve kaynaksız bir yönlendirme ekliyor. Her iki gövde de kısa kaldı.

Her türde tek brief ve tek bağımsız model değerlendiricisi kullanıldı. Sonuç, üslup profilleri ve söz varlığı rehberiyle birlikte kullanılan skill’in tamamını karşılaştırır. Eklenen iki rehberin etkisini tek tek ölçmez.
