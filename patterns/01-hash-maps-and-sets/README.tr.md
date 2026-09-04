> 📌 **Rehber:** Bu dizin, **Hash Maps & Sets** kalıbı için bir Kavram Haritası işlevi görür.
> * **Teorik Mantık:** Temel prensipler, alt varyasyonlar ve zaman/alan karmaşıklığı analizleri için bu `README.tr.md` dosyasını okuyun.
> * **Pratik Uygulamalar:** Kalıbın pratikte nasıl uygulandığını görmek için spesifik soru klasörlerine gidin (örneğin, `0001-Two Sum`). Özel istisnalar (edge cases) ve alternatif çözümler bu klasörlerin içinde belgelenmiştir.

## Hash Map (ve Hash Set) Kalıbı Nedir?

* **Tanım:** Hash Map (Python'daki adıyla sözlük, `dict`), **Anahtar-Değer (Key-Value)** çiftlerini depolayan bir veri yapısıdır. Hash Set (`set`), ilişkili değerler olmadan yalnızca benzersiz (unique) anahtarları depolayan bir varyasyondur.
* **Temel Gücü:** Bir elemanın var olup olmadığını kontrol etmek (**Arama / Lookup**) bir dizide $O(n)$ zaman alırken, bir Hash Map/Set içinde yalnızca **$O(1)$ (sabit zaman)** alır. Bellek (RAM) harcayarak hız kazandırdığı için zaman karmaşıklığını optimize etmenin en güçlü aracıdır.

---

## Temel Varyasyonlar ve Algoritmik Stratejiler

Hash Map kalıbı çok yönlüdür. Genellikle şu şekillerde uygulanır:

### 1. Frekans Sayımı (Frequency Counting)
* **Algoritma:** Bir dizi veya metin üzerinde gezinerek her elemanın kaç kez geçtiğini sayın. Eleman haritada yoksa 1 değeriyle ekleyin; varsa değerini artırın (`map[char] = map.get(char, 0) + 1`).
* **Ne zaman kullanılır:** Hedef bir kelimeyi oluşturmak için gereken harflere tam olarak sahip olup olmadığınızı doğrulamanız gerektiğinde veya iki string'in birebir aynı karakter sayısına sahip olup olmadığını kontrol ederken.
* **Repo Örnekleri:**
  * [0242-Valid Anagram](./0242-Valid%20Anagram)
  * [0383-Ransom Note](./0383-Ransom%20Note)

### 2. Hızlı Eşleştirme ve Tamamlayıcı Arama (Complement Search)
* **Algoritma:** İç içe döngülerle her çifti kontrol etmek yerine, koşulu sağlamak için ihtiyacınız olan "tamamlayıcıyı" hesaplayın. $x + y = target$ denklemi için bunu $y = target - x$ olarak düşünün. Döngüde ilerlerken Hash Map'e şunu sorun: *"Hafızanda ihtiyacım olan `y` var mı?"* Yoksa, mevcut elemanı ve indeksini ilerideki aramalar için haritaya kaydedin.
* **Ne zaman kullanılır:** Diziyi sıralamaya gerek kalmadan toplamı/çarpımı belirli bir hedefe ulaşan çiftleri bulmada.
* **Repo Örnekleri:**
  * [0001-Two Sum](./0001-Two%20Sum)

### 3. Benzersizlik ve Varlık Kontrolü (Hash Set)
* **Algoritma:** Döngü ile gezinirken elemanları bir Hash Set'e ekleyin. Eğer zaten sette var olan bir elemanla karşılaşırsanız, bir kopya (duplicate) buldunuz demektir. Alternatif olarak, referans havuzunu (örneğin mücevherleri) bir sette tutup, hedef elemanları bu sete karşı $O(1)$ sürede kontrol edebilirsiniz.
* **Ne zaman kullanılır:** Bir elemanın havuzda *var olup olmadığını* bilmeniz yeterliyse ve sayılara veya indekslere ihtiyacınız yoksa.
* **Repo Örnekleri:**
  * [0217-Contains Duplicate](./0217-Contains%20Duplicate)
  * [0771-Jewels and Stones](./0771-Jewels%20and%20Stones)

### 4. Gruplama ve İlişki Eşleme (Grouping & Mapping)
* **Algoritma:** Ortak bir "imza" veya özellik bulmak için bir öğeyi işleyin (örneğin bir kelimedeki harfleri alfabetik sıraya dizmek). Bu imzayı Hash Map'te **Anahtar (Key)** olarak kullanın ve orijinal öğeyi o anahtara bağlı bir listenin (**Value**) içine ekleyin (`map[imza].append(öğe)`).
* **Ne zaman kullanılır:** Ortak bir özelliği paylaşan elemanları (anagramlar gibi) gruplamada veya karakter değişim kurallarını (isomorphic strings) haritalamada.
* **Repo Örnekleri:**
  * [0049-Group Anagrams](./0049-Group%20Anagrams)

---

## 💡 Profesyonel Detaylar ve İstisnai Durumlar

* **Alan-Zaman Takası (Space-Time Trade-off):** Bu kalıbı uygulamak neredeyse her zaman Zaman Karmaşıklığını (Time Complexity) $O(n^2)$ veya $O(n \log n)$'den $O(n)$'e düşürür. Ancak, hash tablosu için ekstra bellek ayırdığınız için Alan Karmaşıklığı (Space Complexity) $O(n)$ seviyesine çıkar.
* **Sadece Hashlenebilir Anahtarlar:** Python'da bir Map veya Set içinde Anahtar (Key) olarak yalnızca **değiştirilemez (immutable)** veri türlerini (tam sayılar, stringler veya tuple'lar) kullanabilirsiniz. Listeler veya diğer sözlükler gibi değiştirilebilir (mutable) türler hashlenemez (hata verir).