#Gerekli kütüphaneleri import ettim: Öncelikle, veri setini işlemek için gerekli olan pandas ve sklearn kütüphanelerini import ettim çünkü bu kütüphaneler, veri setlerini yüklemek ve işlemek için gerekli olan fonksiyonları içeriyor.

import pandas as pd
from sklearn.preprocessing import OrdinalEncoder

#Veri setini yükleyedim:Veri setini CSV dosyası olarak saklıysa, pandas'ın read_csv() fonksiyonunu kullanarak veri setini yükledim. Daha sonra, veri setini yükledim ve bir pandas veri çerçevesine (dataframe) dönüştürdüm. 
df = pd.read_csv("irembahar_just_cat2.csv")

#Kategorik verileri seçin: Daha sonra, veri çerçevesinden vektöre çevirmek istediğiniz kategorik verileri seçin. Örneğin, "haber_türü" adında bir sütunun kategorik verilerini vektöre çevirmek istiyorum.
#tabi bunun için öncelikle kategorilerin bulunduğu csv dosyasındaki verileri tabloya dönüştürdüm ve başlık olarak haber_türü ekledim.
#sonrasında dosyayı kullandığım için haber_türü yazısını sildim.
kategorik_veri = df["haber_türü"]
encoder = OrdinalEncoder(categories=[['siyaset', 'dunya', 'ekonomi', 'kultur', 'saglik','spor','teknoloji']])
vektor = encoder.fit_transform(kategorik_veri.values.reshape(-1, 1))

print(kategorik_veri)

