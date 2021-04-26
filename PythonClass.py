#!/usr/bin/env python
# coding: utf-8

# In[7]:


import datetime
class osoba:
    def __init__(self,imie="brak",nazwisko="brak",pesel=11111111111):
        self.imie=imie
        self.nazwisko=nazwisko
        self.pesel=str(pesel)
        self.time=str((str(datetime.datetime.now()).split(" "))[0].split("-"))
        self.time_pass=int(str(str(datetime.datetime.now()).split(" ")[0]).split("-")[0])+10 
                        
    def wypisz(self):
        print("imie: "+self.imie) 
        print("nazwisko: "+self.nazwisko)
        print("data ważności: "+str(self.time_pass))
        print('pesel: ' +str(self.pesel))
    def zmien_nazwisko(self,nowe_nazwisko):
        self.nazwisko=nowe_nazwisko
    def spr(self):
        x=str(self.pesel)
        wynik=9*int(x[0:1]) + 7*int(x[1:2]) + 3*int(x[2:3]) + 1*int(x[3:4]) + 9*int(x[4:5]) + 7*int(x[5:6]) + 3*int(x[6:7]) + 1*int(x[7:8]) + 9*int(x[8:9]) + 7*int(x[9:10])
        wynik=wynik%10
        bo= wynik == int(x[10:11])    
        return bo
    


# In[9]:


o=[3, 4, 5, 1, 1, 0, 3, 4, 5, 6, 0, 4, 3, 2, 1, 1, 1, 1, 2, 4, 5, 3, 3, 3, 3, 1, 2, 0, 0, 1, 3, 5, 4, 5, 2, 5, 4, 5, 2, 5]
o.sort()
print(o)
print(o.count(1))


# In[ ]:





# In[60]:


p=str(10212006012)
mo=p[2:4]
ro=p[0:2]
dz=p[4:6]
if int(mo) > 12:
    pro=20
else:
    pro=19
print(str(pro)+ro+" "+str(int(mo)%12)+" "+dz)


# In[61]:


o=osoba()
print(o.wypisz())
o.zmien_nazwisko("k")
print(o.wypisz())
o1=osoba("a","m",97012006012)
print(o1.wypisz())
print(o1.spr())
k=osoba('j','r',90214091284)
print(k.wypisz())
print(o1.wypisz())


# In[8]:


class Konto():
    def __init__(self,imie,adres,pin=1111,saldo=0):
        self.imie=imie
        self.adres=adres
        self.pin=pin
        self.saldo=saldo
    def wypisz(self):
        return "Konto "+ self.imie
    def wyplata(self):
        sprpin=input("podajpin ")
        if str(self.pin) ==sprpin:
            print("pin poprawny")
            wyplata=int(input("podaj kwote "))
            self.saldo-=wyplata
            if self.saldo < 0:
                self.saldo+=wyplata
                return "brak wystaraczajacych środków na koncie"
            else:
                return "wypłacono "+str(wyplata)+' zl'
        else:
            return 'pin niepoprawny'


# In[ ]:


k=Konto("marek",'agrestowa',3102,saldo=100)
print(k.wypisz())
k.wyplata()


# In[11]:


class Adres:
    def __init__(self,imie,nazwisko,numer):
        self.imie=imie
        self.nazwisko=nazwisko
        self.numer=numer


# In[79]:


getattr(Konto,"wypisz")


# In[9]:


class student(osoba):
    def __init__(self,imie="brak",nazwisko="brak",pesel=11111111111,nrindeksu=111111):
        self.nrind=nrindeksu
        osoba.__init__(self,imie,nazwisko,pesel)
    def nrind(self):
        return self.nrind
    


# In[25]:


k=student("a","m",97012006012,317777)
k.nrind


# In[10]:


class wykładowaca(osoba):
    def __init__(self,imie="brak",nazwisko="brak",pesel=11111111111,tytul='brak'):
        self.tytul=tytul
        osoba.__init__(self,imie,nazwisko,pesel)
    def tytul(self):
        return self.tytul


# In[55]:


wykład=wykładowaca('jurek','ruby',9021409128,"doktor")
wykład.tytul


# In[14]:


