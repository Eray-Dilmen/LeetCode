> 📌 **Rehber:** Bu dizin, **Hash Maps & Sets** kalıbının mantığını ve örnek problemler üzerindeki uygulamalarını içerir.
> * **Teorik Mantık:** Kalıbın çalışma prensibi ve zaman/alan karmaşıklığı analizleri için bu `README.md` dosyasını inceleyebilirsiniz.
> * **Pratik Sorular:** Kalıbın uygulandığı çözümleri görmek için ilgili soru klasörlerine (örn. `0001-Two Sum`) gidebilirsiniz.

## Hash Map (ve Hash Set) Kalıbı Nedir?

* **Tanım:** Bir Hash Map (Python'daki `dict`), **Anahtar-Değer (Key-Value)** ikilisiyle çalışan bir veri yapısıdır. Hash Set (`set`) ise ilişkili bir değer barındırmadan sadece tekil anahtarları tutan versiyonudur.
* **Kritik Süper Gücü:** Bir elemanın içeride var olup olmadığını sorgulamak (**Lookup / Search**) listelerde $O(n)$ zaman alırken, Hash Map/Set içinde **$O(1)$ (sabit zaman)** alır. Bu durum, zaman karmaşıklığını optimize etmek için en güçlü araçtır.

## Ne Zaman Kullanılır? (İpuçları ve Depodaki Örnekler)

1. **Tekillik ve Varlık Kontrolü:** *"Daha önce bu elemanı gördüm mü?"*
   * *Örnek (`0217-Contains Duplicate`):* Bir dizide gezinirken elemanları bir Hash Set'e eklersiniz. Eğer eklenecek eleman zaten Set içinde mevcutsa, dizide kopya (duplicate) var demektir. $O(1)$ arama hızı sayesinde $O(n^2)$ iç içe döngülerden kurtulursunuz.

2. **Hızlı Eşleştirme ve Tamamlayıcılar (Hafıza Takası):** *"Bir çifti tamamlamak için ihtiyacım olan parça elimde var mı?"*
   * *Örnek (`0001-Two Sum`):* $x + y = \text{target}$ denklemini $y = \text{target} - x$ olarak düşünürsünüz. Döngüdeki her $x$ için Hash Map'e şu soruyu sorarsınız: *"Hafızanda beni hedefe ulaştıracak $y$ değeri var mı?"*

3. **Frekans / Adet Sayma:** *"Hangi harf/sayı kaç kez geçti?"*
   * *Örnek (`0383-Ransom Note` & `1189-Maximum Number of Balloons`):* Kaynak bir metindeki (örneğin dergi sayfaları) karakterlerin frekanslarını sayıp bir Hash Map'e atarsınız. Ardından, hedef kelimeyi oluşturmak için yeterli harfiniz olup olmadığını bu Map üzerinden doğrularsınız.

## Hash Set vs Hash Map: Hangisi Seçilmeli?

**Hash Set (`set`)**
* Sadece tekil elemanlardan oluşan bir kümedir.
* **Cevapladığı Soru:** *"Bu eleman havuzda mevcut mu?"*
* **Kullanım Senaryosu (`0771-Jewels and Stones`):** Taşın mücevher olup olmadığını bilmek yeterlidir. Mücevherleri bir Set içine atarsınız (`{"a", "A"}`). Referans metninde o mücevherin kaç kere geçtiğiyle ilgilenmezsiniz.

**Hash Map (`dict`)**
* Bir anahtarı belirli bir değere bağlayan eşleme tablosudur.
* **Cevapladığı Soru:** *"Bu eleman var mı, varsa ona bağlı veri (adet, indeks vb.) nedir?"*
* **Kullanım Senaryosu (`0001-Two Sum`):** Tamamlayıcı sayının var olup olmadığını bilmek yetmez, orijinal dizideki **indeksini** de bulmanız gerekir. Bu yüzden veriyi eşlemeniz şarttır: `{"sayi": indeks}`.

## 💡 Profesyonel Detaylar ve İstisnai Durumlar

* **Zaman-Alan Takası (Space-Time Trade-off):** Bu kalıbı uygulamak neredeyse her zaman Zaman Karmaşıklığını (Time Complexity) $O(n^2)$'den $O(n)$'e düşürür. Ancak hash tablosu için ekstra bellek ayırdığınızdan Alan Karmaşıklığı (Space Complexity) $O(n)$'e çıkar.
* **Sadece Hashlenebilir Anahtarlar (Hashable Keys):** Python'da Map veya Set içinde anahtar (key) olarak yalnızca **değiştirilemez (immutable)** veri tiplerini (tam sayı, string veya tuple) kullanabilirsiniz. Liste (list) veya başka bir sözlük (dict) anahtar olarak kullanılamaz.