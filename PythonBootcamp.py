#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Futbolcu():
    def __init__(self,ad,yas,uyruk,takim,deger):
        self.ad=ad
        self.yas=yas
        self.uyruk=uyruk
        self.takim=takim
        self.deger=deger


# In[2]:


list=[]


# In[ ]:


while True:
    ad=input("Futbolcunun ismini giriniz: (Programdan çıkmak için q tuşuna basın)")
    if ad=="q":
        break
    yas=int(input("Futbolcunun yasini giriniz: "))
    uyruk=input("Futbolcunun uyrugunu giriniz: ")
    takim=input("Futbolcunun mevcut takımı: ")
    deger=int(input("Futbolcunun degeri: "))
    futbolcu=Futbolcu(ad,yas,uyruk,takim,deger)
    list.append(futbolcu)


# In[3]:


for obj in list:
    print( obj.ad, obj.yas, obj.uyruk, obj. takim, obj.deger, sep =' ' )


# In[ ]:




