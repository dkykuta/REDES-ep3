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
from src.router import *
from src.interwebz import *
import src.utils as Utils

#TODO:
#  YO HARUKI!  Coloque aqui código que você quer que fique neste arquivo

########################################################
def Execute(argList):
    if len(argList) < 1:
        print "Wrong program call. Use: "
        print "EP3.py <network_topology_file_name>"
        return

    argFile = argList[0] # Network Topology File Name
    
    #TODO: implemente aqui o código pra executar o programa de fato
    skynet = Interwebz()

    tFile = open(argFile)

    adjMatrix = Utils.parse_network_topology_file(tFile)

    r1 = Router('Router 1')
    r2 = Router('Router 2')
    skynet.addRouter(r1)
    skynet.addRouter(r2)


    return
    
if __name__ == "__main__":
    Execute( sys.argv[1:] )
