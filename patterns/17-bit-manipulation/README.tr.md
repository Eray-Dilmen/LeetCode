> 📌 **Rehber:** Bu dizin, **Bit Manipulation (Bit Manipülasyonu)** kalıbı için bir Kavram Haritası işlevi görür.
> * **Teorik Mantık:** Temel prensipler, alt varyasyonlar ve zaman/alan karmaşıklığı analizleri için bu `README.tr.md` dosyasını okuyun.
> * **Pratik Uygulamalar:** Kalıbın pratikte nasıl uygulandığını görmek için spesifik soru klasörlerine gidin (örneğin, `0136-Single Number`). Özel istisnalar (edge cases) ve alternatif çözümler bu klasörlerin içinde belgelenmiştir.

## Bit Manipulation Kalıbı Nedir?

* **Tanım:** Sayıların ikili (binary - 0'lar ve 1'ler) temsilleri üzerinde doğrudan bit düzeyinde operatörler kullanarak işlem yapma tekniğidir: AND (`&`), OR (`|`), XOR (`^`), NOT (`~`), Sola Kaydırma (`<<`) ve Sağa Kaydırma (`>>`).
* **Temel Gücü:** İnanılmaz hız ve bellek verimliliği. Bit işlemleri, CPU tarafından donanım düzeyinde doğrudan yürütülür, bu da onları standart aritmetik işlemlerden daha hızlı yapar. Ayrıca, boolean (doğru/yanlış) dizilerini veya Hash Set'leri tek bir tam sayıya (Bitmask) sıkıştırmanıza olanak tanıyarak alan karmaşıklığını `O(n)`'den mutlak `O(1)`'e düşürür.

---

## Temel Varyasyonlar ve AlgAlgoritmik Stratejiler

Bit manipülasyonu, ikili mantığın (binary logic) birkaç temel matematiksel özelliğine sıkı sıkıya bağlıdır.

### 1. XOR Sihri (Exclusive OR)
* **Algoritma:** XOR operatörü (`^`), bitler farklıysa `1`, aynıysa `0` döndürür. İki çok önemli özelliği vardır: `a ^ a = 0` (bir sayı kendisiyle XOR'landığında sıfırlanır) ve `a ^ 0 = a`. Bir sayı dizisini sürekli XOR'larsanız, çift olan tüm kopyalar birbirini yok eder ve geriye yalnızca eşi olmayan benzersiz sayı kalır.
* **Ne zaman kullanılır:** Eksik sayıları bulurken, diğer tüm elemanların iki kez geçtiği bir dizideki tekil elemanı bulurken veya geçici bir değişken (temp) kullanmadan iki değişkenin değerini takas ederken (swap).
* **Repo Örnekleri:**
  * [0136-Single Number](./0136-Single%20Number)
  * [0268-Missing Number](./0268-Missing%20Number)

### 2. Brian Kernighan Algoritması
* **Algoritma:** `n & (n - 1)` ifadesi, her zaman `n` sayısının ayarlanmış en düşük bitini (en sağdaki `1`'i) `0`'a çevirir. Bunu bir `while n > 0:` döngüsüne koyar ve `n` sıfır olana kadar döngünün kaç kez çalıştığını sayarsanız, sayının ikili temsilindeki `1`'lerin sayısını çok verimli bir şekilde bulursunuz.
* **Ne zaman kullanılır:** Ayarlanmış bitleri sayarken (Hamming Weight) veya bir sayının 2'nin kuvveti olup olmadığını kontrol ederken (2'nin kuvvetlerinin ikili yazılışında sadece bir tane `1` vardır, yani `n & (n - 1) == 0` olmalıdır).
* **Repo Örnekleri:**
  * [0191-Number of 1 Bits](./0191-Number%20of%201%20Bits)
  * [0231-Power of Two](./0231-Power%20of%20Two)

### 3. Bit Maskeleme (Bitmasking - Kümeleri Tam Sayı Olarak Tutmak)
* **Algoritma:** Alfabedeki küçük harfleri takip etmek için bir Hash Set veya 26 boyutlu bir boolean dizisi kullanmak yerine, tek bir 32-bit tam sayı kullanırsınız. İlgili biti 1 yaparak kümeye bir karakter "ekleyebilirsiniz": `mask |= (1 << char_index)`. İçinde var olup olmadığını AND ile kontrol edebilirsiniz: `(mask & (1 << char_index)) != 0`.
* **Ne zaman kullanılır:** Alt küme (subset) problemlerini çözerken, Dinamik Programlamada durum (state) takibi yaparken (Bitmask DP) veya alfabe gibi küçük, sabit boyutlu alanlarla uğraşırken belleği aşırı derecede optimize etmeniz gerektiğinde.
* **Repo Örnekleri:**
  * [0078-Subsets](./0078-Subsets) (Bitmask yaklaşımı ile)
  * [3133-Minimum Array End](./3133-Minimum%20Array%20End)

### 4. Kaydırma İşlemleri (Hızlı Çarpma / Bölme)
* **Algoritma:** Bir sayıyı sola 1 bit kaydırmak (`x << 1`) onu 2 ile çarpmak demektir. Sağa 1 bit kaydırmak (`x >> 1`) onu 2'ye bölmek (tam sayı bölmesi) demektir. Bir sayıyı sürekli sağa kaydırıp `n & 1` işlemini kontrol ederek (bu size son bitin 1 mi yoksa 0 mı olduğunu söyler) bitleri tek tek ayrıştırabilirsiniz.
* **Ne zaman kullanılır:** Bitleri tersine çevirirken (reverse), bölme operatörü kullanmadan bölümler hesaplarken veya binary metinleri ayrıştırırken.
* **Repo Örnekleri:**
  * [0190-Reverse Bits](./0190-Reverse%20Bits)
  * [0338-Counting Bits](./0338-Counting%20Bits)

---

## 💡 Profesyonel Detaylar ve İstisnai Durumlar

* **Operatör Önceliği (Precedence):** Neredeyse tüm programlama dillerinde bit düzeyi operatörlerin önceliği çok düşüktür (`==` veya `!=`'den bile daha düşük). Bit işlemlerinizi her zaman parantez içine alın. `if mask & 1 == 0:` yazarsanız, bilgisayar bunu `mask & (1 == 0)` olarak algılar, bu da `mask & 0` anlamına gelir ve tüm mantığınız çöker. Her zaman `if (mask & 1) == 0:` şeklinde yazın.
* **Python'un Sonsuz Tam Sayıları:** Tam sayıların kesin olarak 32-bit olduğu (ve sınırları aşınca eksiye döndüğü) Java veya C++'ın aksine, Python tam sayıları rastgele büyüklükte olabilir ve otomatik olarak taşma (overflow) yapmaz. 32-bit işaretli tam sayı davranışına dayanan problemler yaparken (bitleri tersine çevirmek veya negatif binary sayılarla uğraşmak gibi), 32-bit sınırlarını simüle etmek için sonucu manuel olarak `0xFFFFFFFF` ile maskelemeniz (AND'lemeniz) gerekir.
* **Okunabilirlik Takası (Readability Trade-off):** Bit manipülasyonu inanılmaz derecede hızlı olmasına rağmen, okunması ve anlaşılması oldukça zordur. Profesyonel bir kod tabanında, yalnızca performansın kesin bir darboğaz olduğu durumlarda Bitmask veya XOR hileleri kullanmalısınız. Aksi takdirde, kodun bakım edilebilirliği (maintainability) açısından standart bir Hash Set veya boolean dizisi her zaman çok daha fazla tercih edilir.