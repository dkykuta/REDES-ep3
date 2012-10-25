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
import src.teste as T

#TODO:
#  YO HARUKI!  Coloque aqui código que você quer que fique neste arquivo

########################################################
def Execute(argList):
    if len(argList) < 1:
        print "Wrong program call. Use: "
        print "EP3.py <network_topology_file_name>"
        T.alo()
        return

    argFile = argList[0] # Network Topology File Name
    
    #TODO: implemente aqui o código pra executar o programa de fato

    return
    
if __name__ == "__main__":
    Execute( sys.argv[1:] )
