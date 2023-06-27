from datetime import datetime
from typing import Dict

import pandas as pd
import matplotlib.pyplot as plt


def parse():
    with open('mazparse.txt', 'r') as f:
        lines = f.readlines()
    replicas = set()
    for line in lines[1:]:
        replica = line.split(',')[2]
        replicas.add(replica)
    print (len(replicas))

    for replica in replicas:
        print(replica)


def parseLatency():
    map = {}
    map['m'] = [1]
    map['m'] = map['m'] + [2]
    map['n'] = 5
    # str = 'n'
    # map[str] = 10
    with open('mazparse.txt', 'r') as f:
        lines = f.readlines()
    for line in lines[1:]:
        replica = line.split(',')
        strr = replica[2][:-2]
        map[strr] = map.get(strr, []) + [replica[1]]
        #map[strr]=  map[strr] + [replica[1]]

        # if map.get(strr)==None:
        #     map.update({strr, []}
        #

    #print(map.get('latency-6667db9f57-d2fq2'))

    f = open("my_file.txt", mode="wt")
    for key in map.keys():
        f.write(key)
        f.write(str(map[key]))
        # print(key, map[key])
        # print('=========================')

def readPanda():
    data = pd.read_csv('reb1.txt')
    # grouped = data.groupby(axis=1)
    # print(grouped)
    print(data[' text_payload'])
    print(data[' pod_name'])
    data[' text_payload'] = data[' text_payload'].str.extract('latency is (\d+)')

    data[' text_payload'] = data[' text_payload'].astype(float)
    # s = pd.to_numeric(data[' text_payload'])
    # print(s.head)

    your_counter = len(data[' text_payload'][data[' text_payload'] > 500])
    print(your_counter)

    #data[' text_payload'].hist(bins=100)
    data[' text_payload'].hist(cumulative=True, bins=200, density =1)##hist(bins=100)
    #plt.plot( data[' text_payload'])
    plt.show()


    # grouped = data.groupby(' pod_name')
    # print(grouped.keys)
   # print(data)

def getReplicas():
    data = pd.read_csv('mazparse.txt')
    c = data[' pod_name'].nunique()
    u = data[' pod_name'].unique()
    print(type(u))
    print(u)
    print(u[1])

    h = data[' pod_name'].where(data[' pod_name'] == u[1]).last_valid_index()
    m = data[' pod_name'].where(data[' pod_name'] == u[1]).first_valid_index()



    datem = data['timestamp'].values[m]
    dateh = data['timestamp'].values[h]
    print(datem)
    print(dateh)
    print(str(datem)[0:-4])

    datetime_obj1 = datetime.strptime(
        str(datem)[0:-11], '%Y-%m-%dT%H:%M:%S')
    print(datetime_obj1)

    datetime_obj2 = datetime.strptime(
        str(dateh)[0:-11], '%Y-%m-%dT%H:%M:%S')
    print(datetime_obj1)
    t = datetime_obj1 - datetime_obj2

    print(t.seconds/60 )



    print(h)
    print(m)
    print(c)

def getReplicasMinutes():
    #data = pd.read_csv('mazparse.txt')
    data = pd.read_csv('reb1.txt')

    c = data[' pod_name'].nunique()
    u = data[' pod_name'].unique()
    totalseconds =0

    for i in range(len(u)) :
     print(u[i])
     h = data[' pod_name'].where(data[' pod_name'] == u[i]).last_valid_index()
     m = data[' pod_name'].where(data[' pod_name'] == u[i]).first_valid_index()

     datem = data['timestamp'].values[m]
     dateh = data['timestamp'].values[h]
     print(datem)
     print(dateh)


     datetime_obj1 = datetime.strptime(
         str(datem)[0:-11], '%Y-%m-%dT%H:%M:%S')

     datetime_obj2 = datetime.strptime(
        str(dateh)[0:-11], '%Y-%m-%dT%H:%M:%S')

     t = (datetime_obj1 - datetime_obj2).seconds

     totalseconds += t
    print(totalseconds/60)

    # print(t.seconds/60 )



    # print(h)
    # print(m)
    # print(c)




if __name__=='__main__':

    readPanda()
    #getReplicas()
    #getReplicasMinutes()
