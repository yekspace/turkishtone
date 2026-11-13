# Responses API karşılaştırması

Model isteği: `gpt-5.4-mini-2026-03-17`

Tamamlanan içerik sayısı: 6/6

| Tür | Koşul | İlk gövde | Son gövde | Hedef | Son durum |
|---|---|---:|---:|---:|---|
| Haber | skillsiz | 30 | 39 | 45–75 | Sınır dışında |
| Haber | skill-li | 28 | 28 | 45–75 | Sınır dışında |
| Rehber | skillsiz | 47 | 61 | 55–90 | Aralıkta |
| Rehber | skill-li | 42 | 48 | 55–90 | Sınır dışında |
| Ürün içeriği | skillsiz | 42 | 41 | 45–75 | Sınır dışında |
| Ürün içeriği | skill-li | 34 | 41 | 45–75 | Sınır dışında |

## Haber · skillsiz

### İlk taslak · 30 kelime

**Çınar Belediyesi’nden pazar günü ücretsiz bisiklet bakım atölyesi**

Çınar Belediyesi, pazar günü saat 10.00’da ücretsiz bir bisiklet bakım atölyesi düzenleyecek. Atölye için kayıt gerekmiyor. Katılımcılar kendi bisikletleriyle gelebilecek. Belediyenin duyurusunda etkinliğin yapılacağı yer ve bitiş saati yer almıyor.

**Editör notu**

Önceki başlık: “Pedal tutkunları için hafta sonu fırsatı”

### Düzeltilen taslak · 39 kelime

**Çınar Belediyesi’nden pazar günü ücretsiz bisiklet bakım atölyesi**

Çınar Belediyesi, pazar günü saat 10.00’da ücretsiz bir bisiklet bakım atölyesi düzenleyecek. Kayıt gerekmiyor. Katılımcılar kendi bisikletleriyle gelebilir. Belediyenin duyurusunda etkinliğin yapılacağı yer ve bitiş saati yer almıyor; bu yüzden atölyeye gitmek isteyenlerin yalnızca saat 10.00’da hazır bulunması yeterli.

**Editör notu**

Önceki başlık: “Pedal tutkunları için hafta sonu fırsatı”

**Uygulama durumu:** Uzunluk sınırı nedeniyle editör incelemesi gerekiyor.

## Haber · skill-li

### İlk taslak · 28 kelime

**Çınar Belediyesi pazar günü ücretsiz bisiklet bakım atölyesi düzenleyecek**

Çınar Belediyesi, pazar günü saat 10.00’da ücretsiz bisiklet bakım atölyesi düzenleyecek. Atölye için kayıt gerekmiyor. Katılımcılar kendi bisikletleriyle gelebilir. Belediyenin duyurusunda etkinliğin yeri ve bitiş saati yer almıyor.

### Düzeltilen taslak · 28 kelime

**Çınar Belediyesi pazar günü ücretsiz bisiklet bakım atölyesi düzenleyecek**

Çınar Belediyesi, pazar günü saat 10.00’da ücretsiz bir bisiklet bakım atölyesi düzenleyecek. Atölye için kayıt gerekmiyor; katılımcılar kendi bisikletleriyle gelebilir. Belediyenin duyurusunda etkinliğin yeri ve bitiş saati belirtilmedi.

**Uygulama durumu:** Uzunluk sınırı nedeniyle editör incelemesi gerekiyor.

## Rehber · skillsiz

### İlk taslak · 47 kelime

**Geçen Aya Ait Faturaları PDF Olarak İndirme**

Faturalar ekranına gidin. Tarih filtresinden Geçen ay seçeneğini seçerek listeyi daraltın. Ardından indirmek istediğiniz faturaları listeden işaretleyin ve PDF indir düğmesine basın. Bir seferde en fazla 10 fatura seçebilirsiniz. 10’dan fazla fatura varsa, kalanları ayrı bir seçim yaparak indirmeniz gerekir. Bu ekranı yalnızca yönetici rolündeki kullanıcılar görebilir.

### Düzeltilen taslak · 61 kelime

**Geçen Aya Ait Faturaları PDF Olarak İndirme**

Faturalar ekranına gidin. Tarih filtresinden Geçen ay seçeneğini seçerek listeyi daraltın. Ardından indirmek istediğiniz faturaları listeden işaretleyin ve PDF indir düğmesine basın. Bir seferde en fazla 10 fatura seçebilirsiniz. 10’dan fazla fatura varsa, kalanları ayrı bir seçim yaparak indirmeniz gerekir. Bu ekranı yalnızca yönetici rolündeki kullanıcılar görebilir. Böylece geçen aya ait faturaları tek tek değil, seçtiğiniz gruplar halinde PDF olarak indirebilirsiniz.

## Rehber · skill-li

### İlk taslak · 42 kelime

**Geçen aya ait faturaları PDF olarak indirme**

Faturalar ekranını yalnızca yönetici rolündekiler görür. Geçen aya ait faturaları indirmek için Tarih filtresinden Geçen ay seçin. Ardından listeden faturaları işaretleyip PDF indir düğmesine basın. Bir seferde en fazla 10 fatura seçebilirsiniz. 10’dan fazla fatura varsa kalanları ayrı bir seçimle indirmeniz gerekir.

