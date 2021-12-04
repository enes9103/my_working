given_number = input("Bir sayi giriniz : ")
if given_number.isdigit() and int(given_number) > 0:
    
    number_length = len(given_number)
    toplam = 0
    for i in given_number:
        toplam += int(i) ** number_length
    
    if toplam == int(given_number):
        print("Armstrong Number")
    else:
        print("Not an armstrong number")

else:
    print("Please enter a valid number.")



##############  while and for loops 

# looplar vasitasi ile biz bir kodumuzu yada elimizde bulunan birseyi tekrar ettiririz


# while loop ile for loop birbirine benzer seylerdir ancak calisma prensipler farklidir

# for loop iterable lar üzerinden gider. Bir iterable verinin elemanlari sayisinca iterate eder
# iterable in elemanlari bitince for döngüsünün calismasi da durur

# while loop ise condition lar üzerinden gider. Bizim kosulumuz saglandigi sürece while loop 
# calisir kosulumuz False a döndügünde while loop calismayi durdurur

## while loop temel yapisi:

while condition: (: colon önemli)
  body   ## 4 space indentation 

# while looplar, condition kismina boolean degerler yada Truthy Falsy degerler alirlar
# peki biz condition kismina neler yazabiliriz?

# while 3 > 2:   ##  Biz durdurmadigimiz sürece sonsuz döngü

while True:

while None:

while False:

while {}:

while bool(1,2,3,4) + bool("A", "b", "c"):
  

while "ahmet":
  print("ahmet")
  break 

while "ali" and None or 2021:

# mesela cay kahve makinesi:

while para < 1:
  print("Lütfen para ilave ediniz")


bool(1) + bool("")




# condition = 6.8  ##  Attention: Burada 6.5 degilde mesela 6.8 yazarsak
#                     # sürekli 0.5 azalacagindan sonuc 0 a hic düsmez ve sonsuz döngü olur
# while condition:
#   condition -= 0.5
#   print(condition)

# ayni kosulu su sekilde de calistirabilirdik

condition = 5   

while condition > 0:
  condition -= 1
  print(condition)


# Attention: Bizim while döngümüz, kodumuzun herhangi bir bölümünde False a dönmesi 
# gerekir. Aksi takdirde kodumuz sonsuz döngüye girecektir.

# yani bu demek olur ki while döngülerinde, elimizdeki veriyi yani rakamlari harfleri
# bir sekilde degistirmemiz lazim. Eger elimizdeki veri hep sabit, yada hep True sonuc verirse
# bu durumda sonsuz döngü ile sonuclanir

# a += 1  yada a -= 1 gibi degiskenler kullanarak her iteration da 
# verimizin degistirilebilir

# eger kodumuzdan cok emin degil isek o zaman break kelimesini kullanabiliriz

condition = 5

while True:     ## mesela burada, condition kismi True, o nedenle condition = 5 gözardi edilir                 
  condition -= 1        # ve burada if yapisi olmasa bu hic degismeyecektir
  print(condition)
  if condition == 0:
    break







# Not: Eger ic ice yani nested while loop lar ile calisiyorsak

# ve en icteki loop umuzda break kullaniyorsak o zaman, en icteki looptan

# cikar bir üst while loop ise calismaya devam eder

condition = 20

while condition > 0: 
  print(condition)
  condition -= 1              ## 1 kez burada calisir

  while 19 >= condition >= 13:    # 7 kez burada calisti      
    print("condition >= 13")
    condition -= 1      

    while 13 > condition > 7:    ## Burada sayi 8 den büyük oldugu sürece calisacak
      print("condition >= 8")    ##    7 e esit olunca icteki while dan cikacak ve distaki loop 
      condition -= 1             # # calismaya devam edecek
      if condition == 7:
        break

# peki print() func iki kez yazarsak nasil bir output aliriz ??

condition = 5

while condition > 0:
  condition -= 1
  print(condition)

  
print(condition)
  

# print func while loop disinda yazilirsa output ne olur ??

condition = 5

while condition > 0:
  condition -= 1
print(condition)
  

## print while döngüsü üzerine yazilirsa ne sonuc aliriz ??

condition = 5
print(condition)

while condition > 0:
  condition -= 1
  

## condition while loop altinda yazilirsa:

y = 5
while y > 0:
  
  y -= 1
  print(y)





# buradaki while loop'un calisma prensibini manuel olarak kendimiz yapalim:
condition = 5

while condition > 0:
  print(condition)
  condition -= 1
  
  
# condition = 4
# print(condition)   ## bu artik yeni degisken olarak düsünelim. yeni degiskenimiz artik 4 print(condition)

# condition = 3           ## yeni degisken burada 3 oldu
# print(condition)

# condition = 2        
# print(condition)      
                      
# condition = 1
# print(condition)

# condition = 0
# print(condition)   # ama dikkat 0 basildi. cünkü bu islem yapilirken degiskenimiz 1 yani truthy

## while calisma prensip:

while loops  ==>> condition ==>> False ise döngüden cikar bir sonraki condition a gider
                                ==>> True ise loop u calistirir

number = 0

while number < 6:  ## numara 6 dan kücük oldugu sürece bu kod calissin
  print(number)    ## bu örnekte number += 1 print' in altinda.alt hücrede ise farkli
  number += 1    ## bu satira gelince artik yani number degiskeni 0 degil  1 olur
                  ## ve tekrar kontrol eder. 1 < 6 midir. evet kücüktür ve tekrar calisir
                  # bu siralama ta ki 6 < 6 yi görene kadar devam eder. 
                  # ve döngümüz bittikten sonra kod blokumuz devam ediyor. 
                  # cünkü print while disinda

#print("simdi sayi 6 ya esit veya daha büyük")

number = 0

while number < 6: 
  number += 1
  print(number)    

## Dikkat edersek burada print etmeden önce number degiskenine 1 ekliyoruz.
# python yukaridan asagi calistigi icin üstteki hücrede 0 dan baslamistik
# simdi ise 1 den basladik.

# Burada önemli husus sudur. Döngümüzün kac iteration yaptigi ?
# kactan baslarsak baslayalim loop umuz 6 iteration yapar

# while döngüleri condition lar ile calisir demistik ama
# bu condition'i, for döngüsünde kullandigimiz  bir iterable
# vasitasi ile de saglayabiliriz 

liste = ["a", "b", "c", "d", "e"]
a = 0

while a < len(liste):
  a += 1
  print("{}'in karesi = {}" .format(a, a ** 2))

yas = input("yasinizi giriniz: ")
yas.isnumeric()

while not yas.isnumeric():            ## isdigit 
  print("Yanlis formatta girdiniz")
  yas = input("Lütfen yasinizi dogru formatta giriniz: ")

print("Tesekkür ederiz. Yasiniz: ", yas)

# Not: Neden print() func'i while döngüsü disina yazdik?
# Cünkü, eger kullanici yasini dogru formatta girerse kodumuz hic while döngüsü 
# icerisine girmeden dogrudan print satirina atlayacaktir.

# Eger biz print func'i while döngüsü icinde yazarsak o zaman
# kullanici ilk girme hakkinda dogru format girdiginde kodumuz while döngüsü
# icine girmez ama while döngüsü disinda da bir islem olmadigindan
# biz bu durumda hicbir cikti alamayiz.

