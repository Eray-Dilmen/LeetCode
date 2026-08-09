### [1. Two Sum](https://leetcode.com/problems/two-sum/)

Temel Fikir:

elimizde bir dolaştığımız num var. num ile bir şeyin toplamı target’a eşit mi diye bakacağız

işte aradığımız sayı target-num’dır.
İki kere döngü kurup hepsini tek tek tarayarak bulmak yerine eksik olan bu sayıyı hafızada aramak daha mantıklıdır.

<br>
Algoritma: 

sayıları gezerken şu anki sayı olan num için bakarken mapping içinde diğer sayı varsa 
num ile target-num’un index’ini returnluyoruz.

eğer tamamlayıcı sayı sözlükte  yoksa, o anki sayıyı(num) sözlüğe ekliyoruz. 
Değerleri ise index olacak çünkü sözlükten ilgili numaranın bize index’i soruluyor.

return kısmında ‘mapping[target - num]’ demememizin nedeni o sayının index değerini almak için 
çünkü sözlük içerisinde value'ya atanıyor.
Diğerini index olarak bırakmamızın nedeni o anki sayının indeksi zaten enumerate sayesinde elimizde olduğundan doğrudan index yazıyoruz.

### Code
```python
class Solution(object):
    def twoSum(self, nums, target):
        mapping = {}

        for index, num in enumerate(nums): 
            if (target - num) in mapping:
                return [mapping[target - num], index]
            else:
                mapping[num] = index
``` 