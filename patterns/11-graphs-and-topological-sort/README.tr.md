> 📌 **Rehber:** Bu dizin, **Graphs & Topological Sort (Çizgeler ve Topolojik Sıralama)** kalıbı için bir Kavram Haritası işlevi görür.
> * **Teorik Mantık:** Temel prensipler, alt varyasyonlar ve zaman/alan karmaşıklığı analizleri için bu `README.tr.md` dosyasını okuyun.
> * **Pratik Uygulamalar:** Kalıbın pratikte nasıl uygulandığını görmek için spesifik soru klasörlerine gidin (örneğin, `0200-Number of Islands`). Özel istisnalar (edge cases) ve alternatif çözümler bu klasörlerin içinde belgelenmiştir.

## Graphs ve Topological Sort Kalıbı Nedir?

* **Tanım:** Çizge (Graph), **Düğümler (Vertices/Nodes)** ve bu düğümleri birbirine bağlayan **Kenarlardan (Edges)** oluşan bir veri yapısıdır. Yönlü (tek yön) veya yönsüz (çift yön) olabilir. Topolojik Sıralama (Topological Sort) ise Yönlü ve Döngüsüz Çizgelerde (DAG - Directed Acyclic Graph) kullanılan özel bir algoritmadır. Düğümleri doğrusal olarak öyle bir sıralar ki, her `u -> v` yönlü kenarı için, `u` düğümü sıralamada `v`'den önce gelir.
* **Temel Gücü:** Graflar; sosyal ağlar, şehir haritaları ve ağ yönlendirmeleri gibi karmaşık, doğrusal olmayan ilişkileri modeller. Topolojik Sıralama ise özel olarak **bağımlılık zincirlerini** (örneğin, önkoşullu dersler, görev zamanlaması) `O(V + E)` (Düğüm + Kenar) süresinde çözer. Bu yönüyle, birbirine bağımlı olayları sıraya koymak için nihai araçtır.

---

## Temel Varyasyonlar ve Algoritmik Stratejiler

Graf problemleri genellikle gezinme (ağı keşfetme) veya sıralama (bağımlılıkları çözme) olarak ikiye ayrılır.