a = "A"
print(a.islower())

# Not: yukaridaki kod da isdigit() zaten kendisi True ve False gibi boolean 
# degerler döndürdügü icin o nedenle tekrar bir daha == True yada
# == False demeye ihtiyac duymuyoruz

## isdigit() calisma prensibi

# isdigit() gibi methodlar string methodlaridir. Bu nedenle integer yada
# diger veri tipleri ile kullanamayiz

a = "55".isdigit()
print(a)

b = "55.0".isdigit()
print(b)

c = "abc".isdigit()
print(c)

d = "-55".isdigit()
print(d)

## Dersteki Kahoot sorulari:

# if elif ve else ler condition olarak bilinir


condition = (3 > 1) and (1 < 1)

if not condition:   # Dikkat: not var
  print("it works")   
                      
else:
  print("something is wrong")

price = "2200"

if price <= "2100":
  print("ucuz")

else:
  print("pahali")

price = "2200"          ### Burada dikkat etmemiz gereken 2 husus vardir
                        ## birincisi <= dedigimizde icerisinde = oldugu icin 
if price <= "2200":     #  ayni zamanda hem kücük hem de esittir demektir.
  print("ucuz")         # ikincisi ise string icerisinde bulunan 2 tane sayiyi
                        # kücük ve büyük olarak kiyas edebilirz
else:                   #  yani bizim kodumuzda <= degil de sadece < olsa bile
  print("pahali")       ## kodumuz calisirdi    

                       





 ## Dikkat: string veri tipi icerisindeki sayi ve harfleri birbirleri ile
# karsilastirabiliriz. Yani price = "abcd" desek de kodumuz calisir 

# burada ise ascii kodlar devreye girer

print("a" < "aa")

print("a" < "A")

print("a" < "a1")

print("a" < "+")


print("a" == "a")

# aklindan bir sayi tut oyunu:
# Not bu sorunun kolay cözümü bu sekildedir. Yani True kullanacagiz ve bir kosul saglandiginda
# break kullanacagiz ve break bizi döngüden cikaracak 

print("Hadi sayi oyunu oynayalim")
sayi = 55

while True:        
  girdi = int(input("Bil bakalim aklimdan gecen sayiyi: "))

  if girdi > sayi:                ## neden girdi degiskenini while loop icerisine yazdik
    print("Biraz azalt: ")        # cünkü dogru cevap bilinmedigi sürece, her defasinda 
  elif girdi < sayi:              # kullanicidan yeni sayi isteyecegiz. Ve dikkat:
    print("biraz artir: ")        ##  while altinda girdi istedigimizden bir daha if ler 
  else:                           # altinda girdi istemiyoruz
    print("Tebrikler bildin")
    break




# bu sekilde 3 while ile de calistirilabilir

girdi = int(input("Bir sayi söyle!!!: "))
sayi = 55

while girdi < sayi:                 ### Dikkat buralarda break kullanmadik ve buna
  print( "Biraz artir!!!")          # ragmen sonsuz döngü olusmuyor !!!
  girdi = int(input("yeni sayi: ")) #  neden ??

while girdi > sayi:
  print("Biraz azalt!!!")
  girdi = int(input("Yeni sayi: "))

while girdi == sayi:
  print("Tebrikler bildin")
  break

# not: Bu tarz kodlari while ve for kullanmadan sadece if ve else ler ile
# yazamayiz. cünkü kullanicinin kac sefer de bilecegini bilemeyiz ve
# sadece if ler ile bir döngü olusturamayiz 

# kullanicinin girdigi cümlede en uzun kelimenin uzunlugunu bulma

girdi = input("Lütfen bir cümle giriniz(kelime aralarinda bosluk birakiniz): ")
new = girdi.split()
counter = 0
longest = 0

while counter < len(new):
  a = new[counter]
  counter += 1

  if len(a) > longest:
    longest = len(a)
                         ### else' i kullanmasak da kodumuz calisir

print(longest)

## hocanin cözümü:

sentence = input("Lütfen bir cümle giriniz: ")

word_list = sentence.split()

i = 0
longest = 0

while i < len(word_list):

  if len(word_list[i]) > longest:   # sadece if kullandik else e gerek kalmadi

    longest = len(word_list[i])    ### eger yeni kelime uzunlugu longest tan uzun degilse
                                    ## bu durumda longest in eski halinde bir degisiklik olmaz
  i += 1                            #  ve bu durumda sadece alt satirdaki i bir tane artar.

print(longest)         ###  Dikkat eger i counter'i if altinda yazarsak calismaz



####### 13. Session

#### Not:  if yapilarinda indentation lar cok önemli oldugu gibi 
# while ve for loop larda da cok önemlidir.


while condition:
  body
  while condition:
    body
    break

# Buradaki break kelimesi sadece ic kisimdaki while icindir
## eger disaridaki döngüyü de cikarmak istersek onun hizasinda ayrica break yazmamiz gerekir

#### attention:

# while döngüsü kurarken condition olusturma asamasinda dikkat
# edilmesi gereken bir husus:

liste = [10, 11, 12, 13, 14]
bos = []
counter = 0

while counter <= len(liste):
                  ## burada <= kullanirsak toplam iterate sayisi ne olur?
  bos.append(counter)          # sadece < kullanirsak ne olur?
  counter += 1
print(bos)



################       for loop        ###############



# for döngülerinde ana yapimiz:

for variable in iterable:
  body

# while yapisina benzerlikler:
# for satiri sonunda colon yani : kullanimi
# body ye baslamadan önce 1 tab indentation


# while dan farkli olan hususlar:

# iterable lar ile döngü olusturur yani bir iterable verinin elemanlari
# üzerinde gezinir
# condition ile calismaz
# while dan farkli olarak "i" gibi bir degisken alir
# for döngüsünde list comprehension mümkün, while da yok

# Soru? for döngüsünde de while döngüsünde oldugu gibi sonsuz döngü var midir?

# for döngüsü calisma prensibini bu örnekte hem manuel olarak uygulayarak
# hem de for döngüsü calistirarak görelim:

# döngülerde kullanilan "i" harfini genelgecer bir kural olarak görebiliriz.
# uluslararasi olarak bu sekilde alisilmis ve iteration kelimesinden gelmektedir

# for döngüsü her iteration da, i degiskenine atama assigning yapar.
# yani her iteration da i'nin degerinde bir güncelleme gerceklesir.

liste = [1, 2, 3, 4, 5]
i = 3
for i in liste:
  print(i)

print(i)



# a = 1
# a = 2
# a = 3
# a = 4

# i = 0
# i = liste[0]
# print(i)


# i = 1
# i = liste[1]
# print(i)


# i = 2
# i = liste[2]
# print(i)


# i = 3
# i = liste[3]
# print(i)


# i = 4
# i = liste[4]
# print(i)

# print(i)

liste = [1, 2, 3, 4, 5]
i = 1000
for i in liste[2:]:
  print(i)

print(i)





## for döngüsünün body kisminda variable'i yani i degiskenini kullanmak 
# zorunda degiliz. Bunun yerine herhangi bir sey konulabilir.

liste = [1, 2, 3, 4, 5]

for i in range(0, 5):  ## bunun yerine range(0, 5) de kullanabiliriz
  print("mehmet")

