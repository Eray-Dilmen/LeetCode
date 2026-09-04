> 📌 **Rehber:** Bu dizin, **Greedy Algorithms (Açgözlü Algoritmalar)** kalıbı için bir Kavram Haritası işlevi görür.
> * **Teorik Mantık:** Temel prensipler, alt varyasyonlar ve zaman/alan karmaşıklığı analizleri için bu `README.tr.md` dosyasını okuyun.
> * **Pratik Uygulamalar:** Kalıbın pratikte nasıl uygulandığını görmek için spesifik soru klasörlerine gidin (örneğin, `0055-Jump Game`). Özel istisnalar (edge cases) ve alternatif çözümler bu klasörlerin içinde belgelenmiştir.

## Greedy (Açgözlü) Algoritma Kalıbı Nedir?

* **Tanım:** Çözümü adım adım inşa eden ve her adımda anlık olarak en yüksek faydayı sağlayan parçayı seçen algoritmik bir paradigmadır. Bu yerel (lokal) seçimlerin en sonunda **genel (global) en iyi çözüme** yol açacağı umuduyla her adımda **yerel olarak en optimal seçimi** yapar.
* **Temel Gücü:** İnanılmaz hız ve bellek verimliliği. Tüm olası yolları (Backtracking gibi) denemek veya örtüşen alt problemleri (Dinamik Programlama gibi) önbelleğe almak yerine, açgözlü bir algoritma sadece o anki "en iyi" seçeneği alır ve yoluna devam eder. Önceki seçimlerini gözden geçirmek için asla geriye dönüp bakmaz. Zaman karmaşıklığı genellikle `O(n)` veya (sıralama gerekiyorsa) `O(n log n)` olurken, alan karmaşıklığı `O(1)`'dir.

---

## Temel Varyasyonlar ve AlgAlgoritmik Stratejiler

Greedy algoritmalarındaki asıl zorluk kodu yazmak değil, açgözlü bir seçimin o spesifik problem için gerçekten doğru sonucu vereceğini *kanıtlamaktır*.

### 1. Sıralama + Açgözlü Seçim (Sorting + Greedy)
* **Algoritma:** Ham veri kaotiktir ve "en iyi" seçimin ne olduğunu bilmek imkansızdır. Önce girdi dizisini belirli bir metriğe (örn. boyutlar, başlangıç zamanları veya oranlar) göre sıralarsınız. Sıralandıktan sonra dizi üzerinde gezinir ve kaynaklarınız bitene kadar koşulları açgözlü bir şekilde teker teker yerine getirirsiniz.
* **Ne zaman kullanılır:** Kaynak tahsisi, zamanlama veya eşleştirme problemlerinde (en küçük kurabiyeleri en az açgözlü çocuklarla eşleştirmek gibi).
* **Repo Örnekleri:**
  * [0455-Assign Cookies](./0455-Assign%20Cookies)
  * [0406-Queue Reconstruction by Height](./0406-Queue%20Reconstruction%20by%20Height)

### 2. Maksimum Ulaşım / Sıçrama (Maximum Reach / Jumps)
* **Algoritma:** Bir dizi üzerinde gezinirken, bulunduğunuz konumdan ulaşabileceğiniz "mümkün olan en uzak noktayı" (maximum reach) sürekli olarak güncellersiniz. Mevcut indeksiniz maksimum ulaşımınızı geçerse, sıkışıp kalmışsınız demektir. Ulaşımınız son indeksi geçerse kazanırsınız.
* **Ne zaman kullanılır:** Elemanların atlama uzunluklarını veya yakıtı temsil ettiği dizi gezinme (array traversal) problemlerinde.
* **Repo Örnekleri:**
  * [0055-Jump Game](./0055-Jump%20Game)
  * [0045-Jump Game II](./0045-Jump%20Game%20II)

### 3. Açgözlü Birikim (Greedy Accumulation)
* **Algoritma:** Çalışan bir bakiye (örneğin depodaki yakıt) tutarsınız. İlerledikçe bakiyeye ekleme yaparsınız. Bakiye sıfırın altına düşerse, bu mevcut yolun tamamen geçersiz olduğu anlamına gelir. Başlangıç pozisyonunuzu açgözlü bir şekilde *bir sonraki* indekse sıfırlar ve bakiyenizi tekrar sıfır yaparsınız; çünkü önceki herhangi bir başlangıç noktasının da başarısız olacağını matematiksel olarak bilirsiniz.
* **Ne zaman kullanılır:** Dairesel rota problemlerinde veya bir dizide geçerli bir başlangıç noktası bulurken.
* **Repo Örnekleri:**
  * [0134-Gas Station](./0134-Gas%20Station)
  * [0763-Partition Labels](./0763-Partition%20Labels)

---

## 💡 Profesyonel Detaylar ve İstisnai Durumlar

* **Greedy vs. Dinamik Programlama:** Bu en yaygın tuzaktır. Açgözlü bir algoritma yalnızca problem **Greedy Choice Property** (lokal bir optimumun seçilmesiyle global optimuma ulaşılabilmesi) özelliğine sahipse çalışır. Örneğin, `[25, 10, 1]` kuruşluk madeni paralarla `30` kuruş için minimum parayı bulmak:
  * Greedy en büyük olan `25`'i alır, sonra beş tane `1`'e ihtiyaç duyar -> toplam 6 para.
  * DP ise tüm yolları dener ve üç tane `10`'luk bulur -> toplam 3 para (Global Optimum).
  * Anında en büyük/en iyi seçeneği almanın, ileride matematiksel olarak daha iyi bir kombinasyonu bloke edip etmeyeceğini her zaman doğrulayın. Ediyorsa, DP kullanmalısınız.
* **Sıralama Darboğazı (Sorting Bottleneck):** Açgözlü taramanın kendisi genellikle $O(n)$ olsa da, önkoşul olan sıralama adımı $O(n \log n)$ sürer. Bu nedenle, genel zaman karmaşıklığı temel olarak sıralama algoritmasına bağlıdır.
* **Geri Dönüş Yok (No Backtracking):** Gerçek bir Greedy algoritması mevcut durumu değerlendirir, kesin bir seçim yapar ve ilerler. Eğer kendinizi bir seçimi "geri almak" (undo) ve başka bir yolu denemek için kod yazarken bulursanız, yazdığınız şey Greedy değil, bir Backtracking algoritmasıdır.