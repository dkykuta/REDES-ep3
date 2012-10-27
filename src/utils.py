
# Return adjacency matrix and number of routers from given file
def parse_network_topology_file(fileName):
    f = open(fileName, "r")
    lines = f.readlines()
    f.close()
    
    matrix = []
    for s in lines:
        row = s.split()
        if len(row) > 0:
            matrix.append( s.split() )
    
    return matrix, len(matrix[0])
    
