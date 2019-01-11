#!/usr/bin/python3.6/


import numpy as np
import random as rnd
import matplotlib.pyplot as plt
import statistics as st
import math

'''
Będzie tworzyć pakiet z danymi systemami obstawiania
'''

# Definiujemy pola gry, liczby, kolory 
ruletka = np.arange(0,37)

def zwrocparzyste(wybor):
	poleobstawienia =[]
	parzyste_pola = ruletka[ruletka %2 ==0]
	nieparzyste_pola = ruletka[ruletka%2==1]
	if wybor:
		poleobstawienia = parzyste_pola
	else:
		poleobstawienia = nieparzyste_pola
	return(poleobstawienia)
def zwrocczerwone(wybor):
	poleobstawienia =[]
	czerwone = np.array([32,19,21,25,34,27,36,30,23,5,16,1,14,9,18,7,12,3])
	czarne = np.array([15,4,2,17,6,13,11,8,10,24,33,20,31,22,29,28,35,26])
	if wybor:
		poleobstawienia = czerwone
	else:
		poleobstawienia = czarne
	return (poleobstawienia)

def zwrocduze(wybor):
	poleobstawienia =[]
	male_pola = ruletka[ruletka <19]
	duze_pola = ruletka[ruletka > 19]
	if wybor:
		poleobstawienia = male_pola
	else:
		poleobstawienia = duze_pola
	return(poleobstawienia)
def zwroctuziny(tuzin):
	poleobstawienia =[]
	pierwszy_tuzin = ruletka[ruletka<11]
	drugi_tuzin = ruletka[ruletka<23]
	trzeci_tuzin = ruletka[ruletka>24]
	if tuzin == 1:
		poleobstawienia = pierwszy_tuzin
	elif tuzin == 2:
		poleobstawienia = drugi_tuzin
	else
		poleobstawienia = trzeci_tuzin

		
	return(poleobstawienia)
