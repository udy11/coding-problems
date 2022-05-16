// MATH

// Let d be the desired first digits then we
// need to find all integers n such that:
// (d + 1) * 10**i > 2**n >= d * 10**i
// for all integers i. equivalently:
// log10(d+1) + i > n * log10(2) >= log10(d) + i

// Precision errors may cause problems for high values
// but not for the given parameters

#include <iostream>
#include <cmath>

int main()
{
    int d = 123;
    double ld = std::log10(d);
    double ld1 = std::log10(d + 1);
    double il2 = 1.0 / std::log10(2.0);
    int i = 0, j = 0, t = 0;
    int fa, fb;
    while (j < 678910) {
        fa = std::floor(il2 * (ld + i));
        fb = std::floor(il2 * (ld1 + i));
        if (fa != fb) {
            j += 1;
            t = fb;
        }
        i += 1;
    }
    std::cout << t << std::endl;
    return 0;
}
