> 📌 **Rehber:** Bu dizin, **Dynamic Programming (Dinamik Programlama - DP)** kalıbı için bir Kavram Haritası işlevi görür.
> * **Teorik Mantık:** Temel prensipler, alt varyasyonlar ve zaman/alan karmaşıklığı analizleri için bu `README.tr.md` dosyasını okuyun.
> * **Pratik Uygulamalar:** Kalıbın pratikte nasıl uygulandığını görmek için spesifik soru klasörlerine gidin (örneğin, `0070-Climbing Stairs`). Özel istisnalar (edge cases) ve alternatif çözümler bu klasörlerin içinde belgelenmiştir.

## Dynamic Programming (DP) Kalıbı Nedir?

* **Tanım:** Karmaşık problemleri daha basit ve **örtüşen alt problemlere (overlapping subproblems)** bölerek çözen algoritmik bir optimizasyon tekniğidir. İki ana özelliğe dayanır: Örtüşen Alt Problemler (aynı problemin defalarca çözülmesi) ve Optimal Alt Yapı (ana problemin en iyi çözümünün, alt problemlerin en iyi çözümlerinden inşa edilebilmesi).
* **Temel Gücü:** DP, hız kazanmak için belleği feda eder. Aynı durumları tekrar tekrar hesaplamak yerine (ki bu kaba kuvvet özyinelemesinde `O(2^n)` üstel zaman karmaşıklığına neden olur), DP bu alt problemlerin sonuçlarını "önbelleğe alır" (cache/memoize). Bu işlem, zaman karmaşıklığını inanılmaz bir şekilde `O(n)` veya `O(n²)` seviyelerine düşürür.

---

## Temel Varyasyonlar ve Algoritmik Stratejiler

Dinamik Programlamanın iki temel uygulanış biçimi (Yukarıdan Aşağıya ve Aşağıdan Yukarıya) ve problemin değişken sayısına (state) bağlı olarak değişen boyutları vardır.

### 1. Yukarıdan Aşağıya (Top-Down / Memoization)
* **Algoritma:** Ana problemden ("en tepeden") başlayın ve onu alt problemlere bölmek için özyineleme (recursion) kullanın. Bir durumu hesaplamadan önce, bunun bir önbellekte (genellikle bir Hash Map veya dizi) halihazırda var olup olmadığını kontrol edin. Varsa, hesaplamak yerine doğrudan önbellekteki o değeri döndürün. Yoksa hesaplayın, önbelleğe kaydedin ve sonra döndürün.
* **Ne zaman kullanılır:** Problem doğal bir özyineleme (Backtracking gibi) ağacı gibi hissettirdiğinde, ancak aynı parametrelerin özyinelemeli fonksiyona defalarca gönderildiğini fark ettiğinizde.
* **Repo Örnekleri:**
  * [0322-Coin Change](./0322-Coin%20Change)

### 2. Aşağıdan Yukarıya (Bottom-Up / Tabulation)
* **Algoritma:** Özyinelemeden tamamen kaçının. Kesin olarak bilinen en küçük alt problemlerden (temel durumlar / base cases) başlayın ve iteratif bir `for` döngüsü ve bir `dp` dizisi kullanarak nihai cevaba doğru ilerleyin. `dp[i]` hücresinin cevabı, daha önce hesaplanmış olan `dp[i - 1]` veya `dp[i - 2]` gibi değerler kullanılarak bulunur.
* **Ne zaman kullanılır:** Alt problemlerin hangi sırayla çözülmesi gerektiğini tam olarak bildiğinizde ve özyinelemeli fonksiyon çağrılarının yaratacağı bellek yükünden (call stack overflow) kaçınmak istediğinizde.
* **Repo Örnekleri:**
  * [0070-Climbing Stairs](./0070-Climbing%20Stairs)
  * [0198-House Robber](./0198-House%20Robber)

### 3. 2B Dinamik Programlama (2D Grids & Strings)
* **Algoritma:** Problem durumu bir değil, iki değişkene bağlıdır. Sonuçları önbelleğe almak için 2 boyutlu bir matris (örneğin `dp[r][c]`) kullanırsınız. Bir hücrenin değeri genellikle tam üstündeki, solundaki veya çaprazındaki hücrenin değerine bağlıdır.
* **Ne zaman kullanılır:** Sadece sağa/aşağıya hareket edebildiğiniz matris (grid) gezinmelerinde veya iki farklı metni birbiriyle kıyaslarken (Longest Common Subsequence veya Edit Distance gibi).
* **Repo Örnekleri:**
  * [0062-Unique Paths](./0062-Unique%20Paths)
  * [1143-Longest Common Subsequence](./1143-Longest%20Common%20Subsequence)

---

## 💡 Profesyonel Detaylar ve İstisnai Durumlar

* **Durum (State) ve Tekrarlama Bağıntısı (Recurrence Relation):** DP'nin en zor kısmı "Durumu" tanımlamak (`dp[i]` neyi temsil ediyor?) ve "Tekrarlama Bağıntısını" kurmaktır (`dp[i]`, `dp[i-1]` ile nasıl bir ilişkiye sahip?). Herhangi bir kod yazmadan önce mutlaka matematiksel denklemi kağıda yazın (örn. `dp[i] = max(dp[i-1], dp[i-2] + nums[i])`).
* **Alan Optimizasyonu (Space Optimization):** Aşağıdan Yukarıya (Bottom-Up) 1 Boyutlu DP'de, eğer `dp[i]` sadece kendinden önceki iki duruma (`dp[i-1]` ve `dp[i-2]`) bağlıysa, **`O(n)` boyutunda devasa bir dizisine ihtiyacınız yoktur**. Sadece önceki iki değeri takip etmek için iki basit değişken kullanabilir, böylece alan karmaşıklığını (Space Complexity) `O(n)`'den kesin olarak `O(1)`'e düşürebilirsiniz. Bu, mülakatlarda devasa bir artı puandır.
* **Başlangıç Değerleri (Base Cases):** Bir DP algoritması, temel durumları (base cases) kadar iyidir. Her zaman `dp[0]` (ve bazen `dp[1]`) değerlerini çok dikkatli başlatın (initialize). Minimum bulma problemlerinde diziyi sonsuzluk (`float('inf')`) ile başlatın. Maksimum bulma veya sayma problemlerinde ise `0` ile başlatın.