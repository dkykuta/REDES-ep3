#include <cstdio>
#include "utils.h"
#include "manager.h"

using namespace ccep2;

int main(int argc, char *argv[]) {

    Utils* utils = Utils::reference();
    Manager* manager = Manager::reference();

    if (!utils->ParseOptions(argc, argv)) {
        printf("Wrong program arguments. This program should be called as:\n");
        printf("\t./ep2 N pathToInputFile [-debug]\n");
        printf("\t(parameters not necessarily in this order)\n");
        return 0;
    }

    manager->Initialize();
    manager->Run();
    manager->Finalize();
    manager->PrintInfos();

    delete manager;
    delete utils;    
    
    return 0;
}
