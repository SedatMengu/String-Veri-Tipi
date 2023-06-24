# sözlüklerdeki key ler string veya integer olmak zorundadır.
# sözlüklerdeki value ler herhangi bir veri tipinde olabilirler.
# sözlüklerde index olmaz, yerine keys vardır.

kisi = { "isim" : "Ali",
        "soyisim" : "Şeker",
        "yaş" : 22,
        "hobiler" : ["Müzik Dinlemek" , "Resim Yapmak" , "Kitap Okumak"]
}

# dictionary de yazdırma işlemleri.
# index yerine keys ler kullanılır.
print(kisi)                         # / {'isim': 'Ali', 'soyisim': 'Şeker', 'yaş': 22, 'hobiler': ['Müzik Dinlemek', 'Resim Yapmak', 'Kitap Okumak']}
print(kisi["isim"])                 # / Ali
print(kisi["soyisim"])              # / Şeker
print(kisi["yaş"])                  # / 22
print(kisi["hobiler"])              # / ['Müzik Dinlemek', 'Resim Yapmak', 'Kitap Okumak']

# keys değiştirme

kisi ["isim"] = "Ahmet"
kisi ["soyisim"] = "Kara"
kisi ["yaş"] = 32
kisi ["hobiler"] = ["Golf Oynamak" , "Yüzmek" ,"Tenis Oynamak"]

print(kisi)                         # / {'isim': 'Ahmet', 'soyisim': 'Kara', 'yaş': 32, 'hobiler': ['Golf Oynamak', 'Yüzmek', 'Tenis Oynamak']}
print(kisi["isim"])                 # / Ahmet
print(kisi["soyisim"])              # / Kara
print(kisi["yaş"])                  # / 32
print(kisi["hobiler"])              # / ['Golf Oynamak', 'Yüzmek', 'Tenis Oynamak']

# aynı anda birden fazla value değiştirmek:

kisi.update({"isim" : "Tarkan" , "Soyisim" : "Beyaz"})
print(kisi["isim"])                 # / Tarkan
print(kisi["soyisim"])              # / Beyaz


# key eklemek:

kisi ["id"] = 12345
print(kisi)                         # / {'isim': 'Tarkan', 'soyisim': 'Kara', 'yaş': 32, 'hobiler': ['Golf Oynamak', 'Yüzmek', 'Tenis Oynamak'], 'Soyisim': 'Beyaz', 'id': 12345}

# key silme : 

del(kisi["isim"])
print(kisi)                         # / {'soyisim': 'Kara', 'yaş': 32, 'hobiler': ['Golf Oynamak', 'Yüzmek', 'Tenis Oynamak'], 'Soyisim': 'Beyaz', 'id': 12345}


# olmayan bir key arattırıyorsak ve hata almak istemiyorsak : 

print(kisi.get("ikametgah" , "None"))      # / None

# get içerisinde 2.parametre ekrana bastırılan hata mesajıdır.

# dictionary veri tipine ait metotlar


# 1  - .clear () metodu bir sözlüğün içindeki tüm öğeleri siler ve boş bir sözlük oluşturur.
sozluk = {"ad": "Ahmet", "soyad": "Yılmaz", "yas": 25}
sozluk.clear()
print(sozluk)   # {}


# 2  - .copy() metodu  sözlüğün bir kopyasını oluşturur. Kopya, orijinal sözlüğü aynen yansıtır ve bellekte ayrı bir nesne olarak saklanır. Bu nedenle, orijinal sözlük değiştirilse bile, kopya bu değişikliklerden etkilenmez.
original = {1: 'bir', 2: 'iki', 3: 'üç'}
copy = original.copy()

original[1] = 'one'
print(original)  # {1: 'one', 2: 'iki', 3: 'üç'}
print(copy)      # {1: 'bir', 2: 'iki', 3: 'üç'}

# 3  - .fromkeys() metodu belirtilen anahtarlarla ve isteğe bağlı bir varsayılan değerle birlikte yeni bir sözlük oluşturur.
keys = ['a', 'b', 'c']
value = 0
my_dict = dict.fromkeys(keys, value)
print(my_dict) # {'a': 0, 'b': 0, 'c': 0}

# 4  - .get() metodu bir sözlükte belirtilen anahtar için değer döndürür. Eğer anahtar sözlükte yoksa, varsayılan bir değer döndürür.
sozluk = {"a": 1, "b": 2, "c": 3}
print(sozluk.get("a")) # 1
print(sozluk.get("d", 0)) # 0
print(sozluk.get("d")) # None

# 5  - .items() metodu bir sözlükteki tüm anahtar-değer çiftlerini içeren bir görünüm döndürür.
sozluk = {"isim": "Ali", "soyisim": "Kara", "yas": 30}
anahtarlar_ve_degerler = sozluk.items()
print(type(anahtarlar_ve_degerler))
print(anahtarlar_ve_degerler)
# <class 'dict_items'>
# dict_items([('isim', 'Ali'), ('soyisim', 'Kara'), ('yas', 30)])

