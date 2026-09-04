> 📌 **Rehber:** Bu dizin, **Binary Search (İkili Arama)** kalıbı için bir Kavram Haritası işlevi görür.
> * **Teorik Mantık:** Temel prensipler, alt varyasyonlar ve zaman/alan karmaşıklığı analizleri için bu `README.tr.md` dosyasını okuyun.
> * **Pratik Uygulamalar:** Kalıbın pratikte nasıl uygulandığını görmek için spesifik soru klasörlerine gidin (örneğin, `0704-Binary Search`). Özel istisnalar (edge cases) ve alternatif çözümler bu klasörlerin içinde belgelenmiştir.

## Binary Search Kalıbı Nedir?

* **Tanım:** Sıralı (sorted) bir arama alanını sürekli olarak ikiye bölerek (divide-and-conquer) hedef değeri verimli bir şekilde bulan algoritmik bir tekniktir.
* **Temel Gücü:** Zaman Karmaşıklığını (Time Complexity) $O(n)$'den (doğrusal arama) **$O(\log n)$** (logaritmik zaman) seviyesine indirger. Bu, 1 milyar elemanlı bir dizide bile hedefi bulmanın en fazla 30 adım süreceği anlamına gelir. Döngü (iteratif) ile yazıldığında Alan Karmaşıklığı (Space Complexity) kesinlikle $O(1)$ olur.

---

## Temel Varyasyonlar ve Algoritmik Stratejiler

Binary Search, sadece standart bir dizide sayı bulmakla sınırlı değildir. Sınırları, minimum değerleri veya doğrudan "en uygun cevabı" bulmak için uyarlanabilir.

### 1. Standart Binary Search (Birebir Eşleşme)
* **Algoritma:** `left = 0` ve `right = len(nums) - 1` olarak belirleyin. `while left <= right` döngüsü kullanın. `mid` (orta nokta) hesaplayın. Eğer `nums[mid] == target` ise `mid`'i döndürün. Hedef daha büyükse sol yarıyı çöpe atın (`left = mid + 1`). Hedef daha küçükse sağ yarıyı çöpe atın (`right = mid - 1`).
* **Ne zaman kullanılır:** Kusursuz sıralanmış bir dizide hedef elemanın kesin indeksini bulmanız gerektiğinde.
* **Repo Örnekleri:**
  * [0704-Binary Search](./0704-Binary%20Search)
  * [0035-Search Insert Position](./0035-Search%20Insert%20Position)

### 2. Sınırları Bulma (İlk veya Son Görülme)
* **Algoritma:** Dizide tekrar eden (duplicate) elemanlar var ve hedefin ilk veya son örneğini bulmanız gerekiyor. `nums[mid] == target` olduğunda **hemen return etmeyin**. *İlk* konumu bulmak için konumu kaydedip aramaya sol yarıda devam edin (`right = mid - 1`). *Son* konumu bulmak için konumu kaydedip aramaya sağ yarıda devam edin (`left = mid + 1`).
* **Ne zaman kullanılır:** Problem aralık (range), belirli bir hedefin frekansını veya sıralı loglarda bir olayın ilk/son ne zaman gerçekleştiğini sorduğunda.
* **Repo Örnekleri:**
  * [0034-Find First and Last Position of Element in Sorted Array](./0034-Find%20First%20and%20Last%20Position%20of%20Element%20in%20Sorted%20Array)
  * [0278-First Bad Version](./0278-First%20Bad%20Version)

### 3. Cevap Üzerinde Binary Search (Search Space Optimization)
* **Algoritma:** Aramayı size verilen bir dizi üzerinde değil, **olası cevapların aralığı** üzerinde (örn. minimum kapasite `1`'den maksimum kapasite `max(nums)`'a kadar) yaparsınız. Bir cevap tahmin eder (`mid`) ve bu tahminin problemdeki koşulları sağlayıp sağlamadığını kontrol eden bir `isValid(mid)` yardımcı fonksiyonu yazarsınız. Çıkan boolean (doğru/yanlış) sonuca göre, en küçük veya en büyük geçerli cevabı bulmak için `left` veya `right` işaretçilerini güncellersiniz.
* **Ne zaman kullanılır:** Problem belirli kısıtlamalar dahilinde bir işi tamamlamak için "minimum maksimum", "maksimum minimum" veya "en düşük kapasite/hız" değerini sorduğunda.
* **Repo Örnekleri:**
  * [0875-Koko Eating Bananas](./0875-Koko%20Eating%20Bananas)
  * [1011-Capacity To Ship Packages Within D Days](./1011-Capacity%20To%20Ship%20Packages%20Within%20D%20Days)

### 4. Döndürülmüş (Rotated) Sıralı Dizilerde Arama
* **Algoritma:** Dizi sıralıdır ancak bilinmeyen bir noktadan kaydırılmış/döndürülmüştür (örn. `[4,5,6,7,0,1,2]`). `mid` değerini hesaplayın. **Hangi yarının kusursuz sıralı olduğunu** tespit etmeniz gerekir. Eğer `nums[left] <= nums[mid]` ise, sol yarı sıralıdır. Hedefin bu sıralı aralıkta olup olmadığını kontrol edin; içindeyse sola, değilse sağa gidin. Sağ yarı sıralıysa mantığı tam tersine çevirin.
* **Ne zaman kullanılır:** Döndürülmüş veya kaydırılmış veri dizeleriyle uğraşırken.
* **Repo Örnekleri:**
  * [0033-Search in Rotated Sorted Array](./0033-Search%20in%20Rotated%20Sorted%20Array)
  * [0153-Find Minimum in Rotated Sorted Array](./0153-Find%20Minimum%20in%20Rotated%20Sorted%20Array)

---

## 💡 Profesyonel Detaylar ve İstisnai Durumlar

* **Integer Overflow (Tam Sayı Taşması):** Java veya C++ gibi dillerde, `left` ve `right` çok büyük sayılar olduğunda `mid = (left + right) / 2` hesaplaması bellek taşmasına yol açabilir. Profesyonel endüstri standardı bunu `mid = left + (right - left) / 2` şeklinde hesaplamaktır. (Python devasa sayıları otomatik yönetir, ancak bu matematiği alışkanlık haline getirmek her zaman iyidir).
* **Döngü Koşulu (`<=` vs `<`):** 
  * `mid` elemanını arama alanından tamamen çöpe attığınız durumlarda (`left = mid + 1`, `right = mid - 1`), `while left <= right` kullanın.
  * `mid` elemanının bizzat final cevap olma ihtimalinin bulunduğu ve çöpe atamayacağınız durumlarda (`right = mid`), `while left < right` kullanın.
* **"Sıralı" Ön Şartı:** Binary Search doğası gereği sıralı bir arama alanı gerektirir. Veri sırasızsa, önce veriyi sıralamak için harcanacak $O(n \log n)$ zaman karmaşıklığını hesaba katmalısınız. Bazen bu maliyete girmek yerine, probleme bağlı olarak bir Hash Map ($O(n)$) kullanmak daha iyi bir alternatif olabilir.