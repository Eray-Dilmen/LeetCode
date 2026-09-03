### [7. Reverse Integer](https://leetcode.com/problems/reverse-integer/)


* `is_negative` değişkeni, sayının orijinal halinde negatif olup olmadığını tutan bir boolean değerdir. 
* Sayıyı ters çevirmek için string'e dönüştürdüğümüzde eksi (`-`) işaretinin sona kaymasını engellemek amacıyla, sayıyı önce `abs()` (mutlak değer) fonksiyonu ile pozitif yapıyor ve ardından string olarak ters çeviriyoruz.
* İşlem tamamlandıktan sonra, en başta kaydettiğimiz `is_negative` durumunu kontrol ediyoruz. Eğer sayı başlangıçta negatifse, elde ettiğimiz sonucu tekrar negatife çeviriyoruz.
* Son olarak, soruda belirtildiği gibi sonucun 32-bit işaretli tam sayı sınırları (`-2^31` ile `2^31 - 1`) arasında olup olmadığını kontrol ediyoruz. Değer bu sınırların dışına çıkarsa `0` döndürüyoruz.

### Code
```python
class Solution(object):
    def reverse(self, x):
        is_negative = x < 0
        result = int(str(abs(x))[::-1])
        if is_negative:
            result = -result
            
        if result < -2**31 or result > 2**31-1:
            return 0
        return result
```