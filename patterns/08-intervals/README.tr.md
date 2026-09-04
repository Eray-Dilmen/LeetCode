> 📌 **Rehber:** Bu dizin, **Intervals (Aralıklar / Kesişimler)** kalıbı için bir Kavram Haritası işlevi görür.
> * **Teorik Mantık:** Temel prensipler, alt varyasyonlar ve zaman/alan karmaşıklığı analizleri için bu `README.tr.md` dosyasını okuyun.
> * **Pratik Uygulamalar:** Kalıbın pratikte nasıl uygulandığını görmek için spesifik soru klasörlerine gidin (örneğin, `0056-Merge Intervals`). Özel istisnalar (edge cases) ve alternatif çözümler bu klasörlerin içinde belgelenmiştir.

## Intervals Kalıbı Nedir?

* **Tanım:** Genellikle `[başlangıç, bitiş]` sayı çiftleri (aralıklar) olarak temsil edilen menzilleri/zaman dilimlerini yönetmek ve işlemek için kullanılan algoritmik bir tekniktir.
* **Temel Gücü:** Kesişen aralıklar kaotik, `O(n²)` karmaşıklığında karşılaştırma sorunları yaratabilir. Bu kalıp, aralıkları **başlangıç (start) zamanlarına göre sıralayarak** kaosu doğrusal hale getirir. Bu sayede tüm kesişimleri tek bir `O(n)` geçişinde çözebilirsiniz. Başlangıçta yapılan sıralama işleminden dolayı genel zaman karmaşıklığı (Time Complexity) **$O(n \log n)$** olur.

---

## Temel Varyasyonlar ve Algoritmik Stratejiler

Bu kalıpta alt varyasyonları belirleyen şey, `bitiş` (end) zamanlarını nasıl yönettiğinizdir.

### 1. Aralıkları Birleştirme (Merging Intervals)
* **Algoritma:** Aralık dizisini `start` zamanlarına göre küçükten büyüğe sıralayın. İlk aralığı `merged` (birleştirilmiş) listesine ekleyin. Geri kalanlar üzerinde döngü kurun. Eğer mevcut aralığın `start` değeri, listedeki son aralığın `end` değerinden küçük veya ona eşitse (çakışma varsa), son aralığın bitiş değerini `max(önceki_bitiş, mevcut_bitiş)` yaparak bunları birleştirin. Çakışma yoksa, mevcut aralığı doğrudan listeye ekleyin.
* **Ne zaman kullanılır:** Problem sizden çakışan tüm toplantıları, aralıkları veya programları kesintisiz bloklar halinde birleştirmenizi istediğinde.
* **Repo Örnekleri:**
  * [0056-Merge Intervals](./0056-Merge%20Intervals)

### 2. Yeni Bir Aralık Ekleme (Insert Interval)
* **Algoritma:** Size zaten çakışmayan ve sıralı bir aralık listesi ile eklenecek yeni bir aralık verilir. Her şeyi baştan sıralamak ($O(n \log n)$ sürer) yerine, bunu `O(n)` sürede yapabilirsiniz. Aralıklar üzerinde gezinin: yeni aralığın başlangıcından *önce* bitenleri listeye ekleyin, çakışan tüm aralıkları sınırlarını genişleterek (`min(başlangıçlar)`, `max(bitişler)`) yeni aralıkla birleştirin ve son olarak yeni aralığın bitişinden *sonra* başlayanları listeye ekleyin.
* **Ne zaman kullanılır:** Önceden sıralanmış bir takvimi/programı yönetirken ve yeni bir etkinlik eklerken.
* **Repo Örnekleri:**
  * [0057-Insert Interval](./0057-Insert%20Interval)

### 3. Çakışma Sayımı ve Silme (Greedy Intervals)
* **Algoritma:** Birleştirmek yerine, geri kalanların çakışmamasını sağlamak için silinmesi gereken minimum aralık sayısını veya aynı anda yapılabilecek maksimum etkinlik sayısını bulmak isteyebilirsiniz. **`start` zamanına göre sıralayın** (bazı greedy çözümlerde `end` zamanına göre). `prev_end` (önceki bitiş) değerini takip edin. Bir çakışma meydana geldiğinde, silme sayacınızı artırın ve gelecekteki aralıklara daha fazla yer bırakmak için her zaman *daha erken biten* aralığı elinizde tutun (`prev_end = min(prev_end, current_end)`).
* **Ne zaman kullanılır:** Meeting Rooms (Toplantı Odaları) problemlerinde, çakışmayan maksimum etkinlik sayısını bulurken veya çakışmaları (conflict) sayarken.
* **Repo Örnekleri:**
  * [0435-Non-overlapping Intervals](./0435-Non-overlapping%20Intervals)
  * [0252-Meeting Rooms](./0252-Meeting%20Rooms)

### 4. Aralık Kesişimleri (Two Pointers ile)
* **Algoritma:** İki ayrı sıralı aralık listesi (A ve B) verildiğinde, bunların ortak kesişimlerini bulun. İki işaretçi (A için `i`, B için `j`) kullanın. Kesişim ancak `start_max <= end_min` ise mevcuttur. Eğer varsa, kesişim aralığı `[start_max, end_min]` olur. Her adımda, *daha erken biten* aralığın işaretçisini bir adım ilerletin, çünkü erken bitenin gelecekteki aralıklarla kesişme ihtimali kalmamıştır.
* **Ne zaman kullanılır:** İki kişinin programı arasındaki ortak boş zamanı bulurken.
* **Repo Örnekleri:**
  * [0986-Interval List Intersections](./0986-Interval%20List%20Intersections)

---

## 💡 Profesyonel Detaylar ve İstisnai Durumlar

* **Sıralama Zorunludur:** Soruda aralıkların zaten sıralanmış olduğu açıkça belirtilmedikçe, kodunuzun ilk satırı neredeyse her zaman `intervals.sort(key=lambda x: x[0])` olmalıdır.
* **Çakışma Formülü:** `A` ve `B` gibi iki aralık (`A`'nın `B`'den önce başladığı varsayımıyla), yalnızca ve yalnızca `B.start <= A.end` ise çakışır. Tüm bu kalıbın kalbi, bu basit mantıksal kontroldür.
* **Yutulan Aralık Hatası (Subsumed Bug):** İki aralığı birleştirirken, ikinci aralığın bitiş değerinin her zaman daha büyük olduğunu varsaymayın. Örneğin, `[1, 5]` ile `[2, 3]` aralığını birleştirirken ikinci aralık tamamen ilkinin içinde kalır (yutulur). Yeni sınırı belirlerken her zaman `max(A.end, B.end)` kullanın, aksi takdirde birleştirilmiş aralığı yanlışlıkla `[1, 3]`'e daraltırsınız.