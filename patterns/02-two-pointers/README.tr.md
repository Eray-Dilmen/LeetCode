> 📌 **Rehber:** Bu dizin, **Two Pointers (İki İşaretçi)** kalıbı için bir Kavram Haritası işlevi görür.
> * **Teorik Mantık:** Temel prensipler, alt varyasyonlar ve zaman/alan karmaşıklığı analizleri için bu `README.tr.md` dosyasını okuyun.
> * **Pratik Uygulamalar:** Kalıbın pratikte nasıl uygulandığını görmek için spesifik soru klasörlerine gidin (örneğin, `0167-Two Sum II - Input Array Is Sorted`). Özel istisnalar (edge cases) ve alternatif çözümler bu klasörlerin içinde belgelenmiştir.

## Two Pointers Kalıbı Nedir?

* **Tanım:** Bir veri yapısı üzerinde eşzamanlı olarak gezinmek için iki (veya bazen üç) değişken kullanan algoritmik bir tekniktir.
* **Temel Gücü:** İç içe geçmiş döngüleri (`O(n²)`) tek bir eşzamanlı taramaya (`O(n)`) indirgeyerek algoritmaları optimize eder. En önemlisi, sadece işaretçi değişkenleri kullandığı ve ekstra bellek ayırmadığı için alan karmaşıklığını (Space Complexity) kesin bir şekilde `O(1)`'de tutar.

---

## Temel Varyasyonlar ve Algoritmik Stratejiler

"Two Pointers" kalıbı tek bir katı kural değildir; problemin amacına göre şekillenen özel alt varyasyonları vardır.

### 1. Zıt Yönlü İşaretçiler (Opposite Ends / Left & Right)
* **Algoritma:** İşaretçilerden birini dizinin başına (`left = 0`), diğerini sonuna (`right = len - 1`) yerleştirin. Koşulu değerlendirin ve ardından işaretçileri merkeze doğru kaydırın (örn. `left += 1` veya `right -= 1`) ta ki buluşana kadar (`while left < right`).
* **Ne zaman kullanılır:** **Sıralı** bir dizide eş bulmada, simetri kontrolünde (palindromlar) veya uç değerleri kıyaslamada.
* **Temel Şart:** Toplam/Arama problemlerinde dizinin kesinlikle sıralanmış (sorted) olması gerekir.
* **Repo Örnekleri:**
  * [0167-Two Sum II - Input Array Is Sorted](./0167-Two%20Sum%20II%20-%20Input%20Array%20Is%20Sorted)
  * [0125-Valid Palindrome](./0125-Valid%20Palindrome)
  * [0011-Container With Most Water](./0011-Container%20With%20Most%20Water)

### 2. Aynı Yönlü İşaretçiler (Fast & Slow Pointers)
* **Algoritma:** İki işaretçi de `0` indeksinden başlar. `fast` (hızlı) işaretçi elemanları taramak için her adımda ilerler. `slow` (yavaş) işaretçi ise yalnızca belirli bir koşul sağlandığında ilerler ve bir sonraki geçerli elemanın yerleştirileceği konumu tutar.
* **Ne zaman kullanılır:** Diziyi yerinde (in-place) değiştirirken (kopyaları veya sıfırları silme) veya döngü/düğüm tespitinde (Floyd's Cycle).
* **Repo Örnekleri:**
  * [0026-Remove Duplicates from Sorted Array](./0026-Remove%20Duplicates%20from%20Sorted%20Array)
  * [0283-Move Zeroes](./0283-Move%20Zeroes)

### 3. Sabit Nokta + İki İşaretçi (Pivot + Two Pointers / 3Sum)
* **Algoritma:** Bir üçlü (triplet) bulmanız gerektiğinde, dışarıdaki bir döngüyü içerideki Two Pointers ile birleştirmek karmaşıklığı `O(n³)`'ten `O(n²)`'ye düşürür. Bir `for` döngüsü ile ilk elemanı sabitler (pivot) ve kalan iki elemanı bulmak için geri kalan alt dizide **Zıt Yönlü İşaretçiler** tekniğini uygularsınız.
* **Ne zaman kullanılır:** Toplamı belirli bir hedefe ulaşan üçlüleri veya dörtlüleri bulmada.
* **Repo Örnekleri:**
  * [0015-3Sum](./0015-3Sum)

### 4. Bölmeleme / Üç İşaretçi (Partitioning / Dutch National Flag)
* **Algoritma:** Bir diziyi üç farklı bölgeye ayırmak (örn. 0'lar, 1'ler ve 2'ler) için kullanılır. Üç işaretçi tutar: `low` birinci grubun sınırını, `high` üçüncü grubun sınırını, `mid` ise o anki elemanı taramayı sağlar. Elemanlar yerinde (in-place) takas edilir; tek geçişte `O(n)` zaman ve `O(1)` alan karmaşıklığına ulaşılır.
* **Ne zaman kullanılır:** Kütüphane sıralama fonksiyonları kullanmadan, eleman çeşitliliği çok az (3 çeşit) olan dizileri sıralarken.
* **Repo Örnekleri:**
  * [0075-Sort Colors](./0075-Sort%20Colors)

---

## 💡 Profesyonel Detaylar ve İstisnai Durumlar

* **Sınır İhlali (Index Out of Bounds):** Döngü koşullarınızın (`while left < right` veya `while mid <= high`) işaretçilerin hatalı şekilde kesişmesini veya dizinin dışına çıkmasını kesin olarak engellediğinden her zaman emin olun.
* **Kopyaları Engelleme:** Kombinasyon (3Sum gibi) hesaplarken, aynı değeri iki kez işlemekten kaçınmak için yan yana duran aynı sayıları es geçebilirsiniz (`if nums[i] == nums[i-1]: continue`). Bu, kopyaları engellemek için `O(n)` süren bir liste içi arama yapma (linear search) ihtiyacını ortadan kaldırır.