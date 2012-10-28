
class Message:
    def __init__(self, sender, to, msgType, msg):
        self.sender = sender
        self.to = to
        self.msgType = msgType
        self.msg = msg
        self.path = [ self.sender ]

    def addToPath(self, newElem):
        if newElem not in self.path:
            self.path.append(newElem)
        
    def __str__(self):
        return "Message (from %s to %s):\n [Type: %s] %s" % (self.sender, self.to, self.msgType, self.msg)
    def __repr__(self): return self.__str__()
