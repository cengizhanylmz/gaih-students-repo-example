import pandas as pd
import time
print("""
        ÖĞRENCİ VE NOT EKLEMEK İÇİN "1" 
        GİRİLEN ÖĞRENCİLERİN NOTLARI VE ORTALAMALARI GÖRMEK İÇİN "2"
        ÇIKIŞ İÇİN q
""")
ogrenci_list = list()
homework_list = list()
midterm_list = list()
final_list = list()
while True:
    sayi=input("Yapmak istediğiniz işelmi giriniz:")

    try:
        if sayi=="1":
            ogrenci_name=input("Öğrencinin Adı ve Soyadı:")

            ogrenci_list.append(ogrenci_name)

            homework=int(input("Homework:"))

            midterm = int(input("Midterm:"))

            final = int(input("Final:"))

            homework_list.append(homework)

            midterm_list.append(midterm)

            final_list.append(final)
        elif sayi=="2":
            ogrenci_list=pd.DataFrame(ogrenci_list)   #temel seviyedde pandas bilgim olduğu için ödevde bunu kullanmak istedim.

            homework_list=pd.DataFrame(homework_list)

            midterm_list=pd.DataFrame(midterm_list)

            final_list=pd.DataFrame(final_list)

            gruplama=[ogrenci_list,homework_list,midterm_list,final_list]

            abc=pd.concat(gruplama,axis=1)  #gruplama içerisindeki listeleri sütunlar halinde birleştirdim

            abc.columns=["Öğrenci İsmi","Homework","Midterm","Final"] #sütunlara isimlendirme verdim

            toplam=abc["Homework"] + abc["Midterm"] + abc["Final"]

            abc["Ortalama"]=toplam/3

            print(abc,"\n","\n")

            ortalamalar=[abc["Öğrenci İsmi"],abc["Ortalama"]]  #sadece ortalama ve öğrenci isimlerinin olduğu bir liste

            a=pd.concat(ortalamalar,axis=1)

            a.sort_values(by='Ortalama',inplace=True)  #ortaamaya göre küçükten büyüğe sıralama yaptım
            b=pd.pivot_table(a, index=["Öğrenci İsmi"]) #daha düzgün tablo için öğrenci isimlerini indexin yerine aldım
            print("En Yüksek Ortalamaya Sahip Öğrenci:\n")
            print(b.tail(1),"\n") #azdan çoğa doğru bir sıralama yaptıktan sonra sondan birinci datayı çekiyorum

        elif sayi=="q":
            print("Program Sonlandırılıyor...")
            time.sleep(1)
            break

    except ValueError:
        print("Herhangi bir öğrenci bilgisi bulunmamaktadır. Lütfen ilk önce öğrenci bilgisi giriniz!")
        print("---------------")
        break   




