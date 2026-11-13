# Responses API karşılaştırması

Model isteği: `gpt-5.4-mini-2026-03-17`

Tamamlanan içerik sayısı: 8/8

| Tür | Koşul | İlk gövde | Son gövde | Hedef | Son durum |
|---|---|---:|---:|---:|---|
| Makale | skillsiz | 87 | 87 | 85–150 | Aralıkta |
| Makale | skill-li | 79 | 84 | 85–150 | Sınır dışında |
| Duygusal içerik | skillsiz | 38 | 38 | 30–65 | Aralıkta |
| Duygusal içerik | skill-li | 31 | 31 | 30–65 | Aralıkta |
| Seslendirme | skillsiz | 45 | 45 | 45–90 | Aralıkta |
| Seslendirme | skill-li | 30 | 32 | 45–90 | Sınır dışında |
| Sosyal medya | skillsiz | 30 | 30 | 30–65 | Aralıkta |
| Sosyal medya | skill-li | 27 | 37 | 30–65 | Aralıkta |

## Makale · skillsiz

### İlk taslak · 87 kelime

**Ardıç Kütüphanesi’nin Geçici Akşam Uygulaması İlgi Gördü**

Ardıç Kütüphanesi, iki haftalık pilot uygulamada okuma salonunu salı ve perşembe günleri saat 20.00’ye kadar açık tuttu. Bu dört akşam boyunca toplam 48 giriş kaydedildi. Ancak bu sayı tekil ziyaretçi sayısını değil, giriş sayısını gösteriyor; dolayısıyla kaç kişinin faydalandığı kesin olarak bilinmiyor. Ayrıca önceki haftalara ait karşılaştırılabilir akşam verisi bulunmadığı için, artış ya da değişim hakkında doğrudan kıyas yapmak mümkün değil. Pilot çalışma, akşam saatlerinde kütüphaneye bir talep olabileceğini gösterse de, uzatmanın kalıcı olup olmayacağı henüz belli değil. Kütüphane yönetimi, uygulamayı sürdürüp sürdürmeyeceğine daha sonra karar verecek.

### Kaynak kontrolü

Denetim çağrısı bulgu bildirmedi.

## Makale · skill-li

### İlk taslak · 79 kelime

**Ardıç Kütüphanesi’nden iki haftalık pilot: Akşam girişleri kaydedildi**

Ardıç Kütüphanesi, iki haftalık pilot uygulamada okuma salonunu salı ve perşembe günleri saat 20.00’ye kadar açık tuttu. Bu dört akşamda toplam 48 giriş kaydedildi. Ancak bu sayı tekil ziyaretçi sayısını göstermiyor; aynı kişinin birden fazla girişi olabilir. Önceki haftalar için karşılaştırılabilir akşam verisi bulunmadığı için pilotun etkisini önceki dönemle doğrudan kıyaslamak mümkün değil. Kütüphane, uzatmayı sürdürüp sürdürmeyeceğine henüz karar vermedi. Pilot çalışma, akşam saatlerinde salon kullanımına dair ilk ölçümü sağlıyor; fakat karar için daha geniş bir karşılaştırma verisi gerekiyor.

### Düzeltilen taslak · 84 kelime

**Ardıç Kütüphanesi’nden iki haftalık pilot: Akşam girişleri kaydedildi**

Ardıç Kütüphanesi, iki haftalık pilot uygulamada okuma salonunu salı ve perşembe günleri saat 20.00’ye kadar açık tuttu. Bu dört akşamda toplam 48 giriş kaydedildi. Ancak bu sayı tekil ziyaretçi sayısı değil; aynı kişi birden fazla giriş yapmış olabilir. Önceki haftalar için karşılaştırılabilir akşam verisi olmadığı için bu sonucu önceki dönemle doğrudan kıyaslamak mümkün değil. Kütüphane uzatmayı sürdürüp sürdürmeyeceğine henüz karar vermedi. Pilot, akşam saatlerinde salonun nasıl kullanıldığına dair ilk ölçümü sağlıyor; fakat bu verinin neyi gösterdiği, tek başına ziyaretçi sayısını değil, giriş sayısını yansıtıyor.

