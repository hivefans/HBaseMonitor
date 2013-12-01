from django.http.response import HttpResponse
from django.shortcuts import render_to_response
from django.utils import simplejson

def index(request):
    return render_to_response('index.html')

def tableTps(request):
    return render_to_response('table/table_tps.html')

def tableStorageInfo(request):
    return render_to_response('table/table_storage.html')

def getTableTps(request):
    context = {'code':200, 'msg':{'total':0, 'rows':[
                   {'tableName':123, 'writeCount':1234, 'readCount':'mt', 'totalCount':123,'writeTPS':123,'readTPS':123}, 
                   {'tableName':123, 'writeCount':1234, 'readCount':'mt', 'totalCount':123,'writeTPS':123,'readTPS':123}, 
                   {'tableName':123, 'writeCount':1234, 'readCount':'mt', 'totalCount':123,'writeTPS':123,'readTPS':123}
              ]}}
    return HttpResponse(simplejson.dumps(context, ensure_ascii=False))

def getTableStorageInfo(request):
    context = {'code':200, 'msg':{'total':0, 'rows':[
                   {'TableName':123, 'StoreFiles':1234, 'Stores':'mt', 'rootIndexSizeKB':123,'storefileIndexSizeMB':123,
                    'storefileSizeMB':123,'totalStaticBloomSizeKB':123,'currentCompactedKVs':123,'totalCompactingKVs':123,
                    'memStoreSizeMB':123},
                   {'TableName':123, 'StoreFiles':1234, 'Stores':'mt', 'rootIndexSizeKB':123,'storefileIndexSizeMB':123,
                    'storefileSizeMB':123,'totalStaticBloomSizeKB':123,'currentCompactedKVs':123,'totalCompactingKVs':123,
                    'memStoreSizeMB':123}
                   ]}} 
    return HttpResponse(simplejson.dumps(context, ensure_ascii=False))
