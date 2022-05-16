# BRUTE FORCE
# Find key by checking if 'the' exists in message or not

# Program written in quite a hotch-potch manner

def read_data_1(ifln,sep):
    ifl = open(ifln, 'r')
    dn = 0
    dt = []
    while True:
        lyn = ifl.readline().strip()
        i = 0; d0 = []
        if lyn == "":
            break
        while i < len(lyn):
            if not lyn[i] in sep:
                k = 1
                while i+k < len(lyn) and not lyn[i+k] in sep:
                    k += 1
                d0.append(int(lyn[i:i+k]))
                i += k + 1
            else:
                i += 1
        dt.append(d0)
        dn += 1
    ifl.close()
    return dt

dt = read_data_1("059_cipher1.txt",',')[0]
nd = len(dt)
t = 0
for i in range(103, 104):
    for j in range(111, 112):
        for k in range(100, 101):
            msg = ''
            key = chr(i) + chr(j) + chr(k)
            for m in range(0, nd-3, 3):
                m1 = i ^ dt[m]; m2 = j ^ dt[m+1]; m3 = k ^ dt[m+2]
                t += m1 + m2 + m3
                msg += chr(m1) + chr(m2) + chr(m3)
            msg += chr(103 ^ dt[nd - 1])
            print(msg)
t += 103 ^ dt[nd - 1]
print(t)
