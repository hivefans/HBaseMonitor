from HBaseJmx.Master import Master
from HBaseJmx.MasterStatistics import MasterStatistics
import httplib
import json
import datetime

class HBaseMasterJmx(object):

    """docstring for HBaseJmx"""

    def __init__(self, hbasejmx):
        super(HBaseMasterJmx, self).__init__()
        self.hbasejmx = hbasejmx

    def parse_HBaseJmx(self):
        for item in self.hbasejmx:
            if item['name'] == "hadoop:service=Master,name=MasterStatistics":
                self.masterStatistics = MasterStatistics(item)
                self.masterStatistics.set_MasterStatistics_Info()
            if item['name'] == "hadoop:service=Master,name=Master":
                self.master = Master(item)
                self.master.set_Master_Info()

    def print_HBaseJmx(self):
        self.res = []
        '''print self.masterStatistics.cluster_requests
        print self.master.AverageLoad
        print self.master.ClusterId
        print self.master.MasterActiveTime
        print self.master.MasterStartTime
        print self.master.ServerName
        print self.master.ZookeeperQuorum
        print '***regionserInfo***'
        for regionserver in self.master.RegionServers_List:
            print 'RegionServer : %s' % regionserver.regionServerName
            print '             load: %d' % regionserver.load
            print '             maxHeapMB: %d' % regionserver.maxHeapMB
            print '             memStoreSizeInMB: %d' % regionserver.memStoreSizeInMB
            print '             numberOfRegions: %d' % regionserver.numberOfRegions
            print '             numberOfRequests: %d' % regionserver.numberOfRequests
            print '             storefileIndexSizeInMB: %d' % regionserver.storefileIndexSizeInMB
            print '             storefileSizeInMB: %d' % regionserver.storefileSizeInMB
            print '             storefiles: %d' % regionserver.storefiles
            print '             storeHeapMB: %d' % regionserver.storeHeapMB
            print '***************************************************'
            for region in regionserver.regions_List:
                print '                          regionName : %s' % region.regionName'''
        
        for table in self.master.Tables_Dict:
            tmp2 = []
            tmp = {}
            # 'Table Name: %s' % table
            #print 'Table readRequestCount: %d' % self.master.Tables_Dict[table].readRequestsCount
            tmp2.append(self.master.Tables_Dict[table].writeRequestsCount)
            tmp2.append(self.master.Tables_Dict[table].readRequestsCount)
            #print 'Table writeRequestCount: %d' % self.master.Tables_Dict[table].writeRequestsCount
            
            #print 'Table requestCount: %d' % self.master.Tables_Dict[table].requestsCount
            tmp2.append(self.master.Tables_Dict[table].requestsCount)
            tmp2.append(10)
            tmp2.append(20)
            tmp2.append(30)
            tmp[table]=tmp2
            self.res.append(tmp)

    def  getTableTps(self):
        self.TableTps = []
        for table in self.master.Tables_Dict:
            tpsInfo = []
            oneTableTpsInfo = {}

            tpsInfo.append({'writeCount':self.master.Tables_Dict[table].writeRequestsCount})
            tpsInfo.append({'readCount':self.master.Tables_Dict[table].readRequestsCount})
            tpsInfo.append({'totalCount':self.master.Tables_Dict[table].requestsCount})
            tpsInfo.append({'writeTPS':10})
            tpsInfo.append({'readTPS':20})
            tpsInfo.append({'totalTPS':30})
            oneTableTpsInfo[table]=tpsInfo
            self.TableTps.append(oneTableTpsInfo)

    def getTableStorageInfo(self):
        self.TableStorageInfo = []
        for table in self.master.Tables_Dict:
            storageInfo = []
            oneTableStorageInfo = {}

            storageInfo.append({'storefiles':self.master.Tables_Dict[table].storefiles})
            storageInfo.append({'stores':self.master.Tables_Dict[table].stores})
            storageInfo.append({'rootIndexSizeKB':self.master.Tables_Dict[table].rootIndexSizeKB})
            storageInfo.append({'storefileIndexSizeMB':self.master.Tables_Dict[table].storefileIndexSizeMB})
            storageInfo.append({'storefileSizeMB':self.master.Tables_Dict[table].storefileSizeMB})
            storageInfo.append({'totalStaticBloomSizeKB':self.master.Tables_Dict[table].totalStaticBloomSizeKB})
            storageInfo.append({'totalStaticIndexSizeKB':self.master.Tables_Dict[table].totalStaticIndexSizeKB})
            storageInfo.append({'currentCompactedKVs':self.master.Tables_Dict[table].currentCompactedKVs})
            storageInfo.append({'totalCompactingKVs':self.master.Tables_Dict[table].totalCompactingKVs})
            storageInfo.append({'memStoreSizeMB':self.master.Tables_Dict[table].memStoreSizeMB})
            oneTableStorageInfo[table]=storageInfo
            self.TableStorageInfo.append(oneTableStorageInfo)

    def getClusterInfo(self):
        self.ClusterInfo = []
        self.ClusterInfo.append({'name':'ServerName','value':self.master.ServerName})
        self.ClusterInfo.append({'name':'MasterStartTime','value':datetime.datetime.fromtimestamp(self.master.MasterStartTime).strftime('%Y-%m-%d %H:%M:%S')})
        self.ClusterInfo.append({'name':'MasterActiveTime','value':datetime.datetime.fromtimestamp(self.master.MasterActiveTime).strftime('%Y-%m-%d %H:%M:%S')})
        self.ClusterInfo.append({'name':'ZookeeperQuorum','value':self.master.ZookeeperQuorum})
        self.ClusterInfo.append({'name':'ClusterId','value':self.master.ClusterId})\

    def getClusterTps(self):
        self.ClusterTps = []
        self.ClusterTps.append({'regionServer':'Cluster','currentTps':self.masterStatistics.cluster_requests})
        for rs in self.master.RegionServers_List:
            self.ClusterTps.append({'regionServer':rs.regionServerName,'currentTps':rs.numberOfRequests})

