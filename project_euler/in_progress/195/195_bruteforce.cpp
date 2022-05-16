#include <iostream>
#include <cmath>

int main()
{
    int a, b, c, count;
    double s, r;
    count = 0;
    for (c = 1; c < 1000; c++) {
        for (b = c / 2 + 1; b < c; b++) {
            for (a = c - b + 1; a < c / 2; a++) {
                s = 0.5 * (a + b + c);
                r = std::sqrt((s - a) * (s - b) * (s - c) / s);
                if (r <= 100) {
                    if (b*b + c*c - a*a == b*c) {
                        count++;
                        std::cout << r << ' ' << a << ' ' << b << ' ' << c << " m1\n";
                    }
                    if (a*a + c*c - b*b == a*c) {
                        count++;
                        std::cout << r << ' ' << a << ' ' << b << ' ' << c << " m2\n";
                    }
                    if (a*a + b*b - c*c == a*b) {
                        count++;
                        std::cout << r << ' ' << a << ' ' << b << ' ' << c << " m3\n";
                    }
                }
            }
        }
    }
    std::cout << count << std::endl;
}