### Kaynak kontrolü

Denetim çağrısı bulgu bildirmedi.

**Editör incelemesi gerekiyor** · gövde uzunluğu

## Duygusal içerik · skillsiz

### İlk taslak · 38 kelime

**taslak**

Seni Cumartesi buluşmasına haber vermeden bırakıp gelmediğim için özür dilerim. Kafede yarım saat beklemişsin; bunu duyunca gerçekten üzüldüm. O gün neden gelemediğime dair sana bir bilgi vermedim, bu da yanlıştı. İstersen bu hafta telefonla konuşup telafi etmeye çalışayım.

### Kaynak kontrolü

Denetim çağrısı bulgu bildirmedi.

## Duygusal içerik · skill-li

### İlk taslak · 31 kelime

**Taslak**

Cumartesi buluşmasına haber vermeden gelmediğim için özür dilerim. Kafede yarım saat beklettiğimi söylemen beni üzdü; seni böyle bırakmamalıydım. Neden gelemediğimi şimdi açıklamıyorum, ama istersen bu hafta telefonla konuşup telafi etmek isterim.

### Kaynak kontrolü

Denetim çağrısı bulgu bildirmedi.

## Seslendirme · skillsiz

### İlk taslak · 45 kelime

**Müze Girişi Yönlendirmesi**

Ana giriş önündeki merdivenlerde bakım çalışması sürmektedir. Müze girişine ulaşmak için lütfen meydandan bahçe kapısına doğru ilerleyin. Bahçe kapısına kadar yol düzdür. Bahçe kapısı her gün on ile on yedi saatleri arasında açıktır. Ziyaretçiler içeri bu kapıdan girebilir. Bakım çalışmalarının ne zaman tamamlanacağı henüz duyurulmamıştır.

### Kaynak kontrolü

- **uydurulan_iddia** · Brief yalnızca bahçe kapısının 10.00–17.00 arasında açık olduğunu söylüyor; her gün açık olduğu belirtilmiyor. Okur bu bilgiyi günlük düzenli erişim olarak anlayabilir.
  - Metin alintisi · “Bahçe kapısı her gün on ile on yedi saatleri arasında açıktır.”

**Editör incelemesi gerekiyor** · kaynak bulgusu

## Seslendirme · skill-li

### İlk taslak · 30 kelime

**Müze girişi yönlendirme metni**

Ana giriş önündeki merdivenler bakımda. Ziyaretçiler, meydandan bahçe kapısına yönelerek düz yolu izleyebilir. Bahçe kapısından içeri girebilirsiniz. Bahçe kapısı 10.00 ile 17.00 arasında açıktır. Bakımın ne zaman biteceği henüz açıklanmadı.

### Düzeltilen taslak · 32 kelime

**Müze girişi yönlendirme metni**

Ana giriş önündeki merdivenler bakımda. Ziyaretçiler meydandan bahçe kapısına geçip düz yolu izleyebilir. Bahçe kapısından içeri girebilirsiniz. Bahçe kapısı saat on ile on yedi arasında açık. Bakımın ne zaman biteceği henüz açıklanmadı.

### Kaynak kontrolü

Denetim çağrısı bulgu bildirmedi.

**Editör incelemesi gerekiyor** · gövde uzunluğu

## Sosyal medya · skillsiz

### İlk taslak · 30 kelime

**Bostanda tohum takasına davetlisiniz**

Cumartesi saat 14.00’te bostanda tohum takasına davetlisiniz. Kayıt gerekmiyor; tohumu olmayanlar da gelebilir. Yağmur yağarsa buluşma iptal edilecek ve karar cumartesi saat 11.00’de bu hesaptan duyurulacak. Bostanda buluşup tohumları paylaşalım.

### Kaynak kontrolü

Denetim çağrısı bulgu bildirmedi.

## Sosyal medya · skill-li

### İlk taslak · 27 kelime

**Mahalle bostanında tohum takası**

Cumartesi saat 14.00’te bostanda tohum takasına davetlisiniz. Katılmak için kayıt gerekmiyor; tohumu olmayanlar da gelebilir. Yağmur yağarsa buluşma iptal edilecek. Karar, cumartesi saat 11.00’de bu hesaptan duyurulacak.

