# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 12:21:40 2019

@author: micha
"""
import matplotlib.pyplot as plt

#wczytanie danych za pomocą polecenia input
def wczytaj(wsp):
    komunikat = "Podaj współrzędną" + wsp
    x = input (komunikat)
    
# sprawdzenie czy dane są wartosciami liczbowymi
    while (x.lstrip('-').replace('.', ' ', 1).isdigit()==0):
        x = input("Błąd we wpisywanej waspółrzędnej" + komunikat) 
    return float (x)

#Xa = wczytaj(" Xa: ")
#Ya = wczytaj(" Ya: ")
#Xb = wczytaj(" Xb: ")
#Yb = wczytaj(" Yb: ")
#Xc = wczytaj(" Xc: ")
#Yc = wczytaj(" Yc: ")
#Xd = wczytaj(" Xd: ")
#Yd = wczytaj(" Yd: ")


def przeciecia (Xa,Ya,Xb,Yb,Xc,Yc,Xd,Yd):
    
    delXab=Xb-Xa
    delYab=Yb-Ya
    delXcd=Xd-Xc
    delYcd=Yd-Yc
    delXac=Xc-Xa
    delYac=Yc-Ya
    mian=delXab*delYcd-delYab*delXcd
    
    if mian==0:
        wyswietl="Nie da się wyznaczyć współrzędnych przecięcia"
        Xp="Nie da się wyznaczyć"
        Yp="Nie da się wyznaczyć"
        t1=None
        t2=None
    
    else:
        t1=(delXac*delYcd-delYac*delXcd)/mian
        t2=(delXac*delYab-delYac*delXab)/mian
        
        Xp=Xa+t1*delXab
        Yp=Ya+t1*delYab
    
        Xap=[Xa,Xp]
        Yap=[Ya,Yp]
        Xcp=[Xc,Xp]
        Ycp=[Yc,Yp]

        if t1>=0 and t1<=1: 
            if t2>=0 and t2<=1:
                wyswietl="Punkt leży na przecięciu odcinków"
            else:
                wyswietl="Punkt leży na odcinku AB"
                plt.plot(Ycp,Xcp,":")
        else:
            if t2>=0 and t2<=1:
                wyswietl="Punkt leży na odcinku CD"
                plt.plot(Yap,Xap,":")  #przedłużenie odcinka
            else:
                wyswietl="Punkt leży na przedłużeniu odcinków"
                plt.plot(Yap,Xap,":")
                plt.plot(Ycp,Xcp,":")
            
            
        with open("wspolrzedne.txt","w") as plik:
            plik.write("{:20.3s} {:10.3f} {:10.3f} ".format(wyswietl,Xp,Yp))
        
        Xab=[Xa,Xb]
        Yab=[Ya,Yb]
        Xcd=[Xc,Xd]
        Ycd=[Yc,Yd]
        
        plt.plot(Yab,Xab, label="Odcinek AB")
        plt.plot(Ycd,Xcd, label="Odcinek CD")
        plt.scatter(Yp,Xp, label="punkt przecięcia")
        plt.legend()
        
        Xp=round(Xp,3)
        Yp=round(Yp,3)
        
    return(wyswietl,Xp,Yp,t1,t2)

from math import sqrt
 
def dlugoscodc (Xa,Ya,Xb,Yb):
    dlu=sqrt((Xa-Xb)**2+(Ya-Yb)**2)
    dlu=round(dlu,3)
    return dlu
    
            #AMEN
        
    
    

        
        
        
        
        
        
        
        
        



