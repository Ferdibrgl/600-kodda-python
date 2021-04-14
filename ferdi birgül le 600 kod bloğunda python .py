""""PYTHON"""

                                     # print kullanımı
"""

print("merhaba dünya")

print("ferdi",919,"birgül")          # str int birlikte

print("Ferdi \nBirgül")               # alt alta yazdırır

print("03","06","2001",sep = "/")      # boşluksuz olur ve slaş işareti terleştirir virgüllü yerlere

print("{} + {} = {}".format(2,3,2 + 3))  # .format= boşluklara istenilen  değerleri yazdırır

"""
"""
                    # VERİ
                    
a = 2                                                        # int
b = 2.5                                         # float
c = "python"                             #str
d = [1,2,3,4,5,"python"]                             # liste
e ={"elma":4,"armut":5,"çilek":6}                                   # dict
f = (1,2,3,4,5,6 ,"ferdi")                                                          # tuple
g =True                                                # doğrumu yanlısmı true false    deger

print(type(a))
print(type(b))
print(type(c))
print(type(d))                 # bool hangi veri gurubundaysa onu belirtir type
print(type(e))
print(type(f))
print(type(g))

print(a,b,c)

"""

                                      #  matematiksel  operatörler


"""

print(2 * 5)                   # çarpım
print(1 + 4)         # topla
print(9 // 3)              # tam bölüm
print(65425 % 22)                         # mod
print(5485 ** 25448)       # üs
print(25 / 2)                                   # bölüm
print(58 - 25)                 # eksi
print(22  ** 7 + 25 * 2 % 8 // 9)

a = 2
b = 3

print(a * b + a % b ** a // b)

"""


"""
# str matematik
a = " ferdi "
b = " birgül "
c = " python"

d= (a + b + c)
print(d)
print(a * 5 )
"""



                                           # yıldız str

"""
print("*" * 1)
print("*" * 2)
print("*" * 3)
print("*" * 4)
print("*" * 5)
print("*" * 6)
print("*" * 7)
print("*" * 8)
print("*" * 9)

"""

                                     # indeks

"""
a = "python"
b = [1,2,3,4,5,6,7]

print(a[0])            # 0. indeks

print(a[2])            # 2. indeks

print(len(a))                           # len demek kaç tane karekter oldğunu belirtir


print(len(b))

print(a[4])                 # sonuncu indeksi verir

print(len(a)-1)                           # cok uzunsa veri bu işlem ideal

print(len(b)-1)

print(a[0:2])
print(a[2:5])                # istenilen aralık
print(a[2:])                                        # 2 den başla sona kadar git

print(a[ :4])        # baştan başla 4 e kadar

print(b[2 : 5])

print(b[0:6:2])   # 0 dan 6 ya 2 şer git
print(b[::2])    # aynı şey farkı yok

"""

                             # sözlük

"""

a={"elma":4,"kiraz":5, "çilek":6}
print(a["elma"])
print(a["çilek"])
print(a["kiraz"])


"""



                    # İNPUT
"""


yas = input("yaşınızı giriniz")
print("yaşınız",yas)
print("---------------")


a =input("a:")
b =input("b:")                     # yan yana yazdırır değerleri toplamaz
c =input("c:")

print("toplam",a+b+c)



a =int(input ("a:"))
b =int(input("b:"))
c =int(input("c:"))              # toplar değerleri

print("toplam",a+b+c)

"""


                                    #  İF ELİF ELSE


""" 
yas = int(input("yaşınızı giriniz"))

if yas < 18:
    print("yaşınız çok küçük")
    print("mekana giremessiniz")
else:
    print("hoş geldiniz")
    print("----------")


islem =int(input("işlem giriniz"))                  # if koşul demek
if islem == 1:
    print("işlem 1 i seçtiniz")                                         # elif yardımcı ve ikinci koşul  demek
elif islem == 2:
    print("işlem 2 yi seçtiniz")
elif islem == 3:
    print("işlem 3 ü seçtiniz")
else:
    print("işlem seçmediniz")                        # else if çalışmassa çalışır


"""




                                         # and / or / not operatörü

