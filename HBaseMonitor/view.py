from HBaseJmx.HBaseMasterJmx import getTabelTps_List,getTableStorageInfo_List,getClusterInfo,getClusterTPS
from HBaseJmx.ZookeeperJmx import readyZKInfoList,readyZKAttrList
from django.http.response import HttpResponse
from django.shortcuts import render_to_response
from django.utils import simplejson
from django.views.decorators.csrf import csrf_exempt

def index(request):
    return render_to_response('index.html')

def tableTps(request):
    return render_to_response('table/table_tps.html')

def tableStorageInfo(request):
    return render_to_response('table/table_storage.html')

def showMasterInfo(request):
    return render_to_response('master/master.html')

def showRegionServerLoad(request):
    return render_to_response('master/regionserver_load.html')

def showZkInfo(request):
    return render_to_response('zk/zookeeper.html')

def getTableTps(request):
    tableTps = getTabelTps_List()
    context = {'code':200, 'msg':{'total':3, 'rows':tableTps}}
    return HttpResponse(simplejson.dumps(context, ensure_ascii=False))

def getTableStorageInfo(request):
    # context = {'code':200, 'msg':{'total':2, 'rows':[
    #                {'TableName':123, 'StoreFiles':1234, 'Stores':'mt', 'rootIndexSizeKB':123, 'storefileIndexSizeMB':123,
    #                 'storefileSizeMB':123, 'totalStaticBloomSizeKB':123,'totalStaticIndexSizeKB':123, 'currentCompactedKVs':123, 'totalCompactingKVs':123,
    #                 'memStoreSizeMB':123},
    #                {'TableName':123, 'StoreFiles':1234, 'Stores':'mt', 'rootIndexSizeKB':123, 'storefileIndexSizeMB':123,
    #                 'storefileSizeMB':123, 'totalStaticBloomSizeKB':123,'totalStaticIndexSizeKB':123, 'currentCompactedKVs':123, 'totalCompactingKVs':123,
    #                 'memStoreSizeMB':123}
    #                ]}} 
    tableStorageInfo = getTableStorageInfo_List()
    context = {'code':200, 'msg':{'total':3, 'rows':tableStorageInfo}}
    return HttpResponse(simplejson.dumps(context, ensure_ascii=False))

@csrf_exempt
def getClusterAttr(request):
    # context = {'total':5, 'rows':[   
    #                 {'name':'ServerName', 'value':'Bill Smith'},
    #                 {'name':'MasterStartTime', 'value':'2013-12-07 12:00:00'},
    #                 {'name':'MasterActiveTime', 'value':'2013-12-07 12:00:00'},
    #                 {'name':'ZookeeperQuorum', 'value':'test88.hadoop,test89.hadoop,test90.hadoop'},
    #                 {'name':'ClusterId', 'value':'dwe344eer-fefegr55g4g-5gr55grgr59'}
    #         ]}
    clusterInfo = getClusterInfo()
    print clusterInfo
    context = {'total':len(clusterInfo), 'rows': clusterInfo}  
    return HttpResponse(simplejson.dumps(context, ensure_ascii=False))

def getClusterTps(request):
    # context = {'code':200, 'msg':{'total':4, 'rows':[
    #                {'regionServer':'test88.hadoop', 'currentTps':100},
    #                {'regionServer':'test89.hadoop', 'currentTps':100},
    #                {'regionServer':'test90.hadoop', 'currentTps':100},
    #                {'regionServer':'test91.hadoop', 'currentTps':100},
    #                {'regionServer':'Cluster', 'currentTps':400}
    #           ]}}
    clusterTps = getClusterTPS()
    context = {'code':200, 'msg':{'total':len(clusterTps), 'rows':clusterTps}}
    return HttpResponse(simplejson.dumps(context, ensure_ascii=False))

def getRegionServerInfo(request):
    context = {'code':200, 'msg':{'total':4, 'rows':[
                   {'regionServerName':'test88.hadoop', 'load':100, 'memStoreSizeInMB':100, 'usedHeapMB':100, 
                    'maxHeapMB':100, 'storeFiles':100, 'storeFileIndexSizeMB':100, 'storeFileSizeInMB':100},
                   {'regionServerName':'test89.hadoop', 'load':100, 'memStoreSizeInMB':100, 'usedHeapMB':100, 
                    'maxHeapMB':100, 'storeFiles':100, 'storeFileIndexSizeMB':100, 'storeFileSizeInMB':100},
                   {'regionServerName':'test90.hadoop', 'load':100, 'memStoreSizeInMB':100, 'usedHeapMB':100, 
                    'maxHeapMB':100, 'storeFiles':100, 'storeFileIndexSizeMB':100, 'storeFileSizeInMB':100},
                   {'regionServerName':'test91.hadoop', 'load':100, 'memStoreSizeInMB':100, 'usedHeapMB':100, 
                    'maxHeapMB':100, 'storeFiles':100, 'storeFileIndexSizeMB':100, 'storeFileSizeInMB':100},
              ]}}
    return HttpResponse(simplejson.dumps(context, ensure_ascii=False))

