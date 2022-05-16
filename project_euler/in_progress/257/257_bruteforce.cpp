// Problem reduces to finding all a <= b <= c such that (a * p) / (b * c) is integer (let it be k), where p = a + b + c. Some points:
// 1. Only prime p possible is 3
// 2. All multiples of 3 have one known case where a=b=c, p=3*a
// 3. Once a case is found, all its multiples are also valid, thus focus should be on finding co-prime cases
// 4. Using a<c and b<c, we have a*(a+b+c)<3*a*c, which gives p*a=k*b*c<3*b*c, which means k<3. In case a=b=c we have k=3, with which count can be initialized
// 5. a=b case leads to either a=0, 2*a=c or a=c, where first 2 are not possible and last is already counted
// 6. For a given p, 1<=a<p/3, where latter closing to an equilateral triangle. And then (p/2-a)<b<=(p-a)/2, where former comes from triangle inequality and latter comes for small a and b<=c
// 6.1 First inequality can be improved. If a=1, then triangle inequality will be 1+b>c and we also have b<=c, so only possibility will be b=c, in which case we will need 1+2*b=k*b**2 (k<=3), which is not valid for any b except 1 and k=3, thus a cannot be 1 except when b=c=1
// 7. For a given p, c can go from p/3 to p/2, where former closing to an equilateral triangle and latter to a+b=c. And (p/2-a)<b<(p-a)/2, where former comes from triangle inequality and latter comes for small a and b<c

// Known answers:
// 10: 3
// 100: 46
// 1000: 610
// 10000: 7677 (~7s)
// 20000: 16289 (~53s)
// 100000: 92318

#include <iostream>
#include <cmath>

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

int main()
{
    int p, a, b, c;
    int n = 20000;
    int count = n / 3;    // starting with all a=b=c cases
    
    int* primes = new int[n];
    int np = primes_soe_32(n, primes);
    int ip = 4;
    
    for (p = 8; p <= n; p++) {
        if (primes[ip] == p) {
            ip++;
            continue;
        }
        for (a = 2; a < p / 3; a++) {
            for (b = p / 2 - a + 1; 2 * b < p - a; b++) {
                c = p - a - b;
        /*for (c = p / 3 + 1; c < p / 2; c++) {
            for (b = c / 2 + 1; b < c; b++) {
                a = p - b - c;*/
            if (p * a == b * c || p * a == 2 * b * c) {
            //if (p * a == 2 * b * c) {
                    if (2 * b == (p - a)) std::cout << p << ' ' << a << ' ' << b << ' ' << c << '\n';
                    count++;
                }
            }
        }
    }
    std::cout << count << std::endl;
}
