
import random as rd
sayilar=range(2,100)  #2 den 99 a kadar sayı üretilsin
asal_sayilar=[]  #asal sayı değişkenlerini atacağımız bir liste

for i in sayilar:
    a=0
    k=2
    while k<i:  #k değeri sayımızdan büyük olana kadar döngüde kal
        if i%k !=0:
            a +=1  #eğer bölme sonucumuz 0 değilse a katsayısına 1 ekliyoruz
        k +=1
    if a==i-2:  # while döngüsü tamamlandığında eğer i sayımız bir asal sayı ise  atadığımız a sayısı i sayısının 2 eksiği kadar değer almış anlamına gelir.
                #örnek olarak 7 bir asal sayı 2,3,4,5,6 değerlerine tam bölünmeyeceği için a değerine 5 defa 1 eklemesi yaptık. 7-5 =2
        asal_sayilar.append(i)
matrix=[]
for i in range(0,9):
    k=rd.choice(asal_sayilar)  #asal sayılar kümesinden rastgele 9 sayı seç
    matrix.append(k)

print("",matrix[0],matrix[1],matrix[2],"\n",matrix[3],matrix[4],matrix[5],"\n",matrix[6],matrix[7],matrix[8] )










