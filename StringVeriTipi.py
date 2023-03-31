name = "HELLO WORLD!"

print("HELLO"+"\n"+"WORLD")
#print HELLO
#      WORLD  ( \n ifadesi bir alt satıra geç demektir. \t ifadesi ise bir tab mesafesi ötele demektir.)


print(name.capitalize())
#print = Hello world! (Sadece kelimenin ilk harfi büyük olur)

print(name.casefold())
#print = hello world! ( bütün harfler küçük olur)


print(name.center(20,"-"))
#print = ----HELLO WORLD!---- ( string ifadeyi 20 karaktere tamamlayıp ifadeyi ortalar )


print(name.count("L"))
#print = 3 ( string ifade içerisinde kaç tane L harfi olduğunu sayar.)

print(name.encode)

print(name.endswith("!"))
#print = true (ifadenin parantez içinde belirtilen ile bitip bitmediğini kontrol eder. sonuç true / false)

print(name.expandtabs())


print(name.find("O"))
#print=4 ( parantez içerisindeki ifadeyi arar ve ilk bulduğu indexi döner. (1.index 0))


print("HELLO {} !".format("WORLD"))
#print= HELLO WORLD (süslü parantez içini format ile de doldurabiliyoruz.)

print(name.format_map)

print(name.index("!"))
#print = 11 ( parantez içindeki ifadenin hangi indexte olduğunu döner , birden fazla varsa sadece ilkini yakalar)

print(name.isalnum())
#print = false (ifade tek kelimelik ise ve rakam içeriyorsa true döner , aksi halde false döner)

print(name.isalpha())
#print = false ( ifade tek kelimelik ise ve harf içeriyorsa true döner , aksi halde false döner)

print(name.isascii)
print(name.isdecimal())
#print = false ( ifade decimal ise ture döner , aksi halde false döner)

print(name.isdigit)
print(name.isidentifier)
print(name.islower())
#print= False ( ifadenin bütün harflerinin küçük olup olmadığını kontrol eder. True / False olarak döner)

print(name.isnumeric)
print(name.isprintable)
print(name.isspace)
print(name.istitle)

print(name.isupper())
#print = True ( ifadenin bütün harflerinin büyük olup olmadığını kontrol eder. True / False olarak döner)

print(name.join)
print(name.ljust)

print(name.lower())
#print = hello world! ( ifadenin bütün değerlerinin küçük harfli olmasını sağlar)

print(name.lstrip)
print(name.maketrans)
print(name.partition)
print(name.removeprefix)
print(name.removesuffix)
print(name.replace)
print(name.rfind)
print(name.rindex)
print(name.rjust)
print(name.rpartition)
print(name.rsplit)
print(name.rstrip)

print(name.split())
#print = ['HELLO', 'WORLD!'] ( parantez içindeki ifadeden split etmeye yarar. parantez içinde hangi ifade varsa ordan split eder )

print(name.splitlines)

startswith="Hello World"
print(startswith.startswith("H"))
#pint = True (değişkenin parantez içindeki ifade ile başlayıp başlamadığını kontol eder. True / False olarak döner.)

print(name.strip)

swapcase = "MY NAME is sedat mengü"
print(swapcase.swapcase())
#print = my name IS SEDAT MENGÜ (Küçükleri büyük harf , büyükleri küçük harf yapar.)

title = "My name is Sedat MENGÜ"
print(title.title())
#print = My Name Is Sedat Mengü (her kelimenin ilk karakterini büyük yapar.)

print(name.translate)

print(name.upper())
#print = HELLO WORLD! ( ifadenin bütün harflerinin büyük olmasını sağlar)

price = "125"
print(price.zfill(6))

#print = 000125 ( parantez içindeki karakter sayısına tamamlayıp baş tarafına ihtiyaç kadar 0 ekler)








