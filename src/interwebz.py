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


        continueProcess = True
        while continueProcess:
            continueProcess = False
            for r in self.routers:
                if r.bellmanFordStep():
                    continueProcess = True

        for r in self.routers:
            v = []
            for i in xrange(self.numRouters):
                v.append(self.getBellmanFordDelayPath(r.number, i))
            r.bellmanfordDelayPaths = v
            r.bellmanfordDelayCosts = r.distances


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
        print "Message from Router #%d to Router #%d" % (frm, target)
        if self.network[frm][target] == -1:
            print "Hey, these two routers is not directly connected."
        else:
            self.messages[target].append(msg)

    def doBroadcast(self, msg):
        requester = msg.sender
        print "Router #%d requested a broadcast" % ( requester )
        for i in self.getNeighbour(requester):
            self.send(requester, i, msg)

    def getBellmanFordDelayPath(self, frm, to):
        path = []
        router = self.routers[frm]
        while router.number != to:
            path.append(router.number)
            router = self.routers[router.parent[to]]
        path.append(router.number)
        return path