### Düzeltilen taslak · 37 kelime

**Mahalle bostanında tohum takası**

Cumartesi saat 14.00’te bostanda tohum takasına davetlisiniz. Katılmak için kayıt gerekmiyor; tohumu olmayanlar da gelebilir. Yağmur yağarsa buluşma iptal edilecek. Karar cumartesi saat 11.00’de bu hesaptan duyurulacak. Bostanda herkes tohum getirip paylaşabilir; elinizde tohum olmasa da katılabilirsiniz.

### Kaynak kontrolü

Denetim çağrısı bulgu bildirmedi.

## Editör karşılaştırması

Dört kurgusal brief aynı model, çıktı şeması ve kelime denetimiyle iki koşulda çalıştırıldı. Yalnızca skill’li isteklere Türkçe Editör ve ilgili türün rehberi eklendi. Üç kısa gövde birer kez yeniden yazdırıldı. Kaynak denetimine koşul etiketi, skill talimatı ve editör notu gönderilmedi. İlk denetim eş değer cümleleri ve bir kelime sınırını yanlışlıkla işaretledi. Talimat gözden geçirildi, aynı sekiz son metin yeniden denetlendi ve son geçişte denetim için düşük akıl yürütme düzeyi kullanıldı. Tablodaki metinler bu işlem sırasında yeniden üretilmedi.

| Tür | Metinlerin editör gözüyle karşılaştırması |
|---|---|
| Makale | İki metin de 48’in giriş sayısı olduğunu, önceki dönemle kıyas yapılamadığını ve kararın verilmediğini açıklıyor. Skillsiz başlıktaki “İlgi Gördü” yorumu için ölçüt yok. Skill’li düzeltmedeki “ilk ölçümü” de brief’te doğrulanmıyor ve son cümle giriş ile ziyaretçi ayrımını tekrarlıyor. Son denetim bu iki ifadeyi işaretlemedi. |
| Duygusal içerik | Skill’li özür “Cumartesi buluşmasına haber vermeden gelmediğim için özür dilerim” diye daha açık başlıyor. Skillsiz metindeki “seni … bırakıp gelmediğim” söz dizimi aksıyor. Skill’li metindeki “Neden gelemediğimi şimdi açıklamıyorum” da konuşma dilinde yapay duruyor. İki metin de telefon görüşmesini arkadaşın isteğine bırakıyor. |
| Seslendirme | Skillsiz metin brief’te bulunmayan “her gün” ifadesini ekliyor. Son denetim bunu doğru yakaladı. Skill’li ilk taslakta rakamla yazılan saatler düzeltmede yazıya döndü. Son metin kısa kaldı ve “ziyaretçiler”den “girebilirsiniz”e geçerek hitabı değiştirdi. |
| Sosyal medya | İki metin de yağmurda iptali, duyuru saatini ve kayıt koşulunu koruyor. Skill’li düzeltme aralığa girdi ancak tohumsuz katılım bilgisini tekrarladı. |

Son gövdelerin 6/8’i kelime aralığında. Dördü skillsiz, ikisi skill’li. Uygulama iki kısa metni ve bir kaynak bulgusu olan seslendirmeyi editör incelemesine işaretledi. Her türde tek çift üretildiği için bu sonuçlar genellenebilir bir kalite puanı vermez.

## Bilinen hatalarla denetim sınaması

Kurgusal kaynak, cumartesi için planlanan bir etkinliği, yağmurda iptali ve ücretin açıklanmadığını belirtiyor. Bilerek kusurlu gövde “Etkinlik cumartesi yapılacak. Giriş 100 lira.” biçiminde verildi. Son denetim planın kesinleşmiş gibi yazılmasını, yağmur koşulunun atlanmasını ve 100 liralık ücretin uydurulmasını ayrı ayrı işaretledi. Üç bulgunun alıntıları eşleşti. Bu örnek üç kategorinin çalışabildiğini gösterir. Makale örneğindeki kaçan ifadeler, boş listenin editör onayı anlamına gelmediğini gösterir.
