# Kapüşon işlevi ve etkinlik kesinliği için canlı kör karşılaştırma

Sekiz yeni kurgusal brief ve bunlara karşılık gelen sekiz sabit yayın metni hazırlandı. Dört örnek reklam, dört örnek basın bülteni. Metinlerde doğru aktarımlar ve bilerek eklenen kaynak hataları var. Önceki ve güncel denetim her örneği aynı `gpt-5.4-mini-2026-03-17` modeliyle, düşük akıl yürütme düzeyinde inceledi. Üretim kalitesi yerine denetim davranışını ölçmek için yayın metinleri iki koşulda aynen kullanıldı.

Güncel sürüm kullanım sınırı içindeki olağan parça işlevini kabul ediyor. Bir başka cümlede kullanım sınırı aşıldıysa bulguyu o cümlede arıyor. Reklamdaki süre ve performans güvenceleri ayrı iddia olarak değerlendiriliyor. Bültenlerde etkinliğin gerçekleşmesi ve başlangıç zamanının kesinliği ayrı ayrı kontrol ediliyor. Güncel bulgu şeması bu ayrımı `odak` alanında saklıyor. Başlıkla gövdede tekrarlanan aynı iddia bir kez sayılıyor.

Kör değerlendirici brief, metin ve rastgele sıralanan iki bulgu listesini gördü. Sürüm adları, yanıt kimlikleri ve güncel şemanın ayırt edici odak alanı kör dosyada yer almadı. Gerekçeler ve alıntılar değerlendirmeye dâhil edildi.

## Kör değerlendirme sonuçları

| Ölçüm | Önceki denetim | Güncel denetim, ilk kör okuma | Güncel denetim, alıntı doğrulaması sonrası |
|---|---:|---:|---:|
| Geçerli, benzersiz bulgu | 6/6 | 5/6 | 6/6 |
| Temiz metinlerde bulgu | 0/3 | 0/3 | 0/3 |
| Yinelenen bulgu | 1 | 0 | 0 |
| Alıntısı doğrulanamadığı için kabul edilmeyen bulgu | 0 | 1 | 0 |

İki denetim de reklamda işe gidiş boyunca kuru kalma ve gün boyu yorulmadan taşıma vaatlerini saptadı. İlk kör okumada güncel sürümün kuru kalma bulgusu, kaynakta ayrı duran iki cümleyi kesintisiz bir alıntı gibi sunduğu için geçersiz sayıldı. Uygulama, brief’te birer kez ve aynı sırada geçen tam cümleler arasındaki özgün bölümü geri getiriyor. Bu örnekte eksik olan “Kapüşonu ayarlanabilir.” cümlesi de alıntıya girdi. Aynı API yanıtı yeni doğrulamadan geçirildi ve kör editör düzeltilmiş bulguyu kabul etti.

| Bülten senaryosu | Güncel denetim |
|---|---|
| Etkinlik planı kesinmiş gibi yazıldı, başlangıç tarihi öngörü olarak kaldı. | Bir bulgu, etkinliğin gerçekleşmesi |
| Plan ifadesi korundu, başlangıç tarihi kesinmiş gibi yazıldı. | Bir bulgu, başlangıç tarihi |
| Hem etkinlik planı hem başlangıç tarihi kesinmiş gibi yazıldı. | İki ayrı bulgu |

Önceki denetim, ilk senaryoda başlık ve gövdedeki aynı kesinlik artışını iki kez bildirdi. Güncel denetim, kesinlik değişimini bir kez kaydetti. Hem plan hem tarih doğru aktarıldığında iki sürüm de bulgu üretmedi.

## Önceki kapüşon örneği

Sekiz yeni brief’in dışında, önceki testte yanlış pozitif üreten metin güncel sürümle canlı API’de bir kez daha incelendi. Tek bulgu, ürünün hafif yağmur sınırını aşan “beklenmedik bir sağanakta” ifadesiydi. Kapüşonun başı korumaya yardımcı olduğu cümle ayrı bulgu almadı.

Her brief ve sürüm için son karşılaştırmaya bir API yanıtı alındı. Bu çalışma kaynak denetimini ölçer. Örneklem sekiz kurgusal brief ile sınırlıdır.
