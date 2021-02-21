
class cooking():
    def __init__(self,yemek=None,kisilik=None,pisirme_sure=None,pisirme_tarzi=None,hazirlanis_sure=None):
        self.sure=pisirme_sure
        self.pisirme_tarzi=pisirme_tarzi
        self.hazirlanis_sure=hazirlanis_sure
        self.malzemeler1 = []
        self.kisilik=kisilik
        self.yemek=yemek
        self.faydali_bilgi=[]
        self.pisirme_adimlari=[]
class tavuk_sote(cooking):
    def __init__(self):
        super().__init__()
        self.yemek = "TAVUK SOTE"
        malzeme=["2 yemek kaşığı sıvı yağ","300 gram tavuk göğsü","1 adet soğan","1 adet yeşil biber","1 adet domates",
                 "1 çay kaşığı pul biber","1 çay kaşığı kuru nane","1 çay kaşığı tuz","1 çay kaşığı karabiber" ]
        for i in malzeme:
            self.malzemeler1.append(i)
    def __str__(self):

        return "Malzemeler:\n1) {}\n2) {}\n3) {}\n4) {}\n5) {}\n6) {}\n7) {}\n8) {}\n9) {}\n".format(self.malzemeler1[0],self.malzemeler1[1],self.malzemeler1[2],self.malzemeler1[3],
                                                               self.malzemeler1[4],self.malzemeler1[5],self.malzemeler1[6],self.malzemeler1[6],self.malzemeler1[7])
    def bilgiler(self):

        print(self.yemek, "\n")
        self.pisirme_sure = "25 Dakika"
        self.pisirme_tarzi = "Ocakta (Teflon Bir tava gayet ideal olacaktır)"
        self.hazirlanis_sure = "15 Dakika"
        self.kisilik = "2"
        print("{} tarifi {} kişiliktir".format(self.yemek, self.kisilik), "\n")
        print("- Ortalama pişirme süresi:", self.pisirme_sure, "\n")
        print("- Pişirme tarzı:", self.pisirme_tarzi, "\n")
        print("- Ortalama Hazırlama Süresi:", self.hazirlanis_sure, "\n")

    def pisirme(self):
        x="""Tavanın içerisine 2 yemek kaşığı sıvı yağı alın ve üzerine 300 gram kuşbaşı doğranmış tavuğu ilave ederek yüksek ateşte soteleyin.Pişen tavukların üzerine 1 adet doğranmış soğanı ilave ederek sotelemeye devam edin.Doğranmış yeşil biber ve yarım adet doğranmış kapya biberi de ekleyin,1 adet doğranmış domatesi de tavanın içerisine aktarın.Biraz suyunu çektikten sonra sırasıyla birer çay kaşığı tuz, karabiber, pul biber ve kuru nane ilave ederek güzelce karıştırın.İyice pişince tavuk sotenizi ocaktan alın ve servis edin. Afiyet olsun!"""
        print("PİŞİRME ADIMLARI:\n")
        for i in x.split("."): #Hepsini adım adım göstermek itediğim için noktalara göre ayırma işlemi yaptım ve bunlar listeye atadım.
            self.pisirme_adimlari.append(i)
        for i in range(len(self.pisirme_adimlari)-1):
            a=print("Adım-",i+1,":",self.pisirme_adimlari[i],"\n") #listemdeki eleman sayısı kadar Adım ekledim ve Her adımı ilgili indexe karşılık getirdim
    def faydali_bilgiler(self):
        print("***PÜF NOKTALAR!***\n")
        x="""Tavuk soteyi, yanmaz/yapışmaz tabanlı geniş bir tavada hazırlıyorsanız yağ kullanmayın.Aksi takdirde çok az miktarda (örneğin 1 tatlı kaşığı), yanma derecesi yüksek bir çeşit sıvı yağ kullanın.Sote tavası ve kullandığınız yağı önceden kızdırın.Sote edilen doğranmış kabuksuz domates ve biberler suyunu salacağı için ekstra su kullanmayın.
        """
        for i in x.split("."):
            self.faydali_bilgi.append(i)
        for i in range(len(self.faydali_bilgi) - 1):
            a = print("-", self.faydali_bilgi[i], "\n")


