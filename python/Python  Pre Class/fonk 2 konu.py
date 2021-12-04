 ############            Functions 

# Temel olarak, bir  fonksiyon  bizim için mantık yürüten bir kod bloğudur, 
# örneğin bir metin yazdırır, bazı verileri siler veya bir sayının karesini alır. 
# Başka bir deyişle, bir fonksiyon , yalnızca çağrıldığında çalışan bir kod parçasıdır. 

# Fonksiyonlar kodlama sürecini basitleştirir, gereksiz mantığı önler 
# ve kodun takip edilmesini kolaylaştırır.

# Bazı durumlarda, kendi fonksiyonumuzu oluşturmamız gerekebilir. 
# Böylece olusturdugumuz bu function lar kodumuzdaki karışıklığı ortadan kaldırmaya 
# yardımcı olurlar. Cünkü bizi gereksiz tekrarlardan kurtarırlar. 


# Olusturdugumuz function i istedigimiz yer ve zamanda cagirabilir ve kullanabiliriz


# Interview Question
# S : Python'da fonksiyon nedir?
# Bir fonksiyon, yalnızca çağrıldığında yürütülen bir kod bloğudur. 
# Bir Python func tanımlamak için def anahtar sözcüğü kullanılır.

# a function is a piece of code that only runs when its name is called.

###############               Calling a Function

# Bir func cagirma onu kullanma anlamina gelir.

# Basit bir örnekle func yapisini görelim

# multiply(no1, no2)

# Burada multiply fonksiyonumuzun adidir. no1 ve no2 ise bu fonksiyonun 

# carpim islemi icin ihtiyac duydugu parametrelerdir. Cünkü carpim olmasi icin

# en az iki parametreye ihtiyac vardir.

# Birde argument tabiri vardir. Argumentlar ise parametreler arasindaki farki 
# detayli inceleyecegiz





## ###########             Calling print() Function

# Print() fonksiyonunun calisma prensibini hepimiz cok iyi biliyoruz.

# print olarak ismi yazilir ve yanina ()  parantez koyularak cagrilir.

# Ve biz bu func icerisine arguman yazmak zorunda olmadigimiz gibi

# birden cok argument da yazabiliriz.

# For example:

print()

print(1, 2, "Sivas", 3 + 5j)

print("Biz IT kursundayiz")

# Soru :  (Bosluga ne gelmelidir)

# You can enter or input data, known as .........   into a function and 

# it returns something good that you want. (a)



##########         Built-in Functions   (yerlesik fonksiyonlar)

### Python da iki türlü function vardir.

# Birincisi built in func dedigimiz python'in sürümlerinde gelistiriciler tarafindan

# hazir olarak piyasaya sürülmüs ve bizim de hazir olarak kullandigimiz 

# print()  gibi functionlardir.


# Ikincisi ise;  User-defined Functions dedigimiz kullanici tarafindan tanimlanan 

# functionlardir.

# Python da İstediğimiz bir şeyi yapabilecek bir işlev düşünüyorsak, 

# muhtemelen vardır. Sadece varlığından haberdar olmamız gerekiyor.

# ve En son Python 3.9 sürümünde yerleşik functionlarin sayısı 69'dur

# Bunlardan bazilari: print(), int(), list(), input(), range()

# Bu functionlarin bazilari 

# içindeki koşullu algoritmaya göre bool tür döndürür. Örnegin:

# .all(iterable)     any(iterable)      callable(object)   

# Bazıları veri türlerini birbirine dönüştürmenize yardımcı olur. 

# Örneğin; bool(), float(), int()ve str().

# Bazıları, koleksiyon türlerini oluşturmanıza ve işlememize izin verir. 

# Mesela: dict(), list(), tuple(), set(), len(), frozenset(), zip(), 

# ve .filter(function, iterable) enumerate(iterable)

# Bazıları sayılarla islem yapar. Mesela: max(), min(), sum()ve round().

# Birde özel amaçlar için inşa edilmiş functionlar vardir. 

# Bunlar Bazı karmaşık uygulamalar yaparlar. 

# Örneğin:

# .map(function, iterable)

# eval(expression[, globals[, locals]])

# sorted(iterable)

# open()

# dir([object])

# hash()

# help([object])

## Interview Question :

#  Python da Function nedir?  vvvvv





# Bir fonksiyon, programın bir bölümü veya bir kez yazılan ve programda 

# istendiği zaman çalıştırılabilen bir kod bloğudur. 

# Func , geçerli bir isme, parametre listesine ve gövdeye(body ye) sahip bağımsız 

# ifadelerden oluşan bir bloktur. Functionlar, modüler görevleri gerçekleştirmek için 

# programlamayı daha işlevsel ve modüler hale getirir. Python, 

# görevleri tamamlamak için çeşitli yerleşik işlevler sağlar ve ayrıca 

# kullanıcının yeni işlevler oluşturmasına da olanak tanır. 


## Sorular (pre_class)

# Which of the following statements is incorrect about functions?

# Select one or more:

# Functions make the code more complex


# They make the code easier to follow


# Functions simplify the coding process

# Calling a function doesn’t mean using it. 

# Calling and using a function have different meanings.
# Select one:
# True
# False





###########         Defining (Creating) a Function

## Bazen bir program yazarken, yerleşik functionlar bizim için yeterli olmayabilir. 

# Veya bazen programımızda tekrar tekrar bir kod bloğu kullanmamız gerekebilir. 

# Bu durumda kendi fuct imizi yazabiliriz. 

# Buna Python'da kullanıcı tanımlı func yani user-defined function denir . 


#  Kendi func imizi olustururken yapi su sekildedir:

#  def  functionname(parameter(s)):    # def, ingilizce definition dan gelir
#  ----executionbody   

## Dikkat etmemiz gereken hususlar

# 1: anahtar kelime def func in adini tanimlar ve sonra 1 space birakilir
# 2: functionname ve sonrasinda hemen normal parantez.
# 3: colon :
# 4: indentation(4 space)
# 5: body

# Sorular (bosluk a ne gelmeli)

# The ........ introduces the name of the user-defined function. It must be followed by the 
# functionname and the parenthesized list of formal arguments. 


# When built-in functions are not enough, or when you need to use a block of code 

# in your program repeatedly, you write your own functions. 

# They are called user-defined functions
 

##   Main Principles of 'Defining' (tanimlamanin temel ilkeleri)

# Pep 8 Kurallari burada da geçerlidir. Bu yüzden kelimeler arasında 

# alt çizgi kullanilmali ve küçük harflerle yazılmalıdır . 

# Parametreler isteğe bağlıdır, ancak parantezler DEĞİLDİR. () zorunludur

# İki nokta üst üste,  kapanış parantezini takip eder ve fonksiyon gövdemizin 

# başlangıcını gösterir. Fonksiyonun kodları (yürütme gövdesi) def deyimin altına 

# girintili OLMALIDIR .



## Önemli: Asagidaki örnekte eger biz print den önce bosluk vermezsek, bu durumda python, 

# func tanimlama isleminin sona erdigini düsünür ve 

# print ifadesini bizim function imiza dahil degilmis olarak algiladigindan 

# error aliriz

## Örnek:

def first_function(argument1, argument2):
  print(argument1 ** 2 + argument2 ** 2)

