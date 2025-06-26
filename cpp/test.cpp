#include <iostream>

int main() {
    int a = 10;
    int b = 0; // This will cause a division by zero error later
    int c;

    std::cout << "Before calculation." << std::endl; // Debug print

    // Simulate some calculation
    c = a / b; // Potential error point

    std::cout << "After calculation. Result: " << c << std::endl; // Debug print to check result

    // Another section of code
    for (int i = 0; i <= 5; ++i) {
        std::cout << "Loop iteration: " << i << std::endl; // Debug print for loop progress
    }

    return 0;
}
