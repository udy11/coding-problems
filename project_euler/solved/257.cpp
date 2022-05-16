// GEOMETRY, EUCLID'S FORMULA FOR PYTHAGOREAN TRIPLES

/*
The geometric part is straightforward. Some help can be found at:
https://mathworld.wolfram.com/IncentralTriangle.html
EG can be found using formula there, use cosine formulas for cos terms.
AE and AG can be found by applying sine law in triangles AEC and BEC,
sin(C/2)/AE=sin(A)/CE and sin(C/2)/EB=sin(B)/CE,
denoting BC=a, AC=b and AB=c, and noting that AE+EB=c, we get AE=a*sin(C)/(sin(B)+sin(C)) and by applying sine
law in triangle ABC, we get AE=a*c/(b+c). Similarly, AG=a*b/(b+c).
Apply Heron's formula for area of triangle to both triangles
AEG and ABC, we get area(ABC)/area(AEG)=(a+b)*(a+c)/(b*c). The
simplification can also be done using Mathematica.

Equivalently we want integral solutions of a*(a+b+c)/(b*c) or p*a/(b*c)
where perimeter p=a+b+c. Let p*a=k*b*c for integer k.
Noting that a<=b<=c, we note that (a+b+c)*a<=3*a*c<=3*b*c, which
implies k*b*c<=3*b*c, meaning k<=3.
If a=b=c, k=3 and all such cases are valid.
If a=b<c, let 2*a/c=m, then m>1 from triangle inequality and
using a<c, m/2<1, which means m<2, whose only solution is m=1 which
gives a=b=c, thus there is no solution for a=b<c
If a<b=c, then (a+2*b)*a=k*b*b, (1+a/b)^2=k+1 but (1+a/b)^2
cannot be integer for a<b, thus no solutions for a<b=c
So we need to count all solutions for a=b=c (k=3) and a<b<c (k=1,2).
More specifically we want integral solutions for
(1) a*(a+b+c)=b*c
(2) a*(a+b+c)=2*b*c

Before proceeding to actual solution used in code, it would be worth
mentioning how a brute-force approach can be optimized.
1. p=a+b+c cannot be prime number except 3.
2. Once a case is found all its multiples are also valid cases, thus
   only co-prime cases gcd(a,b,c)=1 need to be searched.
3. For a given p, 1<=a<p/3, where latter closing to an equilateral
   triangle. And then (p-2*a)<2*b<(p-a), where former comes from
   triangle inequality and latter comes for small a and b<=c.
4. In point 3, first inequality can be improved. If a=1, then
   triangle inequality will be 1+b>c and we also have b<=c, so
   only possibility will be b=c, in which case we will need 1+2*b=k*b**2
   (k<=3), which is not valid for any b except 1 and k=3, thus a
   cannot be 1 except when b=c=1. Thus we can say 2<=a<p/3.
5. Alternate to point 3; for a given p, c can go from p/3 to p/2,
   where former closing to an equilateral triangle and latter to
   a+b=c. And (p/2-a)<b<(p-a)/2, where former comes from triangle
   inequality and latter comes for small a and b<c.

There's another approach worth mentioning that wasn't explored
further but might also work. From Eq (1) we can find a as:
2*a=-b-c+z, z=sqrt(b*b+6*b*c+c*c), so we want z to be integer
and z-b-c to be even. Similarly, from z*z=b*b+6*b*c+c*c, we
can find b as: b=-3*c+sqrt(8*c*c+z*z), so we want 8*c*c+z*z to
be square and > 9*c*c, which reduces to generalized Pell's equation

Pythagorean Triples and Euclid's Formula approach
Euclid's formula finds integral solutions to a*a+b*b=c*c
by substituting a=m*m-n*n, b=2*m*n, c=m*m+n*n, then all m>n
integers produce Pythagorean triples. In this approach, we
attempt to find similar substitutions. These can be found by
playing around with various substitutions. We can start by assuming
a linear substitution of a,b,c in x,y,z might reduce Eq (1) and (2)
proportional to x*x+y*y-z*z. We can brute-force for such
linear combinations by restricting the coefficients to 0,1,2,-1,-2.
It turns out this much alone can solve our problems. Origially, I
was just playing around with substitutions and noticed that
substitution a+b=x,a+c=y,b+c=z results into
a*(a+b+c)-b*c=(x*x+y*y-z*z)/2,
this substitution is equivalent to
a=(x+y-z)/2, b=(x-y+z)/2, c=(-x+y+z)/2
Notice how x-y+z, x+y-z and -x+y+z will be even because of properties
of Pythagorean triples. Now, substituting from Euclid's formula
we find that
(3) a=n*(m-n), b=m*(m-n), c=n*(m+n)
always satisifes Eq (1).
Strictly proving that such a substitution will indeed produce all
results will require some rigorous math, but for our purpose we can
check against results of brute-force approach.

By using above approach of assuming linear combinations and 
brute-forcing to find right combinations, we find a similar
combination for Eq (2) as:
a=2*(x+y-z), b=(x-2*y+2*z), c=(-x+y+z)
where x,y,z are Pythagorean triples. Equivalently:
(4) a=n*(2*m-n), b=m*(2*m-n), c=n*(m+n)
However, we notice that this substitution does not produce all
the results from brute-force approach. One can see that
if we substitute m->m/sqrt(2) and n->n*sqrt(2), then
we get the following substitution:
(5) a=2*n*(m-n), b=m*(m-n), c=n*(m+2*n)
We can explore other substitutions like m->m/sqrt(d)
and n->n*sqrt(d) for integers d or 1/d but they reproduce similar
or useless results. When we compare results from (4) and (5)
we can note that both produce all results of Eq (2).

Now we need to find proper restrictions on m,n for Eq (3-5).
Let P denote limit on perimeter p.

For Eq (3), using triangle inequalities:
a+b>c => m>2*n
a+c>b => 3*n>m
b+c>a => m*m+n*n>m*n (always satisifed)
So, m/3<n<m/2
p=m*(m+n), so 4*m*m/3<=P
For primitive solutions, gcd(m,n)>1 and m-n odd

For Eq (4), using triangle inequalities:
a+b>c => m*m>n*n
a+c>b => 2*n>m
b+c>a => m*m+n*n>m*n (always satisifed)
So, m/2<n<m
p=2*m*(m+n), so 3*m*m<=P
For primitive solutions, gcd(2*m-n,m+n)>1 and n odd
for some reason gcd(m,n) need not be checked

For Eq (5), using triangle inequalities:
a+b>c => m>2*n
a+c>b => 4*n>m
b+c>a => m*m+4*n*n>2*m*n (always satisifed)
So, m/4<n<m/2
p=m*(m+2*n), so 3*m*m/2<=P
For primitive solutions, gcd(m-n,m+2*n)>1, gcd(m,n)>1 and m odd
*/