# for döngüsünden ciktiktan sonra i'nin degerini kullanmaya ihtiyac duyarsak:
# Bu durumda ne output aliriz ??

for i in range(0,8):
  print(i)   
              
print(i)



##  hatirlatma:
# range func icerisindeki degerleri ortaya cikarmanin birkac yolu vardir
# 1:  for döngüsü icinde kullanma
# 2:  list, tuple ve set gibi func'lar icerisinde kullanma
# 3:  range func önünde yildiz kullanma(asteriks)


print(*range(0,10))

print(list(range(0,10)))
print(tuple(range(0,10)))
print(set(range(10)))
# print(dict(range(0,10) : range(10)))  # dict ile e calisir mi?

for i in range(0,10):
  print(i)

##  Peki: * ile tüm elemanlari ayirip daha sonra bir yerde 
# kullanma sansimiz var midir ? Yani listelerdeki gibi indexleme 
# slayslama yapilabilir mi??

print(*range(0,10))

tuplem = (1, "cilek", 2.5, True, None, 0, 3+5j)

for i in tuplem:         ### tuple larda for loop calisir mi??
  print(i)

setim = {1, "kiraz", 2.5, True, None, 0, 3+5j}

for i in setim:   ## setler unordered dir. setlerde de for loop calisir mi?
  print(i)




a = [5]  ### Burada a degiskenini for döngüsü ile iterate edebilir miyiz??

for i in a:
  print(i)
  

for x in range(i):
  print("Gökhan bey")

# i = 1
# i = 2
# i = 3
# i = 4
i = 5


print(i + 2)


a = (5,)

for i in a:
  print(a)





### Task:
# elimizde isimlerden olusan bir liste var.
# ve biz her bir ismin önüne hello 
# ve her bir isimden sonra iyi günler yazmak istiyoruz.
# nasil yapariz?

liste = ["ayse", "emine", "hakan", "gökhan", "tomy"]

## vvvv

liste = ["ayse", "emine", "hakan", "gökhan", "tomy"]
for i in liste:
  print("Hello", i, "Iyi Günler")







for i in liste:
  print("hello", i, "iyi günler")       
  print(f"Hello, {i}, iyi günler")



## task
# bir tane listemiz var ve biz bu listenin elemanlarini alt alta degil de
# yan yana ve bir liste icerisinde yazdirmak istiyoruz
# ve sadece tek satir output almak istiyoruz.  nasil yapariz ??

liste = [1, "kiraz", 2.5, True, None, 0, 3+5j, "Ankara", "Istanbul"]
bos = []

for i in liste:
  bos.append(i)

  
print(bos)


# task 
# elimizde bir string var ve biz bu string'in her bir elemani arasina
#  # karakteri koymak istiyoruz. ve hepsini tek satirda yan yana
# cikti almak istiyoruz. Output'un Veri tipinin de string olmasini
# istiyoruz.   nasil yapariz??

girdi = input("lütfen bir kelime giriniz: ")
bos = []

for i in girdi:             #  <<<==  2. cözüm yolu
  bos.append(i)
  bos.append("#")
a = "".join(bos)
print(a.strip("#"))



#### Hocanin cözümü:

girdi = input("lütfen bir kelime giriniz: ") # ankara

counter = 0

for i in girdi:
  counter += 1          ### Bu yöntem de counter kullanma sebebi son karaktere # gelmemesi
  if counter < len(girdi):
    print(i, end = "#")
  else:
    print(i)

## burada da diger bir yöntem:
# sadece sonda print yaziyoruz

girdi = input("lütfen bir kelime giriniz: ")

counter = 0

for i in girdi:
  counter += 1
  if counter < len(girdi):
    i = i + "#"
  else:
    i = i
  print(i, end ="")




## dict örnegi:
# normalde bir degiskeni print ettirmek istedigimizde output da o degiskenin
# value sunu görürüz. peki bu durum dict lerde nasildir ?

# önce bu örnege bakalim.Sonra da eger 
# bu kod calisir ise value lari output alalim
# en sonunda da itemlari alalim

user = {"name" : "Daniel", "Surname" : "Smith", "age" : 35}

for i in user.items():
  print(i)





### value lar

user = {
    "name" : "Daniel",
    "Surname" : "Smith",
    "age" : 35
}

for i in user.values():
  print(i)

#   Dikkat: Bu sekilde print edersek nasil  bir sonuc aliriz
# asagidaki hücredeki gibi olsa nasil olur?

user = {
    "name" : "Daniel",
    "Surname" : "Smith",
    "age" : 35
}

for i in user.items():
  print(i)              ## dikkat sadece i print ediliyor. ama asagida i ve j
  print(type(i))        ## output da item ve value aralarina ne girer??
                        # ayrica outputlarda parantez ve "" var mi dikkat edelim

                        # son olarak da burada veri type imiz ne olur??

user = {
    ("name",) : "Daniel",
    58 : "Smith",
    "age" : 35
}

for i, j in user.items():
  print(i , j)                ##  burada output nasil olur. asagida nasil olur?
  print(type(i), type(j))     ###  type dikkat

a = ["ali", "veli", "ankara", "sen"]
b = ("30", "10", "9", "44")
c = {1, 2, 3, 5}
d = [1, 2, 3, 5]

for x, y, *z in a, b, c, d:
  print(x, y, z)







user = {
    "name" : "Daniel",
    "Surname" : "Smith",
    "age" : 35
}

for i, j in user.items():
  print(i , ":" , j)  ###  Dikkat: aralara + koyduk. Ne sonuc aliriz?

user = {
    "name" : "Daniel",
    "Surname" : "Smith",
    "age" : 35
}

for i, j in user.items():
  print(i + ":" + j)

###  task :
# kullanicilardan öncelikle isim ve soyisim bilgilerini alacak sekilde bir
# kod yazalim. sonrasinda alinan bu girdileri dict formatinda olacak sekilde
# isim ve soyisim itemlari yapalim. ve en sonunda da bilgi giris tarih siralamasina
# göre bir liste icinde data base simizde muhafaza edelim.

girdi = list(map(str, input("Aralarda bosluk ile lütfen isim ve soyisimleri giriniz: ").split()))

isim = []
soyisim = []

counter = 0
database = []         ## Not bu kod ile tüm isim soyisimler ayri bir dictionary


for i in girdi:
  if counter % 2 == 0:
    i = [i]
    isim.append(i)
  else:
    i = [i]
    soyisim.append(i)
    
  counter += 1



for i, j in zip(isim, soyisim):      
  zipp = dict(zip(i, j))
  database.append(zipp)

print(database)









girdi = list(map(str, input("Aralarda bosluk ile lütfen isim ve soyisimleri giriniz: ").split()))






girdi = list (map (ahmet    kaya    ali    kaya zeynep kaya)) .split()
[ "ahmet"    kaya    ali    kaya zeynep kaya ]
map(str, girdi)


a = list(map(str, "mustafa ahmet göksel".split()))
print(a)
bos = []
for i in a:
  i = [i]
  bos.append(i)
print([bos[0]])

a = list("mustafa")
print(a)

[["mustafa"]]   



# Burada da tüm veriler sadece bir dict icerisinde 

girdi = list(map(str, input("Aralarda bosluk ile lütfen isim ve soyisimlerini giriniz: ").split()))

new = []
new2 = []
counter = 0


