> 📌 **Rehber:** Bu dizin, **Hash Maps & Sets** kalıbının mantığını ve örnek problemler üzerindeki uygulamalarını içerir.
> * **Teorik Mantık:** Kalıbın çalışma prensibi ve zaman/alan karmaşıklığı analizleri için bu [README.md](README.md) dosyasını inceleyebilirsiniz.
> * **Pratik Sorular:** Kalıbın uygulandığı çözümleri görmek için ilgili soru klasörlerine (örn. `0771-Jewels and Stones`) gidebilirsiniz.

---

### 1. Hash Map (ve Hash Set) Kalıbı Nedir ve Neden Kullanılır?

* **Tanım:** Anahtar-değer (**Key-Value**) ikilisiyle çalışan bir veri yapısıdır (Python'daki `dict`). Set ise sadece tekil anahtarları tutan halidir (`set`).
* **Kritik Süper Gücü:** Bir elemanın içeride var olup olmadığını sorgulamak (**Lookup / Search**) listelerde $O(n)$ sürerken, Hash Map/Set içinde $O(1)$ (**anlık / sabit zaman**) sürer.

### Ne Zaman Kullanılır? (İpuçları ve Örnekler)

1. **Frekans / Adet Sayma:** *"Hangi harf/sayı kaç kez geçti?"*
   * *Örnek (Valid Anagram):* İki kelimedeki harf sayıları aynı mı? Harfleri sayıp Hash Map'e atarsın.

2. **Hızlı Eşleştirme / Arama (Hafıza Takası):** *"Daha önce bu elemanı gördüm mü?"* veya *"Tamamlayıcısı bende var mı?"*
   * *Örnek (Two Sum):* $x + y = \text{target} \implies y = \text{target} - x$. Her elemanda *"Beni tamamlayan $y$ değeri hafızamda var mı?"* diye $O(1)$ sürede Hash Map'e bakarsın.

3. **Kümeye Aitlik Kontrolü:** *"Bu eleman izin verilen/özel grupta var mı?"* (771. soru: *Jewels and Stones*).

---

### 💡 Ekstra Detaylar ve Kod Örnekleri

**Hash Set vs Hash Map (Fark Nedir?)**


* **Hash Set (`set`):** Sadece "Tekil Elemanlar Listesi"dir. İçinde sadece anahtar (Key) tutar, karşılığında bir değer yoktur.
  * Sorduğun tek soru: *"Bu eleman içeride **var mı yok mu?**"*
  * `{"a", "A", "b"}` (Python: `set`)

* **Hash Map (`dict`):** Bir "Sözlük / Eşleme Tablosu"dur. Her anahtarın karşısında tuttuğu bir değer (Value) vardır (**Key $\rightarrow$ Value**).
  * Sorduğun soru: *"Bu eleman var mı, **varsa değeri/adedi/indeksi kaç?**"*
  * `{"a": 2, "A": 1, "b": 4}` (Python: `dict`)

---

### Soru Üzerinden Somut Karşılaştırma

#### 1. Jewels and Stones Sorusu $\rightarrow$ Hash Set yeterlidir:
* **Amacın:** Taşın mücevher olup olmadığını anlamak.
* Taş `'a'` gelince sadece *"Bu mücevher mi (kümede var mı)?"* diyorsun. Ekstra bir bilgiye ihtiyacın yok.
* **Yapı:** `jewel_set = {"a", "A"}`

#### 2. Harf Sayma (Frekans) Sorusu $\rightarrow$ Hash Map zorunludur:
* **Amacın:** Hangi harften kaç tane olduğunu bulmak.
* Taş `'a'` gelince sadece varlığını değil, sayısını da tutman gerekir: `'a'` harfi $\rightarrow$ $3$ adet.
* **Yapı:** `counts = {"a": 3, "A": 1, "b": 4}`

Özetle; bir verinin sadece **varlığını/yokluğunu** kontrol ediyorsan **Set**, o veriye bağlı **ikinci bir bilgi (adet, indeks, karşılık)** saklayacaksan **Map** kullanırsın.