# Eski sürüm, sade çekirdek ve skillsiz koşul

Konuşma, reklam, kampanya ve basın bülteni için önceki dört brief aynen kullanıldı. Model sürümü `gpt-5.4-mini-2026-03-17`. Bütün isteklerde aynı çıktı şeması ve kelime denetimi uygulandı. Sınır dışında kalan ilk gövdeler birer kez düzeltildi. On iki ilk taslak ve altı düzeltme için 18 ayrı canlı API yanıtı alındı.

Eski koşul, ilk kör denemedeki tam talimatı yeniden kullandı. Dört talimatın özeti eski koşu kayıtlarıyla bire bir eşleşti. Sade koşulda yeni çekirdeğe her brief’in tür rehberi eklendi. Skillsiz istekte ek yazım talimatı yoktu. Bağımsız model değerlendiricisi brief’leri ve tür başına karıştırılmış A–C son metinlerini gördü. Puanlar kaydedildikten sonra koşul adları açıldı. Kelime sayımı editör puanına katılmadı.

| Tür | Hedef | Eski sürüm | Sade çekirdek | Skillsiz |
|---|---:|---:|---:|---:|
| Konuşma | 55–105 | 60 | 50 | 55 |
| Reklam | 35–75 | 35 | 36 | 42 |
| Kampanya | 40–85 | 49 | 43 | 41 |
| Basın bülteni | 65–125 | 58 | 48 | 67 |
| **Aralıkta kalan** | | **3/4** | **2/4** | **4/4** |

İlk taslakların dört brief boyunca toplam girdi kullanımı eski sürümde 32.868, sade koşulda 5.628 ve skillsiz koşulda 1.325 token oldu. Sade koşul eski sürümden yaklaşık yüzde 83 daha az girdi kullandı. Bu sayılar düzeltme isteklerini içermez.

| Tür | Eski sürüm | Sade çekirdek | Skillsiz | Editör tercihi |
|---|---:|---:|---:|---|
| Konuşma | A · 6/8 | C · 8/8 | B · 6/8 | Sade çekirdek |
| Reklam | C · 7/8 | B · 5/8 | A · 6/8 | Eski sürüm |
| Kampanya | A · 6/8 | B · 8/8 | C · 7/8 | Sade çekirdek |
| Basın bülteni | B · 6/8 | A · 7/8 | C · 6/8 | Sade çekirdek |
| **Toplam** | **25/32** | **28/32** | **25/32** | |

| Ölçüt | Eski sürüm | Sade çekirdek | Skillsiz |
|---|---:|---:|---:|
| Kaynak sadakati | 6/8 | 6/8 | 7/8 |
| Üslup uyumu | 7/8 | 8/8 | 6/8 |
| Doğallık | 5/8 | 6/8 | 5/8 |
| Mecra ve amaç | 7/8 | 8/8 | 7/8 |

- Konuşmada sade çekirdek olguları korudu ve metni kürsüde söylenebilecek bir davetle bitirdi. Skillsiz metindeki “İstiklal yılları döneminde” ve “hissettirmektedir” ifadeleri dinleyişi ağırlaştırdı. Eski sürüm “bugün” dedi, cumartesi bilgisini vermedi.
- Reklamda eski sürüm, yağmurluğun katlanmasından doğan faydayı “çantada az yer kaplar” diye anlattı. Sade çekirdek, ağırlık bilgisi verilmediği hâlde “hafif yağmurluk” dedi. Skillsiz metin ise “çantanızda yer kaplamaz” iddiasını ekledi.
- Kampanyada sade çekirdeğin “siz de katılın” çağrısı sıcak bulundu ve bütün katılım koşulları görünür kaldı. Eski sürümde “Katılım şartlarını koruyarak” ifadesi yapay durdu. Skillsiz metin “Kitaplarınızı alın, uğrayın” diye başlayıp daha resmî bir dile geçti.
- Basın bülteninde sade çekirdek, başlangıç için “öngörülüyor” ifadesini korudu ve uygulanabilir bilgileri girişte verdi. Eski sürüm gelecekte başka açıklama geleceğini varsaydı. Skillsiz metin yayın gövdesine editör açıklaması kattı. Üç gövdeden yalnızca skillsiz metin alt kelime sınırına ulaştı.

Her koşulda dört brief ve her brief için bir son metin kullanıldı. Puanları tek bağımsız model değerlendiricisi verdi. Sonuç bu koşudaki üslup farkını gösteriyor. Kaynak sadakatinde sade çekirdeğin eski sürüme üstünlüğü görülmedi.