for i in girdi:
  if counter % 2 == 0:
    new.append(i)
  else:
    new2.append(i)
  counter += 1 

zipp = dict(zip(new, new2))
database = []
database.append(zipp)
print(database)



## for döngüsünde birden cok variable ile tuple lar icerisinde gezme:
# unpacking

liste = [("a","b"), ("c", "d")]

for x, y in liste:
  print(x, y)
## Dikkat: burada a  ve b ciftlerimizin tuple olmasi sart degildir.
# liste icinde tuple degil de liste de olsa, set de olsa python cift olduklarini algilar 
# sadece dict ler de calismaz (asagida oldugu gibi)

##  sadece x degiskeni kullansak output ne olur?

liste = [("a","b"), ("c", "d")]

for x in liste:
  print(x)

liste = [{"a" : "b"}, {"c" : "d"}] 

for x, y in liste:
  print(x, y)        ##  Burada sadece x kullanirsak o zaman calisir 

## tuple larin bu özelligi ile yine tuple larin immutable özelliklerini
# birlestirerek biz nerede kullanabiliriz.
# Mesela diyelim sirketimizde calisan personelin ocak, temmuz ve aralik maaslarini
# personelimizden istiyoruz ve bunlarin sirasi degismeden ve bu bilgilerin kaybolmadan
# muhafaza edilmesini istiyoruz. O durumda kullanicidan gelen 3 bilgiyi
# aninda tuple yapip dogrudan liste icine append edebiliriz.


#######         Operations with for loops



##  kullaniciya bir islemi kac kez yapmamiz gerektigini soruyoruz
# daha sonra o islemi o kadar kez icra ediyoruz.
# Mesela telefon alarmi düsünelim. Alarm kac kez tekrar etsin kullaniciya soralim

a = input("Lütfen alarm saatini giriniz: ")

print(f"Saatiniz {a} olarak ayarlandi")

tekrar = int(input("Alarmin kac kez tekrar etmesini istersiniz? "))

for i in range(tekrar):
  print("Guguk Guguk Guguk")

##  Simdi de hepimiz icin sinir bozucu olan Alarm algoritmasi yapalim

saat = round(float(input("Lütfen alarm saatini (18.05) formatinda giriniz: ")), 2)
print(f"Alarminiz {saat} olarak basariyla kuruldu")
print(f"Guguk Guguk Guguk, Uyanma Zamani, Saat = {saat}")

tus = input("Lütfen bir tusa basiniz: ")

while tus == "ortatus" or tus == "erteleme":  ##  burada and olursa calismaz 
  saat += 0.05
  tepki = "Guguk Guguk Guguk"
  print("{} saat {} " .format(tepki, round(saat, 2)))
  tus = input("Lütfen bir tusa basiniz: ")

  if tus == "kapatma":
    print("Alarm Kapatildi")
    break

### basit bir hesap makinesi
# kullanicidan kullanicinin istedigi miktarda sayi alalim ve
# hangi matematiksel islemi yapmak istedigini soralim

sayilar = list(map(int, input("Lütfen sayi giriniz: ").split()))
print(f"Girdiginiz sayilar: {sayilar}")
islem = input("Lütfen yapmak istediginiz islemi giriniz: ")
bos = 1


for i in sayilar:
  if islem == "*":
    bos *= i
    
  elif islem == "+":  ## Not burada islem + - olunca bos degiskeni 0 olmasi gerekir
    bos += i           #  nasil yapabiliriz ??
     
  elif islem == "/":
    bos /= i
    
  elif islem == "-":
    bos -= i
  elif islem == "**":
    bos **= i
  else:
    print("Hatali giris yaptiniz üzgünüz!!!")

print(bos)


  



# derste yaptigimiz basit carpim tablosu

sayi = int(input("Lütfen bir sayi giriniz: "))

for i in range(11):
  print(f"{sayi} * {i} = {sayi * i}")

  

# derste yaptigimiz basit carpim tablosu
# formatlama methodu ile

sayi = int(input("Lütfen sayi giriniz: "))

for i in range(11):
  print("{} x {} = " .format(sayi, i), sayi * i)

####  yari piramit:

sayi = int(input("Lütfen bir sayi giriniz: "))

for i in range(1, sayi +1):
  print(str(i) * i)

##  stringlerin formatlama yöntemlerini hatirlayalim:

# 1:   Aritmetik operatörler ile formatlama(yukarida yaptigimiz gibi)
#      "*" ve "+" isaretleri birden cok stringi birbirine concat yapar
# 2:   f formating ile formatlama
# 3:   .format ile formatlama

#####  13. session Kahoot
condition = (3 > 1) and (1 < 1)

if "condition":  ##  string icinde dikkat
  print("It works")
else:
  print("Something is wrong")

condition = (3 > 1) and (-1 < 1)

if condition: 
  print("It works")
else:
  print("Something is wrong")

condition = (3 > 1) and (1 < 1)

if ["condition"]:  ##  liste icinde dikkat
  print("It works")
else:
  print("Something is wrong")

condition = (3 > 1) and (0 < 1)

if not condition:    ### not condition
  print("It works")
else:
  print("Something is wrong")

## range func calisma prensibi:

# range(start, stop, step) seklindedir.

## Önemli: eger parantez icerisinde tek bir rakam görürsek bu stopdur. range(10) gibi

# listelerde ve stringler de ise bu durum farkli idi. liste[1] seklinde tek rakam
# gördügümüzde bu sadece start oluyordu. liste[1: 5] ise start ve stop du.

# eger range icerisinde range(1, 11) seklinde 2 rakam görürsek bu start ve stop olur
# 3 rakam görürsek bu da start stop ve step olur.

a = list(range(1, 20, 2))  ## stop ayni listeler gibi -1 olarak calisir

print(a)

# peki range func da da negativ step var midir?
##  var ise nasil calisir ??

print(*range(10, 1, -1))     ###  vvvvvvvvvvvv

### Attention:
# Burada önemli olan husus sudur:  Biz parantez icerisinde 1 yazdik ama 
# buna ragmen output da 1 rakamini göremiyoruz.
# Bunun sebebi: calisma prensibi olarak stop -1 olarak calismasidir.
# Bu demek oluyor ki, hangi yönde gidersek gidelim stop dan bir önce duruyoruz

# Burada dikkat etmemiz gereken ikinci husus ise sudur:

a = [1, 2, 3, 4, 5, 6]

print(a[::-1])

# Dikkat edersek listelerde negativ step kullandigimizda ilk eleman 6 ve son eleman
# ise 1 dir. Yani ilk eleman en sagdaki, son eleman da en soldaki elemandir.

# Ancak range de ki ilk ve son elemana baktigimizda bu durumun farkli oldugunu görürüz.
# range de ilk eleman yine en soldaki, son eleman yine en sagdaki elemandir.
# Bunun sebebi sudur: 

# Burada listeyi sadece tersten yazdirdik. Eger listede negatif slayslama yapmak isteseydik
# Bu durumda yine elemanlarin yerini degistirmek zorunda kalacaktik

# örnegin asagidaki kod bos liste döndürür

a = [1, 2, 3, 4, 5, 6]

print(a[0:5:-1])  



##  *  asteriks'in range haricinde kullandigimizda nasil calisir?
#  iterable lar ile kullandigimizda, iterable' i elemanlarina böler:
# peki iterable larda nasil calisir ona bakalim 



