
class Table(object):
    def __init__(self):
        super(Table, self).__init__()
        self.regionList = []
        self.readRequestsCount = 0
        self.writeRequestsCount = 0
        self.requestsCount = 0
        self.storefiles = 0
        self.stores = 0
        self.rootIndexSizeKB = 0
        self.storefileIndexSizeMB = 0
        self.storefileSizeMB = 0
        self.totalStaticBloomSizeKB = 0
        self.totalStaticIndexSizeKB = 0
        self.currentCompactedKVs = 0
        self.totalCompactingKVs = 0
        self.memStoreSizeMB = 0

    def addRegionToTable(self, region):
        self.regionList.append(region)

    def computeTableInfoFromRegions(self):
        for region in self.regionList:
            self.readRequestsCount += region.readRequestsCount
            self.writeRequestsCount += region.writeRequestsCount
            self.requestsCount += region.requestsCount
            self.storefiles += region.storefiles
            self.stores += region.stores
            self.rootIndexSizeKB += region.rootIndexSizeKB
            self.storefileIndexSizeMB += region.storefileIndexSizeMB
            self.storefileSizeMB += region.storefileSizeMB
            self.totalStaticBloomSizeKB += region.totalStaticBloomSizeKB
            self.totalStaticIndexSizeKB += region.totalStaticIndexSizeKB
            self.currentCompactedKVs += region.currentCompactedKVs
            self.totalCompactingKVs += region.totalCompactingKVs
            self.memStoreSizeMB += region.memStoreSizeMB
