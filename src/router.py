from message import Message

MAX_COST=1e100

class Router:
    def __init__(self, number, interwebz):
        self.number = number
        self.connection = interwebz

        self.networkStat = {}
        self.dijkstraDelayCosts = []
        self.dijkstraDelayPaths = []
        self.dijkstraHopsCosts = []
        self.dijkstraHopsPaths = []

        self.distances = {}
        self.parent = {}
        self.neighborhood = []
        self.bellmanfordDelayCosts = []
        self.bellmanfordDelayPaths = []
        self.bellmanfordHopsCosts = []
        self.bellmanfordHopsPaths = []

    def __str__(self): return "Router #%s" % self.number
    def __repr__(self): return self.__str__()

    def printName(self):
        print "Mein Name ist Router #%s" % self.number

    def receiveMessage(self):
        msg = self.connection.getMessage(self.number)
        print "[%s] received %s" % (self, msg)
        if msg.msgType == "PING":
            newmsg = self.createPongMessage(msg)
            self.connection.send(self.number, newmsg.to, newmsg)
            return msg
        if msg.msgType == "PING_BF":
            newmsg = self.createPongBFMessage(msg)
            self.connection.send(self.number, newmsg.to, newmsg)
            return msg
        if msg.msgType == "NEIGHBOR":
            self.networkStat[msg.sender] = msg.msg

        if msg.msgType == "DISTANCE":
            return msg

        if msg.to == self.number:
            # hey, this message is for me!
            if msg.msgType == "PONG":
                if self.number not in self.networkStat:
                    self.networkStat[self.number] = {}
                self.networkStat[self.number][msg.sender] = msg.msg
            if msg.msgType == "PONG_BF":
                self.distances[msg.sender] = msg.msg
                self.parent[msg.sender] = msg.sender
                if msg.sender not in self.neighborhood:
                    self.neighborhood.append(msg.sender)
        else:
            msg.addToPath(self.number)
            links = self.networkStat[self.number]
            for link in links:
                if link not in msg.path:
                    self.connection.send(self.number, link, msg)

        return msg

    def createPongMessage(self, pingMessage):
        return self.createMessage(pingMessage.sender, "PONG", self.connection.getDelay(pingMessage.sender, self.number))

    def createPongBFMessage(self, pingMessage):
        return self.createMessage(pingMessage.sender, "PONG_BF", self.connection.getDelay(pingMessage.sender, self.number))

    def createPingMessage(self):
        return self.createMessage("*", "PING", "")

    def createPingBFMessage(self):
        return self.createMessage("*", "PING_BF", "")

    def createRequestMessage(self, to, request):
        return self.createMessage(to, "REQUEST", "")

    def createNeighborMessage(self):
        return self.createMessage("*", "NEIGHBOR", self.networkStat[self.number])

    def createDistanceMessage(self, to):
        return self.createMessage(to, "DISTANCE", self.distances)

    def createMessage(self, to, msgType, msg):
        m = Message(self.number, to, msgType, msg)
        return m

    def broadcast(self, msg):
        self.connection.doBroadcast(msg)

    def sendMessage(self, msg):
        if msg.to in self.networkStat[self.number]:
            self.connection.send(self.number, msg.to, msg)
        else:
            self.connection.doBroadcast(msg)
        
    def initializeStep1(self):
        self.broadcast(self.createPingMessage())

    def initializeStep2(self):
        self.broadcast(self.createNeighborMessage())

    def processIncomingMessages(self):
        if not self.connection.hasMessage(self.number):
            return False
        while self.connection.hasMessage(self.number):
            self.receiveMessage()
        return True 

    def dijkstra(self):
        matrizComPesos = []
        matrizSemPesos = []

        numR = len(self.networkStat)

        for i in xrange(numR):
            matrizComPesos.append([-1] * numR)
            matrizSemPesos.append([-1] * numR)

        for routerN in self.networkStat.keys():
            neighborhood = self.networkStat[routerN]
            for neighbor in neighborhood.keys():
                matrizComPesos[routerN][neighbor] = neighborhood[neighbor]
                matrizSemPesos[routerN][neighbor] = 1

        self.dijkstraDelayPaths, self.dijkstraDelayCosts = self.dijkstraC(matrizComPesos, numR)
        self.dijkstraHopsPaths, self.dijkstraHopsCosts = self.dijkstraC(matrizSemPesos, numR)

    def dijkstraC(self, adjM, numRouters):
        pre = range(numRouters)
        custosAtuais = [MAX_COST]*numRouters

        N = [True] * numRouters

        for i in xrange(numRouters):
            if adjM[self.number][i] != -1:
                custosAtuais[i] = adjM[self.number][i]
                pre[i] = self.number

        while True:
            minV = -1
            minC = MAX_COST
            for i in xrange(numRouters):
                if custosAtuais[i] < minC and N[i]:
                    minV = i
                    minC = custosAtuais[i]
            if minV == -1:
                break

            N[minV] = False
            for i in xrange(numRouters):
                if adjM[minV][i] != -1:
                    if custosAtuais[minV] + adjM[minV][i] < custosAtuais[i]:
                        custosAtuais[i] = custosAtuais[minV] + adjM[minV][i]
                        pre[i] = minV

        bestPaths = []
        for i in xrange(numRouters):
            pathToI = [i]
            j = i
            while pre[j] != self.number:
                pathToI.insert(0, pre[j])
                j = pre[j]
            pathToI.insert(0, pre[j])

            bestPaths.append(pathToI)

        return bestPaths, custosAtuais


    def sendDistanceToNeighbor(self):
        for neighbor in self.neighborhood:
            self.connection.send(self.number, neighbor, self.createDistanceMessage(neighbor))

    
    def bellmanFordStep(self):
        if self.distances == {}:
            self.broadcast(self.createPingBFMessage())
            while self.connection.hasMessage(self.number):
                self.receiveMessage()
            self.sendDistanceToNeighbor()
            return True
        else:
            retVal = False
            while self.connection.hasMessage(self.number):
                msg = self.receiveMessage()
                if msg.msgType != "DISTANCE":
                    continue
                distanceV, vFrom = msg.msg, msg.sender
                for router in distanceV.keys():
                    if not self.distances.has_key(router):
                        self.distances[router] = distanceV[router] + self.distances[vFrom]
                        self.parent[router] = vFrom
                        retVal = True
                    else:
                        d = distanceV[router] + self.distances[vFrom]
                        if d < self.distances[router]:
                            self.distances[router] = d
                            self.parent[router] = vFrom
                            retVal = True
            if retVal:
                self.sendDistanceToNeighbor()
            return retVal
