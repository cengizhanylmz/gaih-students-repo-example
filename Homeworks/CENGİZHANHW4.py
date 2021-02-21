##HANGMAN GAME##
import random as rd
import time
class HangmanGameData():
    def __init__(self):
        #sorulacak sorular buradan seçiliyor böyle bir sözlüğe atadım
        self.kelimeler={"Bir Başkent":"LONDRA",
                "Türkiye'de bir göl":"MANYAS KUŞ GÖLÜ",
                "Türkiye'de bir şehir":"BURSA",
                "Bir meyve":"GREYFURT",
                "Deyim":"ECEL TERİ DÖKMEK",
                "Türkiye'de Bir Spor Klübü":"GALATASARAY",
                "Atasözü":"ACELE İŞE ŞEYTAN KARIŞIR"}

class HangmanGame(HangmanGameData): #kalıtım kullandım
    def choice_data(self):
        #anahtarları ve değerleri çekerek her birini listeye atadım ve bu listeden rastgele bir indexini seçme işlemi yaptım
        datas=list(self.kelimeler.items())
        a=rd.choice(datas)
        #seçilen indexte doğal olarak bir anahtar ve onun karşılığı var.  0. index anahtar 1. index ise o anahtarın değeridir.
        self.kelime=a[1] #bunları self parametreleri ile değerlere atadım
        self.anahtar=a[0]

    def soru1(self):
            print("SORU:",self.anahtar)  # sözlükteki kelimenin anahtarı soru olduğu için o anahtarı ekrana bastıran fonksiyon
    def question(self):
        #ipucu vermek amacıyla kelimenin bazı harflerini açık göstermek istiyorum bunun için tekrardan kelime içerisinden rastgele birer harf çekiyorum
        harf=rd.choice(self.kelime)
        harf1=rd.choice(self.kelime)

        self.soru=list()  #boş bir liste atıyorum
        for j in self.kelime:
            if j==harf:

                self.soru.append(harf) #seçilen harfi soru listesine atıyorum
            elif j==harf1:#seçilen diğer harfi de soru listesine atıyorum
                self.soru.append(harf1)
            else:
                if(j!=" "):
                    self.soru.append("-") #BOŞLUKLARI DOLDURMAMAK İÇİN TEKRAR İF BLOĞU KOYDUM bunu yapmadığım zaman boşluklara da "-" işareti koyuyor. Bu istemediğim bir şey.

                else:
                    pass

        self.show=' '.join([str(i) for i in self.soru]) #self.soru listesi içindeki ifadeleri yatay şekilde bastırmak için kullandığım kod satırı
        print(self.show) #soruyu bastırıyorum


    def quess(self):
        hak=8   #8 tane tahmin hakkı tanıdım
        while hak>0:

            harf=input("Harf Tahmini Giriniz:")

            b=self.kelime.replace(" ","")  #seçilen kelimedeki boşlukları kaldırıyorum
            for i in b:

                if harf==i:
                    index_list = list()
                     #girilen harf kelimede varsa bu harfin hangi indexlerde olduğunu bulmam gerekiyor
                    a=list(b) #kelimeleyi listeye çevirdim

                    for k in range(len(a)): #indexleri üzerinde geziyorum
                        if a[k]==harf: #eğer indexteki harf tahmin edilen harf ile aynıysa, o harfin indexini listeye atıyorum
                            index_list.append(k)

                    for j in index_list: #doğru harflerin indexlerini buldum
                        self.soru.pop(j)#ilk önce sorduğumuz sorudaki ilgili indexteki "-" işaretini siliyorum
                        self.soru.insert(j, harf)#sildiğim "-" işaretinin yerine doğru tahmin edilen harfi koyuyorum
                    self.show = ' '.join([str(k) for k in self.soru]) #yatay şekilde stringi çevirmek için kullandığım kod

            print(self.show) #tahminden sonraki kelimeyi tekrar bastırıyorum
            print("Tahmininiz yok ise 'YOK' yazınız") #kullanıcıya verdiği harf tahminlerinden sonra soruyu tamamen cevaplamak isterse diye seçenek sunuyorum
            tahmin = input("Herhangi Bir Tahmininiz Var Mı?:")

            if tahmin == self.kelime: #eğer tahmin ettiği kelime seçilen kelimemizle doğru ise oyunu kazanıyor direkt.
                print("Tebrikler Kazandınız!!")
                break
            elif tahmin == "YOK": #oyuncu yok diyerek pas geçebilir
                pass
            elif tahmin!=self.kelime:
                print("Yanlış Tahmin!")
            hak -= 1 #eğer soruyu tahmin edemediyse 1 hak eksiltip devam ediyor program
            print("{} tahmin hakkınız kalmıştır!".format(hak))
            continue
        if hak==0: #eğer soruyu doğru tahmin edemez ise ve hakkı kalmazsa oyun bitiyor.
            print("ÇÖP ADAMIMIZ MAALESEF ASILDI...KAYBETTİNİZ!")


while True:
    print("""
    Basit Adam Asmaca Oyununa HOŞGELDİNİZ!!      
            Oynamak için 1:
            Oyunu sonlandırmak için 2:
    
            """)
    sayi=input("Yapmak istediğiniz işlemi giriniz:")
    if sayi=="1":
        oyun=HangmanGame()
        oyun.choice_data()
        oyun.soru1()
        oyun.question()
        oyun.quess()

    elif sayi=="2":
        print("Program sonlandırılıyor")
        time.sleep(1.5)
        break






