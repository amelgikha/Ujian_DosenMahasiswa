import pymongo
import json
import csv
import pandas as pd 
import matplotlib.pyplot as plt

url = 'mongodb://localhost:27017'
mydb = pymongo.MongoClient(url)

newdb = mydb['Kampus'] 
newcollection = newdb['Dosen'] 

datadosen = []
def ambildatadosen():
    for i in newcollection.find():
        d = {
            'asal': (i['asal']),
            'nama': i['nama'],
            'status': 'dosen',
            'usia': int(i['usia']),
        }
        datadosen.append(d)
    return datadosen

with open('datadosen.csv','w',newline='') as fileku:
    kolom = ['asal','nama','status','usia']
    tulis = csv.DictWriter(fileku,fieldnames = kolom)
    tulis.writeheader()
    tulis.writerows(ambildatadosen())

newdb = mydb['Kampus'] 
newcol = newdb['Mahasiswa'] 

datamahasiswa = []
def ambildatamahasiswa():
    for i in newcol.find():
        d = {
            'asal': (i['asal']),
            'nama': i['nama'],
            'status': 'mahasiswa',
            'usia': int(i['usia']),
        }
        datamahasiswa.append(d)
    return datamahasiswa

with open('datamahasiswa.csv','w',newline='') as fileku:
    kolom = ['asal','nama','status','usia']
    tulis = csv.DictWriter(fileku,fieldnames = kolom)
    tulis.writeheader()
    tulis.writerows(ambildatamahasiswa())

# create dataframe
datadosen = pd.read_csv('datadosen.csv')
datamahasiswa = pd.read_csv('datamahasiswa.csv')
print(datadosen)
print(datamahasiswa)

# Plotting 
plt.bar(datadosen['nama'],datadosen['usia'],color = 'blue')
plt.bar(datamahasiswa['nama'],datamahasiswa['usia'],color = 'orange')
plt.grid(True)
plt.legend(['Dosen','Mahasiswa'])
plt.title('Usia Warga Kampus')
plt.show()