> 📌 **Rehber:** Bu dizin, **Sliding Window (Kayan Pencere)** kalıbı için bir Kavram Haritası işlevi görür.
> * **Teorik Mantık:** Temel prensipler, alt varyasyonlar ve zaman/alan karmaşıklığı analizleri için bu `README.tr.md` dosyasını okuyun.
> * **Pratik Uygulamalar:** Kalıbın pratikte nasıl uygulandığını görmek için spesifik soru klasörlerine gidin (örneğin, `0209-Minimum Size Subarray Sum`). Özel istisnalar (edge cases) ve alternatif çözümler bu klasörlerin içinde belgelenmiştir.

## Sliding Window Kalıbı Nedir?

* **Tanım:** İki işaretçinin (`left` ve `right`) bir "pencere" veya sınır oluşturduğu, Two Pointers (İki İşaretçi) kalıbının özel bir alt türüdür. Bu pencere, bitişik (contiguous) bir eleman alt kümesini izlemek için bir dizi veya metin üzerinde kayar.
* **Temel Gücü:** Bir alt dizinin toplamını, çarpımını veya frekansını iç içe döngüler kullanarak sıfırdan hesaplamak (`O(n²)`) yerine, kayan pencere bir önceki adımda yapılan işi yeniden kullanır. Pencereye yeni giren elemanı ekler ve pencereden çıkan eski elemanı çıkarır. Bu sayede zaman karmaşıklığını tek geçişe (`O(n)`) indirger.

---

## Temel Varyasyonlar ve Algoritmik Stratejiler

Sliding Window kalıbı, alt dizinin boyutunun sabit olmasına veya dinamik bir koşula bağlı olmasına göre farklılık gösterir.

### 1. Sabit Boyutlu Pencere (Fixed Size Window)
* **Algoritma:** `left` ve `right` işaretçileri arasındaki mesafe her zaman tam olarak `k` kadardır. Önce ilk `k` elemanın durumunu (toplam/ortalama) hesaplayın. Ardından, her iki işaretçiyi de birer adım kaydırarak pencereyi ilerletin: `right`'taki yeni elemanı duruma ekleyin ve `left - 1`'de pencereden az önce çıkan elemanı durumdan çıkarın.
* **Ne zaman kullanılır:** Problem açıkça belirli bir uzunluktaki bitişik bir alt dizi veya alt metin istediğinde (örn. "k boyutundaki ardışık herhangi bir alt dizinin maksimum toplamı").
* **Repo Örnekleri:**
  * [0643-Maximum Average Subarray I](./0643-Maximum%20Average%20Subarray%20I)
  * [1343-Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold](./1343-Number%20of%20Sub-arrays%20of%20Size%20K%20and%20Average%20Greater%20than%20or%20Equal%20to%20Threshold)

### 2. Dinamik Boyutlu Pencere (Dynamic Size Window)
* **Algoritma:** Pencere boyutu hedef bir koşula göre genişler ve daralır. `right` işaretçisi bir `for` döngüsü içinde elemanları dahil ederek pencereyi genişletir. Pencerenin durumu problemin koşulunu ihlal ettiğinde (veya hedefe göre koşulu sağladığında), koşul tekrar geçerli olana kadar `left` işaretçisini bir `while` döngüsü ile ileri kaydırarak pencereyi daraltın.
* **Ne zaman kullanılır:** Belirli bir kriteri karşılayan en uzun/en kısa bitişik alt diziyi/alt metni bulmanız gerektiğinde (örn. "toplamı hedef sayıya eşit veya büyük olan en kısa alt dizi").
* **Repo Örnekleri:**
  * [0209-Minimum Size Subarray Sum](./0209-Minimum%20Size%20Subarray%20Sum)
  * [0003-Longest Substring Without Repeating Characters](./0003-Longest%20Substring%20Without%20Repeating%20Characters)

### 3. Yardımcı Veri Yapısı ile Dinamik Pencere (Hash Map/Set)
* **Algoritma:** Dinamik pencere ile aynıdır, ancak pencerenin iç durumunu (karakter frekansları veya benzersiz eleman sayıları gibi) izlemek için bir Hash Map, Set veya frekans dizisi kullanır. `right` genişledikçe haritayı güncelleyin. `left` daraldıkça sayıları azaltın ve değer sıfıra ulaşırsa anahtarı (key) tamamen silin.
* **Ne zaman kullanılır:** Koşulun karakter frekansına, tekrar eden karakterlere veya anagram bulmaya bağlı olduğu metin (string) manipülasyonu problemlerinde.
* **Repo Örnekleri:**
  * [0424-Longest Repeating Character Replacement](./0424-Longest%20Repeating%20Character%20Replacement)
  * [0438-Find All Anagrams in a String](./0438-Find%20All%20Anagrams%20in%20a%20String)

---

## 💡 Profesyonel Detaylar ve İstisnai Durumlar

* **Durum Senkronizasyonu:** Sliding Window algoritmalarındaki en yaygın hata, `left` işaretçisini kaydırmadan *önce* çalışan durumu (toplam, sayaç, harita) güncellemeyi unutmaktır. `left += 1` yapmadan hemen önce her zaman `nums[left]`'i takipçinizden (state tracker) çıkarın.
* **Two Pointers vs. Sliding Window:** Elemanlar birbirinden bağımsızsa veya dizinin herhangi bir yerinden eşleştirilebiliyorsa Two Pointers kullanın. Problem kesinlikle **bitişik (contiguous)** bir alt dizi veya alt metin istiyorsa **sadece** Sliding Window kullanın.
* **Koşul Mantığı (Condition Logic):** `left` işaretçisi için yazdığınız `while` döngüsünün koşuluna çok dikkat edin. Döngünün, koşul *geçerliyken mi* (minimumları bulmak için) yoksa koşul *geçersizken mi* (maksimumları bulmak için tekrar geçerli hale getirmek adına) çalışması gerektiğine doğru karar vermelisiniz.