first_function(2, 3)


## Simdi bir func tanimlayalim

# Outputlarimiz nasil olur ?? 

def multiply(parameter1, parameter2):
  print(parameter1 * parameter2)

multiply(5, 5)

multiply(5, "Antalya ")

multiply(-1, 5.5)







# Daha önce söyledigimiz gibi parametre olmadan da func tanimlayabiliriz

# yani parantez ici bos function

def ders_tekrari():
  print("Biz ders tekrari yapiyoruz")

ders_tekrari()

# önemli bir husus: biz en alt satirda ()  parantez acip kapatmazsak ne olur ??





##########               Execution of a Function 

## Bizler Program akışımızdaki fonksiyonların ürettiği çıktı ve 

# veri tiplerini daha sonra kullanabilmek için return anahtar kelimesine 

# def tanimlama kelimesine ihtiyac duyariz.

def multiply1(argument1, argument2):
  print(argument1 * argument2)

def multiply2(argument1, argument2):
  return (argument1 * argument2)

multiply1(4, 5)           ### Önemli: Outputlara baktigimizda herhangi bir fark 
                          ##  göremeyiz. Ancak asagidaki hücrede ayni islemlerin
multiply2(4, 5)            ## type ini inceleyelim


def multiply1(argument1, argument2):
  print(argument1 * argument2)

def multiply2(argument1, argument2):
  return(argument1 * argument2)

multiply1(4, 5)           

multiply2(4, 5) 


print(type(multiply1(4, 5)))

print(type(multiply2(4, 5)))  

## string ile kullanim

def multiply1(argument1, argument2):
  print(argument1 * argument2)

def multiply2(argument1, argument2):
  return(argument1 * argument2)

multiply1(4, "Kayseri")           
multiply2(4, "Kayseri") 

print(type(multiply1(4, "Kayseri")))
print(type(multiply2(4, "Kayseri")))

def meral(a, b):
  return (a + b)

print(meral(3, 4) + 7)

def meral(a, b):
  print(a + b)

print(meral(3, 4) + 7)

def meral(a, b):
  print(a + b)

print(type(meral(3, 4))) 



def multiply2(argument1, argument2):
  return(argument1 * argument2)



# Ortaya cikan sonuc:

# Yani Kodlamamizin ilerleyen asamalarinda ihtiyaç duyduğumuzda ilk fonksiyonu 

# kullanamiyoruz. Cünkü sonuc olarak bize Nonetype döndürüyor.

# Ancak return kullandigimizda ise , gelecekte ihtiyaç duyduğumuzda kullanabileceğimiz 

# tamsayı, float, string gibi veriler return eder. 

# Peki burada ileride ihtiyac duymaktan kasit nedir. Mesela 

# Bizler internet sitesi kullanicisindan yani user dan input ile veriler aliyoruz.

# Ve hatirlarsaniz input func daima string döndürdügünden biz bu degerleri bazen

# integer a yada float a dönüstürmek zorunda kaliyoruz.

# Ama bizim veri tiplerimiz None type olmus olsa biz bu degerleri 

# Ne toplayabiliriz ne cikarabiliriz. Hicbir islem yapamayiz.

# degiskene Nonetype atama

degisken = print("It can't be assigned to any variable")
print(degisken)

### Dikkat:
# Burada outputlari dikkatle incelersek; ikinci satirdaki kodumuzun outputunun 
# None oldugunu görecegiz. Bunun sebebi sudur: Biz Bir degere veri tipi None olan

# bir deger atayamayiz. Iste print() func. Type i None olan bir veri döndürdügü icin

# biz print()  func in outputunu variable a atayamadik.



##  Not: func cagirirken, tanimlama esnasinda kac adet parameter girildi ise
# ayni sayida argument girilmelidir 

def multiply1(argument1, argument2):   
  print(argument1 * argument2)

def multiply2(argument1, argument2):
  return(argument1 * argument2)

multiply1(4, "Izmir ")          

multiply2(4, "Izmir ") 

a = "Onur"
print(a)  

True  

print()

def carpma(argument1, argument2): 
  print(argument1 * argument2)

carpma(4, "Kayseri")         

## Attention: biz normalde print() yazdigimizda bunun rengini beyaz olarak degil

# sari olarak görürüz. Cünkü bu siradan bir ifade degildir bir functiondir.

# Bu nedenle def yaninda yazili olan carpma ifadesine dikkat edersek 

# onun rengi de saridir.

# biz  carpma kelimesini python a tanitiyoruz ve bu kelime türkce olmasina ragmen

# print kelimesi ile ayni statüye tasiyoruz.

### Attention : Eger bir func tanimlama da birden fazla return var ise 

# sonuc ne olur ??

def multiply2(argument1, argument2):
  print(argument1 + argument2)
  return(argument1 * argument2)       ##  ilk return de calismayi durdurur  
  return(argument1 + argument2)       
  return(argument1 - argument2) 
  print(argument1 + argument2)    
          
print(multiply2(10, 5))





### Peki bu durum print() de nasildir ????

def multiply2(argument1, argument2):
  print(argument1 * argument2)
  print(argument1 + argument2)
  print(argument1 - argument2)
          
multiply2(10, 5)

## Interview Question

# Return etmek(döndürmek) ne demektir?

# Q: What is the return keyword used for in Python?
# The purpose of a function is to receive the inputs and return some output. 

# The return is a Python statement which we can use in a function 

# for sending a value back to its caller.

####                preclass Youtube video 

# Eger kod yazarken bir yada birkac kod satirini birden cok kez

# tekrar ediyorsak o zaman isimizi hizlandirmak ve pratiklestirmek icin

# bu kod blogunu bir fonksiyona atayarak; ona her ihtiyacimiz oldugunda, sadece

# olusturmus oldugumuz bu yeni fonksiyonu cagirabiliriz.

#### Örnek bir kod:

import datetime
 
print("task completed")           
print(datetime.datetime.now()) 
print("merhaba")

                                 
for x in range(0, 10):            
  print(x)                        
                                  
print("task completed")
print(datetime.datetime.now())      #  Not: burada print kisimlarinin tüm kod blokumuzda
print("merhaba")                    # tekrar edildigi simule ediliyor             

def time():
  print("task completed")           
  print(datetime.datetime.now())
  print("hello")         ###  buraya kadar func tanimladik.
                            ## Buradan sonra normal günlük hayattan bir kod blogumuzu
                           #  yaziyoruz olarak hayal  edelim
time()                      ## ve yukaridaki kod ile bu hücredeki kodumuzu kiyas edelim

for x in range(0, 10):            
  print(x)

time()

for x in range(0, 10):            
  print(x)

time()

def time():
  print("task completed")           
  print(datetime.datetime.now())
  print("hello") 
  
time()

for x in range(0, 10):            
  print(x)

time()



## Func kullanmanin bize sagladigi üc fayda:

# 1: kodumuzu daha okunakli yapar

# 2: isimizi pratiklestirir

# 3: biz yazdigimiz kod da bir hata yapmis isek, kendi olusturdugumuz

# func icerisinde degisiklik yaptigimizda bu func'i cagirdigimizda her satirda
# degisiklik otomatik olacaktir.

