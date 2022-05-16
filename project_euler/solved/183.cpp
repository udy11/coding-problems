// MATH

// From simple calculus, one finds that
// required k is round(N / e), where e = exp(1)
// Then terminating decimals are only ones
// in which denominator of reduced fraction of
// N / k has only 2 or 5 as prime divisors

#include <iostream>
#include <cmath>

using namespace std;

bool dv25(int n)
{
    while(n > 1) {
        if(n % 2 == 0) {
            n = n / 2;
        }
        else if(n % 5 == 0) {
            n = n / 5;
        }
        else {
            return false;
        }
    }
    return true;
}

int gcd_32(int m, int n)
{
    int k;
    while(n != 0) {
        k = n;
        n = m % k;
        m = k;
    }
    return m;
}

int main()
{
    double ee = exp(1.0);
    double r;
    int k, ns;
    ns = 0;
    for(int n = 5; n < 10001; n++) {
        k = round(n / ee);
        k = k / gcd_32(n, k);
        if(dv25(k)) {
            ns -= n;
        }
        else {
            ns += n;
        }
    }
    cout << ns << endl;
}