print(*["ankara", "a", "b", "c"])

print(*(*"ankara", "1", "2", "3"))  ## burada cift yildiz var

print(type(* [1]))  # * kullandigimizda veri tipi verinin orjinal tipi olur

## Dikkat: biz bir string in elemanlarini list veya tuple func lari ile
# elemanlarina ayirdigimizda, o elemanlari tek tek kullanabiliyor ve
# üzerlerinde islem yapabiliyorduk.
#  * kullandigimizda da yine elemanlari tek tek baska bir islem icin kullanabilir miyiz?? 

# dict lerde yildiz kullanirsak ne aliriz??

dictim = {"a" : "2", "b" : "4"}

print(*dictim)

###  zip func calisma prensibi:

# fermuar gibi calisir ve 2 iterable'in elemanlarini karsilikli eslestirir.

# iterable larin eleman sayilari esit olmak zorunda degildir.

# Dikkat: zip func da range gibi ketum functionlardandir. O nedenle cözmek gerekir
# (for ile, *  ile, list, tuple, set vb ile)

# Dikkat: zip() func icerisine sinirsiz sayida arguman alabilir. Sadece 2 tane iterable'i
# zip yapmak sart degildir. Alt hücrelerde örneklerini yapacagiz
# Yani bu argumanlar birlestirmek 
# istedigimiz farkli iterable'larin variable isimleridir. Yada direkt olarak zip func icerisine
# iterable larin kendisini de yazabiliriz. Bunun örnegi bir alt hücrede

a = ["a", "b", "c", "d", "e"]

b = (1, 2, 3, 4, 5)

c = set(zip(a, b))

print(c)

# Burada dikkat etmemiz gereken husus:
# Zip ile ürettigimiz tuple lari daha sonra teker teker alip baska bir yerde 
# kullanma sansimiz var midir ??

# parantez icerisinde direkt iterable lari yazma

x = list(zip([1, 2, 3], ("a", "b", "c")))       

print(x)





## Dikkat!!!

## peki zip func icerisine iki degil de tek argüman yazarsak ne olur ??
# error mu aliriz?

x = [1, 2, 3]      

print(list(zip(x)))

## iterable larin tüm elemanlarini degil de, belirli elemanlarini
# zip yapabilir miyiz??

a = ["a", "b", "c", "d", "e"]

b = (1, 2, 3, 4, 5)

c = list(zip(a[1], b[1]))   #  <<<====  Dikkat: Bu sekilde calisir mi?
                                ##    asagidaki hücre calisir mi?
print(c)

a = ["a", "b", "c", "d", "e"]

b = (1, 2, 3, 4, 5)

c = list(zip(a[0:4], b[0:4]))   
                               
print(c)

### Task:
# Diyelim ki iki iterable'i zipledik ama su an icin bizim zipledigimiz 
# iterable larin ürettigi tüm tuple lar bize lazim degil. Su an icin sadece
# her bir iterable' in cift veya tek sayili elemanlarinin ürettigi tuple lar bize lazim ve 
# bunlari cekip almamiz gerekiyor. nasil yapariz?

# Mesela söyle düsünelim. asagidaki iterable larda clarusway ögrenci no ve notlari 
# yaziyor. ve biz bunlari tek sayili ögrenci notlari ve cift sayili ögrenci notlari
# diye ayiracagiz

ögrenci = ["1490", "1491", "1492", "1493", "1494", "1495", "1496"]

notlar = (80, 85, 83, 75, 90, 79, 60)

counter = 0

for i, j in zip(ögrenci, notlar):
  if counter % 2 == 0:   ##  >>>   bu cift sayili olanlari üretir
    print(i, ":", j)
  counter += 1

##  dikkat!!!
# zip func ile sadece i degiskeni kullanirsak ne output aliriz?
# asagidaki hücrede oldugu gibi i ve j kullanirsak output ne olur ??

# !!!!!!    outputlarin veri tiplerine Dikkat

a = ["a", "b", "c", "d", "e"]

b = (1, 2, 3, 4, 5)

for i in zip(a, b):
  print(i)

a = ["a", "b", "c", "d", "e"]

b = (1, 2, 3, 4, 5)

for i, j in zip(a, b):
  print(i, j)

# zip de ikiden fazla degisken calisir mi?

a = ["a", "b", "c", "d", "e"]

b = (1, 2, 3, 4, 5)

c= {"ben", "sen", "o", "biz", "siz"}

print(*zip(a, b, c))

###  Dikkat: zip func tek seferlik output verir ve sonra icerisi bosalir demistik.
# Eger biz tekrar cikti almak istersek zip func i tekrar doldurmamiz gerekir.

a = ["a", "b", "c", "d", "e"]

b = (1, 2, 3, 4, 5)

zipp = zip(a, b)
print(*zipp)
print(*zipp)
print(zipp)  # asteriks kullanmaz isek ne olur??

a = ["a", "b", "c", "d", "e"]
b = (1, 2, 3, 4, 5)
zipp = zip(a, b)

for i in zipp:
  print(i)

print(list(zipp))  ##  BU satir ne döndürür??

### Bu konulari internette generator ve iterator olarak bulabiliriz
# zip func i her doldurusumuz bir generate dir

###  Dikkat zip() func dict üretimi icin cok uygundur.
# Yani bizim dictlerde ihtiyacimiz olan key value pair lari 
# zip func otomatik olarak üretir.

# Elimizde bir tuple ve bir liste olmasina ragmen bunlari
# tek bir komut ile birlestiriyoruz ve daha önemlisi de 
# dict komutu vasitasi ile outputumuz orijinal bir dict görüntüsünde oluyor  

a = ["a", "b", "c", "d", "e"]
b = (1, 2, 3, 4, 5)
zipp = dict(zip(a, b))

print(zipp)

##  zip' i string func ile kullanirsak output ne olur??

a = ["a", "b", "c", "d", "e"]
b = (1, 2, 3, 4, 5)
zipp = dict(zip(a, b))

print(zipp)



a = ["a", "b", "c"]
b = (1, 2, 3)
zipp = str(zip(a, b))

print(zipp)





###  derste cözdügümüz task:

# Range func ile 0 dan 20 ye kadar bir liste olusturacagiz. 
# Ve bu listenin tek elemanlarini tek isimli listeye cift elemanlarini cift
# isimli listeye atacagiz.
# en sonunda da listenin elemanlarini toplayip
# her bir listenin elemanlarinin toplamini söyleyecegiz

tek = []
cift = []

for i in range(20):
  if i % 2:
    tek.append(i)
  else:
    cift.append(i)

print(tek)
print(cift)

# simdi de listenin elemanlarini toplayalim:

tekbos = 0
ciftbos = 0

for i in tek:
  tekbos += i
print(f"Tek sayilarin toplami = {tekbos}")

for i in cift:
  ciftbos += i
print(f"Cift sayilarin Toplami = {ciftbos}")

###   Task:

#  kullanicidan birden cok sayi aliyoruz. Ve kullanicinin kac adet tek sayi
# kac adet cift sayi girdigini tekrar kullaniciya söylüyoruz:

# Bu task a baslamadan önce map func integer ve float ile nasil calisir 
# mantigina bakalim:

# öncelikle map() func su sekilde kurulur:

