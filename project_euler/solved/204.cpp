// SIEVE

// Exclude multiples of primes between 100 and 5*10^8 (using sieve)
// And also exclude number of primes between 5*10^8 and 10^9,
//   which are 24491667 in number (can be easily calculated separately)

#include <iostream>
#include <cmath>

using namespace std;

long long int primes_soe_64(long long int n, long long int np[])
{
    if (n < 2) return 0;
    long long int i, k, m, nsq;
    long long int n2 = (n - 1) / 2;
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

int main()
{
    long long int i,j,m,n,nh,nhs;
    long long int* np = new long long int[51000000];
    nh=1000000000;
    n=500000000;
    bool* h=new bool[1000000000];
    for(i=0;i<nh;i++) {
        h[i]=true;
    }
    cout<<"sieve array initialized..."<<endl;

    m=primes_soe_64(n,np);
    cout<<"primes generated..."<<endl;

    for(i=25;i<m;i++) {                // 25 for prime number 101
        for(j=np[i];j<nh;j=j+np[i]) {
            h[j]=false;
        }
    }
    cout<<"sieving done..."<<endl;

    nhs=0;
    for(i=0;i<nh;i++) {
        if(h[i]) {
            nhs+=1;
        }
    }
    cout<<nhs-24491667<<endl;

    delete[] np,h;
    return 0;
}
