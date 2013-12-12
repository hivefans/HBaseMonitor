from HBaseJmx.Table import Table
from RegionServer import RegionServer
from datetime import datetime


class Master(object):

    """docstring for Master"""

    def __init__(self, masterDict):
        super(Master, self).__init__()
        self.masterDict = masterDict
        self.RegionServers_List = []
        self.Tables_Dict = {}

    def set_Master_Info(self):
        for item in self.masterDict:
            if item == "ClusterId":
                self.ClusterId = self.masterDict[item]
            if item == "MasterStartTime":
                self.MasterStartTime = self.masterDict[item] / 1000
            if item == "MasterActiveTime":
                self.MasterActiveTime = self.masterDict[item] / 1000
            if item == "ServerName":
                self.ServerName = self.masterDict[item]
            if item == "AverageLoad":
                self.AverageLoad = self.masterDict[item]
            if item == "ZookeeperQuorum":
                self.ZookeeperQuorum = self.masterDict[item]
            if item == "RegionServers":
                self.RegionServers_Total_Info_List = self.masterDict[item]
        self.set_RegionServers_Info()

    def set_RegionServers_Info(self):
        for item in self.RegionServers_Total_Info_List:
            regionServer = RegionServer(item)
            regionServer.set_RegionServer_Info()
            self.RegionServers_List.append(regionServer)
        self.set_Table_Info()

    def set_Table_Info(self):
        for regionServer in self.RegionServers_List:
            for region in regionServer.regions_List:
                tableName = region.regionName.split(',')[0]
                if tableName in self.Tables_Dict:
                    self.Tables_Dict[tableName].addRegionToTable(region)
                else:
                    table = Table()
                    table.addRegionToTable(region)
                    self.Tables_Dict[tableName] = table
        self.computeTableInfo()

    def computeTableInfo(self):
        for table in self.Tables_Dict:
            self.Tables_Dict[table].computeTableInfoFromRegions()
