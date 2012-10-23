#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <string.h>
#include <unistd.h>

#include "utils.h"
#include "graph.h"

namespace ccep2 {

Utils* Utils::reference_ = NULL;

Utils::Utils() : path_count_(1), debug_(false) {
}

Utils::~Utils() {
}

bool checkArgOption(const char* arg_name, char* full_arg) {
	int arg_size = strlen(arg_name);
	return strncmp(full_arg, arg_name, arg_size) == 0 && (int)strlen(full_arg) == arg_size;
}


bool Utils::ParseOptions(int argc, char* argv[]) {
	int i;
	bool got_input = false;
    bool got_path_count = false;


	for (i=1; i<argc; i++) {
        if ( checkArgOption("-debug", argv[i]) ) {
            debug_ = true;
        }
        else {
            int n = atoi(argv[i]);
            if (n == 0 && !checkArgOption("0", argv[i])) {
                /*this parameter is the input filename*/
                filename_ = std::string(argv[i]);
                got_input = true;
            }
            else {
                path_count_ = n;
                got_path_count = true;
            }
        }
	}
	return got_input && got_path_count;
}

Graph* Utils::LoadInputFile() {
    std::ifstream ifs ( filename_.c_str(), std::ifstream::in );
    std::string line;
    int i, value;
    
    Graph* G = new Graph();
    i = 0;
    
    while (ifs.good()) {
        std::getline(ifs, line);
        if (line.size() <= 0)   break;
        std::istringstream linestream (line);

        G->PushRow();
        while(linestream.good()) {
            linestream >> value;
            G->PushValueInRow(i, value);
        }
        i++;
    }
    
    return G;
}

int Utils::GetNumProcessors() {
    int p = (int)sysconf(_SC_NPROCESSORS_ONLN);
    if (p < 2)  p = 2;
    return p;
}

void Utils::PrintGraphMatrix(Graph* G) {
    for (int i = 0; i < G->Size(); i++) {
        for (int j = 0; j < G->Size(); j++) {
            std::cout << (*G)(i, j) << " ";
        }
        std::cout << std::endl;
    }
}

int Utils::GetMaxOfIntMatrixRow(IntMatrix matrix, int row) {
    int max = 0;
    for (unsigned i = 0; i < matrix.size(); i++) {
        if (matrix[i] > matrix[max]) {
            max = (int)i;
        }
    }
    return max;
}

}
