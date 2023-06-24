
# 1 - \ n ve \n ifadeleri : \n cursoru alt satıra indiri. \t cusroru 1 tab mesafeye taşır.
print("hello"+"\n"+"world!")
# / hello
#   world!  


# 2 - .capitalize() metodu string ifadenin sadece ilk harfini büyük harfte tutar.  

print("hello Wolrd!".capitalize())
# / Hello world!


# 3 - .casefold() metodu tüm harfleri küçük harflere dönüştürmenin yanı sıra, Unicode karakterlerini de eşleştirir ve dönüştürür.

print("HeLLo wOrLD!".casefold())
# / hello world!


# 4 - .center() metodu  bir stringi belirli bir genişlikte ortalamak için kullanılır ve "width" ve "fillchar" parametrelerini alır. Bu metodun kullanımı, stringleri daha okunaklı hale getirmek için faydalı olabilir.

print("HELLO WORLD".center(20,"-"))
# / ----HELLO WORLD!---- ( string ifadeyi 20 karaktere tamamlayıp girilen ifadeyi ortalar )
print("HELLO WORLD".center(20,"0"))
# / 0000HELLO WORLD00000



# 5 - .count() metodu bir string içinde belirli bir karakter veya karakter dizisinin (substring) sayısını bulmak için kullanılır. başlangıç ve bitiş indexleri verebiliriz.

print("hello wolrd!".count("l"))
# / 3
print("111222333444555".count("1"))
# / 3


# 6 - .endcode() metodu bir stringi belirli bir karakter kodlamasına göre kodlamak için kullanılır. Kodlama, bir stringin karakterlerini, sayısal değerlerle eşleştirerek, karakterleri temsil eden baytların bir dizisini oluşturur.

print("merhaba dünya!".encode)
# / b'Merhaba, D\xc3\xbcnya!'


# 7 - .endswith() metodu bir stringin belirli bir karakter veya karakter dizisiyle bitip bitmediğini kontrol etmek için kullanılır. başlangıç ve bitiş indexi verilebilir.

print("hello wolrd!".endswith("!"))
#print = true (ifadenin parantez içinde belirtilen ile bitip bitmediğini kontrol eder. sonuç true / false)


# 8 - .expandtabs() metodubir string içindeki tab karakterlerini belirli bir sayıda boşluk karakteriyle değiştirmek için kullanılır. herhangi bir değer girilmez ise 8 karakterli boşluk kaplar.

print("hello\twolrd!".expandtabs(5))
# / hello     wolrd! (tab yerine 5 tane boşluk var)


# 9 - .find() metodu bir string içinde belirli bir karakter veya karakter dizisinin (substring) ilk oluşumunun indeksini döndürmek için kullanılır. alt üst index verilebilir. eğer aranan ifade yoksa sonuç -1 döner.

print("hello wolrd!".find("o"))
# / 4
print("hello wolrd!".find("k"))
# / -1


# 10 - .format() metodu bir dizeyi biçimlendirmek için kullanılır. Bu metot, süslü parantez içine alınmış değiştirilebilir verileri (değişkenler, sabitler vb.) kullanarak bir dizeyi biçimlendirmeyi sağlar.

print("HELLO {} !".format("WORLD"))
# / HELLO WORLD


# 11 - .format_map() metodu bir sözlük üzerinde biçimlendirme işlemi yapmak için kullanılan bir metottur. Yer tutucuları sözlük anahtarlarına göre belirler.

person = {'name': 'John', 'age': 25}
print("My name is {name} and I am {age} years old".format_map(person))

# / My name is John and I am 25 years old


# 12 - .index() metodu bir liste, tuple veya dize içinde belirtilen bir öğenin ilk indeksini döndürmek için kullanılır.

print("hello wolrd!".index("!"))
# / 11


