# [383. Ransom Note](https://leetcode.com/problems/ransom-note/)

## Problem Açıklaması
Bize `ransomNote` (fidyeci mektubu) ve `magazine` (dergi) adında iki adet string veriliyor. Amacımız, `magazine` içindeki harfleri kullanarak `ransomNote` metnini oluşturup oluşturamayacağımızı bulmaktır. Eğer oluşturabiliyorsak `true`, oluşturamıyorsak `false` dönmemiz isteniyor.

`magazine` içindeki her bir harf, `ransomNote` içinde yalnızca **bir kez** kullanılabilir. Yani dergideki harf sayısının, mektupta kullanmak istediğimiz harf sayısına eşit veya ondan fazla olması gerekir.

---

## Genel Mantık ve Dikkat Edilmesi Gerekenler

- **Harf Frekansları (Adetleri):** Olayın özü "elimizde yeterince harf var mı?" sorusudur. Bir harften mektupta 3 tane varsa, dergide de en az 3 tane olmalıdır.
- **Hash Map (Sözlük) Avantajı:** Her harf için dergiyi baştan sona taramak yerine, dergideki harflerin sayısını bir sözlükte (Hash Map) tutmak en verimli yoldur. Harf arama işlemleri sabit sürede ($\mathcal{O}(1)$) gerçekleşir.
- **Çözüm Adımları:**
  1. Öncelikle `magazine` içerisindeki harfleri tek tek gezer ve hangi harften kaç adet bulunduğunu `guide` adındaki sözlüğümüze kaydederiz.
  2. Daha sonra `ransomNote` içerisindeki harfleri sırayla kontrol etmeye başlarız.
  3. Mektuptaki mevcut harf, sözlüğümüzde hiç yoksa veya adedi `0`'a düşmüşse (yani elimizde o harften kalmamışsa) anında `False` döndürürüz.
  4. Eğer harf elimizde varsa, harfi kullandığımız için sözlükteki adedini $1$ eksiltiriz.
  5. Döngü sorunsuz biterse, elimizdeki harflerle mektubu yazabilmişiz demektir, `True` döndürürüz.

---

## Kod

```python
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        guide = {}
        for index, letter in enumerate(magazine):
            if letter in guide:
                guide[letter] += 1
            else:
                guide[letter] = 1
                
        for char in ransomNote:
            if char not in guide or guide[char] == 0:
                return False
            guide[char] -= 1
            
        return True
```