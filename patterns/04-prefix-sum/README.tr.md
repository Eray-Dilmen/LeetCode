> 📌 **Rehber:** Bu dizin, **Prefix Sum (Ön Ek Toplamı)** kalıbı için bir Kavram Haritası işlevi görür.
> * **Teorik Mantık:** Temel prensipler, alt varyasyonlar ve zaman/alan karmaşıklığı analizleri için bu `README.tr.md` dosyasını okuyun.
> * **Pratik Uygulamalar:** Kalıbın pratikte nasıl uygulandığını görmek için spesifik soru klasörlerine gidin (örneğin, `0303-Range Sum Query - Immutable`). Özel istisnalar (edge cases) ve alternatif çözümler bu klasörlerin içinde belgelenmiştir.

## Prefix Sum Kalıbı Nedir?

* **Tanım:** Her `i` indeksindeki elemanın, orijinal dizinin başından o `i` indeksine kadar olan tüm elemanların toplamını (veya çarpımını) temsil ettiği, önceden hesaplanmış bir dizi (array) oluşturma tekniğidir.
* **Temel Gücü:** `left` ve `right` indeksleri arasındaki belirli bir alt dizinin toplamını bulmanız gerektiğinde, bunu bir döngü ile hesaplamak `O(n)` zaman alır. Ancak `O(n)` sürede bir kez prefix sum dizisi oluşturursanız, herhangi bir aralık sorgusuna (range query) şu formülle **`O(1)` (sabit zaman)** sürede cevap verebilirsiniz: `Toplam = prefix[right] - prefix[left - 1]`.

---

## Temel Varyasyonlar ve Algoritmik Stratejiler

Prefix Sum kalıbı temel bir yapı taşıdır. Karmaşık problemleri çözmek için genellikle Hash Map gibi diğer veri yapılarıyla birleştirilir.

### 1. Statik Alt Dizi Sorguları (Static Subarray Queries)
* **Algoritma:** Aynı boyutta (veya sınır durumlarını temiz yönetmek için `boyut + 1` boyutunda) bir `prefix` dizisi oluşturun. Girdi dizisi üzerinde gezinerek sürekli artan toplamı tutun ve bunu `prefix` dizisine kaydedin. `i` ve `j` indeksleri arasındaki herhangi bir alt dizinin toplamını bulmak için `prefix[j] - prefix[i - 1]` değerini döndürün.
* **Ne zaman kullanılır:** Bir problem, değişmeyen (immutable) bir dizi üzerinde defalarca farklı alt dizilerin toplamını sorgulamanızı gerektirdiğinde.
* **Repo Örnekleri:**
  * [0303-Range Sum Query - Immutable](./0303-Range%20Sum%20Query%20-%20Immutable)
  * [0724-Find Pivot Index](./0724-Find%20Pivot%20Index)

### 2. Prefix Sum + Hash Map (Dinamik Eşleştirme)
* **Algoritma:** Bütün alt dizileri tek tek kontrol etmek yerine, ilerlerken anlık bir `prefix_sum` (mevcut toplam) tutun. Toplamı belirli bir `target` (hedef) olan alt diziyi bulmak için matematiksel mantığı kullanın: `prefix_sum - target = required_previous_sum` (gereken_onceki_toplam). Tüm önceki prefix sum'ların frekanslarını tutan bir Hash Map içinde bu `required_previous_sum` değerinin var olup olmadığını kontrol edin.
* **Ne zaman kullanılır:** Toplamı belirli bir değere (`k`) ulaşan bitişik alt dizilerin *sayısını* veya *maksimum uzunluğunu* bulmanız gerektiğinde, **özellikle dizi negatif sayılar içeriyorsa** (çünkü negatif sayılar Sliding Window kalıbını bozar).
* **Repo Örnekleri:**
  * [0560-Subarray Sum Equals K](./0560-Subarray%20Sum%20Equals%20K)
  * [0525-Contiguous Array](./0525-Contiguous%20Array)

### 3. Çift Yönlü Diziler (Prefix & Suffix)
* **Algoritma:** Bazı problemler, elemanın kendisini dahil etmeden solunda VE sağında ne olduğunu bilmenizi gerektirir. İki dizi oluşturun: soldan birikerek gelen bir `prefix` dizisi ve sağdan birikerek gelen bir `suffix` (postfix) dizisi. `i` indeksi için sonuç genellikle `prefix[i - 1] * suffix[i + 1]` olur.
* **Ne zaman kullanılır:** Her eleman için `nums[i]` *hariç* diğer tüm elemanların çarpımını/toplamını bulmanız istendiğinde ve bölme işlemi kullanmak yasaksa (veya dizide sıfırlar varsa).
* **Repo Örnekleri:**
  * [0238-Product of Array Except Self](./0238-Product%20of%20Array%20Except%20Self)

---

## 💡 Profesyonel Detaylar ve İstisnai Durumlar

* **Sıfır Başlangıcı / Temel Durum (Base Case):** Prefix Sum + Hash Map varyasyonunu kullanırken, haritanızı her zaman `{0: 1}` ile başlatın (bu, 0 toplamının bir kez görüldüğü anlamına gelir). Bu adım, geçerli bir alt dizi doğrudan `0` indeksinden başlıyorsa, `prefix_sum - target == 0` denkleminin başarıyla yakalanmasını sağlar.
* **Negatif Sayılar ve Sliding Window Karışıklığı:** Eğer bir problem alt dizi toplamı istiyorsa ve dizi **negatif sayılar içeriyorsa**, kesinlikle Sliding Window **kullanmayın**. Kayan pencere (Sliding Window), pencere genişledikçe toplamın artacağı ve daraldıkça azalacağı varsayımına dayanır. Negatif sayılar bu mantığı yok eder. Bu durumlarda zorunlu olarak Prefix Sum + Hash Map kullanmalısınız.
* **Alan Optimizasyonu (Space Optimization):** Çift Yönlü varyasyonlar için (Product of Array Except Self gibi), kesin olarak iki ayrı `O(n)` dizisine ihtiyacınız yoktur. İlk geçişte prefix değerlerini doğrudan `output` dizisine yazabilir, ardından diziyi tersten tararken tek bir tamsayı değişkeni ile suffix durumunu takip edebilirsiniz. Bu teknik, yardımcı belleği `O(1)` seviyesine indirir.