class stypendysta(student):
    def __init__(self,imie="brak",nazwisko="brak",pesel=11111111111,nrindeksu=111111,kstypendium=0):
        self.kstypendium=kstypendium
        student.__init__(self,imie,nazwisko,pesel,nrindeksu)
    def stypendium(self):
        return self.kstypendium


# In[18]:


stypend=stypendysta('jaro','dobramorda',439024023911,112231,1500)
stypend.wypisz()


# In[113]:


class lodz():
    def __init__(self,liczbakadlubuw,nrrejestracyjny,naped):
        self.liczba=str(liczbakadlubuw)
        self.nrrejestracyjny=str(nrrejestracyjny)
        self.naped=str(naped)
    def wypisz(self):
        print("nazwa: "+self.liczba)
        print("nr. rejestracyjny: "+self.nrrejestracyjny)
        print("rocznik : "+self.naped)


# In[114]:


class pojazd():
    def __init__(self,liczbamiejsc,pojemnosc,kola):
        self.liczbamiejsc=str(liczbamiejsc)
        self.pojemnosc=str(pojemnosc)
        self.kola=str(kola)
    def wypisz(self):
        print("liczbamiejsc: "+self.liczbamiejsc)
        print("pojemnosc: "+self.pojemnosc)
        print("koła : "+self.kola)


# In[115]:


class amfibia(pojazd,lodz):
    def __init__(self,liczbakadlubuw,nrrejestracyjny,naped,liczbamiejsc,pojemnosc,kola):
        lodz.__init__(self,liczbakadlubuw,nrrejestracyjny,naped)
        pojazd.__init__(self,liczbamiejsc,pojemnosc,kola)
    def wypisz(self):
        print("liczbamiejsc: "+self.liczbamiejsc)
        print("pojemnosc: "+self.pojemnosc)
        print("koła : "+self.kola)
        print("nazwa: "+self.liczba)
        print("nr. rejestracyjny: "+self.nrrejestracyjny)
        print("naped : "+self.naped)


# In[116]:


adna=amfibia(3,24214,"szybki",4,31,4)
adna.wypisz()


# In[1]:


class cialoniebieski():
    def __init__(self,nazwa,masa,opis="brak :| "):
        self.nazwa=nazwa 
        self.masa=masa
        self.opis=opis
    def dane(self):
        print("nazwa: "+self.nazwa)
        print("masa: "+self.masa)
    def opis(self):
        print(self.opis)


# In[2]:


class gwiazda(cialoniebieski):
    def __init__(self,nazwa,masa,opis,klasa):
        cialoniebieski.__init__(self,nazwa,masa,opis)
        self.klasa=klasa
    def typ(self):
        print(self.klasa)


# In[5]:


gw=gwiazda("siema",30,"duża","A")
gw.typ()


# In[93]:


class ulamek():
    def __init__(self,licznik,mianownik):
        self.licznik=licznik
        self.mianownik=mianownik
    def __str__(self):
        return str(self.licznik)+"/"+str(self.mianownik)
    def __setattr__(self,name,value):
        if name=='licznik':
            self.__dict__['licznik']=value
            zeros=str(self.__dict__['licznik'])
            dot=zeros.find('.')+1
            z=len(zeros[:dot])-dot
            valuecount=10**z
            if value!=0 and type(value)==type(1.0):
                self.__dict__['licznik']=int(value*valuecount)
            else:
                self.__dict__['licznik']=value
        if name=='mianownik':
            self.__dict__['mianownik']=value
            zeros=str(self.__dict__['mianownik'])
            dot=zeros.find('.')+1
            z=len(zeros)-dot
            valuecount=10**z
            if value!=0 and type(value)==type(1.0):
                self.__dict__['mianownik']=int(value*valuecount)
            else:
                self.__dict__['mianownik']=value
    def __add__(self, other):
        
        if self.mianownik != other.mianownik:
            licznik = (self.licznik*other.mianownik )+(other.licznik*self.mianownik)
            mianownik = self.mianownik * other.mianownik            
        else:
            licznik=self.licznik+other.licznik
        return ulamek(licznik,mianownik)
    def __sub__(self, other):
        
        if self.mianownik != other.mianownik:
            licznik = (self.licznik*other.mianownik )-(other.licznik*self.mianownik)
            mianownik = self.mianownik * other.mianownik            
        else:
            self.licznik=self.licznik-other.licznik
        return ulamek(licznik,mianownik)
    def skracanie(self):
        a=self.licznik
        b=self.mianownik
        while b:
            a,b=b,a%b
        if self.licznik != a:
            self.licznik=int(self.licznik/a)
        self.mianownik=int(self.mianownik/a)
        return None
    def __mul__(self, other):
        licznik=self.licznik*other.licznik
        mianownik = self.mianownik * other.mianownik
        return ulamek(licznik,mianownik)
    def __truediv__(self, other):
        licznik=self.licznik*other.mianownik
        smianownik = self.mianownik * other.licznik
        return ulamek(licznik,mianownik)
    def __eq__(self, other):
        licznik=self.licznik*other.mianownik
        licznik2=other.licznik*self.mianownik
        mianownik = self.mianownik * other.mianownik 
        return licznik==licznik2
    def __lt__(self, other):
        licznik=self.licznik*other.mianownik
        licznik=other.licznik*self.mianownik
        self.mianownik = self.mianownik * other.mianownik 
        return licznik<licznik2
    def __gt__(self, other):
        licznik=self.licznik*other.mianownik
        licznik2=other.licznik*self.mianownik
        mianownik = self.mianownik * other.mianownik 
        return licznik>licznik2
    def __le__(self, other):
        licznik=self.licznik*other.mianownik
        licznik2=other.licznik*self.mianownik
        mianownik = self.mianownik * other.mianownik  
        return licznik<=licznik2
    def __ge__(self, other):
        licznik=self.licznik*other.mianownik
        licznik2=other.licznik*self.mianownik
        mianownik = self.mianownik * other.mianownik 
        return licznik>=licznik2