# map(func, iterable) ==>> tüm bu yapiya map object denir

# yani map object iterable bir eleman alir. eger biz integer gibi
# bir veri girersek bu durumda elemanlarina ayiramaz ve hata verir.

# peki map() func calismayi ne zaman durdurur?
# ayni for döngüsü gibi icerisinde bulunan iterable'in elemanlari son buldugunda
#  calismasi son bulur. 

# map() func ismi mapping den gelmektedir yani eşleme olarak bilinir,
#  çünkü yinelenebilir bir girdideki her öğeyi sonuçta yinelenebilir bir şekilde 
# yeni bir öğeyle eşler. Bunu yapmak için, map() yinelenebilir girdideki 
# tüm öğelere bir dönüşüm işlevi uygular.


#  map()  func'nin calisma prensibini anlamak icin for döngüsü
# ile kiyas edelim.

# elimizde bir liste olsun ve biz bu listenin her bir elemaninin karesini 
# alarak yeni bir liste olusturalim

liste = [1, 2, 3, 4, 5]
bos = []

for i in liste:
  i = i ** 2
  bos.append(i)

print(bos)

##  simdi ayni islevi map() ile yapalim.

def kare(sayi):
  return sayi ** 2

liste = [1, 2, 3, 4, 5]

a = map(kare, liste) 

print(list(a))

# Not: eger map func'in sonunda split kullanmaz isek girdigimiz her bir 
# karakteri tek tek ayirir. Örnegin:

sayi = list(map(int, input("Lütfen bir sayi giriniz: " )))

print(sayi)




# map() func'nin split ile calisma prensibi

sayi = list(map(int, input("Lütfen birden cok sayi giriniz: " ).split()))

print(sayi)

# Burada dikkat etmemiz gereken husus nedir?
# split() methodunu tam olarak nereye yazacagimiz hususudur.


# Buradaki mantik su sekilde isler. map() methodu bizim verimizi tek tek
# ayirmadan önce bizim kendi istegimize göre ayirmamiz gerekir.
# Bu nedenle  split() methodunu direkt input verisinin pesine yazariz ki

# verimiz henüz map() islemine tabi tutulmadan ayirma islemini kendimiz
# gerceklestiririz

# eger map() func parantezi disina yazarsak error aliriz


## Dikkat: Normal de input str cikti üretir. Biz burada input alir almaz
# verimizi map func ile int yapiyoruz.

# Burada dikkat etmemiz gereken husus sudur ve önemlidir:
# normalde biz asagida oldugu gibi map func icerisinde int bir deger yazarsak
# hata aliriz demistik

# a = map(int, 123456)

# print(a)



# map burada su sekilde calisir:

# user'in girdigi string veri tipindeki sayisal degeri alir,
# iterable oldugu icin elemanlarina ayirir ve her bir elemani integer'a
# cevirir. Ve son olarak da biz liste istedigimiz icin bunu liste icerisine atar.



# asagidaki hücrede verilerin type'ina bakalim

sayi = list(map(int, input("Lütfen birden cok sayi giriniz: " ).split()))

print(type(sayi[0]))  #  user'in girdigi rakamin 0. index numarasinin veri tipi

# map func float ile nasil calisir?

sayi = list(map(float, input("Lütfen bir sayi giriniz: " )))

print(sayi)



## Simdi task imiza geri dönelim:

###   Task:

#  kullanicidan birden cok sayi aliyoruz. Ve kullanicinin kac adet tek sayi
# kac adet cift sayi girdigini tekrar kullaniciya söylüyoruz:

# Not: Bu task'in iki farkli cözüm methodu vardir.

# önce 1. method ile cözelim: (counter kullanarak)

sayilar = list(map(int, input("Lütfen birden cok sayi giriniz: ").split() ))

countertek = 0
countercift = 0

for i in sayilar:
  if i % 2:
    countertek += 1
  else:
    countercift += 1

print("{} adet tek sayi girdiniz" .format(countertek))

print("{} adet cift sayi girdiniz" .format(countercift))

## ikinci methodumuz ise append() ve len() methodu ile cözüm yoludur:

sayilar = list(map(int, input("Lütfen birden cok sayi giriniz: ").split() ))

tekliste = []
ciftliste = []

for i in sayilar:
  if i % 2:
    tekliste.append(i)
  else:
    ciftliste.append(i)

print(f"{len(tekliste)} adet tek sayi girdiniz")

print(f"{len(ciftliste)} adet cift sayi girdiniz")

## sum()  func kullanimi:

# calisma prensibi:

# sum(iterable, start)  seklinde calisir.

# buradaki iterable dan kasit numeric bir iterable olmasi gerektigidir.
# Bu func,  numeric olmayan degerleri reddeder. Ama ilerleyen 
# hücrelerde buna bir care arayacagiz

# start ifadesindeki anlam ise indexleme ve slicing deki start stop ve step den
# tamamen farklidir. sum() daki start kelimesi toplama islemine baslarken
# baslangic degerini kac kabul ettigimizdir. yani 1, 2, 3 sayilarini topladigimizda
# toplam 6 dir. eger biz baslangic degerini 4 kabul edersek. sonuc 4 + 6 = 10 eder.

a = sum([1,2,3,4,5], 0)  #  start yazmaz isek default 0 dir

print(a)

# Not: sum() icerisinde tek bir iterable kullanilmalidr. Bu nedenle tuple
# kullanmak istersek parantez icerisinde kullanmamiz gerekir.

# Simdi sum func' i biraz inceleyelim:


# Not: mesela bos bir liste kullanirsak sum() icerisinde;

# Bu durumda sonuc bos liste dönmez. Bu func sayilar ile is yaptigi icin 
# sonuc 0 olur.

a = sum([])

print(a)

# sum hangi collection type larda calisir?
# liste evet
# tuple evet
# set evet
# dict ? (asagidaki hücrede bakalim)

a = sum({1,2,3,4,5}, 0)

print(a)

# dictlerde sum() func kullanmanin birkac yöntemi vardir:
# eger items yada values keys gibi parametreler yazmaz isek ve
# bizim keylerimizin hepsi sayisal deger ise o zaman hata vermeden
# default olarak sadece keyleri toplar.


# ama eger tüm value larimiz sayisal deger ise  o zaman sadece value larda toplanabilir


# Ancak item()  lara gelince is biraz degisir. item in elemamlari olan
# value ve keyler bir tuple icerisinde  birlestirildiginden burada toplama
# islemi gerceklesmez ve hata verir. Yani bu islemi tek satir da yapamayiz.
# Ancak burada söyle bir alternatif yol üretebiliirz:

# bir satir da keyler toplanir. Diger satirda value lar ve bunlar
# 3. satirda birlestirilir

a = {1 : 10, 2 : 20, 3 : 30, 4 : 40, 5 : 50}

x = sum(a.keys())
y = sum(a.values()) 
z = x + y

print(z)

#   sum()  func sayisal olmayan degerleri reddeder demistik.
# yani sum ile string icerisinde sayisal degerlerde yazsa biz bu stringin 
# elemanlarini toplayamayiz.

# peki bizlere verilen string bir degerin icerisindeki rakamlari toplamak
# zorunda kalirsak neler yapabilirz ?? Cevabimiz asagida var.
# ama biraz beyin firtinasi yapalim

string = "123456789" # bu string icerisindeki degerleri sum ile toplayalim