class tas_kebabi(cooking):
    def __init__(self):
        super().__init__()
        self.yemek = "TAS KEBABI"
        malzeme = ["800 gram kuşbaşı dana eti", "1 yemek kaşığı ayçiçek yağı", "2 yemek kaşığıtereyağı", "1 adet orta boy kuru soğan",
                   "3 dişsarımsak","1 yemek kaşığıun","1 tatlıkaşığı domates salçası",
                   "2 adet orta boy patates", "1 adet orta boy havuç", "1 tatlı kaşığı tuz", "3 su bardağı sıcak su"]
        for i in malzeme:
            self.malzemeler1.append(i)

    def __str__(self):
        return "Malzemeler:\n1) {}\n2) {}\n3) {}\n4) {}\n5) {}\n6) {}\n7) {}\n8) {}\n9) {}\n10) {}\n11) {}\n".format(
            self.malzemeler1[0], self.malzemeler1[1], self.malzemeler1[2], self.malzemeler1[3],
            self.malzemeler1[4], self.malzemeler1[5], self.malzemeler1[6],self.malzemeler1[7],self.malzemeler1[8],self.malzemeler1[9],self.malzemeler1[10])

    def bilgiler(self):
        print(self.yemek, "\n")
        self.pisirme_sure = "50 Dakika"
        self.pisirme_tarzi = "Ocakta (Dilerseniz Saç tavada)"
        self.hazirlanis_sure = "25 Dakika"
        self.kisilik = "5"
        print("{} tarifi {} kişiliktir".format(self.yemek, self.kisilik), "\n")
        print("- Ortalama pişirme süresi:", self.pisirme_sure, "\n")
        print("- Pişirme tarzı:", self.pisirme_tarzi, "\n")
        print("- Ortalama Hazırlama Süresi:", self.hazirlanis_sure, "\n")
    def pisirme(self):
        x="""1 yemek kaşığı sıvı yağ ve 2 yemek kaşığı tereyağını tencerede kızdırın.Üzerine 800 gram dana kuşbaşı etini ekleyin ve etler suyunu salıp çekene kadar kavurun.Yemeklik doğranmış 1 adet soğanı ve 3 diş doğranmış sarımsağı da ekledikten sonra etlerle beraber kavurmaya devam edin.Bu aşamada ekleyeceğiniz 1 yemek kaşığı unu, kokusu çıkana kadar yaklaşık 2-3 dakika etlerle birlikte kavuru,1 tatlı kaşığı salçayı ekleyin ve karıştırın.Ardından 1 tatlı kaşığı tuz, 1 adet küp doğranmış patates, 1 adet küp doğranmış havuç ve 1 çay kaşığı karabiberi de ekleyip 3 su bardağı su ilave edin.Kapağını kapattığınız tencerede, kısık ateşte 30 dakika kadar pişirin. 
        """
        print("PİŞİRME ADIMLARI:\n")
        for i in x.split("."):
            self.pisirme_adimlari.append(i)
        for i in range(len(self.pisirme_adimlari)-1):
            a=print("Adım-",i+1,":",self.pisirme_adimlari[i],"\n")
    def faydali_bilgiler(self):
        print("***PÜF NOKTALAR!***\n")
        x="""İlk olarak yüksek ateşte renk alana kadar kavuracağınız dana etlerini öncelikle kendi suyunda pişirin.Sosun berrak olması için bu esnada yüzeye çıkan kahverengi köpük kısımlarını tencereden alın.
        """
        for i in x.split("."):
            self.faydali_bilgi.append(i)
        for i in range(len(self.faydali_bilgi) - 1):
            a = print("-",self.faydali_bilgi[i], "\n")