# 13 - .isalnum() metodu bir karakter dizisinin yalnızca harf ve sayısal karakterlerden oluşup oluşmadığını kontrol etmek için kullanılır. Bu metot, bir karakter dizisi yalnızca harf ve sayısal karakterler içeriyorsa "True", aksi takdirde "False" değerini döndürür.

print("hello wolrd!".isalnum())
# / False (! den dolayı)
print("hello wolrd1".isalnum())
# / False (" " den dolayı)
print("hellowolrd1".isalnum())
# / True (harf veya rakamdan başka değer olmadığından dolayı)


# 14 - .isalpha() metodu bir karakter dizisinin yalnızca harf karakterleri içerip içermediğini kontrol etmek için kullanılır. Bu metot, bir karakter dizisi yalnızca harf karakterleri içeriyorsa "True", aksi takdirde "False" değerini döndürür.

print("hello wolrd!".isalpha())
# / False (" " den dolayı)
print("hellowolrd!".isalpha())
# / False ("!" den dolayı)
print("hellowolrd".isalpha())
# / True


# 15 - .isascii() metodu bir karakter dizisinin yalnızca ASCII karakterlerinden oluşup oluşmadığını kontrol etmek için kullanılır. Bu metot, bir karakter dizisi yalnızca ASCII karakterleri içeriyorsa "True", aksi takdirde "False" değerini döndürür.

print("hello wolrd!".isascii())
# / True
print("Привет, мир!".isascii())
# / False


# 16 - .isdecimal() metodubir karakter dizisinin yalnızca ondalık sayısal karakterlerden oluşup oluşmadığını kontrol etmek için kullanılır. Bu metot, bir karakter dizisi yalnızca yalnızca 0-9 arasındaki rakam karakterlerini kabul eder."True", aksi takdirde "False" değerini döndürür.

print("hello wolrd!".isdecimal())
# / False
print("1234".isdecimal())
# / True


# 17 - .isdigit() metodu bir karakter dizisinin yalnızca sayısal karakterlerden oluşup oluşmadığını kontrol etmek için kullanılır. Bu metot, bir karakter dizisi yalnızca sayısal karakterler içeriyorsa "True", aksi takdirde "False" değerini döndürür. Unicode veritabanındaki diğer sayısal karakterler de dahil olmak üzere, tüm sayısal karakterleri kabul eder.

print("hello wolrd!".isdigit())
# / False
print("³12".isdigit())
# / True ( 0-9 arası rakam olması gerekmiyor , unicod sayisal bir ifade de olabilir. yeterki boşluk olmasın.)


# 18 - .isidentifier() metodu bir karakter dizisinin geçerli bir Python tanımlayıcısı (identifier) olup olmadığını kontrol etmek için kullanılır. 

print("hello wolrd!".isidentifier())
# / False (Boşluktan Ötürü)
print("42world".isidentifier())
# / False (Rakamla Başladığı için)
print("world42".isidentifier())
# / True


# 19 - .islower() metodu bir karakter dizisinin tüm harflerinin küçük harf olup olmadığını kontrol etmek için kullanılır. Eğer karakter dizisi içerisinde hiçbir harf yoksa, "False" döndürür.Bu metot sadece ASCII karakterlerinde çalışır.

print("hello wolrd!".islower())
# / True


# 20 - .isnumeric() metodu bir karakter dizisinin tamamen sayısal karakterlerden oluşup oluşmadığını kontrol etmek için kullanılır. Bu metod sadece Unicode karakterlerinde çalışır.Örneğin, "isnumeric()" metodu "²", "½" veya "٢" gibi Unicode karakterlerini de sayısal olarak kabul eder.

print("12345".isnumeric())
# / True


# 21 - .isprintable() metodu bir karakter dizisinin tüm karakterlerinin yazdırılabilir (print edilebilir) olup olmadığını kontrol eder. Bu metot, karakter dizisi içinde herhangi bir yazdırılamaz karakter bulunması durumunda False değerini döndürür.

print("hello wolrd!".isprintable())
print("hello \n wolrd!".isprintable())
# / True
# / False (\n den ötürü)