# birinci yöntem 

string = "123456789"

toplam = sum(map(int, string))   ## Dikkat burada map'i listeye yada tuple'a 
                                  # cevirmeye ihtiyac kalmadi
print(toplam)

# Ikinci yöntem

string = "123456789" 
toplam = 0

for i in string:
  i = int(i)
  toplam += i
print(toplam)





##########         14. session        ###############

### derste cözdügümüz Task:
# 1 ile 74 arasindaki sayilarin toplamini veren kodu yaziniz:
# counter methodu ile cözüm

counter = 0

for i in range(1,75):
  counter += i
print(counter)

# uzun cözüm, iki adet for döngüsü

bos = []

for i in range(1,75):
  bos.append(i)

counter = 0
for i in bos:
  counter += i

print(counter)

#######   nested for loop    #########

##  normal de for döngüsü yapilari su sekildedir:

for variable in iterable:
  body

# nested for döngülerinde ise en distaki for döngüsünün body si 
# alt kisimda bulunan for döngüsüdür

for variable1 in iterable1:
  for variable2 in iterable2:
    body


## if yapilari genel calisma prensibi nasildi?
# i degiskenimiz yazmis oldugumuz iterable icerisine girer ve bu iterable
# icerisinde sadece bir döngü yapar. Ve sonra body kismina gecer, body nin ise tamamini 
# calistirir. 
# yani body nin tamamini calistirdigi icin altta bulunan iterable in tüm elemanlari 
# döndürülür, daha sonra tekrar üstteki for döngüsüne dönüs yapilir.  

a = ["1 ", "2 ", "3 ", "4 "]  ### Burada output nasil olur?

b = ["bir", "iki", "üc", "dört"]

for i in a:
  for ii in b:
    print(i + ii)    # vvv  

# nested for loop larda kac adet output umuz olacagini, iki degiskenimizin value 
# sayilarini carparak hesap edebiliriz.


# yani asagidaki sekilde degerlendirdigimizde, sagdaki tüm degerleri soldaki
# ilk elemana teker teker assign eder, daha sonra soldaki ikinci elemana 
# assign islemine gecer

# ["1 ", "2 ", "3 ", "4 "] <=====> ["bir", "iki", "üc", "dört"] 

## nested for loop lari daha iyi anlamak  ve nested for yapisinin 
# nasil calistigini aklimizda daha iyi tutabilmek icin söyle bir örnek düsünelim.

# ilkokullarda ortaokullarda ve listeler de 1 den 11 e kadar sinif
# numaralari vardir. Ve her bir sinif kendi icerisinde a  b c d e f g
# seklinde harflendirilmistir. Iste bu sinif numaralari ve harflendirme
# islemini tek bir kod ile yapmaya calisalim.

# Burada dikkat etmemiz gereken husus, hangi verinin önce return ettirilmesi istiyorsak
# o veriyi üstteki yani ilk for döngüsü icerisine yerlestirmemiz gerekir

sinif = [1, 2, 3, 4, 5, 6, 7, 8]

harfler = ["a", "b", "c", "d", "e", "f"]

for i in sinif:
  for ii in harfler:
    print(i, ii)

## Bir diger örnegimizde su sekildedir:
# Her bir araba markasinin a, b, c, d ve suv segmentleri ve
# bu segmentlere göre adlandirilmis özel isimleri bulunmaktadir.
# araba markalarindan ve modellerinden olusan bir kod yazalim

marka = ["mercedes", "bmw", "volkswagen", "seat", "audi"]

model = ["a", "b", "c", "d", "suv"]

for i in marka:
  for ii in model:    ### Dikkat: nested for'larda, ayni degisken kullanilmaz
    print(i, ":", ii)



# List Comprehension

# normal bir for loop yapisi:
for item in iterable:
  expression(body)   ## yani önce for satiri sonra body

# list comprehension yapisi ise su sekildedir:

[expression for item in iterable]

# yani önce body sonra for

## Not: Kafa karisikligi olusturmamasi acisindan list comprehension yapisi
# kurmanin en kolay yolu; normal for döngüsü siralamasinda yapi kurularak
# en son basa dönüp body kismini yazmaktir

# normal for loop da, python a öncelikle nerede döngü yapacagini söyleriz
# daha sonra ise bu döngü icerisinde ne yapacagini söyleriz.

# list comp da ise; önce python a ne yapacagini söyleriz daha sonra
# bunu nerede yapacagini söyleriz

# list comprehension kullanarak daha az degisken kullanacagimiz icin,
# ve bu kullanim sayesinde normal for döngüsüne göre daha az kod yazmamiz gerektiginden 
# olusturdugumuz programin hizini artirabiliriz

##  normal for döngülerinde elimizde bos bir liste bulunur ve 

# biz bu listenin icerisine disaridan attigimiz elemanlar ile doldurururuz

# list comprehension da ise listenin icerisindeyiz ve önemli olan sudur

# liste icerisine disaridan eleman cekmiyoruz. Liste icerisinde bulunurken

#  listenin disina cikmadan for döngüsü calistiriyoruz ve iceride eleman üretiyoruz

# expression kismina ne yazdi isek, hepsi listenin elemanlari haline gelir ve

# virgüller ile birbirinden ayrilir.


## klasik bir for döngüsünü list comp yapalim

bos = []

for i in range(8):  ## Dikkat etmemiz gereken husus: Normal for döngülerinde bulunan
  bos.append(i)     # noktalama isaretlerini burada kullanmiyoruz.  sadece space yeterli 

print(bos)    ##  bunu simdi beraber list comp yapalim



##   Dikkat normal for döngüsünde listenin disarisinda oldugumuz icin, 
# listenin icerisine eleman eklemek icin append methodu kullanilir.

# Ancak list comp' larda listenin icerisinde bulundugumuzdan dolayi,
# append kullanmamiza gerek yoktur.

# expression kismina, neyi output almak istiyorsak onu yaziyoruz
# yani bu kisimda outputumuzu istedigimiz sekilde formüle ediyoruz

a = [(i ** 2) / 2 for i in range(8)]

print(a)



##  output taki her elemanimizi nasil ayri ayri liste, tuple yada set yapariz?

# liste ve set icin sadece i'yi [] icerisine yada {} icerisine almamiz yeterlidir.
# ancak tuple yaparken sadece () icerisine almamiz yeterli degildir.
# cünkü tek elemanli tuple yapimi farklidir


a = [[i] for i in range(10)]

print(a)

a = [{i} for i in range(10)]

print(a)

a = [(i,) for i in range(10)]

print(a)

# a = [tuple(i) for i in range(10)]   ##  Bu sekilde ne output aliriz???

# print(a)

# kücük listeler seklinde islem yapmak da mümkündür:
# Mesela elimizde iki tane liste var. Biz bu listenin elemanlarini zip ile

# birlestirelim. birbirleri ile toplayip ikiye bölelim ve karelerini alalim.
# son olarak da hepsini liste icine atip saklayalim

# Not burada ayni zamanda round() func kullanimini hatirlayalim

a = [1, 2, 3, 4, 5]

b = [6, 7, 8, 9, 10]

a = [[round(((i + ii) / 2) ** 2, 1)] for i, ii in zip(a, b)]

print(a)

a = [1, 2, 3, 4, 5]