"""

a = 4

b = 5

if a == 4 and b == 6:                     # a 4 olsun b 6 olsun birden çok koşul hayır diyecek çünkü b = 5

    print("evet")

else:

    print("hayır")

                                  # or  operatörü

a = 4

b = 5
if a == 4 or b == 5:
    print("evet")                        # en az 1 true yeterli and operatörü tersi

else:

    print("hayır")


if (not (3 < 5)):
    print("evet")

                                #true ise false yapar yanlışı doğru olarak gösterir
    
if (not (3 == 5)):
    print("evet")

"""



                                  # DÖNGÜLER

"""
# while

i = 0

while i < 10:

    print(" i :",i)                             #1 den 10 kadar döngü devam eder artı 1 ile

    i = i + 1


i = 0

while i < 10:
                                              # aynı anlama gelir ( += )ifadesi
    print(" i :",i)

    i +=  1

i = 1

while i < 1000:
    print("i:", i)                # bir öncekinin iki katı devam ediyoruz

    i *= 2
""" # while


"""
# break 

i = 0

while (i < 10):
    if i == 5:
        break

    print("i:",i)             # döngüyü sonlandırır break
    i = i + 1

""" # break

"""
i = 0

while (i < 10):

    if i == 5 or i == 3:
        continue                            # imleç sürekli yanıp sönücek çünkü 0 la 3 arasında gidip geliyor dikkat !

    print("i:",i)
    i += 1

"""

"""
# continue

i = 0

while (i < 10):

    if i == 5 or i == 3:
        i += 1
        continue                    # birer sayı artacağı için şimdi doğru çalışacak


    print("i:",i)
    i += 1

"""   # countinue

            #for döngüsü
"""

a = [1,2,3,4,5,6]
for i in a:                       # listedekileri sırasıyla yazar
    print(i)

"""


"""
a = [1,2,3,4,5,6]
b = "python"
for karekter in b:                       # listedekileri sırasıyla yazar
    print(karekter)

"""

                      # range

"""                   
                      
for i in  range(0 , 100):                  # 0 dan 100 e kadar yazdırır 100 dahil değil
    print(i)
    
"""


"""

for i in  range(0 , 100, 2 ):              # 2 şer 2şer artırır
    print(i)

"""



                                                       # FONKSİYONLAR


"""
def seslen():
    print("merhaba")            # belli parametre istenir ve output alınır
    print("nasılsın ?")
seslen()


"""
"""
def seslen(ad):
    print("merhaba",ad)             # input

seslen("ferdi")


"""

"""

def toplam(a ,b , c):
    print("tolam",a+b+c)           # değerler verdik ve karşılık istedik a = 3 b= 4 C = 8
    
toplam(3,4,8)


"""

"""
def toplam(a, b, c):
    print("toplam", a + b + c)  #


a = toplam(3, 4, 8)             # output alamadığımız için none yani hiçbirşey anlamına gelir
print(a)


"""

""" 
#return

def toplam(a, b, c):
    return a + b + c

sonuç = toplam(3, 4, 8)             # output olmasını istersek return kullanırız none olmaması için
print(sonuç)


"""


                                     #liste ve str metotları

"""
liste= [1,2,3,4,5,6]

a = "ferdi"

print(a.startswith("a"))                         # a değişkeni ilk harfi a mı dedik false der çünkü ilk harf f

"""

"""

liste= [1,2,3,4,5,6]

a = "asena"

print(a.startswith("a"))                         # a değişkeni ilk harfi a olduğu için  true dedi


"""

"""

liste= [1,2,3,4,5,6]

a = "asena"

print(a.endswith ("a"))                  # son harfi a ile mi bitiyor dedik ve true dedi 


"""

