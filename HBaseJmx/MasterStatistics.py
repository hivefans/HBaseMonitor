
class MasterStatistics(object):

    """docstring for MasterStatistics"""

    def __init__(self, masterStatisticsDict):
        super(MasterStatistics, self).__init__()
        self.masterStatisticsDict = masterStatisticsDict

    def set_MasterStatistics_Info(self):
        for item in self.masterStatisticsDict:
            if item == 'cluster_requests':
                self.cluster_requests = self.masterStatisticsDict[item]

    def get_MasterStatistics_Info(self):
        return self.cluster_requests
