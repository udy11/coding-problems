/*
MATH

Note that if gcd(c, b)=1 then gcd(c, c-b)=1
c cannot be of form p0*p1*...*pn (p are primes)
rad(a*b*c) < c is equivalent to rad(a)*rad(b)*rad(c) < c for coprimes a,b,c
Use sieve to get all primes, prime divisors and rad upto n
Use prime divisors of c to get coprimes

In forums, people have further suggested that gcd(b, c) and gcd(a, c) need not be checked if gcd(a, b)=1
People have also found limits on a or b using rad(a*b*c) < c condition

C++ version of the algorithm takes about 2.2 seconds but
its Python-3 version takes about 10 minutes

Relevant resources:
abc Conjecture
OEIS A130510, A120498, A007947
http://www.phfactor.net/abc/index.php
*/

#include <iostream>
#include <cmath>

// Computes GCD using Binary GCD/Stein's Algorithm
long long int bgcd(long long int a, long long int b)
{
    long long int k, t;
    if (a == 0) return b;
    if (b == 0) return a;
    k = 0;
    while ((a | b) & 1 == 0) {
        a >>= 1;
        b >>= 1;
        k += 1;
    }
    while (a & 1 == 0) {
        a >>= 1;
    }
    while (b != 0) {
        while (b & 1 == 0) {
            b >>= 1;
        }
        if (a > b) {
            t = b;
            b = a;
            a = t;
        }
        b -= a;
    }
    return a << k;
}

// Generates prime numbers upto n using Sieve of Eratosthenes
long long int primes_soe(long long int n, long long int np[])
{
    if (n < 2) return 0;
    long long int i, k, m, nsq;
    long long int n2 = (n - 1) / 2;
    bool* ip = new bool[n2];
    for (i = 0; i < n2; i++) {
        ip[i] = true;
    }
    k = 3;
    nsq = std::floor(std::sqrt(n) + 0.5);
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

// Checks if any element of array c is > 1
bool anygt1(long long int *c, long long int n)
{
    for(long long int i = 0; i < n; i++){
        if (c[i] > 1) return true;
    }
    return false;
}

int main()
{
    long long int i, i0, j, m;
    long long int n = 120000;
    long long int *prms = new long long int[12000];
    long long int nprms = primes_soe(n, prms);
    
    // store all prime divisors, their counts and rad in pdvs, cpdvs and rad
    long long int** pdvs = new long long int*[n];
    for(i = 0; i < n; i++) pdvs[i] = new long long int[8];
    long long int *npdvs = new long long int[n];
    long long int** cpdvs = new long long int*[n];
    for(i = 0; i < n; i++) cpdvs[i] = new long long int[8];
    long long int *rad = new long long int[n];
    for(i = 0; i < n; i++) {
        rad[i] = 1;
        npdvs[i] = 0;
    }
    for (m = 0; m < nprms; m++) {
        for (j = prms[m]; j < n; j += prms[m]) {
            rad[j] *= prms[m];
            pdvs[j][npdvs[j]] = prms[m];
            npdvs[j] += 1;
        }
    }
    for (i = 2; i < n; i++) {
        for (j = 0; j < npdvs[i]; j++) {
            i0 = i;
            m = 0;
            while (i0 % pdvs[i][j] == 0) {
                i0 /= pdvs[i][j];
                m += 1;
            }
            cpdvs[i][j] = m;
        }
    }
    pdvs[0][0] = 1; npdvs[0] = 1;
    pdvs[1][0] = 1; npdvs[1] = 1;
    cpdvs[0][0] = 1;
    cpdvs[1][0] = 1;
    
    // c should not be of form p0*p1*...*pk
    long long int *cs = new long long int[n];
    long long int ncs = 0;
    for (i = 0; i < n; i++) {
        if (anygt1(cpdvs[i], npdvs[i])) {
            cs[ncs] = i;
            ncs += 1;
        }
    }

    long long int c2, tc = 0;
    bool *cc = new bool[(cs[ncs - 1] + 1) / 2];    // cc will define coprimes of c
    for (i = 0; i < ncs; i++) {
        c2 = (cs[i] + 1) / 2;
        for (j = 0; j < c2; j++) cc[j] = true;
        for (j = 0; j < npdvs[cs[i]]; j++) {
            for (m = pdvs[cs[i]][j]; m < c2; m += pdvs[cs[i]][j]) {
                cc[m] = false;
            }
        }
        for (j = 1; j < c2; j++) {
            if (cc[j] && rad[j] * rad[cs[i] - j] * rad[cs[i]] < cs[i] && bgcd(rad[j], rad[cs[i] - j]) == 1) {
                tc += cs[i];
            }
        }
    }
    std::cout << tc << std::endl;
    return 0;
}
