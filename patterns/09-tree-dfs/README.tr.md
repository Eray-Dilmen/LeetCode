> 📌 **Rehber:** Bu dizin, **Tree DFS (Ağaçlarda Derinlik Öncelikli Arama)** kalıbı için bir Kavram Haritası işlevi görür.
> * **Teorik Mantık:** Temel prensipler, alt varyasyonlar ve zaman/alan karmaşıklığı analizleri için bu `README.tr.md` dosyasını okuyun.
> * **Pratik Uygulamalar:** Kalıbın pratikte nasıl uygulandığını görmek için spesifik soru klasörlerine gidin (örneğin, `0104-Maximum Depth of Binary Tree`). Özel istisnalar (edge cases) ve alternatif çözümler bu klasörlerin içinde belgelenmiştir.

## Tree DFS Kalıbı Nedir?

* **Tanım:** Ağaç (Tree) veri yapılarını gezmek veya aramak için kullanılan algoritmik bir tekniktir. `root` (kök) düğümünden başlar ve geri adım atmadan (backtracking) önce her bir dal boyunca olabildiğince derine iner. Neredeyse her zaman **Özyineleme (Recursion)** kullanılarak (ki bu sistemin çağrı yığınını kullanır) veya açık bir Yığın (Stack) ile iteratif olarak uygulanır.
* **Temel Gücü:** DFS, ağaçların özyinelemeli ve hiyerarşik doğasıyla kusursuz bir şekilde eşleşir. Karmaşık işaretçi (pointer) yönlendirmeleri yapmak yerine, tek bir düğüm için mantığı tanımlarsınız ve gerisini özyinelemenin (recursion) halletmesine izin verirsiniz. Zaman karmaşıklığı kesin olarak **$O(n)$**'dir (her düğümü bir kez ziyaret eder) ve alan karmaşıklığı **$O(h)$**'dir ($h$ ağacın yüksekliğidir ve maksimum çağrı yığını derinliğini temsil eder).

---

## Temel Varyasyonlar ve Algoritmik Stratejiler

Ağaç DFS algoritmaları genellikle iki temel kavramsal yaklaşıma ayrılır: bilgiyi çocuklara (aşağı) aktarmak veya bilgiyi ebeveynlere (yukarı) aktarmak.

### 1. Yukarıdan Aşağıya DFS (Top-Down / Pre-order Traversal)
* **Algoritma:** Önce mevcut `node` (düğüm) işlenir, ardından `node.left` ve `node.right` üzerinde özyinelemeli DFS çağrıları yapılır. Genellikle bir durumu (mevcut yol veya o ana kadarki toplam gibi) parametre olarak alt çağrılara aktarırsınız.
* **Ne zaman kullanılır:** Bir düğümün karar mantığı kökten kendisine kadar olan yola bağlı olduğunda veya belirli bir koşulu karşılayan "kökten yaprağa" (root-to-leaf) bir yol ararken.
* **Repo Örnekleri:**
  * [0112-Path Sum](./0112-Path%20Sum)
  * [0144-Binary Tree Preorder Traversal](./0144-Binary%20Tree%20Preorder%20Traversal)

### 2. Aşağıdan Yukarıya DFS (Bottom-Up / Post-order Traversal)
* **Algoritma:** Mevcut `node` işlenmeden *önce* `node.left` ve `node.right` üzerinde özyinelemeli (recursive) DFS çağrıları yapılır. Temel durum (base case) bir değer döndürür ve ebeveyn düğüm, sol ve sağ çocuklarından gelen dönüş değerlerini kullanarak kendi cevabını hesaplar; ardından bu cevabı kendi ebeveynine döndürür.
* **Ne zaman kullanılır:** Bir düğümün cevabı tamamen alt ağaçlarının (subtrees) cevaplarına bağlı olduğunda (örn. yüksekliği hesaplama, çapı bulma veya ağacın dengeli olup olmadığını kontrol etme).
* **Repo Örnekleri:**
  * [0104-Maximum Depth of Binary Tree](./0104-Maximum%20Depth%20of%20Binary%20Tree)
  * [0543-Diameter of Binary Tree](./0543-Diameter%20of%20Binary%20Tree)
  * [0236-Lowest Common Ancestor of a Binary Tree](./0236-Lowest%20Common%20Ancestor%20of%20a%20Binary%20Tree)

### 3. In-order Gezinme ve İkili Arama Ağaçları (BST)
* **Algoritma:** Önce `node.left` gezilir, sonra `node` işlenir, son olarak `node.right` gezilir.
* **BST Süper Gücü:** Geçerli bir İkili Arama Ağacında (sol çocukların kesinlikle daha küçük, sağ çocukların kesinlikle daha büyük olduğu ağaçlar) In-order DFS yaparsanız, düğümleri **kusursuz olarak sıralanmış, artan düzende** ziyaret eder.
* **Ne zaman kullanılır:** Bir ağacın geçerli bir BST olup olmadığını doğrularken, K'ıncı en küçük/en büyük elemanı bulurken veya bir BST'yi sıralı bir diziye (array) dönüştürürken.
* **Repo Örnekleri:**
  * [0098-Validate Binary Search Tree](./0098-Validate%20Binary%20Search%20Tree)
  * [0230-Kth Smallest Element in a BST](./0230-Kth%20Smallest%20Element%20in%20a%20BST)

---

## 💡 Profesyonel Detaylar ve İstisnai Durumlar

* **Nihai Temel Durum (The Ultimate Base Case):** Neredeyse her DFS fonksiyonunun ilk satırı `if not node: return ...` olmalıdır. `None` (veya `null`) düğümünü yakalayamamak, `AttributeError: 'NoneType' has no attribute 'left'` istisnalarının (hata) 1 numaralı nedenidir.
* **Global Değişkenler ve Return Değerleri:** Aşağıdan Yukarıya DFS (Bottom-Up) yaparken (bir ağacın çapını bulmak gibi), genellikle yüksekliği ebeveyne döndürmeniz gerekir, ancak aynı zamanda dönüş yolunun bir parçası olmayan bir `max_diameter` (maksimum çap) değerini de güncellemeniz gerekir. Profesyonel standart, dağınık global değişkenlere güvenmek yerine bu global durumu takip etmek için sınıf düzeyinde bir değişken (örn. `self.max_diameter`) veya değiştirilebilir (mutable) bir dizi (`[0]`) kullanmaktır.
* **Recursion Sınırı:** Python'ın varsayılan bir özyineleme derinliği sınırı vardır (genellikle 1000). Çizgi şeklini alan, aşırı dengesiz derin ağaçlarda (Linked List'e dönüşen ağaçlar), özyinelemeli bir DFS `RecursionError` fırlatabilir. Üretim (production) kodunda, eğer ağaçlar devasa ve dengesizse, DFS'yi açık bir `Stack` dizisi kullanarak iteratif (döngüsel) olarak yeniden yazmalısınız.