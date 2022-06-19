# EULER's PENTAGONAL NUMBER THEOREM

# Algorithm is to calculate integer partition
# using the recursive relation coming from
# Euler's Pentagonal Number Theorem

# OEIS A000041

def intpart(m):
    ''' (int) -> int
        Function to calculate Integer Partitions
        using recurrence relation
        from Euler's Pentagonal Number Theorem:
        p(n) = Sum[ (-1)**j (p(n- j(3j-1)/2) + p(n- j(3j+1)/2)) ]
        until p(0) or p(n-1) are hit in summation
        where p(n) is integer partition

        Generates OEIS A000041
    '''
    if m == 0:
        return 1
    elif m < 4:
        return m
    t = [0 for i in range(m+1)]
    t[0] = 1
    for i in range(1, 4):
        t[i] = i
    def p(n):
        nonlocal t
        if t[n] != 0:
            return t[n]
        else:
            ps = 0
            j = 1
            jp = 2
            while jp <= n:
                ps += (-1)**(j+1) * p(n - jp)
                j += 1
                jp = j * (3*j+1) // 2
            j = 1
            jn = 1
            while jn <= n:
                ps += (-1)**(j+1) * p(n - jn)
                j += 1
                jn = j * (3*j-1) // 2
            t[n] = ps
            return ps
    return p(m)

print(intpart(100))
