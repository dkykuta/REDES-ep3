from message import *

class Interwebz:
    def __init__(self):
        self.routers = []

    def setNetStat(self, network):
        self.network = network
        self.numRouters = len(network)

    def addRouter(self, router):
        self.routers.append(router)
        print "Jetzt haben wir", len(self.routers), "routers"

    def getNeighbor(self, router):
        return [x for x in range(self.numRouters) if self.network[router.number][x] != -1]

    def doBroadcast(self, requester):
        print "Router", requester.number, "requested a broadcast"
        for i in self.getNeighbor(requester):
            self.routers[i].receiveMessage(Message(requester.number, "alo"*(requester.number+1)))
