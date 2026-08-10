### [13. Roman to Integer](https://leetcode.com/problems/roman-to-integer/)

Sayımız sonraki gelecek olan sayıdan (ki buna da hashmap ile bakıyoruz) küçük ise ana toplam sayımızı (`result`) kendisi kadar küçültüyorduk. 
Çünkü kurala bakarsak aslında bize söylenen şey de o:
- "I can be placed before V (5) and X (10) to make 4 and 9"
- "X can be placed before L (50) and C (100) to make 40 and 90."
- "C can be placed before D (500) and M (1000) to make 400 and 900."

Bu sorunu öncesinde daha küçük bir sayı var mı diye kontrol ederek böyle çözüyoruz:
`roman_map[s[i]] < roman_map[s[i + 1]]`

Ama bir kontrol daha yapmamız lazım. `i+1` ile bir sonraki indekse de baktığımız için taşma (IndexError) sorunundan kurtulmak amacıyla gideceğimiz sınır `i < len(s)-1` olmalı.
3 sembollü bir roman rakamı düşünürsen, indeksler 0, 1 ve 2'dir. `for` döngüsünde `i` son elemana (yani indeks 2'ye) geldiğinde, `i+1` 3 olur ve dizi sınırlarının dışına çıkar.

`s[i + 1]` ifadesinin dizinin sınırları dışına çıkmaması için `i + 1` değerinin en fazla dizinin son indeksi olan `len(s) - 1` olması gerekir. Bu eşitsizliği (`i + 1 <= len(s) - 1`) matematiksel olarak düzenlediğimizde `i <= len(s) - 2` elde ederiz. Tam sayılarla işlem yaptığımız için `i <= len(s) - 2` eşitsizliği ile `i < len(s) - 1` koşulu aynı şeyi ifade eder.

eğer sayıdan sonraki sayı kendisinden büyük değilse normal şekilde sonuca ekleme yapıyoruz  `result += roman_map[s[i]]`

### Code
```python
class Solution(object):
    def romanToInt(self, s):
        roman_map = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        result = 0

        for i in range(len(s)):
            if i < len(s)-1 and roman_map[s[i]] < roman_map[s[i + 1]]:
                result -= roman_map[s[i]]
            else:
                result += roman_map[s[i]]
        return result
```

