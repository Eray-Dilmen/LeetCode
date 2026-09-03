# 771. Jewels and Stones

> 💡 **Not:** Bu soru **Hash Maps & Sets** kalıbı ile çözülmüştür. Kalıbın genel mantığı, kullanım senaryoları ve teorik detayları için [ README.md](../README.md) dosyasına bakabilirsiniz.

---
## Problem Statement
You're given strings `jewels` representing the types of stones that are jewels, and `stones` representing the stones you have. Each character in `stones` is a type of stone you have. You want to know how many of the stones you have are also jewels.

Letters are case sensitive, so `"a"` is considered a different type of stone from `"A"`.

### Example 1:
> **Input:** `jewels = "aA"`, `stones = "aAAbbbb"`  
> **Output:** `3`

### Example 2:
> **Input:** `jewels = "z"`, `stones = "ZZ"`  
> **Output:** `0`

### Türkçe Açıklama
Sana mücevher türlerini temsil eden bir `jewels` metni ve elindeki taşları temsil eden bir `stones` metni veriliyor. `stones` içerisindeki her bir karakter elindeki bir taşı temsil eder. Amacın, sahip olduğun taşların kaç tanesinin aynı zamanda bir mücevher olduğunu bulmaktır.

Harfler büyük-küçük harfe duyarlıdır (case-sensitive), yani `"a"` ile `"A"` farklı türde taşlar olarak kabul edilir.

---

## Verilenler
* `jewels = "aA"` (Uzunluk: $n$)
* `stones = "aAAbbbb"` (Uzunluk: $m$)

---

## 1. Brute Force Yaklaşımı $\implies O(n \cdot m)$

`stones` içindeki her bir taş ($m$ tane) için tek tek `jewels` string'i taranır ($n$ tane). Python'daki `in` operatörü string üzerinde arka planda gizli bir for döngüsü ($O(n)$) çalıştırır.

* İlk taş `'a'` için $\implies$ `'a'` ve `'A'` kontrol edilir ($n$ adım).
* İkinci taş `'A'` için $\implies$ `'a'` ve `'A'` kontrol edilir ($n$ adım).
* **Toplam işlem:** $m \text{ defa } n \text{ arama} = m \cdot n$ adım.

```python
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        
        # stones üzerinde m adım döner
        for stone in stones:
            # String üzerinde arama O(n) sürer (gizli döngü)
            if stone in jewels:
                count += 1
                
        return count
```

* **Time Complexity:** $O(n \cdot m)$ — İç içe iki döngü oluşur.
* **Space Complexity:** $O(1)$ — Ekstra bir veri yapısı oluşturulmaz.

## 2. Hash Set Yaklaşımı (Optimal) $\implies O(n + m)$

String yerine $O(1)$ sürede arama yapabilen bir Hash Set kullanılır. İşlem iki bağımsız aşamaya bölünür:

1. **Aşama 1 (Set Oluşturma):** `jewels` string'indeki tüm karakterler alınıp bir `Set` yapısına atılır (`s = set(jewels)`).
   * $n$ tane karakter tek tek okunup hash tablosuna eklenir.
   * **Maliyet:** $O(n)$
2. **Aşama 2 (Taşları Kontrol Etme):** `stones` string'i üzerinde tek bir döngü kurulur ($m$ adım).
   * Her bir taş için `stone in s` kontrolü yapılır.
   * Set'te arama yapmak $O(1)$ olduğu için her taşın kontrolü anında biter.
   * **Maliyet:** $m \cdot O(1) = O(m)$

--- 
* **Toplam Maliyet:**

$$\text{Set'e yazma } (n) + \text{Set'ten sorgulama } (m) = \mathbf{O(n + m)}$$

* **Time Complexity:** $O(n + m)$ — İç içe döngü çarpılır ($n \cdot m$), ardışık yapılan işlemler toplanır ($n + m$).
* **Space Complexity:** $O(n)$ — `jewels` karakterlerini saklamak için Set kullanılır. 

* (kod içerisinde sadece set'i depoluyoruz o da n karakter kadar. O yüzden O(n) )


```python
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        # Aşama 1: O(n) sürede Set oluşturma
        s = set(jewels)
        count = 0
        
        # Aşama 2: O(m) sürede taşları sorgulama
        for stone in stones:
            # Set üzerinde arama O(1) sürer
            if stone in s:
                count += 1
                
        return count
```