# Ancak func definition yapmayip da tüm satirlari tek tek el ile yazdiysak

# o zaman tüm satirlarda tek tek degisiklik yapmak zorunda kalacaktik




 # Dikkat :Burada dikkat etmmeiz gereken  husus sudur:

# func adi verirken hem kendimiz anlayacagimiz hem de baskalari anlayacak sekilde

# isim verirsek, kodlamamizin cok ilerleyen satirlarinda unutma 

# yada yazdigimizi anlamama gibi sikintilar ortadan kalkmis olur


# Bir diger husus ise; olusturdugumuz her function dan sonra bunun ne ise

# yaradigini ve nerelerde kullanmak icin olusturdugumuzu aciklamak icin 

# birer comment yada docstring yazmamiz cok iyi olacaktir. 

# docstring yazimini ileride inceleyecegiz 

max()

## Eger datetime i bu sekilde kullanirsak print() satirinda ikinci kez

# datetime prefix i ni kullanmaya ihtiyac duymayiz

from datetime import datetime    #  1: modul   2: fonksiyon

def time():
  print(datetime.now())

time()

# today

from datetime import datetime

def time():
  print(datetime.today())

time()



## Simdi func i nerelerde kullanabilecegimizi daha detayli görelim:

# Bir sirkette calisiyoruz ve bize bir task verildi.

# Kullanicilarin isim ve soyisimlerini al.

# Isim ve soyisimlerinin ilk harflerini bulan kodu yazalim ve bunlari bir

# yerde depolayalim

## Bu bizim normal olarak yazacagimiz bir kod blogudur

first_name = input("Adinizi giriniz ")
kisaltma1 = first_name[0:1]

last_name = input("Adinizi giriniz ")
kisaltma2 = last_name[0:1]

print("Isim ve soyisminizin kisaltmasi: ", kisaltma1 + kisaltma2)

### simdi bu kodumuzu bir func define ederek yapalim:

def kisaltma(name):
  kisa = name[0]
  return(kisa)

isim = input("isminizi giriniz ")
isim_kisaltma = kisaltma(isim)  

soyisim = input("soyadinizi giriniz ")
soyisim_kisaltma = kisaltma(soyisim)

print("isminizin ve soyisminizin kisaltmasi: ", isim_kisaltma + soyisim_kisaltma)

def ahmet():
  girdi = input("Lütfen adinizi giriniz")
  girdi = girdi[0]
  girdi2 = input("lütfen soyisiminizi giriniz")
  girdi2 = girdi2[0]
  return girdi + girdi2

ahmet()   ##  return 



###  Burada dikkatimizi birsey cekmesi gerekir:

# def ile func tanimlarken def in altina direkt print("...")  de diyebiliyoruz

# yada def in altina bir degisken atiyoruz ve bu degiskeni print() et diyebiliyoruz

# mesela yukaridaki örnegi degisken atamadan yapalim

def kisaltma(name):
  return (name[0])       ### burada degisken atamadik direkt return ettik

isim = input("isminizi giriniz ")
isim_kisaltma = kisaltma(isim)  

soyisim = input("soyadinizi giriniz ")
soyisim_kisaltma = kisaltma(soyisim)

print("isminizin ve soyisminizin kisaltmasi: ", isim_kisaltma + soyisim_kisaltma)

### mesela ileride bir tarihte kodumuzun arasinda kisaltmis oldugumuz 

# isim ve soyisim bloklarini büyük harfle yazdirmak istedik.

# Bu durumda sadece kendimiz olusturdugumuz function daki kod da oynama 

# yapmamiz yeterlidir.

#örnegin:

def kisaltma(name):
  kisa = name[0:1].upper()
  return(kisa)      

isim = input("isminizi giriniz: ")
isim_kisaltma = kisaltma(isim)  

soyisim = input("soyadinizi giriniz: ")
soyisim_kisaltma = kisaltma(soyisim)

print("isminizin ve soyisminizin kisaltmasi: ", isim_kisaltma + soyisim_kisaltma)

# olusturmus oldugumuz function i iki türlü kullanma sansina sahibiz

### bu function i direkt olarak print icinde de calistirabiliriz

def kisaltma(name):
  kisa = name[0:1].upper()
  return(kisa)  

isim = input("isminizi giriniz: ") ## burada sadece input aldik yukaridaki gibi
                                    # ismin kisaltmasini degiskene atamadik
soyisim = input("soyadinizi giriniz: ")

print(kisaltma(isim), kisaltma(soyisim)) 

## Yani kullanim asamasinda bizim tanimladigimiz function in 

# python da tanimli functionlardan hicbir farki yoktur.



### check yourself sorulari

# If you generate the output of a function using the print keyword, 
# the result will be a NoneType data. 

# But if you use the return keyword, the result will have a data type.

# When built-in functions are not enough, or when you need to use a block of code 
# in your program repeatedly, you write your own functions. They are called 
# user-defined functions

# If there are more than one keyword return in a function, then the execution of that function 
# will end after the last return. (False)

# dikdörtgen alani hesaplayan bir func yaziniz:

def alan(a, b):   # burada a ve b; kisa ve uzun kenar uzunluklaridir
  return (a * b)

alan(3, 4)

## Önce bir func tanimlayalim. Bu func icerisine liste gibi bir iterable alsin 
# daha sonra bu iterable' in elemanlari arasinda gezinerek en uzun olanini bulsun
# ve en uzun elemani bize print etsin. 

# Daha sonra kullanicidan isimler isteyelim ve bu isimlerden hangisinin
# en uzun oldugunu tanimladigimiz bu func vasitasi ile tespit edelim 

def fonksiyon(x):
  counter = 0
  enuzun = ""
  for i in x:
    if len(i) >= counter:
      counter = len(i)
      enuzun = i
  print("Girdiginiz en uzun isim", enuzun, "ve", counter, "karakterdir")


girdi = list(map(str, input("Lütfen girmek istediginiz isimleri yaziniz: ")))

fonksiyon(girdi)

girdi = list(map(int, input("Lütfen bir sayi giriniz: ").split()))

print(girdi)

girdi = tuple(map(str, input("sayi girin").split()))

print(girdi)



def new(2, 3):  # parametre
  return 2 * 3

new(2, "ahmet") 









girdi = input("Lütfen birden cok sayi giriniz: ").split()
bos = []

for i in girdi:
  bos.append(int(i))

print(bos)



###############       The Matter of Arguments     ###########

## argüman nedir parametre nedir ?
# aslinda cok benzer seylerdir ama aralarinda bir fark vardir
# Örnek ile aciklayalim

def kim(isim, soyisim): ###  Burada isim ve soyisim kim func'nin parametleridir
  print("sizin isminiz ve soyisminiz ", isim, soyisim)
  

kim("Merve", "Kaplan")     ###  Burada merve ve kaplan argümanlardir

# Yani kisaca söylemek gerekirse; func'i tanimlayan kisinin yazdigi degiskenler, parametredir
# func'i kullanan kisinin girdikleri ise argümanlar olur
#  Bu durumu built in func larda da test edebiliriz.
# mesela max() yazip bekledigimizde karsimiza cikan aciklamayi okuyabiliriz 


