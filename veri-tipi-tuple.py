demet = (1,2,3,4,5,6) # demet adlı bir değişken oluşturup tuple değerler veriyoruz.
print(demet) # terminalde demet adlı değişkeni yazdırıyoruz.
#print =  (1,2,3,4,5,6)
print(type(demet)) # terminalde demet değişkenini türünü yazdırıyoruz.
#print = <class 'tuple'>


#tuple ların en büyük özellikleri değiştirilemez olmalarıdır. Mesela aşağıdaki gibi bir işlem yapamayız

demet[0] = 5 # demetin 0'ncı objesini 5'e eşitliyoruz.

#print =  TypeError: 'tuple' object does not support item assignment

## tuple da işlem yapabilmemiz için yeni bir listeye tanımlama yapmamız lazım.

yenidemet = demet[0] # yenidemet değişkenini demetin 0'ncı objesine eşitliyoruz.
print(yenidemet) # yenidemet değişkenini terminale yazdırıyoruz.
#print = 1
yenidemet = demet[:5] # yenidemet değişkenini demetin 5'nci objesine kadar eşitliyoruz.
print(yenidemet) # yenidemet değişkenini terminale yazdırıyoruz.
# print = (1,2,3,4,5)

# string bir ifadeyi tuple yapabliriz. 

yazi = "Hello World!" # yazi adlı değişken oluşturuyoruz.
demet = tuple(yazi) # demet adlı değişken oluşturup tuple olarak yazi değişkenini yazpıyoruz.
print(demet) # demet değişkenini terminale yazıyoruz.

#print = ('H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd', '!')

#Demet Objesinden Değerin Kaçıncı İndekste Olduğunu Bulmak:
demet = (12,43,54,31,69,"Enes",35,42) # demet adlı demet değişkeni oluşturuyoruz.
print(demet.index(54)) # demetin 54'ncü objesini kaçıncı indekste olduğunu terminale yazdırıyoruz.
#print = 2


print(demet.index("Enes")) # demetin 54'ncü objesini kaçıncı indekste olduğunu terminale yazdırıyoruz.
#print = 5


# Demet Objesinde Kaç tane Aynı Objede Olduğunu Bulmak:
demet = (1,2,2,2,2,2,3,4,5,4,3,3,3,4,5,6) # demet adlı değişken oluşturuyoruz.
print(demet.count(2)) # demet değişkenin içinde kaç tane 2 olduğunu terminale yazdırıyoruz.
#print = 2 (5 ifadesinden 2 tane varmış. )