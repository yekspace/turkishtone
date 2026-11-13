# Sade Türkçe Editör karşılaştırması

Dört brief değiştirilmeden kullanıldı. Önceki sade talimatların dördü, önceki koşunun kayıtlı özetleriyle bire bir eşleşti. Her iki koşulda aynı `gpt-5.4-mini-2026-03-17` sürümü, çıktı şeması, kelime sayacı ve kaynak denetimi kullanıldı.

Güncel talimat, başlık ve gövdedeki somut iddiaları brief’e bağlar. Reklam örneğinde “hafif” sözcüğünün yağmuru nitelediğini ve “kendi cebine katlanır” ifadesinin giysi cebine sığma veya ağırlık vaadi olmadığını açıklar. Yazmadan önce gövdeyi kaynakta bulunan bilgi birimlerine göre planlamayı ister.

## Kelime sınırı

İlk geçişte iki koşulda da önceki düzeltme isteği kullanıldı. Güncel koşulda yalnızca bir metin aralığa girdi. Aynı dört ilk taslak, ölçülen kelime farkını bildiren ve cümlelerin yeniden sayılmasını isteyen yeni düzeltme isteğiyle tekrar denendi. Bu istekte düşük akıl yürütme düzeyi kullanıldı. Son karşılaştırmada eski koşulun önceki düzeltmesi ve güncel koşulun yeni düzeltmesi yer alır. Her son metin, kendi ilk taslağından en fazla bir düzeltmeyle elde edildi.

| Tür | Hedef | Önceki sade son metin | Güncel sade ilk taslak | Önceki düzeltmeyle | Yeni düzeltmeyle |
|---|---:|---:|---:|---:|---:|
| Konuşma | 55–105 | 58 | 51 | 50 | 55 |
| Reklam | 35–75 | 37 | 29 | 36 | 35 |
| Kampanya | 40–85 | 45 | 38 | 38 | 41 |
| Basın bülteni | 65–125 | 62 | 50 | 63 | 62 |
| **Aralıkta** | | **3/4** | **0/4** | **1/4** | **3/4** |

Yeni düzeltme, aynı dört ilk taslakta uyumu 1/4’ten 3/4’e çıkardı. Son durumda iki sürüm de dört metnin üçünde hedef aralığa girdi. Basın bülteni iki sürümde de alt sınırın altında kaldı ve editör incelemesine işaretlendi.

## Kaynak denetimi

Önceki koşulda otomatik denetim iki bulgu verdi. Reklamdaki “beklenmedik bir sağanakta” ifadesi, hafif yağmur için tasarlanmış ürünü daha ağır yağışta öneriyor. Bültendeki “Programın amacı, çocuklara okuma alışkanlığını destekleyen etkinlik sunmak” cümlesi brief’te belirtilmeyen bir amaç ekliyor. Güncel koşulda otomatik denetim bulgu vermedi. Bu denetim, kör editör puanından ayrı tutuldu.

## Kör editör değerlendirmesi

Bağımsız model değerlendiricisi yalnızca brief’leri ve karıştırılmış A/B son metinlerini gördü. Puan sırası kaynak sadakati, üslup uyumu, doğallık, mecra ve amaç. Kelime sayımı editör puanına katılmadı. A/B etiketleri değerlendirme bittikten sonra açıldı.

| Tür | Önceki sade | Güncel sade | Tercih |
|---|---:|---:|---|
| Konuşma | A · 2/2/1/2 = 7 | B · 2/1/1/2 = 6 | Önceki |
| Reklam | B · 0/2/1/2 = 5 | A · 1/2/1/2 = 6 | Güncel |
| Kampanya | A · 2/2/1/2 = 7 | B · 2/2/2/2 = 8 | Güncel |
| Basın bülteni | A · 1/2/1/1 = 5 | B · 1/2/1/1 = 5 | Güncel, küçük farkla |
| **Toplam** | **24/32** | **25/32** | |

Kaynak sadakati puanı 5/8’den 6/8’e çıktı. Editör, güncel reklamda sağanak ve hacim iddialarının kalkmasını olumlu buldu. “Yol boyunca hazırlıklı kalmanızı sağlar” ifadesini ise brief’in desteklemediği genel bir güvence olarak işaretledi. Otomatik denetim bunu yakalamadı. Güncel bültende “düzenlenecek” sözcüğü planı kesinleştiriyor ve “başvuru takvimi paylaşılmadı” ifadesi kaynakta yalnızca başlangıç tarihinin bilinmediği bilgisinden daha geniş.

Güncel kampanyada “en fazla iki kitabınızı getirin” ve ders kitabı koşulu eylemi açık veriyor. Konuşmada önceki metnin dinleyiciye hitabı daha doğal bulundu. Karşılaştırma dört brief ve tek model değerlendiricisine dayanıyor. Nihai puanlar hem yazım talimatını hem de güncel düzeltme isteğini içeren iş akışını ölçüyor.
