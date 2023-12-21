#include <iostream>
#include <string>

int main(int argc, char* argv[]) {

    if (argc < 2) {
        std::cout << "No cmd arguments present" << std::endl;
        std::cout << "Running default service" << std::endl;
        return 0;
    }

    std::string launch_type(argv[1]);

    if (launch_type == "first-service") {
        std::cout << "Running first-service" << std::endl;
    }
    else if (launch_type == "second-service") {
        std::cout << "Running second-service" << std::endl;
    }
    else {
        std::cout << "Unknown launch type: \"" << launch_type << "\"" << std::endl;
        std::cout << "Running default service" << std::endl;
    }

    return 0;
}