def getRegionInfo(request):
    context = {'code':200, 'msg':{'total':3, 'rows':[
                   {'writeRequestCount':100,'readRequestCount':'test88.hadoop', 'readCount':100, 'stores':100, 
                    'storeFiles':100, 'memStoreSizeMB':100, 'storeFileSizeMB':100, 'RootIndexSizeKB':100,
                    'storeFileIndexSizeMB':100, 'totalStaticBloomSizeKB':100, 'totalStaticIndexSizeKB':100, 
                    'currentCompactedKVs':100,'totalCompactingKVs':100},
                   {'readRequestCount':'test88.hadoop', 'writeRequestCount':100, 'readCount':100, 'stores':100, 
                    'storeFiles':100, 'memStoreSizeMB':100, 'storeFileSizeMB':100, 'RootIndexSizeKB':100,
                    'storeFileIndexSizeMB':100, 'totalStaticBloomSizeKB':100, 'totalStaticIndexSizeKB':100, 
                    'currentCompactedKVs':100,'totalCompactingKVs':100},
                   {'readRequestCount':'test88.hadoop', 'writeRequestCount':100, 'readCount':100, 'stores':100, 
                    'storeFiles':100, 'memStoreSizeMB':100, 'storeFileSizeMB':100, 'RootIndexSizeKB':100,
                    'storeFileIndexSizeMB':100, 'totalStaticBloomSizeKB':100, 'totalStaticIndexSizeKB':100, 
                    'currentCompactedKVs':100,'totalCompactingKVs':100},
              ]}}
    return HttpResponse(simplejson.dumps(context, ensure_ascii=False))

@csrf_exempt
def getRegionList(request):
    context = {'rows':[{   
                "id": 0,
                "text": "All Regions",
                "state": "closed",
                "children": [{   
                "id": 1,
                "text": "Table 1",
                "state": "closed",
                "children": [{   
                              "id":11,
                              "text":"region 11"  
                              }, {   
                              "id":12,
                              "text":"region 12"
                             }]   
                }, {   
                "id": 2,
                "text": "Table 2",
                "state": "closed",
                "children": [{   
                              "id": 21,
                              "text":"region 21"
                              }, {   
                              "id":22,
                              "text":"region 22"  
                             }]    
                }]   
                }
                ]}
    return HttpResponse(simplejson.dumps(context, ensure_ascii=False))

def get_zk_info(request):
    # context = {'code':200, 'msg':{'total':3, 'rows':[
    #                {'zkIp':'10.1.77.88', 'version':'3.4.5','recieved':100, 'send':100, 
    #                 'min_Latency':100, 'avg_Latency':100, 'max_Latency':100, 'connections':100,
    #                 'zxID':100, 'mode':100, 'nodeCount':100},
    #                {'zkIp':'10.1.77.88', 'version':'3.4.5','recieved':100, 'send':100, 
    #                 'min_Latency':100, 'avg_Latency':100, 'max_Latency':100, 'connections':100,
    #                 'zxID':100, 'mode':100, 'nodeCount':100},
    #                {'zkIp':'10.1.77.88', 'version':'3.4.5','recieved':100, 'send':100, 
    #                 'min_Latency':100, 'avg_Latency':100, 'max_Latency':100, 'connections':100,
    #                 'zxID':100, 'mode':100, 'nodeCount':100},
                   
    #           ]}}
    zkinfo = readyZKInfoList()
    print zkinfo
    context = {'code':200, 'msg':{'total':len(zkinfo), 'rows':zkinfo}}
    return HttpResponse(simplejson.dumps(context, ensure_ascii=False))

@csrf_exempt
def getZkAttr(request):
    # context = {'total':5, 'rows':[   
    #                  {'name':'Active MasterServer', 'value':'test85.hadoop,60000,1386848313615','group':'Zookeeper Info'},
    #                  {'name':'Backup MasterServer', 'value':'test87.hadoop,60000,1386848375241','group':'Zookeeper Info',},
    #                  {'name':'ROOT   Region  Addr', 'value':'test91.hadoop,60020,1386840637108','group':'Zookeeper Info',},
    #                  {'name':'Slave Peer  ', 'value':'dev81.hadoop,dev82.hadoop,dev83.hadoop:2181:/hbase','group':'Replication Info'},
    #                  {'name':'Peer  ID    ', 'value':'2','group':'Replication Info'},
    #                  {'name':'Peer  State', 'value':'Enable','group':'Replication Info'},
    #          ]}
    attr = readyZKAttrList()
    context = {'total':len(attr), 'rows':attr}
    return HttpResponse(simplejson.dumps(context, ensure_ascii=False))