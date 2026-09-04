> 📌 **Rehber:** Bu dizin, **Fast & Slow Pointers (Floyd'un Kaplumbağa ve Tavşan Algoritması)** kalıbı için bir Kavram Haritası işlevi görür.
> * **Teorik Mantık:** Temel prensipler, alt varyasyonlar ve zaman/alan karmaşıklığı analizleri için bu `README.tr.md` dosyasını okuyun.
> * **Pratik Uygulamalar:** Kalıbın pratikte nasıl uygulandığını görmek için spesifik soru klasörlerine gidin (örneğin, `0141-Linked List Cycle`). Özel istisnalar (edge cases) ve alternatif çözümler bu klasörlerin içinde belgelenmiştir.

## Fast & Slow Pointers Kalıbı Nedir?

* **Tanım:** Floyd'un Döngü Tespiti (Cycle Finding) algoritması olarak da bilinir. Bir dizi veya liste üzerinde **farklı ve sabit hızlarda** hareket eden iki işaretçi (genellikle yavaş işaretçi 1 adım, hızlı işaretçi 2 adım atar) kullanır.
* **Temel Gücü:** Bağlı Liste (Linked List) problemlerini (ve bazen durum makinesi gibi davranan dizileri) `O(n)` zaman ve `O(1)` alan (space) karmaşıklığı ile çözer. Dizilerde arama/filtreleme için kullanılan standart Two Pointers kalıbından farklı olarak bu kalıp; döngüleri (sonsuz döngüleri) tespit etmek ve ekstra bellek (Hash Set gibi) kullanmadan tek yönlü bir yapının yapısal merkezini bulmak için özel olarak tasarlanmıştır.

---

## Temel Varyasyonlar ve Algoritmik Stratejiler

Bu kalıp tamamen matematiksel bir kaçınılmazlığa dayanır: Eğer iki koşucu dairesel bir pistte koşuyorsa ve biri diğerinden iki kat hızlıysa, hızlı olan koşucu sonunda yavaş olana tur bindirecek ve onu yakalayacaktır.

### 1. Döngü Tespiti (Cycle Detection)
* **Algoritma:** `slow` (yavaş) ve `fast` (hızlı) işaretçilerin her ikisini de `head` (başlangıç) düğümünde başlatın. Bir `while` döngüsü içinde, `slow`'u 1 adım (`slow = slow.next`) ve `fast`'i 2 adım (`fast = fast.next.next`) ilerletin. Eğer işaretçiler herhangi bir anda tam olarak aynı düğümü gösterirse (`slow == fast`), bir döngü var demektir. Eğer `fast` sona (`null` değerine) ulaşırsa, döngü yoktur.
* **Ne zaman kullanılır:** Bir Bağlı Listenin kendi üzerine kapanıp kapanmadığını (loop) kontrol ederken veya matematiksel bir dizinin sonsuz bir döngüye sıkışıp sıkışmadığını doğrularken.
* **Repo Örnekleri:**
  * [0141-Linked List Cycle](./0141-Linked%20List%20Cycle)
  * [0202-Happy Number](./0202-Happy%20Number)

### 2. Yapının Ortasını Bulma (Finding the Middle)
* **Algoritma:** Her iki işaretçiyi de `head` düğümünden başlatın. `slow`'u 1 adım, `fast`'i 2 adım kaydırın. `fast` işaretçisi listenin en sonuna ulaştığında, `slow` işaretçisi mesafenin tam olarak yarısını kat etmiş olacak ve orta düğümün (middle node) üzerinde duracaktır.
* **Ne zaman kullanılır:** Bir Bağlı Listeyi ikiye bölmeniz gerektiğinde (örn. Bağlı Listelerde Merge Sort işlemi için) veya ikinci yarıyı tersine çevirerek Bağlı Listenin bir palindrom olup olmadığını kontrol ederken.
* **Repo Örnekleri:**
  * [0876-Middle of the Linked List](./0876-Middle%20of%20the%20Linked%20List)
  * [0234-Palindrome Linked List](./0234-Palindrome%20Linked%20List)

### 3. Döngünün Başlangıç Düğümünü Bulma
* **Algoritma:** Bu iki aşamalı matematiksel bir hiledir. Önce "Döngü Tespiti" (Cycle Detection) aşamasını uygulayın. `slow` ve `fast` aynı düğümde buluştuğunda döngüyü sonlandırmayın. Bunun yerine, işaretçilerden birini dizinin en başına (`head`) geri götürün. Ardından, **her iki** işaretçiyi de aynı hızda (her seferinde 1 adım) ilerletin. Tekrar çarpıştıkları nokta, döngünün başladığı (bağlandığı) düğümdür.
* **Ne zaman kullanılır:** Problem sizden döngünün başladığı spesifik düğümü döndürmenizi istediğinde veya bir diziyi değiştirmeden ve kesinlikle `O(1)` alan (space) kullanarak içindeki tekrar eden (duplicate) sayıyı bulmanız gerektiğinde.
* **Repo Örnekleri:**
  * [0142-Linked List Cycle II](./0142-Linked%20List%20Cycle%20II)
  * [0287-Find the Duplicate Number](./0287-Find%20the%20Duplicate%20Number)

---

## 💡 Profesyonel Detaylar ve İstisnai Durumlar

* **Null Pointer Hataları (NPE):** En yaygın hata, `fast` veya `fast.next` halihazırda `null` değerine ulaşmışken `fast.next.next` değerine erişmeye çalışmaktır. `while` döngünüzün koşulunu her zaman dikkatli kurgulayın: Python'da `while fast and fast.next:` veya Java/C++ için `while (fast != null && fast.next != null)`.
* **Çift ve Tek Uzunluklar (Even vs. Odd):** Bir Bağlı Listenin ortasını bulurken, uzunluğun çift veya tek olmasına bağlı olarak "orta" tanımı değişir. Uzunluk çift ise iki orta düğüm vardır. Standart `fast = head, slow = head` kurulumu sizi **ikinci** orta düğüme götürür. Eğer **birinci** orta düğümde durmanız gerekiyorsa, başlangıçta `fast = head.next` şeklinde kurgulamalısınız.
* **Dizileri Bağlı Liste Gibi Kullanma:** *Find the Duplicate Number* gibi problemler, içindeki sayıların (value) aslında indeksleri (index) gösterdiği bir dizi verir. `sonraki_dugum = nums[mevcut_dugum]` mantığını kurarak `nums` dizisine tam olarak bir Bağlı Liste (Linked List) muamelesi yapabilir ve Floyd algoritmasını diziler üzerinde de çalıştırabilirsiniz.