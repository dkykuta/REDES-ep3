from message import Message

class Interwebz:
    def __init__(self):
        self.routers = []
        self.network = []
        self.numRouters = 0

    def setNetStat(self, network, numRouters):
        self.network = network
        self.numRouters = numRouters

    def initialize(self, network, numRouters):
        self.setNetStat(network, numRouters)
        for r in self.routers:
            r.initializeStep1()
        for r in self.routers:
            r.initializeStep2()
        print "\n\n\n"
        for r in self.routers:
            print r.networkStat


    def addRouter(self, router):
        self.routers.append(router)
        print "Jetzt haben wir %s routers" % ( len(self.routers) )

    def getDelay(self, routerFrom, routerTo):
        return self.network[routerFrom][routerTo]

    def getNeighbour(self, routerNumber):
        return [x for x in xrange(self.numRouters) if self.network[routerNumber][x] != -1]

    def send(self, frm, target, msg):
        if self.network[frm][target] == -1:
            print "Hey, this two routers is not directly connected."
        else:
            self.routers[target].receiveMessage(msg)

    def doBroadcast(self, msg):
        requester = msg.sender
        print "Router #%d requested a broadcast" % ( requester )
        for i in self.getNeighbour(requester):
            self.routers[i].receiveMessage(msg)
