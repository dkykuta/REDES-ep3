#!/usr/bin/python
# -*- coding: utf-8 -*-

########################################################
#
#  MAC0448 - EP3
#  Diogo Haruki Kykuta   #USP: 6879613
#  Fernando Omar Aluani  #USP: 6797226
#
#   Esse é o principal arquivo do EP, o "main"
#   Rode-o para executar o programa.
#
########################################################
import sys
from src.router import Router
from src.interwebz import Interwebz
import src.utils as Utils

class Prompt:
    def __init__(self, interwebz):
        self.running = False
        self.interwebz = interwebz
        self.algorithms = { "ee": "dijkstra",
                            "vd": "bellmanford"}
        self.metrics = { "h": ["Hops", "%s hops"],
                         "a": ["Delay", "%s milisegundos"]}
        
    def Run(self):
        self.running = True
        print "Running user prompt... ( type 'quit' to exit )"
        while self.running:
            cmd = raw_input(">>> ")
            if cmd == "quit":
                self.running = False
                break
            pcmd = self.ParseCommand(cmd)
            if pcmd:
                self.ExecuteCommand(pcmd)

            
    def ParseCommand(self, cmd):
        tcmd = cmd.split()
        if len(tcmd) != 4:
            print "Unrecognized command. It should be: '<algorithm> <origin> <destination> <metric>'"
            return ()
        try:
            alg = str(tcmd[0])
            origin = int(tcmd[1])
            dest = int(tcmd[2])
            met = str(tcmd[3])
        except:
            print "Error parsing command arguments. Algorithm and Metric should be strings, origin and destination are numbers"
            return ()
        if not alg in self.algorithms.keys():
            print "Unrecognized algorithm %s" % ( alg )
            return ()
        if not met in self.metrics.keys():
            print "Unrecognized metric %s" % ( met )
            return ()
        if not (0 <= origin < self.interwebz.numRouters):
            print "No router matching ID #%s" % (origin)
            return ()
        if not (0 <= dest < self.interwebz.numRouters):
            print "No router matching ID #%s" % (dest)
            return ()
            
        return (self.algorithms[alg], self.interwebz.routers[origin], self.interwebz.routers[dest], self.metrics[met])
            
            
    def ExecuteCommand(self, pcmd):
        alg = pcmd[0]
        origin = pcmd[1]
        dest = pcmd[2]
        met = pcmd[3]
        
        check = alg+met[0]
        path = origin.__dict__[check+"Paths"][dest.number]
        pathstr = " ".join([str(p) for p in path])
        value = origin.__dict__[check+"Costs"][dest.number]
        
        print ( "%s ("+met[1]+")" ) % (pathstr, value)
        
########################################################
def Execute(argList):
    if len(argList) < 1:
        print "Wrong program call. Use: "
        print "EP3.py <network_topology_file_name>"
        return

    argFile = argList[0] # Network Topology File Name
    
    skynet = Interwebz()

    adjMatrix, numRouters = Utils.parse_network_topology_file(argFile)

    skynet.initialize(adjMatrix, numRouters)

    print "-"*50
    prompt = Prompt(skynet)
    prompt.Run()


    return
    
if __name__ == "__main__":
    Execute( sys.argv[1:] )