def getTabelTps_List():
    jmxJsData = getHBaseJmx('192.168.7.80','60010')
    if ''!=jmxJsData:
        jmxPyData = json.loads(jmxJsData)
        hbaseMaster = HBaseMasterJmx(jmxPyData['beans'])
        hbaseMaster.parse_HBaseJmx()   
        hbaseMaster.getTableTps()
        tableTps = []
        for tableDict in hbaseMaster.TableTps:
            table={}
            for key in tableDict:
                i = 0
                table['tableName'] = key
                for kv in tableDict[key]:
                    for k in kv:
                        table[k]=kv[k]
                tableTps.append(table)
        return tableTps
    else:
        return []

def getTableStorageInfo_List():
    jmxJsData = getHBaseJmx('192.168.7.80','60010')
    if ''!=jmxJsData:
        jmxPyData = json.loads(jmxJsData)
        hbaseMaster = HBaseMasterJmx(jmxPyData['beans'])
        hbaseMaster.parse_HBaseJmx()   
        hbaseMaster.getTableStorageInfo()
        tableStorageInfo = []
        for tableDict in hbaseMaster.TableStorageInfo:
            table={}
            for key in tableDict:
                table['tableName'] = key
                for kv in tableDict[key]:
                    for k in kv:
                        table[k] = kv[k]
                tableStorageInfo.append(table)
        return tableStorageInfo
    else:
        return []

def getClusterInfo():
    jmxJsData = getHBaseJmx('192.168.7.80','60010')
    if ''!=jmxJsData:
        jmxPyData = json.loads(jmxJsData)
        hbaseMaster = HBaseMasterJmx(jmxPyData['beans'])
        hbaseMaster.parse_HBaseJmx()   
        hbaseMaster.getClusterInfo()
        return hbaseMaster.ClusterInfo
    else:
        return []

def getClusterTPS():
    jmxJsData = getHBaseJmx('192.168.7.80','60010')
    if ''!=jmxJsData:
        jmxPyData = json.loads(jmxJsData)
        hbaseMaster = HBaseMasterJmx(jmxPyData['beans'])
        hbaseMaster.parse_HBaseJmx()   
        hbaseMaster.getClusterTps()
        return hbaseMaster.ClusterTps
    else:
        return []

def getHBaseJmx(ip, port):
    try:
        conn = httplib.HTTPConnection(ip, port, timeout=30)
        conn.request('GET', '/jmx')
        response = conn.getresponse()
        status = response.status
    except Exception,e:
        return ''
    if (200 == status):
        jmxData = response.read()
        return jmxData
    else:
        return ''

#    try:
    # fileHandle = open('G:/workspace(c java)/java-workspace2/HBaseMonitor/HBaseJmx/10.jmx')
    # jmxJsData = fileHandle.read()
    # fileHandle.close()
    # return jmxJsData
#        conn = httplib.HTTPConnection(ip, port, timeout=30)
#        conn.request('GET', '/jmx')
#        response = conn.getresponse()
#        status = response.status
#    except Exception,e:
#        return ''
#    if (200 == status):
#        jmxData = response.read()
#        return jmxData
#    else:
#        return ''


def main():
    #fileHandle = open('10.jmx')
    #jmxJsData = fileHandle.read()
    #fileHandle.close()

    jmxJsData = getHBaseJmx('192.168.7.80','60010')
    if ''!=jmxJsData:
        jmxPyData = json.loads(jmxJsData)
        hbaseMasterJmx = HBaseMasterJmx(jmxPyData['beans'])
        hbaseMasterJmx.parse_HBaseJmx()
        hbaseMasterJmx.print_HBaseJmx()

if __name__ == '__main__':
    pass

