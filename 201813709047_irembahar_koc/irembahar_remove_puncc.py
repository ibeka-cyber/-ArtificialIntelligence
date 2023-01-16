import csv
#üzerinde işlem yapılacak dosyayı pythona tanıtıyoruz
filename = "irembahar_just_news.csv" 

#Gereksiz karakterleri csv dosyası içerisindeki verilerden kaldırıyoruz
def remove_punc(string):
    punc = ''' !()-[]{};:'"\, <>./?@#$%^&*_~ '''

#fonksiyona gelen metinin içerisindeki eleman yani karakter punc(noktalama işaretleri) içinde varsa
#bu karakter yerine boşluk yazılsın yani karakter silinsin istiyoruz. fonksiyon sonunda da temizlenmiş metin döndürülsün.
    for ele in string:  
       if ele in punc:  
            string = string.replace(ele, " ") 
    return string

#dosya işlemleri yaparken hata bulduğunda program patlamasın diye try catch ile kontrol gerçekleştiriyoruz.
try:
#pythona tanıttığımız dosyayı r yani read komutu ile okuyoruz. Türkçe karakter içerdiği için utf-8 şeklinde tanımlıyoruz. ve dosyadan gelen verileri
#data değişkenimizde tutuyoruz.
    with open(filename,'r',encoding="UTF8") as f:
        data = f.read()
        
#data içerisindeki noktalama işaretlerini temizledikten sonra yeni bir dosya oluşturuyoruz, w(write) ile datanın yeni halini bu dosyaya yazdırıyoruz.
    with open("irembahar_removepunc_news.csv","w",encoding="UTF8") as f:
        f.write(remove_punc(data))
    print("Noktalama işaretleri dosyadan temizlendi.", filename)
except FileNotFoundError:
    print("Dosya bulunamadı.")