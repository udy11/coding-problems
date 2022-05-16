/*
ALGORITHM
Store all ways to partition any k-digit number in a deque p
Skip the combinations that will not satisfy the condition
Such invalid partitions are:
For even k, all partitions that don't have k/2 entry
For odd k, all partitions that don't have 1+k/2 entry or their max entry is k/2
Maybe in odd k, there might be further restriction that if max entry is k/2, it should occur twice, but i don't have any proof
Then simply loop over all squares upto 10^12 and check over valid partitions if sum matches

Another optimization was suggested by ecnerwala in forums:
Only those numbers need to be checked whose %9 is 0 or 1
Though I couldn't understand the reason but it makes the code much faster
*/

#include <iostream>
#include <deque>
#include <cmath>

template <typename tmp>
tmp deqmax(std::deque< tmp > d) {
    tmp max = d[0];
    for (int i = 1; i < d.size(); i++) {
        if (d[i] > max) max = d[i];
    }
    return max;
}

int main()
{
    int n = 13;
    std::deque< std::deque< std::deque< int> > > p;
    std::deque< std::deque< int > > pi;
    std::deque< int > pij;
    pij.push_back(0);
    pi.push_back(pij);
    p.push_back(pi);
    pij.clear();
    pi.clear();
    pij.push_back(1);
    pi.push_back(pij);
    p.push_back(pi);
    pij.clear();
    pi.clear();
    for (int k = 2; k < n; k++) {
        pij.push_back(k);
        pi.push_back(pij);
        pij.clear();
        for (int m = 1; m < k; m++) {
            for (int i0 = 0; i0 < p[m].size(); i0++) {
                for (int i1 = 0; i1 < p[k-m].size(); i1++) {
                    pij = p[m][i0];
                    for (int j1 = 0; j1 < p[k-m][i1].size(); j1++) pij.push_back(p[k-m][i1][j1]);
                    //std::merge(p[m][i0].begin(), p[m][i0].end(), p[k-m][i1].begin(), p[k-m][i1].end(), std::back_inserter(pij)); // can be used instead of above 2 lines but needs #include <algorithm>
                    bool cp = false;
                    for (int l = 0; l < pi.size(); l++) {
                        if (pij == pi[l]) {
                            cp = true;
                            break;
                        }
                    }
                    if (!cp) pi.push_back(pij);
                    pij.clear();
                }
            }
        }
        p.push_back(pi);
        pi.clear();
    }
    for (int k = 2; k < p.size(); k+=2) {
        int i = 0;
        while(i < p[k].size()) {
            bool cp = true;
            for (int j = 0; j < p[k][i].size(); j++) {
                if (p[k][i][j] == k / 2) {
                    cp = false;
                    break;
                }
            }
            if (cp) p[k].erase(p[k].begin() + i);
            else i++;
        }
    }
    for (int k = 3; k < p.size(); k+=2) {
        int i = 0;
        while(i < p[k].size()) {
            bool cp = true;
            for (int j = 0; j < p[k][i].size(); j++) {
                if (p[k][i][j] == 1 + k / 2) {
                    cp = false;
                    break;
                }
            }
            if (cp && deqmax(p[k][i]) == k / 2) cp = false;
            if (cp) p[k].erase(p[k].begin() + i);
            else i++;
        }
    }
    
    long long int kf = 1000000;
    long long int t = (long long int) kf * kf;

    // Original implmentation
    /*for (long long int k = 4; k < kf; k++) {
        long long int k2 = (long long int) k * k;
        long long int nk = std::floor(std::log10(k2)) + 1;
        for (int i = 0; i < p[nk].size(); i++) {
            long long int s = 0;
            long long int kq = k2;
            for (int j = 0; j < p[nk][i].size(); j++) {
                long long int j1 = std::pow(10, p[nk][i][j]);
                long long int kq1 = kq / j1;
                long long int r = kq % j1;
                s += r;
                kq = kq1;
            }
            if (s == k) {
                t += k2;
                break;
            }
        }
    }*/
    // Implementation after using ecnerwala's suggestion
    for (long long int k = 9; k < kf; k+=9) {
        long long int k2 = (long long int) k * k;
        long long int nk = std::floor(std::log10(k2)) + 1;
        for (int i = 0; i < p[nk].size(); i++) {
            long long int s = 0;
            long long int kq = k2;
            for (int j = 0; j < p[nk][i].size(); j++) {
                long long int j1 = std::pow(10, p[nk][i][j]);
                long long int kq1 = kq / j1;
                long long int r = kq % j1;
                s += r;
                kq = kq1;
            }
            if (s == k) {
                t += k2;
                break;
            }
        }
    }
    for (long long int k = 10; k < kf; k+=9) {
        long long int k2 = (long long int) k * k;
        long long int nk = std::floor(std::log10(k2)) + 1;
        for (int i = 0; i < p[nk].size(); i++) {
            long long int s = 0;
            long long int kq = k2;
            for (int j = 0; j < p[nk][i].size(); j++) {
                long long int j1 = std::pow(10, p[nk][i][j]);
                long long int kq1 = kq / j1;
                long long int r = kq % j1;
                s += r;
                kq = kq1;
            }
            if (s == k) {
                t += k2;
                break;
            }
        }
    }
    std::cout << t << std::endl;
    return 0;
}