# 22 - .isspace() metodu bir karakter dizisinin tüm karakterlerinin boşluk karakterleri (boşluk, tab, satırbaşı vb.) olup olmadığını kontrol eder. Metot, karakter dizisinde boşluk karakteri olmadığı durumlarda False değerini döndürür.

print("hello wolrd!".isspace())
print(" ".isspace())
# / False
# / True


# 23 - .istitle() metodu bir karakter dizisinin baş harflerinin büyük harf olup olmadığını kontrol eder. Eğer karakter dizisindeki tüm kelimelerin baş harfleri büyük harf ise metot True değerini, aksi takdirde False değerini döndürür.

print("hello wolrd!".istitle())
print("Hello World".istitle())
# / False
# / True


# 24 - .isupper() metodu bir karakter dizisinin tüm harflerinin büyük harf olup olmadığını kontrol eder. Metot, karakter dizisinde küçük harf veya diğer karakterler varsa False değerini döndürür.

print("hello wolrd!".isupper())
print("Hello World!".isupper())
print("HELLO WORLD!".isupper())
# / False
# / False
# / True


# 25 - .join() metodu bir karakter dizisi veya karakter listesi içerisindeki elemanları belirtilen bir ayracı kullanarak birleştirir. bir öğe listesi veya karakter dizisi gibi bir iterable nesneye uygulanabilir. 

print("-".join("hello world!"))
# / h-e-l-l-o- -w-o-r-l-d-!


#26 - .ljust() mwetodu  bir karakter dizisini belirtilen uzunluğa kadar belirtilen bir karakterle soldan doldurur.iki parametre alır: ljust(<uzunluk>, <karakter>).

print("hello wolrd!".ljust(20,"a"))
# / hello wolrd!aaaaaaaa


# 27 - .lower() metodu bir karakter dizisindeki tüm harfleri küçük harfe çevirir ve bu değiştirilmiş karakter dizisini döndürür. yalnızca ASCII karakterleri için küçük harfe dönüştürme işlemi yapar

print("HELLO WORLD!".lower())
# / hello world! 


# 28 - .lstrip() metodu bir karakter dizisindeki başındaki boşlukları (veya belirtilen başka bir karakteri) kaldırır ve bu değiştirilmiş karakter dizisini döndürür.
x = "hello world!"
print(x)
xlstrip = x.lstrip("he")
print(xlstrip) 
# / hello world!
# / llo world!


# 29 - .maketrans() metodu bir karakter dizisindeki karakterlerin farklı bir karakter dizisindeki karakterlerle eşleştirilmesi için bir sözlük oluşturur. Oluşturulan bu sözlük daha sonra translate() metoduyla kullanılabilir.

print("hello wolrd!".maketrans())


# 30 - .partition() metodu Karakter dizisini belirtilen ayırıcıya göre 3 parçaya böler ve bir tuple döndürür.

print("hello world!".partition("o"))
print(type("hello world!".partition("o")))
# / ('hell', 'o', ' world!')
# / <class 'tuple'>


# 31 - .removeprefix() metodu bir karakter dizisinin başlangıcında belirtilen önek dizesini kaldırır ve sonuçta kalan karakter dizisini döndürür. bu metodu yerine, lstrip() veya replace() metotları kullanılarak da aynı işlem yapılabilir.
x = "hello world!"
print(x)
xremoveprefix = x.removeprefix("hello ")
print(xremoveprefix) 
# / hello world!
# / world!


# 32 - .removesuffix() metodu bir karakter dizisinin sonundaki belirtilen sonek dizesini kaldırır ve sonuçta kalan karakter dizisini döndürür. bu  metodu yerine, rstrip() veya replace() metotları kullanılarak da aynı işlem yapılabilir.

x = "hello world!"
print(x)
xremovesuffix = x.removesuffix("world!")
print(xremovesuffix) 
# / hello world!
# / hello


