# Algoritmik Kalıplar (Patterns)

Bu dizin, LeetCode ve teknik mülakatlarda karşılaşılan problemleri ezbere dayalı çözmek yerine, onları belirli tasarım kalıplarına göre sınıflandırarak çözmeyi amaçlamaktadır.

---

## Neden Kalıp (Pattern) Odaklı Yaklaşım?

* **Kolay Tanıma:** Yeni bir problemle karşılaştığınızda, kilit ipuçlarını belirlemek hangi kalıbı uygulayacağınızı (örn. *Two Pointers* veya *Sliding Window*) hızlıca tespit etmenizi sağlar.
* **Karmaşıklık Optimizasyonu:** Kaba kuvvet (Brute Force) çözümünden (örn. $O(n^2)$), en uygun veri yapısı veya algoritmik kalıbı kullanarak optimal sonuca (örn. $O(n)$ veya $O(\log n)$) geçiş adımlarını standartlaştırır.

---

## Veri Yapıları ve Algoritmalar: Pattern Karar Ağacı

Kalıpları düz bir liste halinde ezberlemek yerine, problemde size verilen **Veri Yapısına (Data Structure)** bakarak doğru **Kalıbı (Pattern)** eşleştirmek için aşağıdaki karar ağacını kullanın.

### 1. Diziler (Arrays) ve Metinler (Strings)
Problem bir dizi/metin üzerinde gezinmeyi veya işlem yapmayı içeriyorsa kendinize sorun:
* **$O(1)$ arama hızına veya frekans sayımına mı ihtiyacım var?** $\rightarrow$ `01-hash-maps-and-sets`
* **Dizi sıralanmış mı (sorted)?** $\rightarrow$ `02-two-pointers` veya `06-binary-search`
* **Bitişik bir alt dizi (subarray) veya alt metin mi arıyorum?** $\rightarrow$ `03-sliding-window`
* **Alt dizilerin toplamlarını birden fazla kez mi sorguluyorum?** $\rightarrow$ `04-prefix-sum`
* **Bir "sonraki daha büyük/küçük" (next greater) elemanı mı bulmam gerekiyor?** $\rightarrow$ `07-monotonic-stack`
* **Çakışan zaman aralıklarını/menzilleri mi birleştiriyorum?** $\rightarrow$ `08-intervals`

### 2. Bağlı Listeler (Linked Lists)
Problem ardışık olarak birbirini gösteren düğümler içeriyorsa:
* **$O(1)$ alan kullanarak döngü, orta nokta veya kopya kontrolü mü yapıyorum?** $\rightarrow$ `05-fast-and-slow-pointers`

### 3. Ağaçlar (Trees) ve Çizgeler (Graphs)
Problem hiyerarşik veri, ağlar veya matrisler (grid) içeriyorsa:
* **Kökten yaprağa (root-to-leaf) yolları mı inceliyorum veya BST'yi mi doğruluyorum?** $\rightarrow$ `09-tree-dfs`
* **En kısa yolu (shortest path) veya seviye bazlı verileri mi arıyorum?** $\rightarrow$ `10-tree-bfs`
* **Ortada bir bağımlılık/önkoşul zinciri mi var?** $\rightarrow$ `11-graphs-and-topological-sort`
* **Devasa boyutlarda metin ön ek (prefix) araması mı yapıyorum?** $\rightarrow$ `16-trie`

### 4. Arama, Optimizasyon ve Kombinasyon
Problem "en iyi", "tüm olası" veya "en verimli" yolu soruyorsa:
* **En büyük/küçük K (Top K) elemanlara mı ihtiyacım var?** $\rightarrow$ `12-heap-and-top-k-elements`
* **TÜM olası kombinasyonları/permütasyonları mı istiyor?** $\rightarrow$ `13-backtracking`
* **Tekrar eden alt problemlerle (overlapping) min/maks/toplam yol sayısını mı soruyor?** $\rightarrow$ `14-dynamic-programming`
* **Sadece yerel (local) en iyiyi seçerek genel (global) optimuma ulaşabiliyor muyum?** $\rightarrow$ `15-greedy-algorithms`

### 5. Matematik ve Donanım Seviyesi
* **Aşırı hızlı, $O(1)$ alan kullanan mantıksal bayraklara veya XOR mantığına mı ihtiyacım var?** $\rightarrow$ `17-bit-manipulation`

---

## Kalıp (Pattern) Listesi

| # | Pattern Adı | Açıklama |
|---|---|---|
| **01** | [01-hash-maps-and-sets](./01-hash-maps-and-sets/) | $O(1)$ sürede frekans takibi, varlık kontrolü ve hızlı arama |
| **02** | [02-two-pointers](./02-two-pointers/) | Sıralı dizilerde çift yönlü veya aynı yönlü gezinme |
| **03** | [03-sliding-window](./03-sliding-window/) | Alt dizi/metin problemlerinde dinamik veya sabit pencereleme |
| **04** | [04-prefix-sum](./04-prefix-sum/) | Menzil toplamlarını ve kümülatif sorguları $O(1)$ sürede hesaplama |
| **05** | [05-fast-and-slow-pointers](./05-fast-and-slow-pointers/) | Bağlı liste gezinmesi ve döngü tespiti (Floyd Cycle) |
| **06** | [06-binary-search](./06-binary-search/) | Sıralı uzaylarda $O(\log n)$ sürede arama ve optimizasyon |
| **07** | [07-monotonic-stack](./07-monotonic-stack/) | Sonraki/önceki daha büyük/küçük elemanları bulma |
| **08** | [08-intervals](./08-intervals/) | Çakışan aralıkları birleştirme ve araya ekleme |
| **09** | [09-tree-dfs](./09-tree-dfs/) | Ağaçlarda derinlik öncelikli (DFS) özyinelemeli gezinme |
| **10** | [10-tree-bfs](./10-tree-bfs/) | Ağaçlarda genişlik öncelikli (BFS) seviye seviye gezinme |
| **11** | [11-graphs-and-topological-sort](./11-graphs-and-topological-sort/) | Graf gezinmesi, döngü tespiti ve bağımlılık (dependency) sıralaması |
| **12** | [12-heap-and-top-k-elements](./12-heap-and-top-k-elements/) | Öncelik kuyrukları kullanarak en iyi/alt $k$ elemanı bulma |
| **13** | [13-backtracking](./13-backtracking/) | Permütasyon, kombinasyon ve durum-uzay ağacı (state-space tree) gezinmesi |
| **14** | [14-dynamic-programming](./14-dynamic-programming/) | Alt problem optimizasyonu ve durum geçişleri (Memoization/Tabulation) |
| **15** | [15-greedy-algorithms](./15-greedy-algorithms/) | Yerel optimal seçimler üzerinden global optimuma ulaşma |
| **16** | [16-trie](./16-trie/) | Ön eke (prefix) dayalı metin ve sözlük aramaları |
| **17** | [17-bit-manipulation](./17-bit-manipulation/) | Bit düzeyinde işlemler ve optimizasyonlar |

---

## Standart Kalıp (Pattern) Yapısı

Her pattern dizini iki temel bileşenden oluşur:
1. **`README.md`:** Pattern'in temel mantığı, ne zaman kullanılacağı ve şablon kod yaklaşımları.
2. **Soru Klasörleri (örn. `0771-Jewels and Stones/`):** Problemin açıklaması, Brute Force yaklaşımı, Optimal yaklaşımı ve karmaşıklık analizi.