class pasta(cooking):
    def __init__(self):
        super().__init__()
        self.yemek = "MİNİ KÖSTEBEK PASTA"
        malzeme = ["3 adet yumurta", "1 su bardağı toz şeker", "Yarım çay bardağı süt", "Yarım çay bardağı sıvı yağ",
                   "2 tepeleme yemek kaşığı kakao","1 paket kabartma tozu","1 paket vanilya",
                   "1,5 su bardağı un", "2 paket krem şanti", "1,5 su bardağı soğuk süt", "2 adet muz"]
        for i in malzeme:
            self.malzemeler1.append(i)

    def __str__(self):
        return "Malzemeler:\n1) {}\n2) {}\n3) {}\n4) {}\n5) {}\n6) {}\n7) {}\n8) {}\n9) {}\n10) {}\n11) {}\n".format(
            self.malzemeler1[0], self.malzemeler1[1], self.malzemeler1[2], self.malzemeler1[3],self.malzemeler1[4], self.malzemeler1[5], self.malzemeler1[6],
            self.malzemeler1[7], self.malzemeler1[8],self.malzemeler1[9],self.malzemeler1[10])
    def bilgiler(self):

        print(self.yemek, "\n")
        self.pisirme_sure = "20 Dakika"
        self.hazirlanis_sure = "30 Dakika"
        self.kisilik = "4"
        print("{} tarifi {} kişiliktir".format(self.yemek, self.kisilik), "\n")
        print("- Ortalama pişirme süresi:", self.pisirme_sure, "\n")
        print("- Ortalama Hazırlama Süresi:", self.hazirlanis_sure, "\n")
    def pisirme(self):
        x=" İç dolgusu için krem şantiyi hazırlayın. 1,5 su bardağı soğuk süt ile 2 paket krem şantiyi bir mikser yardımıyla iyice çırpın. Hazırladığınız krem şantiyi soğuması için dolaba kaldırın.Kek için; yumurta ve şekeri mikser yardımıyla 5 dakika boyunca çırpın. Ardından gerekli olan diğer malzemeleri ekleyin ve güzelce karıştırın. Kek hamurunuz hazır.Dikdörtgen bir fırın tepsisinin dibine yağlı kağıt serin ve üstüne hazırladığınız kek karışımını dökün. Önceden ısıtılmış 180 derece fırında yaklaşık 20 dakika pişirin.Kek piştikten sonra fırından alın ve ılıklaşmasını bekleyin. Yuvarlak bir kesme kalıbıyla kekinizi yuvarlak yuvarlak kesin.Kalan kek parçalarını iyice soğumaları için bir kenara alın.Krem şantiyi bir sıkma torbasına alın ve yuvarlak kestiğiniz her bir kek parçasının üstüne bir miktar sıkın.Muzları yuvarlak yuvarlak dilimleyin ve üstlerine yerleştirin.Muzların üstüne tekrar bir tepe oluşturacak şekilde krem şantiyi sıkın.Kalan ve iyice soğumuş olan kek parçalarını mutfak robotunda un haline gelene dek çekin.Üstüne krem şanti sıktığınız kekleri bu un haline getirdiğiniz kek kırıntıları ile kaplayın ve soğuması için tekrar buzdolabına kaldırın."
        print("PİŞİRME ADIMLARI:\n")
        for i in x.split("."):
            self.pisirme_adimlari.append(i)
        for i in range(len(self.pisirme_adimlari)-1):
            a=print("Adım-",i+1,":",self.pisirme_adimlari[i],"\n")

    def faydali_bilgiler(self):
        print("***PÜF NOKTALAR!***\n")
        x=""" Kek hamurunu hazırladıktan sonra büyükçe bir dikdörtgen tepsiye dökerseniz,hem alt tabanı daha ince olacaktır,hem de daha fazla porsiyon çıkacaktır.Yuvarlak yuvarlak kesmek için geniş ağızlı bir bardak ya da yuvarlak kesme kalıbı kullanabilirsiniz."""
        for i in x.split("."):
            self.faydali_bilgi.append(i)
        for i in range(len(self.faydali_bilgi) - 1):
            a = print("-",self.faydali_bilgi[i], "\n")

t=tavuk_sote()
tas=tas_kebabi()
pas=pasta()
print("""
    YEMEK TARİFLERİNE HOŞGELDİNİZ 
    TARİF LİSTESİNE ULAŞMAK İÇİN 1"
    ÇIKIŞ YAPMAK İÇİN 2""")
while True:
    sayi=input("Yapmak istediğiniz işlem:")
    if sayi=="1":
        print(t.yemek)
        print(tas.yemek)
        print(pas.yemek)
        secim=input("Ulaşmak istediğiniz tarifi yazınız:\n")
        if secim.upper()==t.yemek:

            t.bilgiler()
            print(t)
            t.faydali_bilgiler()
            t.pisirme()
        elif secim.upper()==tas.yemek:

            tas.bilgiler()
            print(tas)
            tas.faydali_bilgiler()
            tas.pisirme()
        elif secim.upper()==pas.yemek:

            pas.bilgiler()
            print(pas)
            pas.faydali_bilgiler()
            pas.pisirme()
        else:
            print("Yanlış işlem yaptınız!")
        continue
    elif sayi=="2":
        print("Progradan çıkılıyor...")
        break