## Parametreler, func'i tanimlayan kisi tarafindan verilen 
# sadece bir isimden ibarettir. Herhangi bir isim yazilabilir.
# ve parametre isimleri ve sayilari tanimlayici tarafindan
# bir kez belirlendikten sonra artik sabittirler


 # Ancak argümanlar sürekli degisirler. Bizim tanimladigimiz
# fonksiyonu kullanan user, argüman olarak ne girmek isterse
# girebilir

## Dikkat:

# func tanimlayan kisi kac parametre belirledi ise, kullanici o kadar sayida
# argüman girmek zorundadir. Aksi takdir de kodumuz calismaz

# ### pre class soru

# Look at the definition of a function given below.

def who(first, last) :      
  print('Your first name is :', first)
  print('Your last name is :', last)

who('Marry', 'Bold')

# Which of the following statements is incorrect about this function?

# Select one or more:

# 'first' and 'last' are the parameters.
# The first three lines are the function itself, and the 
# last line has been used to call the function.

# This function has one parameter and it takes one argument.

# 'Marry' and 'Bold' are the arguments.



#######   Correct Use of Arguments 

# Bir fonksiyon cagirmada argümanlari kullanmanin 2 farkli yöntemi vardir
# 1: Positional argument(konumsal)
# 2: keyword arguments(kisaltmasi kwarg)

# Aslında, su ana kadar öğrendiğimiz argümanlar konumsal olanlardır. 
# Bu argämanlarda, Argümanların konumu yani kullanim sirasi önemlidir. 
# Eger yerlerinde degisiklik yaparsak yada hatali yazarsak kodumuz calismaz yada
# hatali calisir.

# Konumsal argümanlarla bir fonksiyon çağırırken , bunlar soldan sağa sırayla iletilmelidir .

# Konumsal argümanlara örnek:

def pos_args(a, b):   ##  Burada a ve b konumsal argümanlardir ve yerleri degisir ise
    print(a, 'is the first argument')     # kodumuz farkli bir output verir
    print(b, 'is the second argument')

pos_args(3,4)

pos_args(4,3)

## diger bir örnek:

def pos_args(a, b):   
    print(a, 'is the first argument')     
    print(b, 'is the second argument')
    
pos_args('first','second')  ##  bunlar da positional argümanlardir

pos_args('second', 'first')



#################       Keyword Arguments

# Ne icin ve nasil kullanilirlar?

# Bir işlevi çağırdığımızda argümanların pozisyonlarının 
# bizi kısıtlamasıni istemiyorsak, bu argümanları anahtar kelimelerle 
# çağıririz. Genel olarak ve geleneksel olarak,  kwargs  anahtar kelimesi
#  keyword argümanlarının kısaltması olarak kullanılır 

# su sekilde formüle edilirler

# kwargs = values.

def who(first, last) :          
  print('Your first name is :', first)
  print('Your last name is :', last)

who(first='Guido', last='van Rossum') 

# Burada func cagirirken sadece "Guido" ve "van Rossum" yazmis olsaydik
# kodumuz yine calisacakti.
# Ancak burada keyword argüman kullanmamizin amaci farkli. Asagidaki örnege bakalim

def who(first, last) :            
  print('Your first name is :', first)
  print('Your last name is :', last)

who(last='kilic', first='ali')

# Dikkat edersek burada  kullanici önce soyisim yazdi daha sonra isim.
# Ama output a bakarsak önce isim sonra soyisim görülecektir.

# iste bu durum positional argümanlarda söz konusu degildir. Orada önce ne
# yazilir ise cikti olarak önce o alinir.

## Önemli:

# Positional arguman kullaniminda kullanicinin girmesi gereken argümana;
# required argument denir.


# Keyword argüman kullaniminda ise;
# optional arguments denir.



kus("dokunmak")

# Burada ise kus func cagirmanin cesitli yöntemlerini inceleyegiz

def kus(etki, tüyler='sert', action='cik cik', renk='Norvec mavisi'):
    print("Bu kus", action, "etmedi")
    print("Eger", etki, "yaparsaniz", "kus öter")
    print("Bu kusun rengi", renk)
    print("Ve kusun tüyleri", tüyler)

kus(1000)                                          # 1 positional argument
kus(etki=1000)                                  # 1 keyword argument
kus(etki=1000000, action='VOOOOOM')             # 2 keyword arguments
kus(action='VOOOOOM', etki=1000000)             # 2 keyword arguments  # Dikkat etki ve action yerleri degisti
kus('a million', 'bereft of life', 'jump')         # 3 positional arguments
kus('a thousand', tüyler='pushing up the daisies')  # 1 positional, 1 keyword

# herbirini ayri bir hücrede inceleyelim

def kus(etki, tüyler='sert', action='cik cik', type='Norvec mavisi'):
    print("Bu kus", action, "etmedi")
    print("Eger", etki, "yaparsaniz", "kus öter")
    print("Bu kusun rengi", type)
    print("Ve kusun tüyleri", tüyler)

kus(1000)  ### tek bir positional yazdigimizda etki olur

def kus(etki, tüyler='sert', action='cik cik', type='Norvec mavisi'):
    print("Bu kus", action, "etmedi")
    print("Eger", etki, "yaparsaniz", "kus öter")
    print("Bu kusun rengi", type)
    print("Ve kusun tüyleri", tüyler)


kus(etki="dokunmak")    ### tek bir keyword argüman

def kus(etki, tüyler='sert', action='cik cik', type='Norvec mavisi'):
    print("Bu kus", action, "etmedi")
    print("Eger", etki, "yaparsaniz", "kus öter")
    print("Bu kusun rengi", type)
    print("Ve kusun tüyleri", tüyler)


kus(etki="dokunmak", action='pir pir')   # 2 keyword

def kus(etki, tüyler='sert', action='cik cik', type='Norvec mavisi'):
    print("Bu kus", action, "etmedi")
    print("Eger", etki, "yaparsaniz", "kus öter")
    print("Bu kusun rengi", type)
    print("Ve kusun tüyleri", tüyler)


kus(action='pir pir', etki="dokunmak")  #yukaridakinin aynisi ama yerler degisik
                                        # yerler degisik ama output ayni

def kus(etki, tüyler='sert', action='cik cik', type='Norvec mavisi'):
    print("Bu kus", action, "etmedi")  
    print("Eger", etki, "yaparsaniz", "kus öter")
    print("Bu kusun rengi", type)
    print("Ve kusun tüyleri", tüyler)


kus('dokunmak', 'yumusak', 'pir pir')

#  Dikkat:   Biz burada hic positional arg. kullanmadik sadece keyword kullandik.
# Peki burada python keyword argümanlari nasil siraladi ?

#  1. satirdaki print() 3. siradaki argümani alip print ediyor
#  2. satirdaki print() 1. siradaki argümani alip print ediyor
#  3. satirdaki print() zaten type'i alip print ediyor
#  4. satirdaki print() 2. siradaki argümani alip print ediyor

# Burada asil dikkat etmemiz gereken husus sudur:
# Biz tüm elemanlari string olarak yazdik. Ancak python bunlarin ilkini
# positional argümana atadi. Digerlerini keywordlere atadi.

def ekrem(a, b):     # positional
  return a, b

print(ekrem())
print(ekrem())

def ekrem(a = 3, b = 4):   ## keyword 
  return a, b

