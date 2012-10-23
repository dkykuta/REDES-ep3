#ifndef UTILS_H_
#define UTILS_H_

#include <string>
#include <vector>
#include "safepqueue.h"
#include "safequeue.h"

namespace ccep2 {

class Mutex;
class Graph;
class Path;

typedef std::vector< std::vector<int> > IntMatrix;
typedef std::vector< std::vector<bool> > BoolMatrix;
typedef std::vector<Mutex*> MutexList;
typedef std::vector<int> IntList;

class Utils {
public:
    static Utils* reference() { return reference_ ? reference_ : reference_ = new Utils; }
    ~Utils();

    bool ParseOptions(int argc, char* argv[]);

    int PathCount() { return path_count_; }
    bool IsDebug() { return debug_; }
    Graph* LoadInputFile();
    int GetNumProcessors();
    int GetMaxOfIntMatrixRow(IntMatrix matrix, int row);
    
    void PrintGraphMatrix(Graph* G);

private:
    static Utils* reference_;

    int path_count_;
    bool debug_;
    std::string filename_;

    Utils();
};

}

#endif
