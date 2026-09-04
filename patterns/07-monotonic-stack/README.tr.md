> 📌 **Rehber:** Bu dizin, **Monotonic Stack (Monotonik Yığın)** kalıbı için bir Kavram Haritası işlevi görür.
> * **Teorik Mantık:** Temel prensipler, alt varyasyonlar ve zaman/alan karmaşıklığı analizleri için bu `README.tr.md` dosyasını okuyun.
> * **Pratik Uygulamalar:** Kalıbın pratikte nasıl uygulandığını görmek için spesifik soru klasörlerine gidin (örneğin, `0739-Daily Temperatures`). Özel istisnalar (edge cases) ve alternatif çözümler bu klasörlerin içinde belgelenmiştir.

## Monotonic Stack Kalıbı Nedir?

* **Tanım:** Elemanların kesinlikle artan veya kesinlikle azalan bir sırada tutulduğu bir Yığın (Stack) veri yapısıdır. Yeni gelen bir eleman bu sıralama kuralını bozarsa, monotonik durum tekrar sağlanana kadar yığındaki elemanlar çıkarılır (pop).
* **Temel Gücü:** **"Sonraki Daha Büyük Elemanı" (Next Greater Element)** veya **"Sonraki Daha Küçük Elemanı"** bulmak için nihai araçtır. Daha büyük bir değeri bulmak için iç içe döngüler kullanıp ileriye doğru arama yapmak (`O(n²)`) yerine, bu kalıp her elemanı tam olarak iki kez (bir kez ekleyip, bir kez çıkararak) işler ve son derece optimize edilmiş `O(n)` zaman karmaşıklığı sunar.

---

## Temel Varyasyonlar ve Algoritmik Stratejiler

Monotonic Stack, "bekleme" prensibine dayanır. Yığındaki elemanlar, kendilerini çözecek uygun bir eleman gelene kadar "çözülmemiş" (bir sonraki daha büyük/küçük karşılığını bulmayı bekleyen) olarak kalır.

### 1. Sonraki Daha Büyük / Küçük Eleman (Next Greater/Smaller)
* **Algoritma:** Sonraki *daha büyük* elemanı bulmak için **monotonik azalan** bir yığın tutun. Dizi üzerinde gezinin. Yığın boş değilken ve mevcut eleman yığının en üstündeki elemandan *daha büyükse*, üstteki eleman için "sonraki daha büyük elemanı" buldunuz demektir. Üsttekini çıkarın (pop), cevabını kaydedin ve mevcut elemanı yığına ekleyin (push).
* **Ne zaman kullanılır:** Bir problem sizden mevcut elemandan kesinlikle daha büyük veya daha küçük olan sağdaki (veya soldaki) en yakın elemanı bulmanızı istediğinde (örn. "Daha sıcak bir güne kadar kaç gün var?").
* **Repo Örnekleri:**
  * [0739-Daily Temperatures](./0739-Daily%20Temperatures)
  * [0496-Next Greater Element I](./0496-Next%20Greater%20Element%20I)

### 2. Dairesel Diziler (Circular Arrays)
* **Algoritma:** Dizi kendi üzerine kapanır (son eleman tekrar ilk elemana bağlanır). Tek bir geçiş yapmak yerine, döngüyü `2 * n`'e kadar çalıştırarak ve modülo operatörünü (`i % n`) kullanarak dizi üzerinde iki kez gezinin. Monotonik yığın mantığı tamamen aynı kalır.
* **Ne zaman kullanılır:** Dairesel bir yapıda sonraki daha büyük elemanı ararken.
* **Repo Örnekleri:**
  * [0503-Next Greater Element II](./0503-Next%20Greater%20Element%20II)

### 3. Önceki Sınır (Maksimum/Minimum Alan)
* **Algoritma:** Bir elemanın açıklığını (span) veya sınırlarını bulmak için kullanılır. Önceki daha küçük elemanı bulmak için artan bir yığın tutun. Sırayı korumak için elemanları çıkardığınızda (pop), mevcut elemanı eklemeden hemen önce yığının en üstünde *kalan* eleman, o elemanın "önceki daha küçük" sınırıdır.
* **Ne zaman kullanılır:** Histogram problemleri, dikdörtgenlerin maksimum alanlarını hesaplama veya su tutma (trapping water) senaryolarında.
* **Repo Örnekleri:**
  * [0084-Largest Rectangle in Histogram](./0084-Largest%20Rectangle%20in%20Histogram)
  * [0901-Online Stock Span](./0901-Online%20Stock%20Span)

---

## 💡 Profesyonel Detaylar ve İstisnai Durumlar

* **Değerleri Değil, İndeksleri Saklayın:** Monotonic Stack problemlerindeki en önemli profesyonel standart, yığına dizideki sayının kendisini değil, **indeksini** eklemektir. İndeksi saklamak, mesafeyi (örn. `mevcut_indeks - cikarilan_indeks`) kolayca hesaplamanıza olanak tanır ve `nums[indeks]` diyerek değere ulaşmaya devam edebilirsiniz.
* **Kesin ve Kesin Olmayan Monotoniklik (Strict vs. Non-Strict):** Tekrar eden elemanlara (kopyalara) dikkat edin. Problem kesinlikle daha büyük (`>`) olanı istiyorsa, mevcut eleman kesinlikle daha büyük olduğunda pop yapın. Büyük veya eşit (`>=`) olmasını istiyorsa, `while` döngüsü koşulunuzu buna göre ayarlayın.
* **Geriye Kalan Elemanlar:** Döngü bittikten sonra yığında kalan indeksler, kendilerinden sonraki daha büyük/küçük elemanı *hiçbir zaman* bulamayan elemanları temsil eder. Çoğu zaman sonuç dizinizi (result array) en başta `-1` (veya `0`) ile doldurmanız gerekir, böylece çözülemeyen bu elemanlar varsayılan olarak doğru cevaba sahip olur.