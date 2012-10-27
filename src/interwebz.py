from message import Message

class Interwebz:
    def __init__(self):
        self.routers = []
        self.network = []
        self.numRouters = 0

    def setNetStat(self, network):
        self.network = network
        self.numRouters = len(network)

    def addRouter(self, router):
        self.routers.append(router)
        print "Jetzt haben wir %s routers" % ( len(self.routers) )

    def getNeighbour(self, router):
        return [x for x in xrange(self.numRouters) if self.network[router.number][x] != -1]

    def doBroadcast(self, requester):
        print "%s requested a broadcast" % ( requester )
        for i in self.getNeighbour(requester):
            self.routers[i].receiveMessage(Message(requester.number, "alo"*(requester.number+1)))