# In[94]:


u1=ulamek(8,6)
u2=ulamek(3,2)

u3=ulamek(223123.0000003,322.03103421422)
print(u3)
print(u2)


# In[86]:


import math
class zespolona():
    def __init__(self,a,b):
        self.a=a
        self.b=b
        self.argument=math.atan2(self.b,self.a)
        self.z=math.sqrt(((self.a)**2)+((self.b)**2))
    def __str__(self):
        return str(self.a)+"+"+str(self.b)+"i"
    def __add__(self,other):
        a=self.a +other.a
        b=self.b +other.b
        return zespolona(a,b)
    def __sub__(self,other):
        a=self.a -other.a
        b=self.b -other.b
        return zespolona(a,b)
    def __mul__(self,other):
        if isinstance(other, int):
            a=other*self.a
            b=other*self.b
            return zespolona(a,b)
        else :
            a =(abs(self.z*other.z))*(math.cos(self.argument+other.argument))
            b =(abs(self.z*other.z))*(math.sin(self.argument+other.argument))
            return zespolona(round(a),round(b))
    def __truediv__(self,other):
        a=((self.a*other.a)+(self.b*(other.b)))/((other.a**2)+(other.b**2))
        b=((self.a*(-1*(other.b)))+(self.b*other.a))/((other.a**2)+(other.b**2))   
        return zespolona(round(a),round(b))
    def __pow__(self,n):
        self.a=((self.z)**n)*(math.cos(n*self.argument))
        self.b=((self.z)**n)*(math.sin(n*self.argument))
        self.argument=math.atan2(self.b,self.a)
        self.z=math.sqrt(((self.a)**2)+((self.b)**2))
        return zespolona(round(self.a),round(self.b))
    def pierwiastek(self,n):
        zw=[]
        for k in range(n):
            zw.append(zespolona(math.log(self.z,n)*(math.cos(self.argument*(2*k*math.pi))/n),math.log(self.z,n)*
                            (math.sin(self.argument*(2*k*math.pi))/n)))
        return zw
    def trygonometryczna(self):
        return str(self.z)+"(cos "+str(self.argument)+" + isin "+str(self.argument)+")"
        


# In[87]:


z1=zespolona(5,2)
z2=zespolona(3,-7)
z3=z1*3
print(z1.trygonometryczna())
print(z3)
print(z1)
print(z1.trygonometryczna())
tab=[z1,z2]
print(tab)
type(3)


# In[49]:


z4=zespolona(1,8)
z5=zespolona(2,3)
z6=z4/z5
print(z6.z)
print(z4.pierwiastek(4)[2])
z1.argument


# In[8]:


math.log(8,3)
math.pi


# In[4]:


s=3600
f=bin(s)
print(f.count("1"))