# 6  - .keys() metodu sözlükteki tüm anahtarları (keys) içeren bir görünüm (view) döndürür. Sözlüğe yeni bir anahtar eklendiğinde veya mevcut bir anahtarın değeri değiştirildiğinde, keys() yöntemi tarafından döndürülen görünüm otomatik olarak güncellenir.
my_dict = {"a": 1, "b": 2, "c": 3}
keys = my_dict.keys()
print(keys)
# / dict_keys(['a', 'b', 'c'])


# 7  - .pop() metodu belirtilen anahtarın değerini sözlükten kaldırır ve değeri döndürür. Eğer anahtar sözlükte bulunamazsa, belirtilen varsayılan değeri döndürür. Eğer varsayılan değer belirtilmezse, KeyError yükseltir.
sozluk = {'a': 1, 'b': 2, 'c': 3}

# pop() yöntemi ile 'a' anahtarının değerini sözlükten kaldıralım ve değerini döndürelim
a_degeri = sozluk.pop('a')
print(a_degeri)  # çıktı: 1
print(sozluk)  # çıktı: {'b': 2, 'c': 3}

# pop() yöntemi ile 'd' anahtarının değerini sözlükten kaldıralım ve değerini döndürelim
# ancak 'd' anahtarı sözlükte bulunmadığı için KeyError oluşacaktır
# d_degeri = sozluk.pop('d')  # bu satır hata verecektir
# print(d_degeri)
# KeyError: 'd'

# pop() yöntemi ile 'd' anahtarının değerini sözlükten kaldıralım ve değerini döndürelim
# ama eğer 'd' anahtarı sözlükte bulunmazsa, 0 değerini döndürelim
d_degeri = sozluk.pop('d', 0)
print(d_degeri)  # çıktı: 0
print(sozluk)  # çıktı: {'b': 2, 'c': 3}
# Burada, pop() yöntemi sozluk sözlüğünden a anahtarının değerini kaldırdı ve değerini a_degeri değişkenine atadı. Daha sonra d anahtarının sözlükte bulunmadığını kontrol etmek için pop() yöntemi çağrıldı. Ancak bu kez varsayılan bir değer belirtildi, böylece KeyError yerine 0 değeri döndürüldü.


# 8  - .popitem() metodu sözlükteki son çifti kaldırır ve bunu bir demet olarak döndürür. Ancak, sözlük boşsa, bu durumda KeyError hatası verir.
# Örnek kullanım
sozluk = {1: 'bir', 2: 'iki', 3: 'üç'}
son_cift = sozluk.popitem()
print(son_cift)  # (3, 'üç')
print(sozluk)    # {1: 'bir', 2: 'iki'}

# 9  - .setdefault() metodu  bir sözlükte belirtilen anahtarın değerini döndürür. Anahtar sözlükte yoksa, sözlükte belirtilen anahtarın değeri verilen varsayılan değere ayarlanır ve bu varsayılan değer döndürülür. Eğer varsayılan değer belirtilmezse, varsayılan değer None olarak ayarlanır.
sozluk = {"elma": 3, "armut": 5, "kiraz": 10}
deger = sozluk.setdefault("elma", 0)  # sozlukteki "elma" anahtarı için değer 3 olacaktır
print(deger)  # 3

deger = sozluk.setdefault("portakal", 0)  # sozlukte "portakal" anahtarı yok, bu yüzden değer 0 olur ve "portakal" anahtarı sözlüğe eklenir
print(deger)  # 0

print(sozluk)  # {"elma": 3, "armut": 5, "kiraz": 10, "portakal": 0}

# 10 - .update() metodu bir sözlüğü başka bir sözlükle güncellemek için kullanılır. Bu yöntem, anahtarlar sözlükte mevcut ise, onların değerlerini günceller ve yeni anahtarlar ekler. Eğer aynı anahtar her iki sözlükte de varsa, update() metodu, yeni sözlüğün değeri ile günceller.
sozluk1 = {"ad": "Ali", "yas": 23}
sozluk2 = {"ad": "Ahmet", "meslek": "öğrenci"}

sozluk1.update(sozluk2)
print(sozluk1)  # {"ad": "Ahmet", "yas": 23, "meslek": "öğrenci"}

# 11 - .values() metodu bir sözlükteki tüm değerleri içeren bir görünüm döndürür. Bu görünüm, orijinal sözlükteki değerlerin bir kopyasını içerir ve bu değerlerde yapılan değişiklikler orijinal sözlükte etkili olmaz.
my_dict = {"a": 1, "b": 2, "c": 3}
values = my_dict.values()

print(values)  # dict_values([1, 2, 3])
print(type(values))  # <class 'dict_values'>

# values üzerinde yapılan değişiklikler, orijinal sözlüğü etkilemez
values_list = list(values)
values_list.append(4)

print(values_list)  # [1, 2, 3, 4]
print(my_dict)  # {"a": 1, "b": 2, "c": 3}


# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------# 

