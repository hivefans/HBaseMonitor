from Region import Region

class RegionServer(object):

    """docstring for RegionServer"""

    def __init__(self, regionServerInfoDict):
        super(RegionServer, self).__init__()
        self.regionServerInfoDict = regionServerInfoDict
        self.regions_List = []

    def set_RegionServer_Info(self):
        self.regionServerName = self.regionServerInfoDict['key']
        regionServerInfoDict = self.regionServerInfoDict['value']
        for item in regionServerInfoDict:
            if item == 'load':
                self.load = regionServerInfoDict[item]
            if item == 'maxHeapMB':
                self.maxHeapMB = regionServerInfoDict[item]
            if item == 'memStoreSizeInMB':
                self.memStoreSizeInMB = regionServerInfoDict[item]
            if item == 'numberOfRegions':
                self.numberOfRegions = regionServerInfoDict[item]
            if item == 'numberOfRequests':
                self.numberOfRequests = regionServerInfoDict[item]
            if item == 'storefileIndexSizeInMB':
                self.storefileIndexSizeInMB = regionServerInfoDict[item]
            if item == 'storefileSizeInMB':
                self.storefileSizeInMB = regionServerInfoDict[item]
            if item == 'storefiles':
                self.storefiles = regionServerInfoDict[item]
            if item == 'usedHeapMB':
                self.storeHeapMB = regionServerInfoDict[item]
            if item == 'regionsLoad':
                self.regionLoad_Total_Info_List = regionServerInfoDict[item]
        self.set_Regions_Info()

    def set_Regions_Info(self):
        for item in self.regionLoad_Total_Info_List:
            region = Region(item)
            region.set_Region_Info()
            self.regions_List.append(region)
