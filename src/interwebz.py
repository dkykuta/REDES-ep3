from message import Message
from router import Router

class Interwebz:
    def __init__(self):
        self.routers = []
        self.network = []
        self.numRouters = 0
        self.messages = {}

    def setNetStat(self, network, numRouters):
        self.network = network
        self.numRouters = numRouters
        for i in xrange(numRouters):
            self.addRouter(Router(i, self))


    def initialize(self, network, numRouters):
        self.setNetStat(network, numRouters)

        for r in self.routers:
            r.initializeStep1()

        continueProcess = True
        while continueProcess:
            continueProcess = False
            for r in self.routers:
                if r.processIncomingMessages():
                    continueProcess = True
        
        for r in self.routers:
            r.initializeStep2()

        continueProcess = True
        while continueProcess:
            continueProcess = False
            for r in self.routers:
                if r.processIncomingMessages():
                    continueProcess = True
        
        for r in self.routers:
            r.dijkstra()


    def addRouter(self, router):
        self.routers.append(router)
        self.messages[router.number] = []

    def getDelay(self, routerFrom, routerTo):
        return self.network[routerFrom][routerTo]

    def hasMessage(self, router):
        return self.messages[router] != []

    def getMessage(self, router):
        return self.messages[router].pop(0)

    def getNeighbour(self, routerNumber):
        return [x for x in xrange(self.numRouters) if self.network[routerNumber][x] != -1]

    def send(self, frm, target, msg):
        if self.network[frm][target] == -1:
            print "Hey, these two routers is not directly connected."
        else:
            self.messages[target].append(msg)

    def doBroadcast(self, msg):
        requester = msg.sender
        print "Router #%d requested a broadcast" % ( requester )
        for i in self.getNeighbour(requester):
            self.send(requester, i, msg)