#include <iostream>

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

int main()
{
    long long int m, n, p, pmax, count;
    pmax = 100000000;
    count = pmax / 3;
    
    m = 2;
    while (4 * m * m <= 3 * pmax) {
        n = m / 3 + 1;
        if (((m - n) & 1) == 0) n++;
        p = m * (m + n);
        while (p <= pmax && 2 * n < m) {
            if (bgcd(m, n) > 1) {
                n += 2;
                p = m * (m + n);
                continue;
            }
            count += pmax / p;
            n += 2;
            p = m * (m + n);
        }
        m++;
    }
    
    m = 2;
    while (3 * m * m <= pmax) {
        n = m / 2 + 1;
        if ((n & 1) == 0) n++;
        p = 2 * m * (m + n);
        while ((p <= pmax) && (n < m)) {
            if (bgcd(2 * m - n, m + n) > 1) {
                n += 2;
                p = 2 * m * (m + n);
                continue;
            }
            count += pmax / p;
            n += 2;
            p = 2 * m * (m + n);
        }
        m++;
    }
    
    m = 3;
    while (3 * m * m <= 2 * pmax) {
        n = m / 4 + 1;
        p = m * (m + 2 * n);
        while ((p <= pmax) && (2 * n < m)) {
            if (bgcd(m + 2 * n, m - n) > 1) {
                n++;
                p = m * (m + 2 * n);
                continue;
            }
            count += pmax / p;
            n++;
            p = m * (m + 2 * n);
        }
        m += 2;
    }
    
    std::cout << count << std::endl;
    return 0;
}
