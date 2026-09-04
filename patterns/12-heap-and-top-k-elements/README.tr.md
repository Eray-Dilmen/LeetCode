> 📌 **Rehber:** Bu dizin, **Heap (Yığın) & Top K Elements** kalıbı için bir Kavram Haritası işlevi görür.
> * **Teorik Mantık:** Temel prensipler, alt varyasyonlar ve zaman/alan karmaşıklığı analizleri için bu `README.tr.md` dosyasını okuyun.
> * **Pratik Uygulamalar:** Kalıbın pratikte nasıl uygulandığını görmek için spesifik soru klasörlerine gidin (örneğin, `0215-Kth Largest Element in an Array`). Özel istisnalar (edge cases) ve alternatif çözümler bu klasörlerin içinde belgelenmiştir.

## Heap & Top K Elements Kalıbı Nedir?

* **Tanım:** Heap (Yığın), özel bir ağaç tabanlı veri yapısıdır. Bir **Min-Heap**'te ebeveyn düğüm her zaman çocuklarından daha küçük veya onlara eşittir (en küçük eleman her zaman köktedir/root). Bir **Max-Heap**'te ise ebeveyn her zaman daha büyüktür.
* **Temel Gücü:** Bir veri setindeki en büyük, en küçük veya en sık tekrar eden "K" adet elemanı bulmak için nihai araçtır. Tüm bir diziyi sıralamak (sort) **$O(n \log n)$** zaman alır. Ancak boyutunu kesin olarak `k` ile sınırladığınız bir Heap kullanarak, En İyi K (Top K) elemanı **$O(n \log k)$** sürede bulabilirsiniz. Eğer `k` küçük bir sayıysa, bu yöntem çok daha hızlıdır ve bellekte yalnızca **$O(k)$** ekstra alan (auxiliary space) kullanır.

---

## Temel Varyasyonlar ve Algoritmik Stratejiler

Heap'ler, dizinin geri kalanının kusursuz bir şekilde sıralanmasına gerek kalmadan "en iyi", "en yakın" veya "en sık" elemanlar istendiğinde evrensel olarak kullanılır.

### 1. En Büyük / En Küçük K Eleman
* **Algoritma:** En büyük K elemanı bulmak için `k` boyutunda bir **Min-Heap** tutun. Dizi üzerinde gezinin ve her elemanı yığına (push) ekleyin. Yığının boyutu `k`'yı aşarsa, kökü çıkarın (pop). Min-Heap'te kök her zaman en küçük eleman olduğu için, bu işlem sayesinde küçük elemanları sürekli çöpe atmış olursunuz. Döngü bittiğinde yığında tam olarak en büyük `k` adet eleman kalır. En küçük elemanları bulmak için mantığı tersine çevirin (Max-Heap kullanın).
* **Ne zaman kullanılır:** K'ıncı en büyük/en küçük eleman veya başlangıç noktasına en yakın K nokta sorulduğunda.
* **Repo Örnekleri:**
  * [0215-Kth Largest Element in an Array](./0215-Kth%20Largest%20Element%20in%20an%20Array)
  * [0973-K Closest Points to Origin](./0973-K%20Closest%20Points%20to%20Origin)

### 2. En Sık Tekrar Eden K Eleman (Top K Frequent)
* **Algoritma:** Önce, tüm elemanların frekanslarını saymak için bir Hash Map kullanın ($O(n)$ sürer). Ardından, Hash Map üzerinde dönerek `(frekans, eleman)` formatındaki tuple'ları (demetleri) `k` boyutunda bir Min-Heap'e ekleyin. Boyut `k`'yı geçerse en küçüğü pop edin. Heap, tuple'ları otomatik olarak ilk değere (frekansa) göre sıralar.
* **Ne zaman kullanılır:** Verileri görülme sıklığına veya popülerliğine göre filtrelerken.
* **Repo Örnekleri:**
  * [0347-Top K Frequent Elements](./0347-Top%20K%20Frequent%20Elements)
  * [0692-Top K Frequent Words](./0692-Top%20K%20Frequent%20Words)

### 3. K Yönlü Birleştirme (K-way Merge)
* **Algoritma:** Size `k` adet sıralı dizi veya Bağlı Liste (Linked List) verilir ve bunları tek bir sıralı listede birleştirmeniz istenir. `k` adet listenin ilk elemanlarını bir Min-Heap'e atın. Heap'ten mutlak en küçük elemanı (kökü) pop edin, sonucunuza ekleyin ve hemen ardından **o pop edilen elemanın geldiği listedeki bir sonraki elemanı** Heap'e ekleyin.
* **Ne zaman kullanılır:** Eşzamanlı akan birden fazla sıralı veri akışını tek potada eritirken.
* **Repo Örnekleri:**
  * [0023-Merge k Sorted Lists](./0023-Merge%20k%20Sorted%20Lists)

### 4. İki Heap (Veri Akışının Medyanını Bulma)
* **Algoritma:** Dinamik olarak büyüyen bir sayı akışının medyanını (ortanca değerini) $O(1)$ sürede bulmak için iki Heap tutun. Sayıların küçük olan yarısını saklamak için bir **Max-Heap**, büyük olan yarısını saklamak için bir **Min-Heap** kullanın. İkisi arasındaki boyut farkı asla 1'i geçmeyecek şekilde onları dengeleyin. Medyan, ya boyutu büyük olan Heap'in köküdür ya da her iki kökün ortalamasıdır.
* **Ne zaman kullanılır:** Hareketli medyanları hesaplarken veya bir veri setinin dinamik yarılarını dengelerken.
* **Repo Örnekleri:**
  * [0295-Find Median from Data Stream](./0295-Find%20Median%20from%20Data%20Stream)

---

## 💡 Profesyonel Detaylar ve İstisnai Durumlar

* **Python Max-Heap Hilesi:** Python'ın yerleşik `heapq` modülü yalnızca Min-Heap sunar. Bir Max-Heap simüle etmek (taklit etmek) için, değerleri yığına eklemeden önce `-1` ile çarpın. Onları pop edip dışarı çıkardığınızda, orijinal değere dönüştürmek için tekrar `-1` ile çarpın.
* **Tuple Karşılaştırmaları (Tie-Breaker):** Heap içine `(öncelik, değer)` gibi tuple'lar eklediğinizde, Heap bunları `öncelik` (ilk eleman) bazında karşılaştırır. Ancak, iki öğe *tam olarak aynı önceliğe* sahipse, Heap bu kez `değer` (ikinci eleman) bazında karşılaştırma yapmaya çalışır. Eğer `değer` karşılaştırmayı desteklemeyen bir nesneyse (örneğin özel bir sınıf veya ListNode), Python `TypeError` fırlatır. Bunu çözmek için araya benzersiz bir sayaç veya ID ekleyin: `(öncelik, tie_breaker_id, değer)`.
* **Heapify vs. Push:** Eğer elinizde zaten elemanlarla dolu bir dizi varsa ve bunu bir yığına dönüştürmek istiyorsanız, bir `for` döngüsü kullanıp elemanları tek tek push etmeyin (bu $O(n \log n)$ sürer). Bunun yerine, diziyi yerinde (in-place) kesin olarak **$O(n)$** sürede yeniden düzenleyen `heapq.heapify(dizi)` fonksiyonunu kullanın.