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

    # prompt


    return
    
if __name__ == "__main__":
    Execute( sys.argv[1:] )
