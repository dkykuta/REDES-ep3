class Interwebz:
    def __init__(self):
        self.routers = []

    def addRouter(self, router):
        self.routers.append(router)
        print "Jetzt haben wir", len(self.routers), "routers"
