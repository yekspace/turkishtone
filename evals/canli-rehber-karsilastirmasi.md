# Üslup profilleri ve söz varlığı için kör karşılaştırma

Önceki konuşma, reklam, kampanya ve basın bülteni brief’leri değiştirilmeden kullanıldı. Dört koşulun tamamında aynı sade çekirdek, tür rehberi, model sürümü, çıktı şeması ve kelime denetimi vardı. Koşullar yalnızca üslup profilleri ile söz varlığı rehberinin eklenip eklenmemesi bakımından ayrıldı. Model `gpt-5.4-mini-2026-03-17`. On altı ilk taslak ve on bir düzeltme için 27 canlı yanıt alındı.

Bağımsız model değerlendiricisi her brief’te rastgele sıralanmış A–D son metinlerini okudu. Kaynak sadakati, üslup uyumu, doğallık, mecra ve amaç için ayrı ayrı 0–2 puan verdi. Koşul adları puanlar kayda geçtikten sonra eşleştirildi. Kelime sınırı bu puana katılmadı.

| Tür | Çekirdek | + Üslup | + Söz varlığı | + İkisi |
|---|---:|---:|---:|---:|
| Konuşma | D · 8 | B · 7 | A · 6 | C · 7 |
| Reklam | D · 3 | A · 6 | C · 4 | B · 6 |
| Kampanya | B · 8 | D · 6 | A · 7 | C · 6 |
| Basın bülteni | B · 7 | C · 3 | D · 5 | A · 6 |
| **Toplam** | **26/32** | **22/32** | **22/32** | **25/32** |

| Ölçüt | Çekirdek | + Üslup | + Söz varlığı | + İkisi |
|---|---:|---:|---:|---:|
| Kaynak sadakati | 5/8 | 4/8 | 5/8 | 7/8 |
| Üslup uyumu | 7/8 | 7/8 | 6/8 | 7/8 |
| Doğallık | 7/8 | 4/8 | 5/8 | 4/8 |
| Mecra ve amaç | 7/8 | 7/8 | 6/8 | 7/8 |
| Hedef aralıkta son gövde | 3/4 | 3/4 | 2/4 | 2/4 |

Üslup tek başına reklamda çekirdeğin 3 puan üzerine çıktı. Konuşmada 1, kampanyada 2, bültende 4 puan geride kaldı. Söz varlığı tek başına reklamda 1 puan kazandırdı. Diğer üç türde toplam 5 puan kaybetti. Üslup rehberi, söz varlığı zaten eklendiğinde toplam puanı 3 artırdı. Söz varlığı rehberi de üslup zaten eklendiğinde toplamı 3 artırdı. Birlikte kullanım kaynak sadakatinde en yüksek puanı aldı.

- **Konuşma.** Çekirdeğin “Bugün, cumartesi günü” ifadesi metni açılış anına bağladı. Söz varlığı eklenen metin açılışta hazır olanlara “bu açılışa bekliyoruz” dedi. Dört metin de olguları korudu.
- **Reklam.** Üslup eklenen metinle iki rehberin kullanıldığı metin 6 puanda eşitlendi. Hiçbir sürüm kaynak sadakatinden tam puan almadı. “Yer kaplamadan”, “hafif yapısı” ve “beklenen kısa yağışlar” gibi ifadeler brief’te olmayan boyut, ağırlık veya yağış süresi iddiaları ekledi.
- **Kampanya.** Çekirdeğin “getirin, … değiş tokuş edin” ifadesi katılım eylemini açık anlattı. Üslup eklenen sürüm “raflar arasında” diyerek verilmeyen bir mekân ayrıntısı ekledi. İki rehberin kullanıldığı sürüm katılım çağrısını yineledi.
- **Basın bülteni.** Çekirdek akıcılık ve mecra uyumuyla toplamda öne geçti, ancak “başka ayrıntı paylaşmadı” diyerek brief’teki kapsamı aştı. İki rehberin kullanıldığı metin “öngörülen” sözcüğüyle planın kesinleşmediğini korudu. Üslup eklenen sürüm, “başvuru yapılması gerekiyor” diyerek brief’te açıkça verilmeyen bir usul çıkardı. Dört gövde de 65 kelimenin altında kaldı.

Bu deneme her koşulda dört brief, her hücrede tek çıktı ve tek model değerlendiricisi içeriyor. Önceki sürüm ve skillsiz koşul aynı koşuda yeniden çalıştırılmadı. Sonuçlar, bu sade çekirdeğe rehber eklemenin gözlenen etkisini gösteriyor. Sadeleştirmenin önceki sürüme göre etkisi ve tekrarlı üretimdeki değişkenlik ayrıca ölçülebilir.

## Kaynaksız yazım

İki ayrı canlı istekte bağlantı, belge veya örnek metin verilmedi. Sade çekirdek, boş bir vapur iskelesinde geçen kurmaca üretti. Çekirdek ve makale rehberi, zor bir konuşmadan önce not almanın ne işe yarayabileceğini iki paragrafta anlattı. Bu iki metin üretimin yapılabildiğini gösteriyor. Dört kaynaklı brief’in kör puanlarına dâhil edilmedi.
