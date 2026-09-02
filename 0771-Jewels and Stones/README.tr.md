# [771. Jewels and Stones](https://leetcode.com/problems/jewels-and-stones/)

## Problem Açıklaması
Bize, mücevher olan taş türlerini temsil eden bir `jewels` stringi ve elimizdeki taşları temsil eden bir `stones` stringi veriliyor. `stones` içerisindeki her bir karakter elimizdeki bir taşı temsil eder. Amacımız, elimizdeki taşlardan kaç tanesinin aynı zamanda bir mücevher olduğunu bulmaktır.

Harfler büyük/küçük harfe duyarlıdır (case-sensitive), yani `"a"` ile `"A"` farklı taş türleri olarak kabul edilir.

---

## Genel Mantık ve Dikkat Edilmesi Gerekenler

- **Büyük/Küçük Harf Farkı:** Karakter karşılaştırması yaparken küçük harf ile büyük harfi birbirinden tamamen farklı türler olarak ele almalıyız.
- **Tekrarlı Sayım:** Elimizdeki `stones` stringinde aynı mücevherden birden fazla olabilir; her birini tek tek saymamız gerekir.
- **Kümelerin (Set) Avantajı:** İki iç içe döngü kurup her taşı tüm mücevherlerle tek tek karşılaştırmak yerine, `jewels` stringini bir **Hash Set** yapısına dönüştürürüz. Bu sayede bir taşın mücevher olup olmadığını aramak her adımda sabit zamanda ($\mathcal{O}(1)$) gerçekleşir.
- **Çözüm Adımları:**
  1. `jewels` içerisindeki karakterleri benzersiz elemanlar tutan bir kümeye (`jews = set(jewels)`) aktarırız.
  2. Eşleşen taşları saymak için `count` değişkenini `0` olarak başlatırız.
  3. `stones` içerisindeki her bir taşı sırayla gezer, kümemizin içinde olup olmadığını kontrol ederiz. Varsa `count` değerini $1$ artırırız.
  4. Döngü bittiğinde toplam `count` değerini döndürürüz.

---

## Kod

```python
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jews = set(jewels)
        count = 0
        for stone in stones:
            if stone in jews:
                count += 1
        return count
```