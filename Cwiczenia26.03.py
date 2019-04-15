# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 12:30:54 2019

@author: micha
"""
import sys
from PyQt5.QtWidgets import QLineEdit, QPushButton, QLabel, QWidget, QApplication, QGridLayout, QColorDialog
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from Projekt1 import przeciecia, dlugoscodc
import matplotlib.pyplot as plt

class AppWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.title="matplotlib.example"  
        self.initInterface()
        self.initWidgets()
        
    def initInterface(self):
        self.setWindowTitle(self.title)      #tytuł aplikacji
        self.setGeometry(300,200,500,400)
        self.show()
    
    def initWidgets(self):
        btn=QPushButton("RYSUJ", self)
        btnCol=QPushButton("Kolor AB", self)
        btnCol2=QPushButton("Kolor CD", self)
        btnclear=QPushButton("Czysc",self)
        xaLabel=QLabel("Xa:",self)
        yaLabel=QLabel("Ya:",self)
        xbLabel=QLabel("Xb:",self)
        ybLabel=QLabel("Yb:",self)
        xcLabel=QLabel("Xc:",self)
        ycLabel=QLabel("Yc:",self)
        xdLabel=QLabel("Xd:",self)
        ydLabel=QLabel("Yd:",self)
        xpLabel=QLabel("Xp:",self)
        ypLabel=QLabel("Yp:",self)
        dlABLabel=QLabel("długosc AB:",self)
        dlCDLabel=QLabel("długosc CD:",self)
        odpLabel=QLabel("Odpowiedz:",self)
        
        self.xaEdit=QLineEdit()
        self.yaEdit=QLineEdit()
        self.xbEdit=QLineEdit()
        self.ybEdit=QLineEdit()
        self.xcEdit=QLineEdit()
        self.ycEdit=QLineEdit()
        self.xdEdit=QLineEdit()
        self.ydEdit=QLineEdit()
        self.xpEdit=QLineEdit()
        self.ypEdit=QLineEdit()
        self.dlABEdit=QLineEdit()
        self.dlCDEdit=QLineEdit()
        self.odpEdit=QLineEdit()
        
        self.figure=plt.figure()
        self.canvas=FigureCanvas(self.figure)
        
        #wyswietlenie
        grid=QGridLayout()
        grid.addWidget(xaLabel, 0,0)
        grid.addWidget(self.xaEdit, 0, 1)
        grid.addWidget(yaLabel, 1, 0)
        grid.addWidget(self.yaEdit, 1, 1)
        
        grid.addWidget(xbLabel, 0,2)
        grid.addWidget(self.xbEdit, 0,3)
        grid.addWidget(ybLabel, 1, 2)
        grid.addWidget(self.ybEdit, 1, 3)
        
        grid.addWidget(xcLabel, 0,4)
        grid.addWidget(self.xcEdit, 0, 5)
        grid.addWidget(ycLabel, 1, 4)
        grid.addWidget(self.ycEdit, 1, 5)
        
        grid.addWidget(xdLabel, 0,6)
        grid.addWidget(self.xdEdit, 0, 7)
        grid.addWidget(ydLabel, 1, 6)
        grid.addWidget(self.ydEdit, 1, 7)
        
        grid.addWidget(xpLabel, 2, 2)
        grid.addWidget(self.xpEdit, 2, 3)
        grid.addWidget(ypLabel, 2, 4)
        grid.addWidget(self.ypEdit, 2, 5)
        
        grid.addWidget(dlABLabel, 3, 2)
        grid.addWidget(self.dlABEdit, 3, 3)
        grid.addWidget(dlCDLabel, 3, 4)
        grid.addWidget(self.dlCDEdit, 3, 5)
        
        grid.addWidget(odpLabel, 4, 0)
        grid.addWidget(self.odpEdit, 4, 1, 1, 7)
        
        grid.addWidget(btn,5,0,1,2)
        grid.addWidget(btnCol,6,0,1,2)
        grid.addWidget(btnCol2,7,0,1,2)
        grid.addWidget(btnclear,8,0,1,2)
        grid.addWidget(self.canvas, 5,2,-1,-1)  #rozciagniecie na cale okno
        
        self.setLayout(grid)
        
        btn.clicked.connect(self.oblicz)
        btnCol.clicked.connect(self.zmienKolor)
        btnCol2.clicked.connect(self.zmienKolor2)
        btnclear.clicked.connect(self.czysc)
    
    def czysc(self):
        self.xaEdit.clear()
        self.yaEdit.clear()
        self.xbEdit.clear()
        self.ybEdit.clear()
        self.xcEdit.clear()
        self.ycEdit.clear()
        self.xdEdit.clear()
        self.ydEdit.clear()
        self.xpEdit.clear()
        self.ypEdit.clear()
        self.dlABEdit.clear()
        self.dlCDEdit.clear()
        self.odpEdit.clear()
    
    def zmienKolor(self):
        kolor=QColorDialog.getColor()
        if kolor.isValid():
#            print(kolor.name())
            self.rysuj(kol=kolor.name())
            
    def zmienKolor2(self):
        kolor=QColorDialog.getColor()
        if kolor.isValid():
            self.rysuj(kol2=kolor.name())
    
    def sprawdzliczbe(self, element):
        if element.text().lstrip('-').replace('.','',1).isdigit():
            return float(element.text())
        else:
            element.setFocus() #wstawianie kursora tam gdzie jest błąd i zwrócenie wartosci pustej
            return None #NIC
        
    def oblicz(self):
        self.rysuj()
        
    def rysuj(self, kol='red',kol2='blue'):
        xa=self.sprawdzliczbe(self.xaEdit)
        ya=self.sprawdzliczbe(self.yaEdit)
        xb=self.sprawdzliczbe(self.xbEdit)
        yb=self.sprawdzliczbe(self.ybEdit)
        xc=self.sprawdzliczbe(self.xcEdit)
        yc=self.sprawdzliczbe(self.ycEdit)
        xd=self.sprawdzliczbe(self.xdEdit)
        yd=self.sprawdzliczbe(self.ydEdit)
        
        if None not in [xa,ya,xb,yb,xc,yc,xd,yd]:
            xa=float(self.xaEdit.text())  #zczytujemy
            ya=float(self.yaEdit.text())
            xb=float(self.xbEdit.text())  
            yb=float(self.ybEdit.text())
            xc=float(self.xcEdit.text())  
            yc=float(self.ycEdit.text())
            xd=float(self.xdEdit.text())  
            yd=float(self.ydEdit.text())
            
            wyswietl,Xp,Yp,t1,t2=przeciecia(xa,ya,xb,yb,xc,yc,xd,yd)
            self.xpEdit.setText(str(Xp))
            self.ypEdit.setText(str(Yp))
            self.odpEdit.setText(str(wyswietl))
            
            self.figure.clear()
            ab=self.figure.add_subplot(111)
            ab.plot([ya,yb],[xa,xb],color=kol,marker="o", label='Odcinek AB')  #kółeczka ba końcach odcinków
            ab.plot([yc,yd],[xc,xd],color=kol2,marker="o", label='Odcinek CD')
            ab.legend() #wyswietlenie Label na wykresie
            ab.scatter(Yp,Xp, label="Punkt P")
            
        if t1>=0 and t1<=1: 
            if t2>=0 and t2<=1:
                pass              #nie mamy odp więc idzie dalej
            else:
                ab.plot([yc,Yp],[xc,Xp],":")
        else:
            if t2>=0 and t2<=1:
                    ab.plot([ya,Yp],[xa,Xp],":")  #przedłużenie odcinka
            else:
                    ab.plot([ya,Yp],[xa,Xp],":")
                    ab.plot([yc,Yp],[xc,Xp],":")
            self.canvas.draw()
        
        dlu1=dlugoscodc (xa,ya,xb,yb)
        dlu2=dlugoscodc (xc,yc,xd,yd)
        
        self.dlABEdit.setText(str(dlu1))
        self.dlCDEdit.setText(str(dlu2))
        
def main():
    app=QApplication(sys.argv)
    window = AppWindow()
    app.exec_()
    
if __name__=='__main__':
    main()





