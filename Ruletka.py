'''
W co celujemy
 1 - wybieramy określoną liczbę
 2 - wybieramy czerwone/czarne kolory
 3 - wybieramy parzystą/nieparzysta liczbe
 4 - wybieramy liczbe z tuzinów
 5- wybieramy dwa numery
 6 - wybieramy trzy numery
 7 - wybieramy cztery numery
 8 - wybieramy sześć numerów
Ratio Win
 35:1- trafiamy określoną liczbę
 2:1 - trafiamy czerwony/czarny kolor
 2:1 - trafiamy parzystą/nieparzystą liczbe
 3:1 - trafiamy liczbe z określonego tuzina
 18:1 - trafiamy dwie liczby
 12:1 - trafiamy trzy liczby
 6:1 - trafiamy sześć numberóœ
 
'''
import numpy as np
import random as rnd
import matplotlib.pyplot as plt
import statistics as st
import math

startowa_suma = 1000
liczba_gier = 10
ratiowin = 35
ruletka = np.arange(0,37)


parzyste_pola = ruletka[ruletka %2 ==0]
nieparzyste_pola = ruletka[ruletka%2==1]
czerwone = np.array([32,19,21,25,34,27,36,30,23,5,16,1,14,9,18,7,12,3])
czarne = np.array([15,4,2,17,6,13,11,8,10,24,33,20,31,22,29,28,35,26])

'''
Teraz będziemy definiować rodzaj obstawiania
Płaski system - zawsze taka sama kwota
Progresja - system będzie się zwiększał
Martyngał - podwajamy kwote aby nadrobić straty
'''



def obstawienie(wybor):
	wyborobstawiania = {
		1: 35,
		2: 1,
		3: 1,
		4: 2,
		5: 17,
		6: 11,
		7: 8,
		8: 5,
	}
	return wyborobstawiania.get(wybor,null)
# plaski system z obstawianiem jednego numeru wygrana odchodzimy
def flat_system(kwota_startowa,liczbagier,ratiowin):
	# Wybieramy liczbe z zakresu od 1 do 36
	gracz_wybor = rnd.randint(0,36)
	ruletka_losowanie = np.random.randint(0,36,liczbagier)
	stawka = kwota_startowa/liczbagier
	for losowanie in ruletka_losowanie:
		if gracz_wybor == losowanie:
			kwota_startowa +=(ratiowin*stawka)
			
		else:
			kwota_startowa -=stawka
	return kwota_startowa
def martingale_system(kwota_startowa,liczbagier,ratiowin):
	#gracz_wybor = rnd.randint(0,36)
	ruletka_losowanie = np.random.randint(0,36,liczbagier)
	# Suma szeregu geometrycznego
	geom_sum = (1-math.pow(2,liczbagier))/(1-2)
	stawka = kwota_startowa/geom_sum
	for losowanie in ruletka_losowanie:
		if losowanie%2==0:
			kwota_startowa += (ratiowin*stawka)
		else:
			kwota_startowa =-stawka
			stawka = stawka *2
	return kwota_startowa


# Tworzymy tablice wyników
wyniki_gry_system_plaski = []
wyniki_gry_system_martingale = []
# Generujemy liczbe testów jako rozmiar tablicy wyniki_gry
liczbatestow = 100
testy = np.arange(1,liczbatestow+1)
for test in range(0,liczbatestow):
	flatprofit = flat_system(startowa_suma,liczba_gier,35)-startowa_suma
	martingaleprofit = martingale_system(startowa_suma,liczba_gier,35)-startowa_suma
	wyniki_gry_system_plaski.append(flatprofit)
	wyniki_gry_system_martingale.append(martingaleprofit)
wyniki_gry_system_plaski = np.array(wyniki_gry_system_plaski)
wyniki_gry_system_martingale = np.array(wyniki_gry_system_martingale)

fig = plt.figure()

plt.subplot(1, 2, 1)
plt.bar(liczbatestow, wyniki_gry_system_plaski)
plt.xlabel('Numer wizyty w kasynie')
plt.ylabel('Zysk z serii 10 gier')
plt.title('Analiza plaskiego systemu gry w kasynie '+str(liczbatestow)+" wizyt w kasynie")
plt.grid()


plt.subplot(1, 2, 2)
plt.bar(liczbatestow, wyniki_gry_system_martingale)
plt.xlabel('Numer wizyty w kasynie')
plt.ylabel('Zysk z serii 10 gier')
plt.title('Analiza plaskiego systemu gry w kasynie '+str(liczbatestow)+" wizyt w kasynie")
plt.grid()


plt.show()

