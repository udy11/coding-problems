/*
SIEVE

Let x = a+r, y = a, z = a-r
Then, a*(4*r-a) = n
a and 4*r-a should be divisor pairs of n, for it to have integer solutions
Let p,q be a divisor pair of n (i.e., p*q = n)
Let a = p, so 4*r-a = q
Therefore, 4*r = p+q
Hence p+q should be divisible by 4
In addition, a > r ==> p > (p+q)/4 ==> 3*p > q

So just iterate over p and generate q so that p+q
is divisible by 4 and 3*p > q. Count all p*q
*/

#include <iostream>

int pe135(int n, int s)
{
    int *nc = new int[n];
    int p, q, m;
    for (p = 1; p < n; p++) nc[p] = 0;
    for (p = 1; p < n; p++) {
        q = 4 - (p % 4);
        m = p * q;
        while (q < 3 * p && m < n) {
            nc[m] += 1;
            q += 4;
            m = p * q;
        }
    }
    int sc = 0;
    for (p = 1; p < n; p++) {
        if (nc[p] == s) sc += 1;
    }
    delete[] nc;
    return sc;
}

int main()
{
    std::cout << pe135(1000000, 10) << std::endl;
    return 0;
}
