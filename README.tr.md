# Data Structures, Algorithms & LeetCode Solutions

Bilgisayar bilimleri temellerinde güçlü bir altyapı oluşturmak ve teknik mülakatlar için pratik problem çözme becerilerini geliştirmek amacıyla özenle hazırlanmış bir koleksiyon. Bu depo; teorik algoritma analizlerini, kalıp tabanlı (pattern-based) kodlama tekniklerini ve Python ile SQL'de optimize edilmiş LeetCode çözümlerini bir araya getirir.

> **Not:** Her klasördeki problem başlıkları, doğrudan ilgili LeetCode problem sayfasına yönlendiren köprüler (hyperlink) içerir.

---

## Depo Yapısı

Depo; teorik kavramları, algoritmik pratiği, veritabanı sorgularını ve temel problemleri birbirinden ayırmak için dört ana bölüme ayrılmıştır:

* **`patterns/`**: Kalıp tabanlı pratik problem çözümleri (Veri Yapıları ve Algoritmalar).
* **`sql/`**: LeetCode SQL problem çözümleri ve sorgu optimizasyonları.
* **`core-concepts/`**: Temel matematik, string manipülasyonu ve simülasyonları içeren temel programlama problemleri.
* **`algorithms/`**: Teorik temeller, matematiksel analizler ve Big-O gösterimi.

### Problem Klasörü Formatı
Hangi bölümde (DSA veya SQL) olursa olsun, her bir problem kendi dizininde saklanır ve şunları içerir:
* `solution.sql` / `solution.py`: Temiz ve optimize edilmiş kod.
* `README.md`: İngilizce problem özeti, adım adım çözüm yaklaşımı ve asimptotik karmaşıklık analizi.
* `README.tr.md`: Problem açıklamasının Türkçe çevirisi ve zaman zaman eklenen kişisel çalışma notları.

---

## 1. Algoritmik Kalıplar (`patterns/`)

Bireysel LeetCode problemlerini ezberlemek yerine, bu bölüm onları 17 temel problem çözme kalıbına (pattern) ayırır. Her problem için, en verimli ve temiz yaklaşıma hemen odaklanmak amacıyla önce **Optimal** çözümü sunuyoruz. Ardından, ekstra teorik bağlam ve karşılaştırma sağlamak için **Brute Force** (kaba kuvvet) veya alternatif çözümleri inceliyoruz.

**`patterns/`**  
├── [01-hash-maps-and-sets](patterns/01-hash-maps-and-sets)  
├── [02-two-pointers](patterns/02-two-pointers)  
├── [03-sliding-window](patterns/03-sliding-window)  
├── [04-prefix-sum](patterns/04-prefix-sum)  
├── [05-fast-and-slow-pointers](patterns/05-fast-and-slow-pointers)  
├── [06-binary-search](patterns/06-binary-search)  
├── [07-monotonic-stack](patterns/07-monotonic-stack)  
├── [08-intervals](patterns/08-intervals)  
├── [09-tree-dfs](patterns/09-tree-dfs)  
├── [10-tree-bfs](patterns/10-tree-bfs)  
├── [11-graphs-and-topological-sort](patterns/11-graphs-and-topological-sort)  
├── [12-heap-and-top-k-elements](patterns/12-heap-and-top-k-elements)  
├── [13-backtracking](patterns/13-backtracking)  
├── [14-dynamic-programming](patterns/14-dynamic-programming)  
├── [15-greedy-algorithms](patterns/15-greedy-algorithms)  
├── [16-trie](patterns/16-trie)  
└── [17-bit-manipulation](patterns/17-bit-manipulation)  

> Her kalıp klasörü, o kalıbın *ne zaman* ve *neden* kullanılacağını açıklayan temel bir `README.md` dosyası ve ardından bu kalıbın uygulandığı ilgili LeetCode problem klasörlerini içerir.

---

## 2. Veritabanı ve SQL (`sql/`)

LeetCode veritabanı problemlerine ayrılmış özel bir bölüm. Bu dizin, SQL kullanarak verimli ve ölçeklenebilir sorgular yazmaya odaklanır. 

Kapsanan konular şunlardır:
* Karmaşık Birleştirmeler (Complex Joins) ve Alt Sorgular (Subqueries)
* Toplama (Aggregations) ve Gruplama (Grouping)
* Pencere Fonksiyonları (Window Functions)
* Sorgu performansı ve çalışma mantığı

---

## 3. Temel Kavramlar (`core-concepts/`)

Bu bölüm, hem standart 17 algoritma kalıbının hem de SQL veritabanı sorgularının dışında kalan temel programlama zorluklarını barındırır. Bunlar; temel dil yeterliliğine, mantıksal kuralları takip etmeye ve temel matematiksel işlemlere odaklanan bağımsız problemlerdir.

Kapsanan konular şunlardır:
* **Temel Matematik (Basic Math):** Tam sayıları ters çevirme, palindrom kontrolleri ve rakam manipülasyonu.
* **String Manipülasyonu:** Ortak ön ek (prefix) arama, metin biçimlendirme ve ayrıştırma (parsing).
* **Simülasyon ve Kural Uygulama:** Adım adım mantık çevirisi (örn. Roma Rakamlarını Tam Sayıya çevirme).

---

## 4. Temel Algoritmalar ve Karmaşıklık Analizi (`algorithms/`)

Deponun teorik ve matematiksel omurgası. Bu bölüm, herhangi bir kod yazmadan önce algoritmik analizin temel kurallarını kapsar.

* **Zaman ve Alan Karmaşıklığı (Time & Space Complexity):** Asimptotik gösterimler (Big O, Big $\Omega$, Big $\Theta$).
* **Analiz Teknikleri:** Döngü maliyetleri, ardışık işlemler, iç içe yapılar ve rekürsif bağıntıların analizi.
* **Klasik Algoritmalar:** Temel arama, sıralama (sorting) ve veri manipülasyon yaklaşımlarının teorik karşılaştırmaları.