print(ekrem(a = 8))

def kus(etki, tüyler='sert', action='cik cik', type='Norvec mavisi'):
    print("Bu kus", action, "etmedi")  
    print("Eger", etki, "yaparsaniz", "kus öter")
    print("Bu kusun rengi", type)
    print("Ve kusun tüyleri", tüyler)

kus('pat pat', tüyler='mor')

#  Dikkat: keyword olarak atadigimiz parametreler icin, func'i cagirirken 
# özellikle atama yapmazsak, output da default olani görürüz.

# Yani biz func' i tanimlarken action = "cik cik" yazdiysak ve
# func'i cagirirken tekrar action tanimlamadi isek bu durumda
# default olan degismeyecektir.

## Bu hücrede bulunan func cagirma yöntemlerinin hepsi yanlistir.

def kus(etki, tüyler='sert', action='cik cik', type='Norvec mavisi'):
    print("Bu kus", action, "etmedi")  
    print("Eger", etki, "yaparsaniz", "kus öter")
    print("Bu kusun rengi", type)
    print("Ve kusun tüyleri", tüyler)


# kus()                     # required argument missing 
#kus(etki = "dokunmak", 'dead')  # non-keyword argument after a keyword argument
# kus("pat pat", etki = "tik tik")     # duplicate value for the same argument
kus(actor = 'John Cleese')  # unknown keyword argument

###  Attention

# In a function call, keyword arguments must follow positional arguments.



###  Special Arguments (Optional)   (Bu konu inclass da yok)

# Resmi ilgili Python belgelerine göre: Varsayılan olarak, argümanlar 
# bir Python fonksiyonuna ya positional olarak ya da keyword ile iletilebilir.


# Okunabilirlik ve performans için, bir developer in öğelerin sadece konuma göre mi, 
# konuma veya anahtar kelimeye göre mi yoksa sadece anahtar kelimeye 
# göre mi iletildiğini belirlemek için yalnızca func tanımına bakması yeterli

# burada / veya  * kullanimi isteğe bağlıdır. Kullanılırsa, bu semboller, 
# argümanların func'a nasıl iletilecegine göre parametre türünü belirtir: 
# 1: yalnızca positional , 
# 2: positional or keyword
# 3: yalnızca keyword 


# Eger kullanilmazlarsa o zaman sadece iki secenek kalmaktadir:
# 1:  sadece positional
# 2:  sadece keyword 


# Not:  Keyword argümanlar, bazi yerlerde "named arguments" yada "named parameters"

# olarak da adlandirilirlar

#  Simdi bu 3 secenegi detayli inceleyelim

#  1:  Positional-Only Arguments

# Yalnızca  konumsalsa , parametrelerin sırası önemlidir ve 
# parametreler anahtar kelimeyle calismaz

# Yalnızca konumsal parametreler bir / (eğik çizgi) önüne yerleştirilir . 
# Yalnızca konumsal parametreleri diğer parametrelerden ayırmak için "/" kullanılır. 
# Eger func tanımında "/" yoksa, yalnızca konumsal parametre yoktur demektir


# "/" egik cizgiyi takip eden parametreler ise positional-or-keyword parametreler
# yada sadece keyword parametreler olabilir

# 2:   Keyword-Only Arguments  

# Parametreleri yalnızca keyword olarak kullanmak için, 
# parametrelerin keyword tarafından iletilmesi gerektiğini belirtmemiz gerekir.
# Peki bu islemi nasil yapariz??


# func()'in sag tarafinda bulunan parantez icerisinde, kullanmak istedigimiz
# keyword-only arguments'larin ilkinin önüne "*"  yerlestirilir

def mix(pos1, pos2, pos_or_kwrd,*, kwrd1, kwrd2):  # burada / kullanimina izin vermiyor
  print(pos1, pos2, pos_or_kwrd, kwrd1, kwrd2)

mix("a", "b", pos_or_kwrd = "c", kwrd1 = "d", kwrd2 = "e")

mix("a", "b", "c", kwrd1 = "d", kwrd2 = "e")  # 3. eleman yazimi farkli olabilir

mix("a", pos2 = "b", pos_or_kwrd = "c", kwrd1 = "d", kwrd2 = "e")  

## pos2'nin degeri keyword ile atanabilir ama pos1 atanamaz. Cünkü positional argümanlar 
# basa alinmak zorundadir. Eger pos1'in degerini keyword ile atamak istiyorsak pos2 de 
# keyword ile atanmalidir.



##########     inclass       ###########

# multiply(2, 3)  #  Burada multiply isim, 2 ve 3 ise argumanlardir

# mesela print("Hello world")  

# burada print func ismi
# Hello world ise argumandir

# Not: her func' in icerisine arguman yazmak zorunda degiliz.
# Icerisine arguman almayan func'larda vardir

# ama cogu func icine arguman alir

def metin():
  print("metin bey")

metin()

#################       built in functions         ##############

# all

# and operatörü gibi calisir
# ismi all oldugu icin herseyin true olmasini ister

# eger bir tane bile False varsa False return eder
# hepsi True ise True verir

# Dikkat: bos eleman da True verir
# False odakli calisir. False bulamadigi zaman bos bile olsa True verir


# Kullanim alani: Cok uzun bir iterable imiz var ve biz bunun icerisinde 
# Falsy bir eleman olup olmadigini ögrenmek istiyoruz

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 16, 17, 18]
b = ["a", "b", ""]
c = {}

print(all(a))
print(all(b))
print(all(c))

d = all([1, 2, 3, 4])   # Bu sekilde degiskene atayarak da kullanilabilir 
print(d)

# all() func iterable lar ile kullanilir.
# Eger sadece tek bir elemanin falsy mi truthy mi oldugunu ögrenmek 
# istiyorsak o zaman bool() da kullanabiliriz all()  da

# a = 1

# print(all(a)) #  Burada output ne olur???


b = [1]
print(all(b))   #  Output lar nedir?


c = []
print(all(c))

d = set()
print(all(d))

# any

# any() func ise or gibi calisir. Eger bir tane bile True varsa
# True döndürür. Hepsi False ise False döndürür

# Dikkat:  bos iterable da ise False döndürür

a = ["a", "n", ""]
b = [None, "", 0]
c = set()

print(any(a))
print(any(b))
print(any(c))

listA = ["susan", "tom", False]
listB = [None, (), 0]
empty = {}               

print(any(listA))
print(any(listB))
print(any(empty))



# callable(object)

# filter(function, iterable)

# Filter func icerisine bir func bir tane de iterable alir.

# Buradaki func'i kendimiz de yapabiliriz yada built in func da kullanabiliriz

# filter,  icerisine aldigi func'i iterable'in tüm elemanlarina uygular ve 
# sonrasinda True yada False döndürür. Dolayisi ile bize filter icerisinde 
# kullanmak icin True yada False döndürecek bir func lazimdir.


# Bu func icerisine aldigi iterable'i yine icerisine aldigi func ile filtreden gecirir.

# filter da ketum bir func' dir ve ayni zip gibi range gibi acmak icin birkac yola 
# ihtiyac duyar

# eger biz filter func icerisine bir func degil de sadece None yazarsak
# Bu durumda sadece Truety leri gecirir ve herhangi bir func'a ihtiyac duymaz.

