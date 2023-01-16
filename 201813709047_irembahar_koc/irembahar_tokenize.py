import csv
from itertools import zip_longest
from nltk.tokenize import sent_tokenize
dosya = "irembahar_removepunc_news.csv" 
satirlar = []
token_text = []
with open(dosya, 'r',encoding='utf8') as csvfile:
    csvreader = csv.reader(csvfile)
    fields = next(csvreader)
    for satir in csvreader: 
        satirlar.append(satir)       
for satir in satirlar:   
    for cumle in satir:
        cumle=cumle.lower()              
        nltk_tokens = sent_tokenize(cumle)
        token_text.append(nltk_tokens)       
tokenize_dosya = [token_text]
export_data = zip_longest(*tokenize_dosya, fillvalue ='')
with open('irembahar_tokenize.csv', 'w', encoding='UTF8', newline='\n') as myfile:
     wr = csv.writer(myfile)
     wr.writerows(export_data)
     myfile.close()    