"""

liste= [1,2,3,4,5,6]

a = "ankara"

a = (a.replace ("a" , "o"))            # a ları o ya çevir dedik   yani karekter değişimi

print(a)

"""
"""
liste= [1,2,3,4,5,6]

liste.append("python")                 # python str sini listeye ekledik yani listeye ekleme yapan fomksiyon

print(liste)

"""
"""

liste= [1,2,3,4,5,6]

liste.pop()               # listedeki son  alanı temizler  örnek 6 gibi

print(liste)

"""
"""

liste= [1,2,3,4,5,6]

liste.pop(0)                     # 0. indeksi bize temizler

print(liste)


"""


                                          # dosya işlemleri

"""


file = open("dosya.tex","w")              # dosya açar            # w dosya kipi w ile dosya açılır anlamına gelir

file.write("naber ferdi")            # dosya içi yazdırma

file.close()                   # dosya sonlandırma

"""

"""

file = open("dosya.tex","a")             #**   ( a ) tek dosyada naber ferdinin yanına naber esra yazdırır a kipi çoklu yazdırma anlamına geir.


file.write( "naber esra")

file.close()

"""

"""

file = open("dosya.tex","a")

file.write( "naber esra\n")
file.write("naber ferdi\n")                      # alt alta yazdırır.
file.write("naber python\n")

file.close()

"""

"""

file = open("dosya.tex","r")

tahmin = file.read()                    # dosya okuma     # text  te değil run bloğunda gözükür dosya

                                # file.read()  parantez içine değer verilirse o kadarını işleme alır örnek 10 yazılsa parantez içine sadece 10 tane değer alır         
print(tahmin)

"""

"""

file = open("dosya.tex","r")

file.seek(10)                           # sadece 10 değeri alınır yani 10. karektere gelir ve 10 tane karekter alır

tahmin = file.read(10)

print(tahmin)

"""

"""

file = open("dosya.tex","r")
                                         # for döngüsüyle dosyamızı yzdık daha basit bir şekilde 
for tahmin in file:
    
    print(tahmin)

"""


                                   # NESNE YÖNELİMLİ PROGRAMLAMA


"""
class Account :
    def __init__(self,isim,numara,bakiye):             # init fonksiyonuyla objenin hangi özellike olacağına karar verilir

        self.isim = isim
        
        self.numara = numara            # sırasıyla listeledik
        
        self.bakiye = bakiye

    def hesapBilgileri(self):                     # hesap bilgileri girdik


        print("isim :",self.isim)
        print("numara : ",self.numara)            # self karşılığına gelecek olan str seçtik
        print("bakiye : ", self.bakiye)
        
    def paraCek(self,miktar):                         # para çekmesini istedik
        
        if ( self.bakiye - miktar < 0 ):              # bakiye yetersizse bakiyeniz yetersiz dönütü olacaz 
            
            print("bakiyeniz yeterli değil...!")
            
        else:
            self.bakiye -= miktar
            print("yeni bakiye",self.bakiye)               #  yeterli bakiye olup olmadığını değerlendirdik 
            
    def paraYatır(self,miktar):
        
        self.bakiye += miktar          # bakiyemizde fazlalık olmasını istedik += ifadesiyle
        
        print("yeni bakiye :",self.bakiye)         # yeni bakiyemiz aktif oldu
        



account = Account("ferdi birgül",123456,2586)        # self e karşılık gelecek veriler

account.hesapBilgileri()    # hesap bilgilerini istedik

account.paraCek(12000)        # para çekmek istedik

account.hesapBilgileri()       #güncel hesap bakiyesi

account.paraYatır(200)         # bakiyemize ekleme yaptık



"""

  # NOT ( """ ) İFADELERİNİ SIRASIYLA KAPATMANINIZI ÖNERİRİM


                                     # FERDİ BİRGÜL'LE 610 KODTA PYTHON