# Yani buradan cikan sonuc sudur:

# filter()  iki sekilde kullanilabilir. 

# Birincisi filter(func(), iterable)

# ikincisi filter(None, iterable)

a = [1, 2, 3, 4, 5, 6, 0, None, False]
b = list(filter(None, a))

print("Filtrelenmis elemanlar sunlardir: ", b)

# for döngüsü ile kullanim:

a = [1, 2, 3, 4, 5, 6, 0, None, False]
b = list(filter(None, a))

for i in b:
  print(i, end = " ")
print(type(i))

# Önemli:  all() func da filter()  gibi True yada False döndürür. 
# Ancak arada büyük bir fark vardir.

# all() icerisine bir iterable alir ve bu iterable' in tüm elemanlarina bakar,
# eger bir tane bile Falsy varsa False döndürür. Yani sonuc True yada False' dur.

# Ancak filter da ise yine iterable'in tüm elemanlari süzgecten gecirilir. Ancak,
# sonuc olarak elemanlarin kendisi döndürülür. Yani filter, output olarak;
# Truthy degerlerden olusan bir iterable döndürür.

a = [1, 2, 3, 4, 5, 6, 0]
print(any(a))



## filter func'in bir fonksiyon ile kullanimi

def cift(iterable):       ## Burada cift sayilari bulan bir func tanimliyoruz
  c = []
  for i in iterable:
    if int(i) % 2 == 0:
      c.append(i)
  return c

a = ["1", "2", "3", "0"]

d = list(filter(cift, a))       ## Burada ise listeyi filtreden geciriyoruz

print(d)                      



# enumerate()

# icerisine iterable alir ve ana yapisi su sekildedir.

# enumerate(iterable, start)

# start' in defaultu 0 dir ama biz bunu degistirebiliriz. Start'a kac yazarsak
# o numaradan baslar ve artarak gider 

# bu func da zip()  gibi ketumdur. output olarak bir enumerate object döndürür.
# Bu nedenle biz bu func'i acmak zorunda kaliriz.

# Her bir eleman ile sayi eslestirmesi yapar ve bu ciftlerin herbirini
# bir tuple'a dönüstürür.

liste = ["a", "b", "c", "d"]
new = enumerate(liste, 1)
print(new)       

new2 = list(enumerate(liste, 1))
print(new2)
print(type(new2[0])) 

#  enumerate func() ciftler olusturarark tuple meydana getirdigi icin,
# dict func ile kullanima cok uygundur.

liste = ["a", "b", "c", "d"]
new = enumerate(liste, 1)
print(new)        

new2 = dict(enumerate(liste, 1))
print(new2)



# max()   

# icerisine hem iterable alarak calisir hem de iterable almadan birden cok argument
# alarak calisir.

liste = [1, 2, 3, 4, 5]    #  iterable ile kullanim
print(max(liste))

print(max(1, 2, 3, 4, 5))   # birden cok arguman ile kullanim

# output nedir ???

liste1 = [1, 2, 3, 4, 5]
liste2 = [6, 7, 8, 9, 10]
liste3 = [11, 12, 13, 14, 15]

print(max(liste1, liste2, liste3))  



# stringlerden olusan bir iterable' da max() func hareket tarzi:

liste = ["a"]
liste2 = ["a", "b"]
liste3 = ["a", "b", "c"]

print(max(liste, liste2, liste3))

#  max()  func eger bos bir iterable ile calistirilirsa ne döndürür ? 

a = []
print(a)

## output ???

a = max("ahmet AHMET 12345")
print(a)

# Kullanicidan bir cümle alalim ve bunun en uzun kelimesini yazdiralim
# tarzinda sorularda max func() kullanabiliriz.

girdi = input("Lütfen bir cümle giriniz: ").split()
bos = []
for i in girdi:
  bos.append(len(i))
  enuzun = max(bos)
  enkisa = min(bos)

print(enuzun)
print(enkisa)

# min

# max()  icin gecerli olan tüm özellikler min icin de gecerlidir. Sadece max'dan 
# farkli olarak en kücükleri return eder 

# sum 

# bu func() sayilar ile calisir. sayi disindaki veri tiplerini reddeder.
# Dikkat: max ve min de sayilar ile calisir ama string gibi 
# diger veri tipleri ile de calistirilabilir.

# ana yapi su sekilde kurulur:
# sum(iterable, start)

# eger start bos birakilir ise toplamaya default olarak 0 dan baslar. Start yazilir ise
# start degerinden baslar.

#  Eger bu func ile bos bir iterable kullanilir ise bu durumda
# start degeri döndürülür

a = [1, 4, 6, 7, 9, 10]

print(sum(a))

print(sum(a, 10))



## Bu func'i nerelerde kullanabiliriz? 

# mesela bir sirketin finans departmanin da calisiyoruz ve sirketin aylik 
# kazanclarini ciro ve giderler olarak ayri ayri listelerde tutuyoruz.
# yil sonunda tüm yilin kar, ciro ve masraf miktarini hesaplayabiliriz 

aylikciro = [10000, 12000, 20000, 50000, 100000]
aylikmaliyet = [5000, 6000, 10000, 25000, 50000]

topciro = sum(aylikciro)
topmaliyet = sum(aylikmaliyet)

print(topciro)
print(topmaliyet)

# aylik kar hesaplama(her bir ayin cirosundan o ayin maliyetini cikaracagiz)

aylikkar = []

for i, j in zip(aylikciro, aylikmaliyet):
  kar = i -j
  aylikkar.append(kar)
print(aylikkar)

## simdi de toplam yillik kari hesaplayalim

toplamkar = sum(aylikkar)  # yada
toplamkar2 = topciro - topmaliyet

print(toplamkar)
print(toplamkar2)
# bos iterable ile sum()

a = []
print(sum(a))           # output?

print(sum(a, 10))       # output?

# sum() func icerisine direkt olarak bir iterable da yazilabilir
# ancak sadece tek bir iterable alir

print(sum([10000, 12000, 20000, 50000, 100000]))

print(sum(1, 2, 3, 4, 5))    # output?

## herhangi bir func() ' a ait parantez icerisinde yazdigimiz ve virgüller ile
# ayrilmis her bir deger bir argümandir


# max ile sum arasindaki en büyük fark sudur:
# sum tek bir iterable alirken
# max hem tek bir iterable alir , hem de birden fazla deger alabilir 

print(max(1, 2, 3, 4, 5))
# print(sum(1, 2, 3, 4, 5)) # error



############  round()  func

# sayilarda yuvarlama islevi görür
# ana yapi su sekildedir:

# round(number, ndigits=None)  # virgülden sonra basamak kismi default olarak None dir.

print(round(12))
print(round(12, 2))                   ##   outputlar nasildir?
print(round(10.8))
print(round(10.8, 5))
print(round(3.665, 2))
print(round(3.675, 2))
print(round(3.123456789, 5))

# Not: rakamlar binary sistem üzerinden calistigi icin float rakamlarda
# pc den pc ye farkliliklar görülebilir
# mesela 3.675'in orjinal hali 3.6746570565065095640956495645444   seklindedir
# Bu nedenle bakildiginda 3. 675 yani yukaridaki degere yuvarlanir gibi 
# görünseler de bu sayilar round func icerisine girdiginde asagiya yuvarlanir

