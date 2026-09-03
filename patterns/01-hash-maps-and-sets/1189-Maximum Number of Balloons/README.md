# [1189. Maximum Number of Balloons](https://leetcode.com/problems/maximum-number-of-balloons/)

> 💡 **Not:** Bu soru **Hash Maps & Sets** kalıbı ile çözülmüştür. Kalıbın genel mantığı, kullanım senaryoları ve teorik detayları için [ README.md](../README.md) dosyasına bakabilirsiniz.

---
## Problem Açıklaması
Sana `text` adında bir metin (string) veriliyor. Amacın, bu metindeki karakterleri kullanarak oluşturabileceğin maksimum **"balloon"** kelimesi sayısını bulmaktır.

Metindeki her bir karakteri en fazla bir kez kullanabilirsin. Kaç tane "balloon" kelimesi oluşturulabileceğini döndürmen isteniyor.

### Örnek 1:
> **Girdi:** `text = "nlaebolko"`  
> **Çıktı:** `1`

### Örnek 2:
> **Girdi:** `text = "loonbalxballpoon"`  
> **Çıktı:** `2`

### Örnek 3:
> **Girdi:** `text = "leetcode"`  
> **Çıktı:** `0`

---

## Yaklaşım 1: Hash Map (Frekans Sayımı) - Optimal Çözüm

### Mantık
"balloon" kelimesini oluşturmak için belirli miktarda harflere ihtiyacımız var: Bir 'b', bir 'a', iki 'l', iki 'o' ve bir 'n'. Verilen `text` metnindeki tüm karakterlerin frekanslarını (kaç kez geçtiklerini) bir Sözlük (Hash Map) kullanarak sayabiliriz.

Oluşturabileceğimiz kelime sayısı, elimizdeki harflerden **en az (yetersiz)** olana göre belirlenir (buna darboğaz diyoruz). "balloon" kelimesinde 'l' ve 'o' harflerinden ikişer tane kullanıldığı için, bu harflerin toplam sayısını 2'ye bölerek potansiyellerini hesaplarız. Son olarak, tüm bu gerekli harflerin eldeki miktarları arasından en küçüğünü alarak sonucu buluruz.

**Kodun Detaylı Açıklaması:**
* **Neden `.get()` kullanıyoruz?** Normalde sözlükte olmayan bir harfi (örneğin 'b') `letters['b']` olarak çağırsaydık, Python o harf sözlükte olmadığı için `KeyError` hatası verip programı çökertecekti. `.get('b', 0)` fonksiyonu şunu söyler: *"Sözlükte 'b' harfini ara, eğer bulamazsan hata verme, onun yerine bana `0` değerini döndür."*
* **Neden `min()` kullanıyoruz?** Bir kelimeyi üretmek bir kek tarifi gibidir. Elinde 100 tane 'b' ve 'a' olsa bile, sadece 1 tane 'n' harfin varsa en fazla 1 tane "balloon" yazabilirsin. `min()` fonksiyonu, elindeki gerekli malzemeler (harfler) arasından miktarı **en az** olanı bulur ve maksimum üretim kapasiteni belirler.
* **Neden `// 2` yapıyoruz?** "balloon" kelimesinde 2 adet 'l' ve 2 adet 'o' vardır. Yani elinde 5 tane 'l' varsa bundan ancak $5 // 2 = 2$ tane balon çıkar. Tam sayı bölmesi (`//`) kullanarak küsuratları atıp gerçek kapasiteyi buluyoruz.

### Algoritma
1. `letters` adında boş bir sözlük oluştur.
2. `text` içindeki her bir `letter` için döngü kur ve harflerin sayılarını sözlükte tut.
3. `min()` fonksiyonunu kullanarak 'b', 'a', 'l', 'o', 'n' harflerinin sayısını kontrol et.
4. 'l' ve 'o' harflerinin sayısını `// 2` ile ikiye böl.
5. `min()` fonksiyonunun döndürdüğü sonucu (en az olan harf miktarını) return et.

### Karmaşıklık
- **Zaman Karmaşıklığı (Time Complexity):** `O(n)` — `n` uzunluğundaki `text` metnini sadece bir kez gezeriz (`O(n)`). Sözlüğe yazma, sözlükten okuma ve `min()` işlemi `O(1)` sürer.
- **Alan Karmaşıklığı (Space Complexity):** `O(1)` (veya `O(k)`) — Hash map içerisinde sadece İngilizce küçük harfler tutulur (maksimum 26 karakter). Girdi olan metnin uzunluğu ne kadar artarsa artsın, hafızada kaplanan alan 26 karakteri geçemeyeceği için sabit kalır (Constant Space).
### Kod

```python
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        letters = {}
        
        # Aşama 1: O(n) sürede metindeki frekansları hesaplama
        for letter in text:
            # Sözlükte arama O(1) sürer
            if letter in letters:
                letters[letter] += 1
            else:
                letters[letter] = 1
                
        # Aşama 2: O(1) sürede eldeki malzemelerle minimumu (darboğazı) bulma
        return min(
            letters.get('b', 0),
            letters.get('a', 0),
            letters.get('l', 0) // 2, # İki tane gerektiği için ikiye bölüyoruz
            letters.get('o', 0) // 2, # İki tane gerektiği için ikiye bölüyoruz
            letters.get('n', 0)
        )
```