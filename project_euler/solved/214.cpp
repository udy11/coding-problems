// SIEVE

// Generate all totients using sieve.
// Rest is straightforward.

#include <iostream>
#include <cmath>

using namespace std;

int primes_soe_32(int n, int np[]);

int main()
{
    int m, n, i, j;
    int pc, tt;
    long long int psm;
    int* np = new int[2433655];
    n = 40000000;
    m = primes_soe_32(n, np);
    
// Generating all Totients
    long long int* phi = new long long int[n];
    for (i = 0; i < n; i++) {
        phi[i] = i + 1;
    }
    for (j = 0; j < m; j++) {
        i = np[j] - 1;
        while (i < n) {
            phi[i] = phi[i] * (np[j] - 1) / np[j];
            i += np[j];
        }
    }
    
    psm = 0;
    for (j = 2; j < m; j++) {
        pc = 3;
        tt = np[j] - 1;
        while (pc < 25 && tt > 2) {
            tt = phi[tt - 1];
            pc++;
        }
        if (pc == 25 && tt == 2) {
            psm += np[j];
        }
    }
    
    cout << "Sum: " << psm << endl;

    delete[] np, phi;
    return 0;
}

int primes_soe_32(int n, int np[])
{
    if (n < 2) return 0;
    int i, k, m, nsq;
    int n2 = (n - 1) / 2;
    bool* ip = new bool[n2];
    for (i = 0; i < n2; i++) {
        ip[i] = true;
    }
    k = 3;
    nsq = floor(sqrt(n) + 0.5);
    while (k <= nsq) {
        for (i = k * k / 2 - 1; i < n2; i += k) {
            ip[i] = false;
        }
        while (k <= nsq) {
            k += 2;
            if(ip[k / 2 - 1]) break;
        }
    }
    m = 1;
    np[0] = 2;
    for (i = 0; i < n2; i++) {
        if (ip[i]) {
            np[m] = 2 * i + 3;
            m++;
        }
    }
    delete[] ip;
    return m;
}
