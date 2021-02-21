def prime_first(number):
    a = 0
    k = 2
    if number<500:
        while k<number:
            if number % k != 0:
                a += 1  # eğer bölme sonucumuz 0 değilse a katsayısına 1 ekliyoruz
            k += 1
        if a == number - 2:  # while döngüsü tamamlandığında eğer i sayımız bir asal sayı ise  atadığımız a sayısı i sayısının 2 eksiği kadar değer almış anlamına gelir.
            print("1. fonksiyon tarafından bulunan değer:",number)    # örnek olarak 7 bir asal sayı 2,3,4,5,6 değerlerine tam bölünmeyeceği için a değerine 5 defa 1 eklemesi yaptık. 7-5 =2
    else:
        print("Bu fonksiyon sadece 0 ile 500 arasında çalışmaktadır")
        return number
def prime_second(number):
    a = 0
    k = 2
    if number>=500 and number<=1000:
        while k < number:
            if number % k != 0:
                a += 1
            k += 1
        if a == number - 2:
            print("2. fonksiyon tarafından bulunan değer:",number)
    else:
        print("Bu fonksiyon sadece 500 ile 1000 arasında çalışmaktadır.")
        return number



for i in range(1001):
    if i>=0 and i <=499:
        prime_first(i)
    elif i>=500 and i<=1000:
        prime_second(i)

##BU KISIM DENEME AMAÇLIDIR
#for i in range(1001):
    #if i>=0 and i <=499:
        #prime_first(i)
    #elif i>=500 and i<=1000:
        #prime_first(i)