### Düzeltilen taslak · 48 kelime

**Geçen aya ait faturaları PDF olarak indirme**

Faturalar ekranını yalnızca yönetici rolündekiler görebilir. Geçen aya ait faturaları indirmek için önce Tarih filtresinden Geçen ay seçin. Ardından listeden faturaları işaretleyip PDF indir düğmesine basın. Bir seferde en fazla 10 fatura seçebilirsiniz. 10’dan fazla fatura varsa kalanları ayrı bir seçimle indirmeniz gerekir; böylece her indirmenin sınırı korunur.

**Uygulama durumu:** Uzunluk sınırı nedeniyle editör incelemesi gerekiyor.

## Ürün içeriği · skillsiz

### İlk taslak · 42 kelime

**Stok listesini CSV olarak dışa aktarın**

Stok ekranındaki filtrelerinize uyan satırları artık CSV olarak indirebilirsiniz. Yönetici rolündeki kullanıcılar, Stok ekranındaki CSV dışa aktar seçeneğiyle listeyi kendi bilgisayarına alır ve ardından ekip arkadaşıyla dilediği gibi paylaşır. Bu sürümde Excel biçimi ve otomatik gönderim bulunmuyor; paylaşımı siz manuel olarak yaparsınız.

### Düzeltilen taslak · 41 kelime

**Stok listesini CSV olarak dışa aktarın**

Stok yönetimini bir üst seviyeye taşıyoruz. Yönetici rolündeki sizler, Stok ekranındaki CSV dışa aktar seçeneğiyle ekrandaki filtrelere uyan satırları indirebilirsiniz. Dosyayı kendiniz paylaşır, ekip arkadaşınıza ulaştırırsınız. Excel biçimi ve otomatik gönderim yoktur. Böylece stok listesini yalnızca ihtiyacınız olan kayıtlarla kolayca paylaşabilirsiniz.

**Uygulama durumu:** Uzunluk sınırı nedeniyle editör incelemesi gerekiyor.

## Ürün içeriği · skill-li

### İlk taslak · 34 kelime

**Stok listesini CSV olarak indirin**

Yönetici rolündekiler Stok ekranındaki filtrelere uyan satırları CSV dışa aktar seçeneğiyle indirebilir. Dosyayı kendileri paylaşır; otomatik gönderim yoktur. Excel biçimi desteklenmez. Stok listesini ekip arkadaşınızla paylaşmak için CSV dosyasını indirip uygun kanaldan iletmeniz yeterlidir.

### Düzeltilen taslak · 41 kelime

**Stok listesini CSV olarak indirin**

Yönetici rolündeyseniz Stok ekranındaki filtrelere uyan satırları CSV dışa aktar seçeneğiyle indirebilirsiniz. Dosyayı kendiniz paylaşırsınız; otomatik gönderim yoktur. Excel biçimi desteklenmez. Stok listesini ekip arkadaşınızla paylaşmak için CSV dosyasını indirip uygun kanaldan iletmeniz yeterlidir. Bu sayede ekrandaki veriyi filtrelediğiniz şekilde aktarabilirsiniz.

**Uygulama durumu:** Uzunluk sınırı nedeniyle editör incelemesi gerekiyor.

## Editör değerlendirmesi

İlk taslaklar aynı üç brief, model sürümü ve çıktı şemasıyla üretildi. İlk gövde sınır dışındaysa uygulama aynı koşulda bir kez düzeltme istedi. İkinci isteğe ilk metni, orijinal brief’i, ölçülen sayıyı ve hedef aralığı ekledi. Skill’li koşul bu sürümün Türkçe Editör talimatlarını kullandı. Rapor 6 ilk taslak ve 6 düzeltme olmak üzere 12 canlı yanıt içeriyor.

- Haber. İki son gövde de sınırın altında. Skill’li metin yer ve bitiş saatinin bilinmediğini doğru aktardı ancak editör notunu boş bıraktı. Skillsiz düzeltme “yalnızca saat 10.00’da hazır bulunması yeterli” dedi. Etkinlik yeri bilinmediği için bu sonuç kaynaktan çıkarılamaz.
- Rehber. Skillsiz düzeltme 61 kelimeyle aralığa giren tek sonuç. Eklediği son cümle, grup hâlinde PDF indirmeyi yeniden söylüyor. Skill’li düzeltme yönetici erişimini, 10 fatura sınırını ve işlem adımlarını korudu. 48 kelimeyle alt sınırı kaçırdı.
- Ürün içeriği. İki düzeltilmiş gövde de Excel ve otomatik gönderim kısıtlarını korudu. Skillsiz düzeltme arşivdeki “Stok yönetimini bir üst seviyeye taşıyoruz” girişini yeniden kullandı. Skill’li metinde CSV’yi indirip paylaşma bilgisi birkaç kez yinelendi. İkisi de 41 kelimede kaldı.

İlk taslaklarda 0/6, düzeltme sonrasında 1/6 gövde aralıkta. Uygulama diğer beşini editör incelemesine işaretledi. Uzunluk kontrolü, metnin olgusal doğruluğunu veya yayına uygunluğunu belirlemez. Bu denemede yeni makale, duygusal içerik, seslendirme ve sosyal medya rehberleri kullanılmadı. Bunların ayrı brief’lerle denenmesi gerekir.
