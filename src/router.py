class Router:
    def __init__(self, number):
        self.number = number

    def printName(self):
        print "Mein Name ist Router #", self.number

    def receiveMessage(self, msg):
        print "Router", self.number, "received message from", msg.sender, ". Content: '", msg.msg
