def Topla(x, y):
     return x + y

def Cikar(x, y):
     return x - y

def Bol(x, y):
     return x / y
def Carp(x, y):
     return x * y
print("Yapılacak İşlemi Seçiniz: ")
print("+-/+-/+-/+-/+-/+-/+-/+-/+-/")
print("1. Toplama")
print("2. Çıkarma")
print("3. Bölme")
print("4. Çarpma")

secim = input("Seçimiz(1/2/3/4) : ")
sayi1 = int(input("1. Sayı: "))
sayi2 = int(input("2. Sayı: "))
if secim == '1':
   print(sayi1,"+",sayi2,"=", Topla(sayi1,sayi2))

elif secim == '2':
   print(sayi1,"-",sayi2,"=", Cikar(sayi1,sayi2))

elif secim == '3':
   print(sayi1,"/",sayi2,"=", Bol(sayi1,sayi2))

elif secim == '4':
    print(sayi1,"x",sayi2,"=", Carp(sayi1,sayi2))


else:
   print("Geçersiz Giriş")

