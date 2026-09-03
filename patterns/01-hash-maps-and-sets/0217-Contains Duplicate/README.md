# 217. Contains Duplicate

> 💡 **Not:** Bu soru **Hash Maps & Sets** kalıbı ile çözülmüştür. Kalıbın genel mantığı, kullanım senaryoları ve teorik detayları için [ README.md](../README.md) dosyasına bakabilirsiniz.

---
## Problem Statement
Given an integer array `nums`, return `true` if any value appears at least twice in the array, and return `false` if every element is distinct.

### Example 1:
> **Input:** `nums = [1,2,3,1]`  
> **Output:** `true`

### Example 2:
> **Input:** `nums = [1,2,3,4]`  
> **Output:** `false`

### Example 3:
> **Input:** `nums = [1,1,1,3,3,4,3,2,4,2]`  
> **Output:** `true`

### Türkçe Açıklama
Sana `nums` adında tam sayılardan oluşan bir dizi veriliyor. Eğer dizideki herhangi bir değer en az iki kez geçiyorsa `true`, tüm elemanlar birbirinden farklıysa (hiç tekrar yoksa) `false` döndürmen isteniyor. Amacın dizide kopya/tekrar eden eleman olup olmadığını bulmaktır.

---

## Verilenler
* `nums = [1, 2, 3, 1]` (Dizinin uzunluğu: $n$)

---

## 1. Hash Set Yaklaşımı (Optimal) $\implies O(n)$

Dizi üzerinde $O(1)$ sürede arama yapabilen bir Hash Set kullanılır. Elemanları tek tek kümeye (set) eklerken, o elemanın zaten kümede olup olmadığına bakarız. Eğer kümede varsa, o elemandan daha önce de görülmüş demektir ve anında `True` döneriz (Erken Çıkış / Early Exit).

```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numbers = set()
        
        # nums üzerinde n adım döner
        for number in nums:
            # Set üzerinde arama O(1) sürer
            if number in numbers:
                return True
            
            # Set'e ekleme işlemi
            numbers.add(number)
            
        return False
```

* **Toplam Maliyet:**
Dizideki elemanlar tek tek gezilir ($n$). Set'te arama yapmak $O(1)$'dir.
$$\text{Maksimum Döngü Sayısı } (n) \cdot \text{Arama Maliyeti } (1) = \mathbf{O(n)}$$

* **Time Complexity:** $O(n)$ — En kötü senaryoda (hiç tekrar yoksa) dizi bir kez tamamen gezilir.
* **Space Complexity:** $O(n)$ — En kötü senaryoda tüm benzersiz elemanlar Set içinde saklanır.

---

## 2. Frequency Map Yaklaşımı (Benim kodum) $\implies O(n)$

Bir sözlük (Dictionary) kullanılarak her sayının dizide kaç kez geçtiği hesaplanır. Daha sonra sözlükteki elemanlar gezilerek herhangi bir sayının frekansının 1'den büyük olup olmadığına bakılır.

* **Aşama 1 (Sözlüğü Doldurma):** Dizideki $n$ eleman gezilerek sayıların frekansları sözlüğe eklenir ($O(n)$).
* **Aşama 2 (Tekrar Kontrolü):** Sözlükteki benzersiz elemanlar (en kötü durumda $m = n$ adet) gezilip frekans kontrolü yapılır ($O(n)$).

```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        number_count = {}
        
        # Aşama 1: O(n) sürede frekansları hesaplama
        for number in nums:
            # Sözlükte arama O(1) sürer
            if number not in number_count:
                number_count[number] = 1
            else:
                number_count[number] += 1
        
        # Aşama 2: En kötü durumda O(n) sürede tekrar arama
        for number in number_count:
            if number_count[number] > 1:
                return True
        
        return False
```

* **Toplam Maliyet:**
$$\text{Sözlüğe Yazma } (n) + \text{Sözlüğü Gezme } (n) = O(2n) \implies \mathbf{O(n)}$$

> **Not:** Asimptotik karmaşıklığı optimal çözümle aynı ($O(n)$) olsa da, sözlükler değerleri (values) de tuttuğu için bellekte daha çok yer kaplar ve iki ayrı döngü çalıştığı için sabit bir çarpan (constant factor) dezavantajı yaratır.

* **Time Complexity:** $O(n)$ — En kötü durumda $2n$ işlem yapılır, başkatsayı atıldığı için $O(n)$'dir.
* **Space Complexity:** $O(n)$ — En kötü durumda tüm benzersiz sayılar ve sayı frekansları sözlükte tutulur.

---

## 3. Brute Force Yaklaşımı $\implies O(n^2)$

İç içe iki döngü kurularak dizideki her bir eleman, kendisinden sonraki tüm elemanlarla tek tek karşılaştırılır. Eğer eşleşen iki eleman bulunursa `True` döndürülür. Ekstra alan kullanılmaz ancak zaman açısından çok yavaştır ve büyük dizilerde **Time Limit Exceeded (TLE)** hatası alır.

```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Dış döngü n adım döner
        for i in range(len(nums)):
            # İç döngü n - i - 1 adım döner
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return True
                    
        return False
```

* **Time Complexity:** $O(n^2)$ — İç içe döngüler diziyi ortalama $\frac{n(n-1)}{2}$ kez gezer.
* **Space Complexity:** $O(1)$ — Ekstra bir veri yapısı oluşturulmaz.