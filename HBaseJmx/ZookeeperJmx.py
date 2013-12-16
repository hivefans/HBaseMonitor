import httplib
import json
import BeautifulSoup,re

class ZookeeperJmx(object):
    def __init__(self, ip, port):
        super(ZookeeperJmx, self).__init__()
        self.ip = ip
        self.port = port

    def getZkJmx(self):
        try:
            conn = httplib.HTTPConnection(self.ip, self.port, timeout=30)
            conn.request('GET', '/zk.jsp')
            response = conn.getresponse()
            status = response.status
        except Exception,e:
            self.zkjmx = ''
        if (200 == status):
            self.zkjmx = response.read()
        else:
            self.zkjmx = ''

    def parseZkJmx(self):
        soup=BeautifulSoup.BeautifulSoup(self.zkjmx).findAll("pre")
        contentList = re.split('\n',str(soup[0]))
        self.RsList = []
        self.ZkList = []
        index = 0

        while index < len(contentList):
            if 'Active master address' in contentList[index]:
                self.activeMaster = contentList[index].strip().split(':')[1].strip()
            if 'Backup master addresses' in contentList[index]:
                self.backupMaster = contentList[index].strip().split(':')[1].strip()
            if 'Region server holding ROOT' in contentList[index]:
                self.rootRegionser = contentList[index].strip().split(':')[1].strip()
            if 'Region servers:' in contentList[index]:
                index += 1        
                while '/hbase/replication' not in contentList[index]:
                    self.RsList.append(contentList[index])
                    index += 1
            if '/hbase/replication/state:' in contentList[index]:
                self.peerState = contentList[index].strip().split(' ')[1]
            if '/hbase/replication/peers' in contentList[index] and '2181' in contentList[index]:
                self.peerSlave = contentList[index].strip().split(' ')[1]
            if '/hbase/replication/peers' in contentList[index] and 'peer-state' in contentList[index]:
                self.peerState += '/'+contentList[index].strip().split(' ')[1]
                self.peerID = contentList[index].strip().split(' ')[0].split('/')[4]
            if 'Quorum Server Statistics:' in contentList[index]:
                index += 1
                while '2181' in contentList[index]:  #need modify
                    zkHost = {}
                    zkHost['address'] = contentList[index]
                    index += 1
                    if 'version' in contentList[index]:
                        version = contentList[index].strip().split(',')[0].split(':')[1]
                        zkHost['zkVersion'] = version.strip()
                        index += 1
                    while 'Clients:' in contentList[index]:
                        index += 1
                        zkHost['Clients'] = []
                        while 'queued' in contentList[index]:
                            zkHost['Clients'].append(contentList[index].strip())
                            index += 1
                    index += 1
                    if 'Latency' in contentList[index]:
                        nameList = contentList[index].strip().split(' ')[1].rstrip(':').split('/')
                        valueList= contentList[index].strip().split(' ')[2].split('/')
                        for i in range(len(nameList)):
                            zkHost[nameList[i]] = valueList[i]
                        index += 1
                    if 'Received' in contentList[index]:
                        rec = contentList[index].strip().split(':')
                        zkHost[rec[0]] = rec[1].strip()
                        index += 1
                    if 'Sent' in contentList[index]:
                        sent = contentList[index].strip().split(':')
                        zkHost[sent[0]] = sent[1].strip()
                        index += 1
                    if 'Connections' in contentList[index]:
                        conn = contentList[index].strip().split(':')
                        zkHost[conn[0]] = conn[1].strip()
                        index += 1
                    if 'Outstanding' in contentList[index]:
                        out = contentList[index].strip().split(':')
                        zkHost[out[0]] = out[1].strip()
                        index += 1
                    if 'Zxid' in contentList[index]:
                        zkid= contentList[index].strip().split(':')
                        zkHost[zkid[0]] = zkid[1].strip()
                        index += 1
                    if 'Mode' in contentList[index]:
                        mode = contentList[index].strip().split(':')
                        zkHost[mode[0]] = mode[1].strip()
                        index += 1
                    if 'Node' in contentList[index]:
                        node = contentList[index].strip().split(':')
                        zkHost[node[0]] = node[1].strip()
                        index += 1
                        self.ZkList.append(zkHost)
            index += 1

def readyZKAttrList():
    zk = ZookeeperJmx('192.168.7.80','60010')
    zk.getZkJmx()
    zk.parseZkJmx()
    zkAttrList = [   
        {'name':'Active MasterServer', 'value':zk.activeMaster,'group':'Zookeeper Info'},
        {'name':'Backup MasterServer', 'value':zk.backupMaster,'group':'Zookeeper Info',},
        {'name':'ROOT   Region  Addr', 'value':zk.rootRegionser,'group':'Zookeeper Info',},
        {'name':'Slave Peer  ', 'value':zk.peerSlave,'group':'Replication Info'},
        {'name':'Peer  ID    ', 'value':zk.peerID,'group':'Replication Info'},
        {'name':'Peer  State', 'value':zk.peerState,'group':'Replication Info'},
    ]
    return zkAttrList

def readyZKInfoList():
    zk = ZookeeperJmx('192.168.7.80','60010')
    zk.getZkJmx()
    zk.parseZkJmx()
    zkList = []

    for item in zk.ZkList:
        zkHost = {}
        zkHost['zkIp'] = item['address']
        zkHost['version'] = item['zkVersion']
        zkHost['recieved'] = item['Received']
        zkHost['send'] = item['Sent']
        zkHost['min_Latency'] = item['min']
        zkHost['avg_Latency'] = item['avg']
        zkHost['max_Latency'] = item['max']
        zkHost['connections'] = item['Connections']
        zkHost['zxID'] = item['Zxid']
        zkHost['mode'] = item['Mode']
        zkHost['nodeCount'] = item['Node count']
        zkList.append(zkHost)
    return zkList


if __name__ == '__main__':
    print readyZKInfoList()
    print readyZKAttrList()
