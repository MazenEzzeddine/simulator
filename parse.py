from typing import Dict


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




if __name__=='__main__':
    parse()
    parseLatency()