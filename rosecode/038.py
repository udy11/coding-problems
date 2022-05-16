cfr=[50,31,22,23,14,29,26,11,16,73,26,8,22,14,26,11,18,13,83,12,4,73,1,0,22,5,93,101]
n = len(cfr)

for i in range(97,123):
    for j in range(97,123):
        for k in range(97,123):
            for m in range(97,123):
                msg = ''
                for z in range(0, n, 4):
                    msg += chr(cfr[z]^i) + chr(cfr[z+1]^j) + chr(cfr[z+2]^k) + chr(cfr[z+3]^m)
                if 'myster' in msg:
                    print(msg)
                    input()
