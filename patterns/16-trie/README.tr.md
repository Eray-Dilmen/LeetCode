> 📌 **Rehber:** Bu dizin, **Trie (Ön Ek Ağacı)** kalıbı için bir Kavram Haritası işlevi görür.
> * **Teorik Mantık:** Temel prensipler, alt varyasyonlar ve zaman/alan karmaşıklığı analizleri için bu `README.tr.md` dosyasını okuyun.
> * **Pratik Uygulamalar:** Kalıbın pratikte nasıl uygulandığını görmek için spesifik soru klasörlerine gidin (örneğin, `0208-Implement Trie (Prefix Tree)`). Özel istisnalar (edge cases) ve alternatif çözümler bu klasörlerin içinde belgelenmiştir.

## Trie (Prefix Tree) Kalıbı Nedir?

* **Tanım:** Trie ("tray" diye okunur), anahtarların (keys) genellikle string (metin) olduğu dinamik bir kümeyi depolamak için kullanılan özel bir ağaç veri yapısıdır. İkili arama ağaçlarından farklı olarak, düğümlerin (nodes) kendisi o düğümle ilişkili anahtarı saklamaz; bunun yerine, düğümün ağaçtaki konumu (yolu) temsil ettiği anahtarı tanımlar.
* **Temel Gücü:** **Ön Ek Eşleştirme (Prefix Matching)** ve **Otomatik Tamamlama (Autocomplete)** sistemleri için nihai araçtır. Bir Hash Set, tam bir kelimeyi $O(1)$ sürede bulabilirken, "oto-" ile başlayan tüm kelimeleri kolayca bulamaz. Bir Trie, ağaçta kaç milyon kelime depolanmış olursa olsun, bir kelimeyi veya ön eki kesin olarak **$O(L)$** süresinde (buradaki $L$ kelimenin uzunluğudur) bulur.

---

## Temel Varyasyonlar ve Algoritmik Stratejiler

Trie kalıbı, özel bir `TrieNode` sınıfı oluşturmak ve bunu karakter karakter dolaşmak etrafında şekillenir.

### 1. Standart Trie (Ekleme / Arama / Ön Ek Kontrolü)
* **Algoritma:** Çocuklarını (children) tutmak için bir Hash Map (veya 26 elemanlı bir dizi) ve bir boolean `is_word` (kelime mi?) bayrağı içeren bir `TrieNode` oluşturun.
  * **Insert (Ekleme):** Kelimenin karakterleri üzerinde dönün. Eğer karakter mevcut düğümün çocuklarında yoksa, yeni bir düğüm oluşturun. İşaretçiyi aşağıya kaydırın. Son düğümün `is_word = True` bayrağını işaretleyin.
  * **Search (Arama):** Karakterleri kullanarak aşağı doğru ilerleyin. Bir karakter eksikse hemen `False` döndürün. Kelimenin sonuna gelirseniz, o düğümdeki `is_word` bayrağının durumunu döndürün.
  * **StartsWith (Ön Ek Kontrolü):** Arama ile aynıdır, tek farkı ön ekin sonuna başarıyla ulaşırsanız doğrudan `True` döndürmenizdir.
* **Ne zaman kullanılır:** Otomatik tamamlama sistemleri, yazım denetleyicileri (spell checker) ve IP yönlendirme sistemleri.
* **Repo Örnekleri:**
  * [0208-Implement Trie (Prefix Tree)](./0208-Implement%20Trie%20%28Prefix%20Tree%29)
  * [0211-Design Add and Search Words Data Structure](./0211-Design%20Add%20and%20Search%20Words%20Data%20Structure)

### 2. Trie + DFS / Backtracking (Matris Gezinmesi)
* **Algoritma:** 2B bir matris içinde birden fazla kelimeyi ararken (Boggle/Word Search oyunu gibi), her kelimeyi DFS ile tek tek aramak inanılmaz derecede yavaştır. Bunun yerine, tüm hedef kelimeleri bir Trie içine ekleyin. Matris üzerinde DFS çalıştırırken, mevcut `TrieNode` nesnesini de parametre olarak geçirin. Eğer matristeki karakter `TrieNode`'un çocuklarında yoksa, o DFS dalını hemen budayın (pruning) ve geri dönün.
* **Ne zaman kullanılır:** Bir matris veya uzun bir string içinde bulmanız gereken bir kelime sözlüğü (dictionary) olduğunda.
* **Repo Örnekleri:**
  * [0212-Word Search II](./0212-Word%20Search%20II)
  * [0140-Word Break II](./0140-Word%20Break%20II)

### 3. Bitwise Trie (Bit Düzeyinde Trie)
* **Algoritma:** Trie karakterleri saklamak yerine, tam sayıların bitlerini (`0` ve `1`) saklar (genellikle 32 seviye derinliğinde). Bir dizideki herhangi iki sayının maksimum XOR sonucunu bulmak için, tüm sayıları Trie'ye ekleyin. Ardından, her sayı için Trie'de aşağı inerken XOR sonucunu maksimize etmek adına her zaman mevcut bitin zıttını (`0` ise `1`'i) seçmeye çalışın.
* **Ne zaman kullanılır:** Maksimum XOR çiftlerini veya alt dizilerini $O(n^2)$ yerine $O(n)$ sürede bulurken.
* **Repo Örnekleri:**
  * [0421-Maximum XOR of Two Numbers in an Array](./0421-Maximum%20XOR%20of%20Two%20Numbers%20in%20an%20Array)

---

## 💡 Profesyonel Detaylar ve İstisnai Durumlar

* **Çocuklar İçin Hash Map vs. Dizi:** `TrieNode` içinde çocukları `children = {}` (Sözlük) veya `children = [None] * 26` (Dizi) olarak tutabilirsiniz. Karakter seti çok büyük veya dağınıksa (Unicode gibi) Hash Map bellek açısından çok daha verimlidir. Dizi ise önbellek konumu (cache locality) nedeniyle çok az daha hızlıdır ancak sadece birkaç dalınız varsa büyük ölçüde bellek israf eder. Python'da `dict` yaklaşımı profesyonel endüstri standardıdır.
* **Alan Karmaşıklığı Uyarısı (Space Complexity):** Trie'ler inanılmaz derecede hızlı olsalar da tam bir bellek canavarıdır. Her karakter potansiyel olarak yeni bir düğüm nesnesi oluşturur. Belleğin kesin olarak sınırlı olduğu üretim (production) ortamlarında sıkıştırılmış Trie'ler (Radix Trees) kullanılır, ancak LeetCode problemleri için buna nadiren ihtiyaç duyulur.
* **"Ön Ek Silme" Tuzağı:** Bir Trie'den kelime silmek son derece dikkat gerektirir. Düğümleri doğrudan silemezsiniz, çünkü diğer kelimeler o ön eki paylaşıyor olabilir. Bir düğümü ancak başka bir kelimenin sonu değilse ve başka çocuğu yoksa tamamen silebilirsiniz. Pratik hayatta, çoğunlukla sadece `is_word = False` yapmak en güvenli "tembel silme" (lazy deletion) stratejisidir.