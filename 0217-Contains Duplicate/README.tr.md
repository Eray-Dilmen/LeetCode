# [217. Contains Duplicate](https://leetcode.com/problems/contains-duplicate/)

## Problem Açıklaması
Sana `nums` adında tam sayılardan oluşan bir dizi veriliyor. Eğer dizideki herhangi bir değer en az iki kez geçiyorsa `true`, tüm elemanlar birbirinden farklıysa (hiç tekrar yoksa) `false` döndürmen isteniyor.

### Örnek 1:
> **Girdi:** `nums = [1,2,3,1]`  
> **Çıktı:** `true`

### Örnek 2:
> **Girdi:** `nums = [1,2,3,4]`  
> **Çıktı:** `false`

### Örnek 3:
> **Girdi:** `nums = [1,1,1,3,3,4,3,2,4,2]`  
> **Çıktı:** `true`

---

## Yaklaşım 1: Hash Set (Optimal Çözüm)

### Mantık
Bir dizide tekrar eden eleman olup olmadığını bulmak için sadece bir sayıyı daha önce görüp görmediğimizi bilmemiz yeterlidir. Her sayının frekansını tutmak yerine bir Hash Set kümesi kullanabiliriz. Dizi üzerinde gezinirken, mevcut sayının set içinde olup olmadığını kontrol ederiz. Eğer varsa, tekrar eden bir sayı bulmuşuz demektir ve anında `True` dönebiliriz (erken çıkış). Yoksa, sayıyı set'e ekler ve devam ederiz.

### Algoritma
1. `numbers` adında boş bir hash set oluştur.
2. `nums` içindeki her bir `number` için döngü kur.
3. `number` değerinin `numbers` setinde olup olmadığını kontrol et:
   - **Eğer varsa:** Anında `True` döndür.
   - **Eğer yoksa:** `number` değerini `numbers` setine ekle.
4. Döngü, hiçbir kopya bulamadan biterse `False` döndür.

### Karmaşıklık
- **Zaman Karmaşıklığı (Time Complexity):** $\mathcal{O}(n)$ — $n$ uzunluğundaki diziyi en fazla bir kez gezeriz. Hash set üzerinde arama ve ekleme işlemleri ortalama $\mathcal{O}(1)$ zaman alır.
- **Alan Karmaşıklığı (Space Complexity):** $\mathcal{O}(n)$ — En kötü senaryoda (hiç tekrar eden eleman yoksa), set içerisine tüm $n$ eleman eklenir.

### Kod

```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numbers = set()
        
        for number in nums:
            if number in numbers:
                return True
            numbers.add(number)
            
        return False
```

---

## Yaklaşım 2: Hash Map / Frekans Sayımı (Alternatif Çözüm)

### Mantık
Bu yaklaşım, bir Hash Map (sözlük) kullanarak dizideki her sayının kaç kez geçtiğini hesaplar. Frekanslar doldurulduktan sonra, harita üzerinde gezilerek herhangi bir sayının 1'den büyük bir sayıya sahip olup olmadığı kontrol edilir. Bu yöntem doğru çalışsa ve doğrusal zaman karmaşıklığına sahip olsa da, iki ayrı döngü (biri sözlüğü oluşturmak, diğeri kontrol etmek için) gerektirir ve hem anahtarları (keys) hem de değerleri (values) sakladığı için daha fazla bellek kullanır.

### Algoritma
1. `number_count` adında boş bir sözlük (hash map) oluştur.
2. Sözlüğü doldurmak için `nums` üzerinde döngü kur. Bir sayı sözlükte yoksa 1 değeriyle ekle. Eğer varsa değerini (frekansını) 1 artır.
3. Doldurulan `number_count` sözlüğü üzerinde döngü kur.
4. Eğer herhangi bir sayının frekansı 1'den büyükse, `True` döndür.
5. Hiçbir kopya bulunamazsa `False` döndür.

### Karmaşıklık
- **Zaman Karmaşıklığı (Time Complexity):** $\mathcal{O}(n)$ — Diziyi bir kez ($\mathcal{O}(n)$) gezeriz ve ardından en kötü ihtimalle sözlüğü bir kez ($\mathcal{O}(n)$) gezeriz. Toplam işlem miktarı $n$ ile orantılı artar.
- **Alan Karmaşıklığı (Space Complexity):** $\mathcal{O}(n)$ — Hash map içerisinde $n$ adede kadar benzersiz sayı ve onların frekanslarını saklarız.

### Kod

```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        number_count = {}
        
        for number in nums:
            if number not in number_count:
                number_count[number] = 1
            else:
                number_count[number] += 1
        
        for number in number_count:
            if number_count[number] > 1:
                return True
        
        return False
```

---

## Yaklaşım 3: Brute Force

### Mantık
Brute force yaklaşımı, iç içe geçmiş döngüler kullanarak dizideki her elemanı kendisinden sonra gelen diğer tüm elemanlarla karşılaştırır. Eşleşme bulunursa kopya (duplicate) var demektir.

### Algoritma
1. Dış döngü ile `i` indeksindeki bir sayıyı seç.
2. İç döngüyü `i + 1` indeksinden başlatarak dizinin sonuna kadar devam ettir.
3. `i` indeksindeki sayı ile `j` indeksindeki sayıyı karşılaştır. Eğer eşitlerse `True` döndür.
4. Tüm karşılaştırmalar bir eşleşme olmadan biterse `False` döndür.

### Karmaşıklık
- **Zaman Karmaşıklığı (Time Complexity):** $\mathcal{O}(n^2)$ — İç içe döngüler her bir elemanı geri kalanlarla kıyaslar, bu da yaklaşık $\approx \frac{n(n-1)}{2}$ işlem yaratır. Bu durum karesel bir zaman karmaşıklığı oluşturur ve büyük dizilerde Time Limit Exceeded (TLE) hatası almanıza yol açar.
- **Alan Karmaşıklığı (Space Complexity):** $\mathcal{O}(1)$ — Kıyaslama işlemi yerinde yapıldığı için ekstra alan (bellek) kullanılmaz.

### Kod

```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return True
                    
        return False
```