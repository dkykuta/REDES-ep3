
# Return adjacency matrix and number of routers from given file
def parse_network_topology_file(fileName):
    f = open(fileName, "r")
    lines = f.readlines()
    f.close()
    
    matrix = []
    for s in lines:
        row = [ float(elem) for elem in s.split() ]
        if row:
            matrix.append(row)
    
    return matrix, len(matrix[0])
    
