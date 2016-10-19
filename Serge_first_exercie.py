
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 12:07:04 2016

@author: serge
"""

import requests
from bs4 import BeautifulSoup

url_to_scrape = "http://missingmigrants.iom.int/latest-global-figures"

r = requests.get(url_to_scrape)

soup = BeautifulSoup(r.text)

inmates_links = []

right_table=soup.findAll('table', class_='table table-striped')
right_table_2015 = right_table[1]
right_table_2016 = right_table[0]

A=[]
B=[]
C=[]
D=[]
E=[]
F=[]
G=[]
H = []
I = []
J = []
K = []
L = []
M = []
N = []
O = []

AA = []
for row in right_table_2015.findAll("tr"):
    cells = row.findAll('td')
    if len(cells)!=0:
        A.append(cells[0].find(text=True))
        B.append(cells[1].find(text=True))
        C.append(cells[2].find(text=True))
        D.append(cells[3].find(text=True))
        E.append(cells[4].find(text=True))
        F.append(cells[5].find(text=True))
        G.append(cells[6].find(text=True))
        H.append(cells[7].find(text=True))
        I.append(cells[8].find(text=True))
        J.append(cells[9].find(text=True))
        K.append(cells[10].find(text=True))
        L.append(cells[11].find(text=True))
        M.append(cells[12].find(text=True))
        N.append(cells[13].find(text=True))
        O.append(cells[14].find(text=True))

        
                       
for row in right_table_2016.findAll("tr"):
    cells = row.findAll('td')
    if len(cells)!=0:
        AA.append(cells[14].find(text=True))

#import pandas to convert list to data frame
import pandas as pd
df=pd.DataFrame(A,columns=[''])
df2 = pd.DataFrame(AA,columns=['Total 2016'])
df['January']=B
df['Febraury']=C
df['March']=D
df['April']=E
df['May']=F
df['June']=G
df['July']=H
df['August']=I
df['September']=J
df['October']=K
df['November']=L
df['December']=M
df['Month Not Specied']=N
df['Total 2015']=O

print (df)
