from datetime import datetime
from typing import Dict

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import dates


def readPanda():
    data = pd.read_csv('graph/latency3.txt')
    data = data.iloc[::-1].reset_index()
    # grouped = data.groupby(axis=1)
    # print(grouped)
    print(data[' text_payload'])
    print(data[' pod_name'])
    data[' text_payload'] = data[' text_payload'].str.extract('latency is (\d+)')

    data[' text_payload'] = data[' text_payload'].astype(float)
    data['timestamp'] =pd.to_datetime( data['timestamp'])
    # s = pd.to_numeric(data[' text_payload'])
    # print(s.head)

    fig, ax = plt.subplots()

    # ax.xaxis.set_major_formatter(dates.DateFormatter('%H:%M'))
    #
    # plt.xticks(rotation=45, ha='right')


    your_counter = len(data[' text_payload'][data[' text_payload'] > 1500])
    print(your_counter)

    #data[' text_payload'].hist(bins=100)
    data[' text_payload'].hist(cumulative=True, bins=200, density =1)##hist(bins=100)
    #ax.plot(data['timestamp'], data[' text_payload'])
    plt.show()


    # grouped = data.groupby(' pod_name')
    # print(grouped.keys)
   # print(data)



def getReplicasMinutes():
    #data = pd.read_csv('mazparse.txt')
    data = pd.read_csv('graph/latency3.txt')

    u = data[' pod_name'].unique()
    print(u)
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

    #readPanda()
    getReplicasMinutes()