b = [6, 7, 8, 9, 10]

for i, ii in a, b:  ##  Önemli:  eger burada oldugu gibi iki listenin ismi 
  print(i, ii)      # zip gibi herhangi bir func yada method kullanmadan yazarsak
                    # kodumuz calismayacaktir.

###  if statements ile list comprehension birlesimi:
# Bu if yapilarina ternary if condition denir. yani tek satirda if yapilari

# Burada yapimiz su sekildedir:

#  [ne yapmali?(body)   ne icin ve nerede yapmali?(for)   hangi durumda yapmali(if else) ]

# bunu asagidaki örnekle inceleyelim

# elimizde bir liste var. Biz bu listenin elemanlarindan tek sayi olanlarin
# karesini almak istiyoruz ve bunu bos bir listede depolamak istiyoruz.
# bunu öncelikle normal for döngüsü ile yapalim


listem = [10, 11, 12, 13, 14, 15, 16, 17, 18]
bos= []
for i in listem:
  if i % 2: 
    bos.append(i ** 2)          ## bu yapida bos bir liste atamak ve append kullanmak
print(bos)                      # zorundayiz

##  simdi de list comprehension ile yapalim

# Dikkat: bir liste icerisinde for if else ve body leri ayni anda kullaniyoruz

# ve aralarda hicbir noktalama isareti kulanmiyoruz

listem = [10, 11, 12, 13, 14, 15, 16, 17, 18]

a = [i ** 2 for i in listem if i % 2]

print(a)           

#  Bu yapilarda elif yoktur. sadece if ve else vardir

# Dikkat: Eger kurdugumuz yapida body, for ve if'in yerlerini degistirir isek,
# o zaman kodumuz calismaz.

# Dikkat etmemiz gereken bir diger husus sudur:
# for döngüsü  body si for un solunda kalan kisimdir.
# if döngüsü body si ise if in solunda kalan komple kisimdir.(for da buna dahildir)



# yani buradan cikan sonuc sudur: 
# normal yapilarda hem for loop'un hem de if statement'in body leri 
# kendilerinden sonra yani alt satirda gelir. Ama list comprehension larda
# bu durum tam tersine döner ve body ler kendilerinden önce gelir.



## peki else de kullanmak istersek nasil  bir yapi kurmaliyiz ??

listem = [10, 11, 12, 13, 14, 15, 16, 17, 18]

a = [i ** 2 for i in listem if i % 2]

print(a)         

#  diger bir else' li örnek

# fruits = ["mango" if i%3 == 0 else "orange" for i in range(10)]
# print(fruits)

# nested for looplar ile list comprehension

liste = [f"{str(i)} - {j}" for i in range(1, 4) for j in ["a", "b", "c"]]

print(liste)



## nested if statements lar ile list comprehension:


liste = [i for i in range(50) if i % 2 == 0 if i % 3 == 0 if i % 4 == 0]

print(liste)

# Dikkat bu örnekte sadece tek bir cikti var o da i dir.
# Peki list comprehension ile birden cok cikti print ettirebilir miyiz?
# mesela 
# if i % 2 == 0   print(2)
# if i % 3 == 3   print(3)
# else            print("x")    # vvv









liste = ["2" if i % 2 == 0 else "3" if i % 3 == 0 else "x" for i in range(10)]

print(liste)

a = [1, 2, 3, 4, 5]

b = ["yes" if i == 1 else "no" if i == 2 else "idle" for i in a]

print(b)

##  araba modelleri sorusunu list comprehension ile cözelim:

marka = ["mercedes", "bmw", "volkswagen", "seat", "skoda"]

model = ["a", "b", "c", "d", "suv"]


# Dikkat nested for yapisi kuracagiz ve ana for nerede olacak
# nested for nerede olacak?







marka = ["mercedes", "bmw", "volkswagen", "seat", "skoda"]

model = ["a", "b", "c", "d", "suv"]

new = [i + " -" + ii for i in marka for ii in model]
                                               
print(new)

# Dikkat:

## list comprehension kullanarak ayni liste icerisine degil de baska

# bir liste icerisine append yapilabilir mi??

bos = []

a = [bos.append(i) for i in range(5)]

print(bos)   ##  print(a)  dersek output ne olur?

### Dikkat!!!!!!
# peki bu list comprehension a disaridaki bir for ile eleman
# ekleyebilir miyiz??

bos = []
a = [bos.append(i) for i in range(5)]

print(a)

for i in range(5):
  a.append(i)

print(a)

a = ["a", "b", "c", "d"]
b = ["1", "2", "3", "4"]

for i in a, b:          # Burada i ve ii zip seklinde 2 degisken kullanirken
   print(i)             # zip kullanmazsak kodumuz calismaz demistik.
                        # peki iki listede tek i degiskeni kullanirsak
                        # ne sonuc aliriz ?  

# derste cözdügümüz örnek

(monday, tuesday, wednesday, thursday, friday, saturday, sunday) = range(1, 8)

print(monday)
print(friday)

## dikkat 1 deyince gün gelmez

## enumerate kullanimi:

günler = ("monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday")

yeni = list(enumerate(günler, 1))  ## ketum function dir

# yeni.reverse()      #  reverse kullanirsak output ne olur?

print(yeni)

## enumerate ve for ile terse cevirme:

günler = ("monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday")

yeni = list(enumerate(günler, 1))  

listyeni = []

for i in yeni:    ## enumerate verileri tuple'a dönüstürdügü icin önce liste yapiyoruz
  i = list(i)
  listyeni.append(i)
  i = i.reverse()
  
print(listyeni)

###  append() methodu ile bir seferde en fazla tek eleman eklenebilir

# ve append() ile bir listeye baska birden cok elemani liste olarak eklemek istersek
# bu listenin elemanlarini tek tek degil, asagida oldugu gibi
# listeyi komple append() eder.

a = [1, 2 ,3]
b= [4, 5, 6]

a.append(b)

print(a)             

# bu nedenle birden cok elemani bir seferde eklemek istersek
#asagidaki methodu kullanabiliriz

a = [1, 2 ,3]
b= [4, 5, 6]

c = a + b

print(c)

# Hatirlatma:

x, y,*z = (11, 22, 33, 44, 55)

print(x)
print(y)
print(z)  ###   dikkat * kullaninca output umuz liste olur

### placeholder

## binlerce elemandan olusan bir tuple var
# ve biz bunun sadece ilk 2 elemanini simdi atamak istyoruz
# digerleri de hafiza da yer kaplamasin istiyoruz


x, y, *_ = (10, 20, 30, 40 ,50, 60, 70, 80 ,90)

print(x)
print(y)

# asteriks herhangi bir yerde kullanilabilir

x, y, *z, t= (10, 20, 30, 40 ,50, 60, 70, 80 ,90)

print(x)
print(y)
print(z)
print(t)

## iki yildiz kullaninca hata aliriz

x, *y, *z, t= (10, 20, 30, 40 ,50, 60, 70, 80 ,90)

print(x)
print(y)
print(z)
print(t)

### derste cözdügümüz örnek

names = ["susan", "tom", "edward"]

mood = ["happy", "sad"]

a = [i + " is " + j for i in names for j in mood]

print(a)

## derstek örnek:

count = 0

while count >= 0:
  print(count)
  count += 1
  if count == 10:
    count = -1