# The behavior of round() for floats can be surprising: 
# for example, round(2.675, 2) gives 2.67 instead of the 
# expected 2.68. This is not a bug: it’s a result of the 
# fact that most decimal fractions can’t be represented exactly as a float

# map

# eval

# sorted(iterable)

# open()  dosya veya herhangi birsey acma kapamaya yarar

# dir([object])    icerik listeler

# help(object)  

### hatirlatma:

# eger sayilardan olusan bir listeye ihtiyac duyarsak 
# range func(),  collection type larin func() lari ile kombineli olarak kullanilabilir
# ve bunun icerisinde detayli slayslama yada indexleme yapilabilir

# mesela 5 den 20 ye kadar olan tek sayilar yada cift sayilar
# Bu durumlarda, bazen döngüleri kullanmadan da islerimizi yapabiliriz

a = list(range(5, 20, 2))
b = tuple(range(6, 20, 2))

print(a)
print(b)



##################  defining a function


# bir func olustururken ana yapimiz su sekildedir:

def functionname(parameter(s)):  ##  bu iki satirda yaptigimiz isleme defining a func denir
  execution body         

# python da bu yapi evrenseldir. for, while  ve if yapilarin da da aynidir

#  python orjinal dökümanlarinda bile argüment ile parametre bazi yerlerde 
# birbirlerinin yerine kullanilirlar
# ama temelde bir fark vardir:

# func() tanimlanirken kullandigimiz degiskenlere parametre denir
# ancak func() cagirirken kullandigimiz degiskenlere argüman denir
# yani bu durumda yapimiz su sekilde olur

def functionname(parameter1, parameter2):
  print(parameter1 * parameter2)

functionname(argument1, argument2)  

# hipotenüs hesaplayan bir func tanimlayalim

def hipotenüs(a, b):   # bunlar parametre
  print("Hipotenüs = ", (a ** 2 + b ** 2) ** 0.5)

hipotenüs(3, 4)      ##  argümanlar

def carpma(a, b):
  print(a * b)

carpma("computer ", 5)

##  Dikkat: Burada aslinda bir assigning islemi vardir.
# Yani a yerine "computer", b yerine de 5 assign edildi

## her fonksiyonun parametresi olmak zorunda degildir

def slogan():
  print("Kendini kesfetmekten korkma")

slogan()

# Bu tarz func' lari split(), sort(). pop() methodlari gibi düsünebiliriz.
# Bu tarz func'larin yada methodlarin icerisinde daha önce tanimlanmis islemler vardir.

# Biz parantez icerisine hicbir sey yazmamamiza ragmen o kendinde default
# olarak tanimlanmis islemi yapar.

# örnegin:

liste = [1, 2, 3, 4, 5]
liste.pop()

print(liste)

def toplama(a, b, c):
  print(a + b + c)

toplama("4", "4", "4")

# basit bir hesap makinesini func olarak tanimlama:
# 3 parametre alacagiz. Bunlardan ilk 2 tanesi sayi 3. ise yapilacak islemdir

def hesap(a, b, c):
  if c == "+":
    print(a + b)
  elif c == "-":
    print(a - b)
  elif c == "/":
    print(a / b)
  elif c == "*":
    print(a * b)
  else:
    print("Gecersiz bir deger girdiniz")

hesap(10, 2, "+")
hesap(10, 2, "-")
hesap(10, 2, "/")
hesap(10, 2, "*")
hesap(10, 2, "**")



#################   Execution of a function     ###############

# print ve return farkli seylerdir.

# Dikkat edersek Bizim kullandigimiz bütün built in func' lar bir sonuc döndürür.
# Ancak biz bu sonucu print etmedigimiz takdirde herhangi bir sonuc alamayiz.

# örnegin:

liste = [10, 5, 9, 2, 0, 8]

sorted(liste)    ## Burada aldigimiz sonuc colab' in kendi özelligidir. Aslinda
                  # normal bir python kod yaziminda biz bu sekilde bir kod yazdigimizda
                  # hicbir sonuc alamayiz.

                  # Peki Burada sorted func() bize ne döndürdü?
                  # Bize listemizin kücükten büyüge dogru siralanmis halini döndürdü

liste = [10, 5, 9, 2, 0, 8]
max(liste)          # # ayni sekilde max func() bize listemizin en büyük elemanini döndürdü

                    # yani buradan su cikmaktadir. print() haricinde hicbir
                    # built in func() 'in print etme özelligi yoktur.
                    # func lar bir deger döndürür biz de görmek istedigimiz degeri print ederiz        

# simdi ise return islemini kendimiz define ettigimiz bir func()  da görelim

def carpma(a, b, c):
  return a * b * c

## burada func' i cagirmadigimiz sürece herhangi bir sonuc alamayiz

# return ve print kullandigimizda veri tipleri de farkli olacaktir.

def carpma(a, b, c):
  return a * b * c

print(type(carpma(2, 4, 5)))

def carpma(a, b, c):
  print(a * b * c)

print(type(carpma(2, 4, 5)))

## Bunun sebebi sudur:
# Biz bir func defining yaparken print kullanirsak,ve daha sonra bunu
# print func ile print etmek istersek,  ayni asagida oldugu gibi
# print icerisinde print kullanmis oluruz.

# Bu durumda da type imiz none type olur

a = [1, 2, 3]
print(type(print(a)))

## Dikkat:  Nasil ki bir degiskeni print ettigimizde o degiskenin kendisi degil
# valuesu print ediliyorsa, ayni sekilde bir fonksiyonu cagirdigimizda da 
# o fonksiyonun karsiligi olan deger print edilir. Örnegin:

a = 1234
print(a)  #  degisken value iliskisi

def a():
  return 1234

a()   # Dikkat edersek burada print ettirmedik, buna ragmen a'yi cagirdigimizda 1234 geldi

##  fonksiyonlarin bu özelligini her yerde kullanabiliriz:

def a():
  return True         ## True döndüren bir func yazdik

if a():                  # burada a func() bize True döndürür. Bu nedenle if calisir
  print("ali")          


# matematiksel olarak baktigimizda a() = "ali"  diyebiliriz

## diger bir örnek:

listem = [1, 2, 3, 4, 5]
print(listem)


def listem():
  return [1, 2, 3, 4, 5]

# artik listem func() 'i cagirdigimizda bize liste gelecektir. Dolayisi ile
# biz bu listeyi artik her yerde kullanabiliriz. Mesela for döngüsünde:

for i in listem():        ##  dikkat: () unutmuyoruz
  print(i)
                          ## buradaki listem isimli func bir iterable' a esittir 

#  listeden tuple'a cevirme islemlerini ayni sekilde func ' da da yapabiliirz

listem = [1, 2, 3, 4, 5]   ## normal islem

tuplem = tuple(listem)
print(tuplem)


def listem():
  return [1, 2, 3, 4, 5]

new = tuple(listem())     ### dikkat ()
print(new)

##  Bu func bir liste oldugu icin, bunun üzerinde indexleme slayslama da 
# yapabiliriz:

def listem():
  return [1, 2, 3, 4, 5]

print(listem()[2])   ##  Dikkat () unutmayalim

