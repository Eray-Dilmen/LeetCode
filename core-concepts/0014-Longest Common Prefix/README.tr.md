### [14. Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/)

* Algoritma, dizideki ilk kelimeyi (`strs[0]`) referans alarak karakterleri sırayla kontrol eder.
* Ortak öneki tutmak için boş bir `cm_pref` string'i kullanılır.
* Dış döngü, ilk kelimenin karakter indekslerinde (`i`) ilerler. İç döngü ise dizideki ardışık kelimeleri (`strs[j]` ve `strs[j+1]`) kıyaslar.
* Kontrol sırasında, `i` indeksinin her iki kelimenin sınırları içinde olup olmadığına ve bu indeksteki karakterlerin eşleşip eşleşmediğine bakılır.
* Karakterler eşleşiyorsa bir sonraki kelimeye geçilir. Eşleşmezse veya kelimelerden birinin sonuna gelinmişse, `is_common` değeri `False` yapılarak iç döngüden çıkılır.
* Eğer iç döngü sonucunda karakter tüm kelimelerde aynıysa (`is_common` durumu korunmuşsa), o karakter `cm_pref`'e eklenir. Uyuşmazlık bulunduğu an dış döngü de kırılarak elde edilen string döndürülür.

### Code
```python
class Solution(object):
    def longestCommonPrefix(self, strs):
        cm_pref = ''
        for i in range(len(strs[0])): 
            is_common = True
            for j in range(len(strs)-1): 
                if i < len(strs[j]) and i < len(strs[j+1]) and strs[j][i] == strs[j+1][i]:
                    continue
                else:
                    is_common = False
                    break
                      
            if is_common:
                cm_pref += strs[0][i]
            else:
                break    
        
        return cm_pref
```