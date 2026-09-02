# [1189. Maximum Number of Balloons](https://leetcode.com/problems/maximum-number-of-balloons/)

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

## Yaklaşım 1: Hash Map / Frekans Sayımı (Optimal Çözüm)

### Mantık
"balloon" kelimesini oluşturmak için belirli miktarda harflere ihtiyacımız var: Bir 'b', bir 'a', iki 'l', iki 'o' ve bir 'n'. Verilen `text` metnindeki tüm karakterlerin frekanslarını (kaç kez geçtiklerini) bir Sözlük (Hash Map) kullanarak sayabiliriz.

Oluşturabileceğimiz kelime sayısı, elimizdeki harflerden **en az (yetersiz)** olana göre belirlenir (buna darboğaz diyoruz). 
* **Neden `.get()` kullanıyoruz?** Sözlükte olmayan bir harfi (örneğin 'b') `letters['b']` olarak çağırsaydık, Python `KeyError` hatası verecekti. `.get('b', 0)` fonksiyonu, o harf yoksa hata vermek yerine `0` döndürerek eldeki sayının sıfır olduğunu güvenle belirtir.
* **Neden `min()` kullanıyoruz?** `min()` fonksiyonu, elimizdeki gerekli malzemeler (harfler) arasından miktarı **en az** olanı bulur. Elinde 100 tane 'b' olsa bile, sadece 1 tane 'n' harfin varsa en fazla 1 tane "balloon" yazabilirsin. Üretim sınırımızı bu en küçük değer belirler.

### Algoritma
1. Karakter frekanslarını tutmak için `letters` adında boş bir sözlük oluştur.
2. `text` içindeki her bir `letter` için döngü kur. Harf sözlükte varsa değerini 1 artır, yoksa 1 değeriyle sözlüğe ekle.
3. `min()` fonksiyonunu kullanarak 'b', 'a', 'l', 'o', 'n' harflerinin sayısını kontrol et.
4. "balloon" kelimesinde 2'şer adet geçtikleri için, 'l' ve 'o' harflerinin sayısını `// 2` ile ikiye böl (tam sayı bölmesi).
5. `min()` fonksiyonunun döndürdüğü sonucu (en az olan harf miktarını) döndür.

### Karmaşıklık
- **Zaman Karmaşıklığı (Time Complexity):** $\mathcal{O}(n)$ — $n$ uzunluğundaki `text` metnini sözlüğü doldurmak için sadece bir kez gezeriz. Sözlüğe yazma ve okuma işlemleri $\mathcal{O}(1)$ sürer.
- **Alan Karmaşıklığı (Space Complexity):** $\mathcal{O}(1)$ — Hash map içerisinde sadece İngilizce küçük harfler tutulur (maksimum 26 karakter). Girdi olan metnin uzunluğu ne kadar artarsa artsın, hafızada kaplanan alan 26 karakteri geçemeyeceği için sabit kalır.

### Kod
```python
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        letters = {}
        for letter in text:
            if letter in letters:
                letters[letter] += 1
            else:
                letters[letter] = 1
                
        return min(
            letters.get('b', 0),
            letters.get('a', 0),
            letters.get('l', 0) // 2,
            letters.get('o', 0) // 2,
            letters.get('n', 0)
        )
```

---

## Yaklaşım 2: Çoklu Tarama / Built-in Count (Alternatif Çözüm)

### Mantık
Frekans haritasını (sözlük) manuel olarak oluşturmak yerine, Python'un yerleşik `.count()` metodunu kullanarak doğrudan string üzerinde arama yapabiliriz. Sadece ihtiyacımız olan 5 harfe bakarız. Kod çok daha kısa görünür ancak string üzerinde arka arkaya 5 kez tam tur atıldığı için büyük verilerde Hash Map kadar performanslı değildir.

### Algoritma
1. 'b', 'a', 'l', 'o' ve 'n' harfleri için `text.count()` metodunu çağır.
2. 'l' ve 'o' harflerinin dönüş değerlerini 2'ye böl (`// 2`).
3. Bu değerlerin hepsini `min()` fonksiyonu içine koy.
4. Çıkan sonucu döndür.

### Karmaşıklık
- **Zaman Karmaşıklığı (Time Complexity):** $\mathcal{O}(n)$ — String üzerinde 5 bağımsız arama yapılır. Toplamda $5n$ işlem olsa da asimptotik olarak $\mathcal{O}(n)$ kabul edilir.
- **Alan Karmaşıklığı (Space Complexity):** $\mathcal{O}(1)$ — Ekstra hiçbir veri yapısı oluşturulmaz.

### Kod
```python
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        return min(
            text.count('b'),
            text.count('a'),
            text.count('l') // 2,
            text.count('o') // 2,
            text.count('n')
        )
```