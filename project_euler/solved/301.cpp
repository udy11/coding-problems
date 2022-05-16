// BOUTON'S THEOREM

// Bouton proved that for second player to have winning
// strategy, XOR of all heap sizes should be 0. Its proof
// is easy to understand and need not be mentioned here.
// So, X(n,2n,3n)=n^2n^3n.

// So, we need all n such that X(n,2n,3n)=0. Note that
// X(n,2n,3n)=X(2n,4n,6n). Hence once we have checked
// for n, we need not check for 2n.

// The given limit pow(2,30) poses some memory
// problems, which can be tackled by not checking for
// pow(2,30), because we know X(n,2n,3n)=0 for n=pow(2,30).

// Quique12 on 2nd page of forums has explained why the
// answer should be a fibonacci number, it is worth
// checking out.

#include <iostream>
#include <cmath>

using namespace std;

int main()
{
    int k, c;
    bool m;
    int n = pow(2, 30) - 1;
    bool * f = new bool[n];
    bool * g = new bool[n];
    for(int i = 0; i < n; i++) {
        f[i] = true;
    }
    for(int i = 1; i <= n; i++) {
        if(f[i - 1]) {
            c = i ^ (2 * i) ^ (3 * i);
            m = c == 0;
            k = i;
            while(k <= n) {
                g[k - 1] = m;
                f[k - 1] = false;
                k *= 2;
            }
        }
    }
    c = 1;          // already counting for pow(2,30)
    for(int i = 1; i <= n; i++) {
        if(g[i - 1]) {
            c++;
        }
    }
    cout << c << endl;
    delete[] f, g;
    return 0;
}