# 33 - replace() metodu bir karakter dizisi içindeki belirli bir alt dizesi başka bir alt dizeyle değiştirir ve sonuçta kalan yeni karakter dizisini döndürür.

x = "hello world!"
print(x)
xreplace = x.replace("hello","hi")
print(xreplace) 
# / hello world!
# / hi world!


# 34 - .rfind() metodu bir karakter dizisi içinde belirli bir alt dizinin sağdan başlayarak (son karakterden başlayarak) ilk konumunu bulur ve bu konumu döndürür. Eğer alt dize bulunamazsa -1 değerini döndürür.
print("hello wolrd!".rfind("o"))
# / 7 (sondan arar ama index baştan başlar)

# 35 - .rindex() metodu bir karakter dizisi içinde belirli bir alt dizinin sağdan başlayarak (son karakterden başlayarak) ilk konumunu bulur ve bu konumu döndürür. Eğer alt dize bulunamazsa ValueError hatası verir.
# eğer alt dize bulunamazsa ValueError hatası verdiği için, aranan alt dizenin varlığını kontrol etmek için önce in anahtar kelimesi kullanmanız önerilir.
print("hello wolrd!".rindex("l"))
#/ 8 (sondan arar ama index baştan başlar)

# 36 - .rjust() metodu belirtilen genişlikte bir karakter dizisi oluşturur ve orijinal karakter dizisini sağa hizalar. Oluşturulan yeni karakter dizisi, belirtilen genişlikten daha uzunsa, eksik kısmı belirtilen bir dolgu karakteri ile doldurur.
# string.rjust(width, fillchar)
# Burada width, oluşturulan karakter dizisinin minimum genişliğini belirtir. fillchar ise, karakter dizisinin genişliğinden fazla olan kısmın nasıl doldurulacağını belirtir. Varsayılan olarak, fillchar boşluk karakteridir.

string = "Python"
new_string = string.rjust(10, "-")
print(new_string)
# / ----Python


# 37 - .rpartition() metodu bir stringi belirli bir ayırıcıya göre 3 parçaya ayırmak için kullanılır. Ayırıcı string'in sağ tarafında aranır ve ilk bulduğu ayırıcıdan itibaren string'i üç parçaya ayırır.
# Bu metot, partition() metoduna benzer, ancak aramanın string'in sağ tarafında başlar ve string'i sağdan sola tarar.

print("hello wolrd! python".rpartition(" "))
# / ('hello wolrd!', ' ', 'python')


# 38 - .rsplit() metodu  bir stringi belirtilen bir ayırıcıya göre sağdan parçalara ayırmak için kullanılır.Metod, parametre olarak ayırıcıyı (delimiter) ve opsiyonel olarak kaç parçaya ayırmak istendiğini alır. Varsayılan olarak, metod ayırıcı olarak boşlukları kullanır ve tüm parçalara ayırır.
print("hello wolrd!".rsplit())
# / ['hello', 'wolrd!']


# 39 - rstip() metodu bir string'in sağ tarafındaki belirli karakterleri kaldırmak için kullanılır. Varsayılan olarak, bu metot string'in sağ tarafındaki boşlukları kaldırır, ancak belirli bir karakter kümesi vererek bu karakterleri de kaldırabilirsiniz.

print("hello wolrd!".rstrip("d!"))
# / hello wolr


# 40 - .split() metodu bir karakter dizisini belirtilen bir ayraç karakterine göre böler ve böylece karakter dizisini bir liste halinde döndürür. Bu metot, bir karakter dizisi içindeki belirli bir deseni veya karakter dizisini ayırmak için de kullanılabilir.
# string.split(separator, maxsplit)
# Burada separator parametresi, karakter dizisini ayırmak için kullanılacak olan ayraç karakteridir. Varsayılan olarak, bu parametre boşluk karakteridir.
# maxsplit parametresi ise isteğe bağlıdır ve en fazla kaç kez ayırmak istediğinizi belirler. Varsayılan olarak, bu parametre None olarak atanır ve tüm ayrılmalar yapılır.

