
class Region(object):

    """docstring for Region"""

    def __init__(self, regionInfoDict):
        super(Region, self).__init__()
        self.regionInfoDict = regionInfoDict

    def set_Region_Info(self):
        regionValueDict = self.regionInfoDict['value']
        self.regionName = regionValueDict['nameAsString']
        self.currentCompactedKVs = regionValueDict['currentCompactedKVs']
        self.memStoreSizeMB = regionValueDict['memStoreSizeMB']
        self.readRequestsCount = regionValueDict['readRequestsCount']
        self.requestsCount = regionValueDict['requestsCount']
        self.rootIndexSizeKB = regionValueDict['rootIndexSizeKB']
        self.storefileIndexSizeMB = regionValueDict['storefileIndexSizeMB']
        self.storefileSizeMB = regionValueDict['storefileSizeMB']
        self.storefiles = regionValueDict['storefiles']
        self.stores = regionValueDict['stores']
        self.totalCompactingKVs = regionValueDict['totalCompactingKVs']
        self.totalStaticBloomSizeKB = regionValueDict['totalStaticBloomSizeKB']
        self.totalStaticIndexSizeKB = regionValueDict['totalStaticIndexSizeKB']
        self.writeRequestsCount = regionValueDict['writeRequestsCount']
