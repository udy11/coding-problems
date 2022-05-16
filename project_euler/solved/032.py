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
    print("Number of lines:",dn)
    ifl.close()
    return dt

p9 = read_data_1("032_p9.txt"," ")

pl = []
for d in p9:
    a1=d[0]
    b1=d[1]+10*d[2]+100*d[3]+1000*d[4]
    c1=d[5]+10*d[6]+100*d[7]+1000*d[8]
    if(a1*b1==c1):
        pl.append([a1,b1,c1])
    a2=d[0]+10*d[1]
    b2=d[2]+10*d[3]+100*d[4]
    c2=d[5]+10*d[6]+100*d[7]+1000*d[8]
    if(a2*b2==c2):
        pl.append([a2,b2,c2])

print(pl)
