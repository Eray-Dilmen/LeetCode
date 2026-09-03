# Algoritmik Kalıplar (Algorithmic Patterns)

Bu dizin, LeetCode ve teknik mülakatlarda karşılaşılan problemleri ezberlemek yerine belirli tasarım kalıplarına (patterns) göre sınıflandırarak çözmeyi hedefler.

---

## Neden Kalıp Tabanlı Yaklaşım?

* **Tanıma Kolaylığı:** Yeni bir problemle karşılaşıldığında, problemin anahtar ipuçlarına bakarak hangi kalıbın (örneğin *Two Pointers* veya *Sliding Window*) uygulanacağını hızlıca belirlemeyi sağlar.
* **Karmaşıklık Optimizasyonu:** Brute Force çözümden ($O(n^2)$ vb.) en uygun veri yapısı veya algoritma kalıbı kullanılarak optimal sonuca (O(n), O(log n) vb.) geçiş adımlarını standartlaştırır.

---

## Kalıp Listesi

| # | Kalıp Adı | Açıklama |
|---|---|---|
| **01** | [01-hash-maps-and-sets](./01-hash-maps-and-sets/) | $O(1)$ frekans takibi, varlık kontrolü ve hızlı erişim |
| **02** | `02-two-pointers` | Sıralı dizilerde çift yönlü/aynı yönlü tarama |
| **03** | `03-sliding-window` | Alt dizi (subarray/substring) problemlerinde dinamik/sabit pencereleme |
| **04** | `04-prefix-sum` | Aralık toplamı ve kümülatif sorguları $O(1)$ sürede hesaplama |
| **05** | `05-fast-and-slow-pointers` | Bağlı liste ve döngü tespiti (Floyd's Cycle Algorithm) |
| **06** | `06-binary-search` | Sıralı uzayda $O(\log n)$ arama ve optimizasyon aralıkları |
| **07** | `07-monotonic-stack` | Sonraki/önceki daha büyük/küçük eleman tespiti |
| **08** | `08-intervals` | Çakışan aralıkların birleştirilmesi ve yerleşimi |
| **09** | `09-tree-dfs` | Ağaçlarda derinlik öncelikli özyinelemeli arama |
| **10** | `10-tree-bfs` | Ağaçlarda seviye bazlı (level-order) arama |
| **11** | `11-graphs-and-topological-sort` | Çizge gezintisi, döngü kontrolü ve bağımlılık sıralaması |
| **12** | `12-heap-and-top-k-elements` | En büyük/en küçük $k$ eleman ve öncelik kuyrukları |
| **13** | `13-backtracking` | Permütasyon, kombinasyon ve olası durum uzayı taraması |
| **14** | `14-dynamic-programming` | Alt problem optimizasyonu ve durum geçişleri (Memoization/Tabulation) |
| **15** | `15-greedy-algorithms` | Lokal optimum seçimlerle global optimuma ulaşma |
| **16** | `16-trie` | Prefix (ön ek) tabanlı metin ve sözlük aramaları |
| **17** | `17-bit-manipulation` | Bit seviyesinde işlemler ve optimizasyonlar |

---

## Kalıp İçi Standart Yapı

Her kalıp klasörünün içinde iki temel yapı bulunur:
1. **`README.md`:** Kalıbın çalışma mantığı, ne zaman kullanılacağı ve şablon yaklaşımları.
2. **Soru Klasörleri (Örn: `771-Jewels and Stones/`):** Problemin açıklaması, Brute Force yaklaşımı, Optimal yaklaşımı ve karmaşıklık analizi.