print(listem()[::-1])

print(listem()[1:4])

#  append gibi methodlar calisir mi peki?

def listem():
  return [5, 4, 3, 2, 1]

listem().append(6)
print(listem())      ## output nedir

print(sorted(listem()))   ## output nedir

listem().insert(1,8)     ## output nedir?
print(listem())



## hesap makinesini return ile yapalim:

def hesap2(a, b, c):
  if c == "+":
    return (a + b)
  elif c == "-":
    return (a - b)
  elif c == "/":
    return (a / b)
  elif c == "*":
    return (a * b)
  else:
    return "Gecersiz bir deger girdiniz"

hesap2(10, 2, "+")
hesap2(10, 2, "-")
hesap2(10, 2, "/")
hesap2(10, 2, "*")
hesap2(10, 2, "**")

# Dikkat: Bu kodu yukarida print ile olusturdugumuzda, alt alta her cagirdigimizda
# hepsinden de output almistik. Ama burada return ile yaptigimizda sadece
# en son satirin outputunu verdi. Bunun sebebi sudur:

# bizim bu fonksiyonu her cagirdigimizda bunu print etmemiz gerekir.
# biz ise burada print etmedigimiz icin colab in özelligi geregi sadece son
# satir  print edildi

# yani sonuc olarak sunu söyleyebiliriz. print ile return farkli seylerdir.
# print sadece output'u ekrana yazdirir. return ise func icerisinde kullandigimiz
# degeri func' in kendisine esitler

## burada da en alt satirda print kullanalim
# output ne olur ??

def hesap2(a, b, c):
  if c == "+":
    return (a + b)
  elif c == "-":
    return (a - b)
  elif c == "/":
    return (a / b)
  elif c == "*":
    return (a * b)
  else:
    return "Gecersiz bir deger girdiniz"

hesap2(10, 2, "+")
hesap2(10, 2, "-")
hesap2(10, 2, "/")
hesap2(10, 2, "*")
hesap2(10, 2, "**")

print(hesap2(10, 2, "*"))  

# derste yaptigimiz kahoot

count = 0   ## output nedir?

for i in ["bus"]:
  count += 1
  print(i, count, end = "")

## Kullanicinin girdigi sayinin absolute degerini yazdiran bir func yazalim:

def absolute(a):
  if a < 0:
    return -a
  else:
    return a

girdi = int(input("Lütfen bir sayi giriniz: "))

absolute(girdi)

# Bizim yazmis oldugumuz bu kod ile ayni vazifeyi yapan birde abs()
# func vardir. Bu func built in func dir ve kullanima hazirdir.

# calisma prensibi su sekildedir:

# abs(argument)

# Dikkat:  abs()  func sadece tek bir argüman alir. daha fazla almaz


# simdi bununla ilgili birkac örnek yapalim:

mutlak = abs(-3)      # output?

print(mutlak)

mutlak = abs("ali")      # output?

print(mutlak)

mutlak = abs(-2.6)      # output?

print(mutlak)

mutlak = abs(0)
print(mutlak)

##  simdi de matematiksel olarak bir mutlak deger sorusu cözelim:

## |6 – 2| + |2 – 5| – |1 + 4| = ?   ##  output nedir ?

a = 6 -2
b = 2 - 5
c = 1 + 4

print(abs(a) + abs(b) - abs(c))

####  fonksiyonlarda docstring yazimi:

# docstring ne demektir ?

# bu isim document dan gelmektedir ve bir func' a ait olan dökümantasyonu icerir

# fonksiyonun ilk satirindan hemen sonra yazilir.

# peki bir func' a ait olan docstring nasil okunur ? 

# functionname.__doc__   yazarak görüntüleyebiliriz

def absolute(a):
  "Bu fonksiyon girilen sayinin mutlak degerini return eder"

  if a < 0:
    return -a
  else:
    return a

girdi = int(input("Lütfen bir sayi giriniz: "))
absolute(girdi)

print(absolute.__doc__)

               ##  Dikkat: Bizim yazmis oldugumuz user defined func'lar artik
                # python tarafindan taninmis demektir. Ve bu nedenle colab'in de 
                # özelligi olarak funcname yazip () parantez acip bekledigimizde
                # docstring cikar
# absolute()

## simdi de abs func orjinal docstringini okuyalim

print(abs.__doc__)    ## dikkat buraya sadece doc yaziyoruz. docstring degil

###  tuple lar ile list comprehension yapabilir miyiz ??

generate = (i ** 2 for i in range(6))   ## output nedir ?

print(generate)         #vvvvvvvv

# tuple ile list comprehension yaptigimizda bu bize bir generator object döndürür
# Bu durumda Bizim output'u aciga cikarmamiz lazim: 

generate = (i ** 2 for i in range(6))

print(*generate)

print(list(generate))   ##  peki burada output nedir?

## simdi de for döngüleri icerisinde bulunan ve arka planda calisan 
# next func' i inceleyelim:

generate = (i ** 2 for i in range(6))

print(next(generate))   ## dikkat normal de bizim comprehension' imiz liste icinde 
                        # degil. tuple icerisinde. Yani normal de bir output vermiyor
                        # bunun yerine bir generator object döndürüyor.

                        # ama next func for döngüsü gibi calistigi icin bu generator
                        # objecti aciga cikariyor ve her seferinde bir eleman return ediyor

print(next(generate))
print(next(generate))
print(next(generate))   

#####  Attention Attention:  

# next func bizim sahip oldugumuz generator object gibi on the air object lerde 
# calisir. Yani bizim print edemedigimiz ve * gibi list gibi etkilerle
# aciga cikardigimiz object lerde islem görür

# Eger biz next func'i normal liste yada tuple larda kullanmak istersek hata aliriz

# eger next() yazip beklersek colab bize next hakkinda detayli bilgi verecektir
# Bu bilgiler arasinda, next' in bir iterable degil iterator aldigi bilgisi bulunur
# iterable ile iterator farkli seylerdir. iterator dedigimiz bir generator dir


tuplem = (1,2,3, 4, 5)
print(next(tuplem))  ### yada


liste = [1,2,3, 4, 5]
print(next(liste))

#  next func'i kapali bir object üreten tüm func'lar da kullanabiliriz

tuplem = (1, 2)
liste = ["ali", "veli"]

zipp = zip(tuplem, liste)

print(next(zipp))
print(next(zipp))
#print(next(zipp))  # bu satirdaki next calisirsa output ne olur ?




## Not:

# for loop, * asteriks ve list gibi collection func'lar outputlari
# bir cirpida topluca verir. Ama next func tek tek verir

generate = (i ** 2 for i in range(10))

print(next(generate))
print(next(generate))
print(next(generate))

print(*generate)  ## bu satirdaki kodun ciktisi ne olur ?  



text= "Clarusway"
count = 0

for i in text : 
  count += 1
  if count < len(text) :
    i += "-" 
  print(i, end = "")

liste = [(1, 2, 3), (3, 4, 5)]

for i, j, k in liste:
  print(i, j, k)

numara = int(input(""))

for i in range(0,10):
  print("{}x{} = " .format(numara, i), numara * i)

text = ["1", "2", "3", "4"]
number = {1, 2, 3, 4}

for x, y in zip(text, number):
  print(x, y)