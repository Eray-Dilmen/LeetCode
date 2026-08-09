
Pythonda slicing method kullanırken sonuncu parametre kaçar kaçar gideceğini belirten bir koşuldur, `[::-1]` yaptığımız zaman -1'er adım olarak git demek oluyor ve bu sondan başlayıp 1'er adım gitmesini sağlar. 

O yüzden tersten şekilde printlememizi sağlar. 

Fakat sayı negatif ise bizden istenen bunun palindrom olmadığını belirtmemizdir. 
Bunun kontrolünü de en son çevirdikten sonra `if s == x_reverse` kontrolü ile sağlıyoruz.