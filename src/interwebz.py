from message import *

class Interwebz:
    def __init__(self):
        self.routers = []

    def addRouter(self, router):
        self.routers.append(router)
        print "Jetzt haben wir", len(self.routers), "routers"

    def receiveBroadcastRequest(self, router):
        print "router", router.number, "requested a broadcast"
        self.routers[1].receiveMessage(Message(42, "Jubs Nubs"))
