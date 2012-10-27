
class Message:
    def __init__(self, sender, msg):
        self.sender = sender
        self.msg = msg
        
    def __str__(self):
        return "Message (from %s): %s" % (self.sender, self.msg)
    def __repr__(self): return self.__str__()
