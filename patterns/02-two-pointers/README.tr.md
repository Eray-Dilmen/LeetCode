> 📌 **Rehber:** Bu dizin, **Two Pointers (İki İşaretçi)** kalıbının mantığını ve örnek problemler üzerindeki uygulamalarını içerir.
> * **Teorik Mantık:** Kalıbın çalışma prensibi ve zaman/alan karmaşıklığı analizleri için bu `README.md` dosyasını inceleyebilirsiniz.
> * **Pratik Sorular:** Kalıbın uygulandığı çözümleri görmek için ilgili soru klasörlerine (örn. `0167-Two Sum II - Input Array Is Sorted`) gidebilirsiniz.

## Two Pointers Kalıbı Nedir?

* **Tanım:** Bir veri yapısı (genellikle dizi veya string) üzerinde aynı anda gezinmek için iki farklı değişkenin (işaretçi veya indeks) kullanıldığı algoritmik bir tekniktir.
* **Kritik Süper Gücü:** İç içe döngüleri (`O(n²)`) tek bir eşzamanlı taramaya (`O(n)`) dönüştürerek algoritmaları hızlandırır. En büyük avantajı, Hash Map gibi ekstra bellek tüketen yapılar kullanmak yerine sadece iki tam sayı değişkeni kullanarak bu işlemi **`O(1)` (sabit alan)** karmaşıklığında başarmasıdır.

## Ne Zaman Kullanılır? (İpuçları ve Depodaki Örnekler)

1. **Sıralı Diziler ve Hedef Bulma:** *"Toplamı belirli bir değere eşit olan çifti bul."*
   * *Örnek (`0167-Two Sum II`):* Sıralı bir dizinin en başına ve en sonuna birer işaretçi koyarak, mevcut toplamın çok büyük veya çok küçük olmasına göre arama alanını daraltırsınız.

2. **Simetri ve Palindrom Kontrolü:** *"Bu metin tersten de aynı mı okunuyor?"*
   * *Örnek (`0125-Valid Palindrome`):* İşaretçileri iki uçtan başlatıp merkeze doğru ilerletirsiniz. İşaretçiler farklı karakterleri gösterdiği an metin palindrom değildir.

3. **Yerinde (In-Place) Dizi Değişiklikleri:** *"Ekstra hafıza kullanmadan kopyaları sil."*
   * *Örnek (`0026-Remove Duplicates from Sorted Array`):* Benzersiz son elemanın yerini tutan "Yavaş (Slow)" bir işaretçi ile yeni elemanları arayan "Hızlı (Fast)" bir işaretçi kullanarak diziyi anında güncellersiniz.

## Zıt Yön (Opposite) vs Aynı Yön (Same Direction): Hangisi Seçilmeli?

**Sol ve Sağ İşaretçiler (Zıt Yön)**
* İşaretçiler `0. indeks` ve `son indeks` üzerinden başlayıp ortada buluşana kadar birbirine doğru hareket eder (`left < right`).
* **Cevapladığı Soru:** *"Bu dizinin iki ucu birbiriyle nasıl bir ilişkiye sahip?"*
* **Kullanım Senaryosu:** Sıralı diziler (Two Sum II), string ters çevirme veya palindrom kontrolü.

**Yavaş ve Hızlı İşaretçiler (Aynı Yön)**
* İki işaretçi de baştan başlar. Hızlı (Fast) olan her adımda ilerlerken, Yavaş (Slow) olan yalnızca belirli bir koşul sağlandığında ilerler.
* **Cevapladığı Soru:** *"Veriyi okurken aynı anda nasıl filtreleyebilir, kaydırabilir veya döngü (cycle) tespit edebilirim?"*
* **Kullanım Senaryosu:** Kopyaları yerinde (in-place) silme, sıfırları sona taşıma veya Bağlı Liste (Linked List) ortasını bulma.

## 💡 Profesyonel Detaylar ve İstisnai Durumlar

* **Sıralama Şartı (Sorted Prerequisite):** Zıt yönlü işaretçilerin arama veya toplam problemlerinde çalışabilmesi için verinin **kesinlikle sıralı olması** gerekir. Veri sıralı değilse ve sıralamak (`O(n log n)`) istemiyorsanız, Two Pointers yerine Hash Map kullanmalısınız.
* **İşaretçi Sınırları (Index Out of Bounds):** Döngü koşulunuzun (`while left < right` veya `while fast < len(nums)`) işaretçilerin dizinin sınırları dışına çıkmasını veya hatalı şekilde birbirini geçmesini engellediğinden daima emin olun.