### 1. Matris / Izgara Gezinmesi (Örtülü Çizgeler - Implicit Graphs)
* **Algoritma:** 2B (2D) bir ızgara aslında örtülü bir graftır; her hücre bir düğüm ve 4 yönü (yukarı, aşağı, sol, sağ) kenarlarıdır. Bağlı bileşenleri keşfetmek için DFS (Özyineleme) veya BFS (Kuyruk) kullanın. **En kritik adım:** Sonsuz döngüleri önlemek için ziyaret edilen hücreleri mutlaka işaretlemelisiniz (örneğin, `1`'i `0` yapmak veya bir `visited` kümesi kullanmak).
* **Ne zaman kullanılır:** Adaları bulurken, bağlantılı bölgelerin alanını hesaplarken veya labirentlerde gezinirken.
* **Repo Örnekleri:**
  * [0200-Number of Islands](./0200-Number%20of%20Islands)
  * [0695-Max Area of Island](./0695-Max%20Area%20of%20Island)

### 2. Standart Graf DFS/BFS (Açık Çizgeler - Explicit Graphs)
* **Algoritma:** Graf size bir Komşuluk Listesi (Adjacency List - bir düğümü komşularının listesiyle eşleyen bir sözlük) veya Kenar Listesi (Edge List) olarak verilir. Önce Komşuluk Listesini inşa edersiniz. Daha sonra, bir `visited` (ziyaret edildi) kümesi kullanarak yolları keşfetmek, grafı kopyalamak veya ağırlıksız ağlarda en kısa yolu bulmak için DFS veya BFS yaparsınız.
* **Ne zaman kullanılır:** Ağ bağlantılarını haritalarken, ortak arkadaşları bulurken veya bir graf yapısını kopyalarken (Clone).
* **Repo Örnekleri:**
  * [0133-Clone Graph](./0133-Clone%20Graph)
  * [0323-Number of Connected Components in an Undirected Graph](./0323-Number%20of%20Connected%20Components%20in%20an%20Undirected%20Graph)

### 3. Topolojik Sıralama (Kahn Algoritması / BFS Yaklaşımı)
* **Algoritma:** İlk olarak, her düğüm için `in-degree` (giriş derecesi - ona doğru gelen kenar sayısı) değerini hesaplayın. `in-degree` değeri 0 olan (hiçbir önkoşulu olmayan) tüm düğümleri bir Kuyruğa (Queue) atın. Kuyruk boş değilken; bir düğümü çıkarın, topolojik sıralama sonuç listenize ekleyin ve tüm komşularının `in-degree` değerini 1 azaltın. Eğer bir komşunun `in-degree` değeri 0'a düşerse, onu da kuyruğa ekleyin.
* **Ne zaman kullanılır:** Önkoşulları olan görevleri zamanlarken, yazılım derleme (build) sıralarını belirlerken veya kod bağımlılıklarını çözerken.
* **Repo Örnekleri:**
  * [0207-Course Schedule](./0207-Course%20Schedule)
  * [0210-Course Schedule II](./0210-Course%20Schedule%20II)

### 4. Yönlü Çizgelerde Döngü Tespiti (Cycle Detection)
* **Algoritma:** Eğer yönlü bir grafikte döngü (kısır döngü/cycle) varsa, geçerli bir Topolojik Sıralama yapmak imkansızdır. Kahn Algoritmasını kullanırken, nihai topolojik sıralama dizisinin uzunluğu toplam düğüm sayısından *daha az* çıkarsa, bu geri kalan düğümlerin bir döngüye sıkıştığı (in-degree değerlerinin asla 0'a ulaşmadığı) anlamına gelir.
* **Ne zaman kullanılır:** Bir dizi görevi bitirmenin matematiksel olarak mümkün olup olmadığını doğrularken veya yazılım modüllerindeki dairesel (circular) bağımlılıkları tespit ederken.
* **Repo Örnekleri:**
  * [0207-Course Schedule](./0207-Course%20Schedule) (çoğunlukla sadece döngü tespiti için kullanılır)

---

## 💡 Profesyonel Detaylar ve İstisnai Durumlar

* **Kopuk Graf Tuzağı (Disconnected Graph):** Bir graf her zaman tek parça, birbirine bağlı bir ağ olmak zorunda değildir; izole edilmiş adaları (düğümleri) olabilir. Her zaman girdideki *tüm* düğümler üzerinde dönen dış bir döngü (outer loop) kullanın. Bir düğüm `visited` (ziyaret edildi) içinde *değilse*, DFS/BFS taramanızı ancak o zaman o düğümden başlatın.
* **Komşuluk Listesi vs. Matris:** Profesyonel hayatta, bir Kenar Listesini (örn. `[[0, 1], [1, 2]]`) tarama işlemlerine başlamadan önce mutlaka bir Komşuluk Listesine (Adjacency List - sözlük/dictionary formatında) dönüştürün. Komşuluk Listesi üzerinde gezinmek $O(V + E)$ sürerken, bir Kenar Listesini tekrar tekrar aramak programınızı yavaşlatarak $O(V \times E)$ süresine geriletebilir.
* **DFS ile Topolojik Sıralama (Alternatif):** Topolojik sıralama, 3 durumlu (0 = ziyaret edilmedi, 1 = ziyaret ediliyor, 2 = ziyaret edildi) özyinelemeli (recursive) bir DFS kullanılarak da yapılabilir. Eğer `1` durumunda bir düğüme rastlarsanız döngü (cycle) tespit etmiş olursunuz. Başarılı olursa, tüm komşularını ziyaret ettikten *sonra* düğümü bir yığına (stack) eklersiniz ve en sonda yığını tersine çevirirsiniz. Ancak Kahn'ın (BFS) algoritması genellikle uygulaması ve mantığını kavraması daha kolay olan yöntemdir.