
class Router:
    def __init__(self, number):
        self.number = number

    def printName(self):
        print "Mein Name ist Router #%s" % self.number

    def receiveMessage(self, msg):
        print "[%s] received %s" % (self, msg)
        
    def __str__(self): return "Router #%s" % self.number
    def __repr__(self): return self.__str__()
