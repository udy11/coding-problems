#include <iostream>

int main()
{
    int x, y;
    for (y = 2; y < 100; y++) {
        for (x = 0; x < y; x++) {
            std::cout << 2 * x + y << ' ' << y - x << '\n';
        }
    }
    return 0;
}