string = "Python Java JavaScript"
result = string.split()
print(result)  
# / ['Python', 'Java', 'JavaScript']

string = "Python,Java,JavaScript"
result = string.split(",", 1)
print(result) 
# / ['Python', 'Java,JavaScript']


# 41 - .splitlines() metodu bir karakter dizisini satırlara ayırmak için kullanılır. Bu metot, bir karakter dizisindeki satırları bulmak için belirli bir ayraç karakteri veya karakter dizisini kullanır.
# Burada keepends parametresi isteğe bağlıdır. Eğer bu parametre True olarak belirtilirse, ayracın kendisi de her bir satırın sonuna eklenir. Varsayılan olarak, keepends parametresi False olarak atanır ve ayraç karakterleri çıkarılır.

string = "Python\nJava\nJavaScript"
result = string.splitlines()
print(result)  # (Bu örnekte, splitlines() metodu "\n" karakterinin varlığına bakarak karakter dizisini üç ayrı satıra ayırır ve sonuç olarak bir liste döndürür.)
# / ['Python', 'Java', 'JavaScript']

string = "Python\nJava\nJavaScript"
result = string.splitlines(True)
print(result)  # (Bu örnekte ise, keepends parametresi True olarak ayarlanır ve sonuçta her bir satırın sonuna "\n" karakteri eklenir.)
# ['Python\n', 'Java\n', 'JavaScript']  


# 42 - .startswith() metodu bir karakter dizisinin belirtilen bir önek ile başlayıp başlamadığını kontrol eder. Metot, karakter dizisi önekinin bir parçasıysa True değerini döndürür; aksi takdirde False değerini döndürür.

print("Hello World".startswith("H"))
# / True


# 43 - .strip() metodu bir karakter dizisinin başındaki ve sonundaki boşlukları (veya başka belirtilen karakterleri) kaldırmak için kullanılır. Bu metot, orijinal karakter dizisini değiştirmez, bunun yerine boşlukları (veya belirtilen karakterleri) kaldırılmış yeni bir karakter dizisi döndürür.

x = "!!hello world!!"
xs =x.strip("!")
print(x)
print(xs)
# / !!hello world!!
# / hello world


# 44 - .swapcase() metodu Karakter dizisindeki tüm harflerin büyük ve küçük harflerini tersine çevirir.

print("hello WORLD!".swapcase())
# / HELLO world!


# 45 - .title() metodu Karakter dizisindeki tüm kelime başlıklarını büyük harfe dönüştürür.

print("hello world!".title())
# Hello World!


# 46 - .translate() metodu bir karakter dizisindeki karakterleri belirli bir karakter setiyle değiştirmek için kullanılır. Bu metot, str.maketrans() metoduyla oluşturulan bir karakter dönüştürme tablosunu kullanır.
# orijinal karakter dizisini değiştirmez, bunun yerine değiştirilmiş karakterlerden oluşan yeni bir karakter dizisi döndürür.

kelime = "hello world!"
cevirme_tablosu = str.maketrans("ro", "sk")
yeni_kelime = kelime.translate(cevirme_tablosu)
print(kelime)
print(yeni_kelime)
# / hello world!
# / hellk wksld! ( r harfi s ile o harfi k ile değiştirildi)


# 47 - .upper() metodu bir karakter dizisindeki tüm harfleri büyük harfe dönüştürür. Bu metot, orijinal karakter dizisini değiştirmez, bunun yerine büyük harflerden oluşan yeni bir karakter dizisi döndürür.

x = "hello world"
xl = x.upper()
print(x)
print(xl)
# / hello world!
# / HELLO WORLD!


# 48 - .zfill() metodu bir karakter dizisini belirtilen genişliğe kadar sıfırlarla doldurur. 

print("123".zfill(6))
# / 000123 
