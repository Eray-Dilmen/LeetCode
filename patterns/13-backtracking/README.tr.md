> 📌 **Rehber:** Bu dizin, **Backtracking (Geri İzleme)** kalıbı için bir Kavram Haritası işlevi görür.
> * **Teorik Mantık:** Temel prensipler, alt varyasyonlar ve zaman/alan karmaşıklığı analizleri için bu `README.tr.md` dosyasını okuyun.
> * **Pratik Uygulamalar:** Kalıbın pratikte nasıl uygulandığını görmek için spesifik soru klasörlerine gidin (örneğin, `0078-Subsets`). Özel istisnalar (edge cases) ve alternatif çözümler bu klasörlerin içinde belgelenmiştir.

## Backtracking Kalıbı Nedir?

* **Tanım:** Bir çözümü adım adım, parça parça inşa etmeye çalışarak özyinelemeli (recursive) problemleri çözme tekniğidir. Eğer kısmi bir çözüm problemin kurallarını/kısıtlamalarını ihlal ederse, o yoldan vazgeçer (geri adım atar / backtrack) ve mevcut diğer seçeneği dener.
* **Temel Gücü:** Tüm olası kombinasyonları/durumları keşfeder, ancak karar ağacındaki geçersiz dalları erkenden **budayarak (pruning)** kaba kuvvet (brute-force) yaklaşımını akıllıca optimize eder. Çıktı alanının kendisi devasa olduğu için zaman karmaşıklığı tipik olarak üstel `O(2^n)` veya faktöriyel `O(n!)` olur. Alan karmaşıklığı (Space Complexity) ise özyineleme (recursion) yığınının maksimum derinliğini temsil eden `O(n)` seviyesindedir.

---

## Temel Varyasyonlar ve Algoritmik Stratejiler

Backtracking algoritmaları genellikle `backtrack(baslangic_indeksi, mevcut_yol)` şeklinde bir yardımcı fonksiyonla yapılandırılır. Varyasyonlar, sonraki elemanları nasıl seçtiğinize bağlı olarak değişir.

### 1. Alt Kümeler ve Kombinasyonlar (Sıra Önemli Değil)
* **Algoritma:** `[1, 2]` ile `[2, 1]`'in aynı kabul edildiği gruplamalar oluşturmak istersiniz. Kopya gruplamaları önlemek için `for` döngünüzde bir `start_index` kullanın. Özyinelemeli çağrı, yeni başlangıç indeksi olarak `i + 1`'i iletecektir. Bu, dizide sadece ileriye bakmanızı ve asla geriye dönmemenizi garanti eder.
* **Ne zaman kullanılır:** Bir kümenin tüm alt kümelerini (subsets) veya `k` adet sayının kombinasyonlarını bulurken.
* **Repo Örnekleri:**
  * [0078-Subsets](./0078-Subsets)
  * [0077-Combinations](./0077-Combinations)

### 2. Permütasyonlar (Sıra Önemli)
* **Algoritma:** `[1, 2]` ile `[2, 1]`'in farklı kabul edildiği dizilimler oluşturmak istersiniz. `start_index` **kullanmayın**. Bunun yerine, `for` döngünüz her zaman `0`'dan başlar. Aynı elemanı aynı yolda tekrar kullanmayı önlemek için `if nums[i] in current_path` kontrolü yapmalı (veya bir `visited` dizisi/kümesi kullanmalı) ve o elemanı atlamalısınız.
* **Ne zaman kullanılır:** Tüm olası şifreleri, dizilimleri veya bir veri setinin tüm sıralamalarını üretirken.
* **Repo Örnekleri:**
  * [0046-Permutations](./0046-Permutations)
  * [0047-Permutations II](./0047-Permutations%20II)

### 3. Kısıt Sağlama ve Budama (Constraint Satisfaction & Pruning)
* **Algoritma:** Alt Kümeler/Kombinasyonlara benzer, ancak açık bir hedef veya kısıtlama (constraint) vardır. Özyinelemede daha derine inmeden önce, mevcut durumun hedefi aşıp aşmadığını kontrol edin. Aşıyorsa, hemen `return` yapın (ağacı budayın). Eğer aynı elemanı birden fazla kez kullanabiliyorsanız, özyinelemeli çağrıya `i + 1` yerine `i` değerini gönderin.
* **Ne zaman kullanılır:** Para üstü (Coin Change) problemleri, belirli bir toplama ulaşan kombinasyonlar veya bir satranç tahtasına vezir yerleştirme (N-Queens).
* **Repo Örnekleri:**
  * [0039-Combination Sum](./0039-Combination%20Sum)
  * [0051-N-Queens](./0051-N-Queens)

### 4. Geri İzlemeli Izgara DFS (Grid DFS with Backtracking)
* **Algoritma:** Belirli bir yolu (bir kelime gibi) aradığınız 2 boyutlu (2D) bir matriste gezinirken kullanılır. Yönleri keşfetmek için DFS kullanırsınız. En kritik geri izleme (backtrack) adımı şudur: Özyinelemeli çağrılardan *önce* mevcut hücreyi "ziyaret edildi" olarak işaretlemelisiniz (örn. karakteri `#` yapmak) ve çağrılar bittikten *sonra* o işareti **kaldırmalısınız** (orijinal karaktere geri döndürmek). Bu, hücrenin farklı bir yol üzerinden tekrar ziyaret edilebilmesini sağlar.
* **Ne zaman kullanılır:** Kelime Arama (Word Search), birden fazla olası yolu olan labirent çözümleri.
* **Repo Örnekleri:**
  * [0079-Word Search](./0079-Word%20Search)

---

## 💡 Profesyonel Detaylar ve İstisnai Durumlar

* **Derin Kopya Hatası (The Deep Copy Bug):** En yaygın Backtracking hatası, `current_path` listesini doğrudan `results` (sonuçlar) dizisine eklemektir (`results.append(path)`). Listeler referansla aktarıldığı için, özyineleme geri adım atıp `path`'ten elemanları çıkardığında (pop), bu elemanlar `results` dizisinden de silinecektir. **Her zaman derin bir kopya (deep copy) ekleyin:** Python'da `results.append(path[:])` veya Java'da `new ArrayList<>(path)`.
* **Kopyaları Yönetmek (Sıralama ve Atlama):** Girdi dizisi tekrar eden sayılar içeriyorsa ve siz benzersiz (unique) alt kümeler/kombinasyonlar istiyorsanız, diziyi mutlaka önceden sıralamalısınız (`nums.sort()`). Ardından, `for` döngünüzün içine şu kontrolü ekleyin: `if i > start_index and nums[i] == nums[i-1]: continue`. Bu kod, özyineleme ağacının aynı derinlik seviyesinde aynı sayının tekrar işlenmesini kesin olarak engeller.
* **`O(2^n)` Karmaşıklığını Kabul Etmek:** Backtracking problemlerinde üstel zaman karmaşıklığından korkmayın. Bir problem sizden "tüm olası kombinasyonları döndürmenizi" istiyorsa, kombinasyonların matematiksel sayısı zaten `2^n`'dir. Çıktı bu kadar büyük olduğu için `O(2^n)` algoritması bu problemlerdeki mutlak en optimum çözümdür.