> 📌 **Rehber:** Bu dizin, **Tree BFS (Ağaçlarda Genişlik Öncelikli Arama)** kalıbı için bir Kavram Haritası işlevi görür.
> * **Teorik Mantık:** Temel prensipler, alt varyasyonlar ve zaman/alan karmaşıklığı analizleri için bu `README.tr.md` dosyasını okuyun.
> * **Pratik Uygulamalar:** Kalıbın pratikte nasıl uygulandığını görmek için spesifik soru klasörlerine gidin (örneğin, `0102-Binary Tree Level Order Traversal`). Özel istisnalar (edge cases) ve alternatif çözümler bu klasörlerin içinde belgelenmiştir.

## Tree BFS Kalıbı Nedir?

* **Tanım:** Bir ağaç veri yapısını seviye seviye (yukarıdan aşağıya, soldan sağa) dolaşmak için kullanılan algoritmik bir tekniktir. Önce `root` (kök) ziyaret edilir, ardından kökün doğrudan çocukları (seviye 1), sonra onların çocukları (seviye 2) işlenir. **Kuyruk (Queue - İlk Giren İlk Çıkar / FIFO)** veri yapısı kullanılarak iteratif (döngüsel) olarak uygulanır.
* **Temel Gücü:** Düğümleri yatay gruplar (katmanlar) halinde işlemek ve bir hedefe giden **en kısa yolu (shortest path)** bulmak için nihai araçtır. Merkezden dışa doğru eşit şekilde yayıldığı için, hedefe ilk ulaştığı an matematiksel olarak o hedefe giden en kısa yoldur. Zaman karmaşıklığı **$O(n)$**, alan karmaşıklığı ise **$O(w)$**'dir ($w$ ağacın maksimum genişliğidir, bu da dengeli bir ağacın yaprak seviyesi için $O(n/2)$'ye kadar çıkabilir).

---

## Temel Varyasyonlar ve Algoritmik Stratejiler

`while` döngüsünü nasıl yapılandırdığınız, BFS'nin ağacı nasıl işleyeceğini belirler.

### 1. Standart Seviye Seviye Gezinme (Level-by-Level Traversal)
* **Algoritma:** `root` ile bir kuyruk (queue) başlatın. Dışarıda bir `while queue:` döngüsü kullanın. İçeride, mevcut kuyruk uzunluğunun bir anlık görüntüsünü (snapshot) alın (`level_size = len(queue)`). Sadece o sayıdaki düğümü kuyruktan çıkarmak (pop) için içeride bir `for i in range(level_size):` döngüsü kurun. Bu, onların çocuklarına geçmeden önce kesinlikle sadece mevcut seviyedeki düğümleri işlediğinizi garanti eder.
* **Ne zaman kullanılır:** Düğüm değerlerini derinlik seviyelerine göre gruplamanız gerektiğinde veya her seviyenin en sağındaki/solundaki düğümü bulurken (Right Side View).
* **Repo Örnekleri:**
  * [0102-Binary Tree Level Order Traversal](./0102-Binary%20Tree%20Level%20Order%20Traversal)
  * [0199-Binary Tree Right Side View](./0199-Binary%20Tree%20Right%20Side%20View)

### 2. Erken Çıkış (En Kısa Yol / Minimum Derinlik)
* **Algoritma:** Standart seviye seviye yaklaşımını kullanın, ancak bir `depth` (derinlik) sayacı tutun. Hedef koşulu sağlayan bir düğümü kuyruktan çıkardığınız anda (örneğin, `not node.left and not node.right` olan bir yaprak düğüm), hemen mevcut `depth` değerini döndürün.
* **Ne zaman kullanılır:** Bir ağacın minimum derinliğini veya belirli bir düğüme giden en kısa yolu bulurken. Hedef sadece 2 adım aşağıdayken, DFS yanlış dala girip 10.000 düğümlük devasa bir dalı boş yere tarayarak zaman kaybedebilir. BFS ise hedefe anında ulaşır ve döngüyü kırar; bu yüzden bu durumlarda DFS'den kat kat daha verimlidir.
* **Repo Örnekleri:**
  * [0111-Minimum Depth of Binary Tree](./0111-Minimum%20Depth%20Binary%20Tree)

### 3. Seviye Metrikleri Hesaplama (Level Aggregation)
* **Algoritma:** Seviye seviye gezinmeye benzer. Düğüm değerlerini sadece bir listeye eklemek yerine, dıştaki `while` döngüsünün içinde geçici değişkenler (`level_sum`, `level_max` vb.) tanımlarsınız. İçteki `for` döngüsünde bu değişkenleri günceller ve bir sonraki seviyeye geçmeden önce çıkan sonucu (ortalama, maksimum değer vb.) ana cevaba eklersiniz.
* **Ne zaman kullanılır:** Ağacın her bir spesifik derinlik seviyesi için ortalama, maksimum veya toplam değerleri hesaplarken.
* **Repo Örnekleri:**
  * [0637-Average of Levels in Binary Tree](./0637-Average%20of%20Levels%20in%20Binary%20Tree)
  * [0515-Find Largest Value in Each Tree Row](./0515-Find%20Largest%20Value%20in%20Each%20Tree%20Row)

---

## 💡 Profesyonel Detaylar ve İstisnai Durumlar

* **`deque` Kuralı:** Python'da, kuyruktan ilk elemanı çıkarmak için `pop(0)` kullanıyorsanız, **asla** standart bir liste (`[]`) kullanmayın. Standart bir listeden ilk elemanı sildiğinizde, arkadaki tüm elemanlar bellekte bir sıra kaydırılır. Bu, $O(n)$ zaman alan bir işlemdir ve BFS'nizi ciddi şekilde yavaşlatır. Her zaman `collections.deque` kütüphanesini içe aktarın (import) ve kusursuz `O(1)` sürede çalışan `popleft()` metodunu kullanın.
* **Boş (Null) Düğüm Yönetimi:** Kuyruğa `None` (veya null) değerlerini eklemeyin. Endüstri standardı, çocukları kuyruğa eklemeden önce kontrol etmektir: `if node.left: queue.append(node.left)`. Bu, kuyruğu temiz tutar ve döngünün içinde gereksiz `NoneType` hatalarının oluşmasını engeller.
* **İç Döngü Fotoğrafı (Snapshot):** Yeni başlayanların en sık yaptığı hata, kuyruğun uzunluğunun anlık fotoğrafını (snapshot) almadan dinamik olarak kuyruk üzerinde dönmektir. İçeride başlangıçtaki `len(queue)` ile sınırlandırılmış bir `for` döngüsü kurmazsanız, yeni eklenen çocuk düğümleri de aynı seviyedeymiş gibi eritmeye başlarsınız ve BFS'nin o kusursuz "seviye seviye" gruplandırma mantığı tamamen çöker.