# In[16]:


i=2
n=49
while True:
    if i>=n :
        print("tak")
        break
    elif n%i==0 :
        print("nie")
        break
    i+=1


# In[24]:


pol=math.sqrt(24)
round(pol-0.5)
math.log(27,3)


# In[100]:


class matrix():
    def __init__(self,lista):
        self.lista=lista
        self.rows=len(lista)
        self.columns=len(lista[0])
    def __str__(self):
        k=""
        for p in self.lista :
            k+= str(p)
            k+="\n"
        return k
    def __add__(self,other):
        dod1=self.lista
        dod2=other.lista
        
        if self.rows == other.rows and self.columns == other.columns:
            for r in range(self.rows):
                for c in range(self.columns):
                    p1=dod1[r][c]
                    p2=dod2[r][c]
                    dod2[r][c]=p1+p2
            return matrix(dod2)
    def __sub__(self,other):
        sub=self.lista
        if self.rows == other.rows and self.columns == other.columns:
            for r in range(self.rows):
                for c in range(self.columns):
                    p1=self.lista[r][c]
                    p2=other.lista[r][c]
                    sub[r][c]=p1-p2
            return matrix(sub)
    def skalar(self,n):
        mul=self.lista
        for r in range(self.rows):
                for c in range(self.columns):
                    mul[r][c]=mul[r][c]*n
        return matrix(mul)
    def __mul__(self,other):
        mul2=range(self.rows)
        if self.rows == other.columns and self.rows == other.columns:
            for r in range(self.rows):
                for c in range(self.columns):
                    self.lista[r][c]*other.lista[c][r]


# In[102]:


n0=matrix([[2,3,4],[5,6,7]])
n1=matrix([[2,3,4],[5,6,7]])
print(n0)
n=n0+n1
print(n)
print(n0)
print(n1)
n4=n0.skalar(3)

print(n4)


# In[113]:


import numpy
h1=numpy.array([[2,3],[4,6],[5,6]])
h2=numpy.array([[2,3,4],[5,6,7]])
h1.dot(h2)


# In[116]:


def simpleGeneratorFun(n): 
    for x in range(n):
        if x%2==0:
            yield x
    
simpleGeneratorFun(10)


# In[ ]:


class helloFifohere():
    def __init__(self,lista):
        self.lista=lista
    def __iter__(self,n):


# In[5]:


class node():
    def __init__(self,data,negzt=None):
        self.data=data
        self.negzt=negzt
class FIFO1():
    def __init__(self,first,last,lenght):
        self.first=first
        self.last=last
        self.lenght=lenght
        self.kolejka=[]
    def add(self,n):
        self.kolejka.append(n)
        self.first=n
    def usun(self,n):
        
        self.kolejka.pop(self.first)


# In[6]:


node([3,4,1,41,1,51,8,9])
FIFO1()


# In[12]:


import queue 
#Lifo
l= queue.LifoQueue(maxsize=10)
l.put(4)
l.put(3)
l.put(2)
l.put(5)
l.full()
l.get()
l.get()


# In[10]:


import queue 
#Fifo
l= queue.Queue(maxsize=10)
print(l.empty())
l.put(4)
l.put(3)
l.put(2)
l.put(5)
l.full()
l.get()
l.get()
l.qsize()
print(l.full())


# In[5]:


print(l.task_done())


# In[64]:


z1=zespolona(2,3)
z2=zespolona(4,3)
z3=zespolona(6,4)
def square(a,b,c):
    delta=b**2+a*c*(-4)
    x1=(delta.pierwiastek(2)[0]-b*-1)/a*2
    x12=(delta.pierwiastek(2)[1]-b*-1)/a*2
    x2=(delta.pierwiastek(2)[0]-b)/a*2
    x22=(delta.pierwiastek(2)[1]-b)/a*2
    return [x1,x12,x2,x22]

l=square(z1,z2,z3)
print(l[0],l[1],l[2],l[3])


# In[21]:



class dziennik:
    def __init__(self,lizta):
            self.lizta=lizta.sort()

k=dziennik([1,3,2])
print(dziennik.__mro__)


# In[7]:


(map((lambda x,y:x+y ), [1,2,3,4]))
    


# In[12]:


t=[1,2,3,4]
for next in t[1:]:
    print(next)


# In[ ]:




