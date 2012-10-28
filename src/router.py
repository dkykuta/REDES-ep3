from message import Message

class Router:
    def __init__(self, number, interwebz):
        self.number = number
        self.connection = interwebz
        self.networkStat = {}

    def printName(self):
        print "Mein Name ist Router #%s" % self.number

    def receiveMessage(self, msg):
        print "[%s] received %s" % (self, msg)
        if msg.msgType == "PING":
            newmsg = self.createPongMessage(msg)
            self.connection.send(self.number, newmsg.to, newmsg)
            return
        if msg.msgType == "NEIGHBOR":
            self.networkStat[msg.sender] = msg.msg

        if msg.to == self.number:
            # hey, this message is for me!
            if msg.msgType == "PONG":
                if self.number not in self.networkStat:
                    self.networkStat[self.number] = {}
                self.networkStat[self.number][msg.sender] = msg.msg
        else:
            msg.addToPath(self.number)
            links = self.networkStat[self.number]
            for link in links:
                if link not in msg.path:
                    self.connection.send(self.number, link, msg)

    def createPongMessage(self, pingMessage):
        return self.createMessage(pingMessage.sender, "PONG", self.connection.getDelay(pingMessage.sender, self.number))

    def createPingMessage(self):
        return self.createMessage("*", "PING", "")

    def createRequestMessage(self, to, request):
        return self.createMessage(to, "REQUEST", "")

    def createNeighborMessage(self):
        return self.createMessage("*", "NEIGHBOR", self.networkStat[self.number])

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
        
    def __str__(self): return "Router #%s" % self.number
    def __repr__(self): return self.__str__()
