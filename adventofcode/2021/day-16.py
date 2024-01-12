# Pretty messy but works...
import sys

def operation(t, items = 0):
    if t == 0:
        op = 'sum'
    elif t == 1:
        op = 'prd'
    elif t == 2:
        op = 'min'
    elif t == 3:
        op = 'max'
    elif t == 5:
        op = 'grt'
    elif t == 6:
        op = 'lst'
    elif t == 7:
        op = 'eqt'
    if items > 0:
        return op + '-' + str(items)
    else:
        return op

def hex2bin(inp):
    ''' Not an actual hex to bin converter '''
    s = ''
    for c in inp:
        s += format(int('0x' + c, 16), '04b')
    return s

def prod(nn):
    p = 1
    for n in nn:
        p *= n
    return p

def optn(o, vals):
    if o == 'sum':
        return sum(vals)
    elif o == 'prd':
        return prod(vals)
    elif o == 'min':
        return min(vals)
    elif o == 'max':
        return max(vals)
    elif o == 'grt':
        return int(vals[0] > vals[1])
    elif o == 'lst':
        return int(vals[0] < vals[1])
    elif o == 'eqt':
        return int(vals[0] == vals[1])

def evaluate(ops):
    def ev():
        nonlocal k
        if k >= n:
            return
        if isinstance(ops[k], int):
            k += 1
            return ops[k-1]
        elif len(ops[k]) == 3:
            o = ops[k]
            k += 2
            vals = []
            while ops[k] != ')':
                vals.append(ev())
            k += 1
            return optn(o, vals)
        else:
            o = ops[k][:3]
            m = int(ops[k][4:])
            k += 1
            vals = []
            for i in range(m):
                vals.append(ev())
            return optn(o, vals)
    n = len(ops)
    k = 0
    return ev()

def acd16(packet):
    def p1(subpacket):
        nonlocal vt
        n = len(subpacket)
        if n < 11:
            return
        v = int('0b' + subpacket[:3], 2)
        t = int('0b' + subpacket[3:6], 2)
        vt += v
        if t == 4:
            k = 6
            s = ''
            while True:
                if k < n:
                    if subpacket[k] == '0':
                        s += subpacket[k+1:k+5]
                        k += 5
                        break
                    s += subpacket[k+1:k+5]
                    k += 5
                if k >= n:
                    break
            ops.append(int('0b' + s, 2))
            p1(subpacket[k:])
        elif subpacket[6] == '0':
            ops.append(operation(t))
            ops.append('(')
            l = int('0b' + subpacket[7:22], 2)
            p1(subpacket[22:22+l])
            ops.append(')')
            p1(subpacket[22+l:])
        elif subpacket[6] == '1':
            ns = int('0b' + subpacket[7:18], 2)
            ops.append(operation(t, items = ns))
            p1(subpacket[18:])
    pkt = hex2bin(packet)
    vt = 0
    ops = []
    p1(pkt)
    return vt, evaluate(ops)

in00 = 'D2FE28'
in01 = '38006F45291200'
in02 = 'EE00D40C823060'
in03 = '8A004A801A8002F478'
in04 = '620080001611562C8802118E34'
in05 = 'C0015000016115A2E0802F182340'
in06 = 'A0016C880162017C3686B18A3D4780'
in07 = 'A052E04CFD9DC0249694F0A11EA2044E200E9266766AB004A525F86FFCDF4B25DFC401A20043A11C61838600FC678D51B8C0198910EA1200010B3EEA40246C974EF003331006619C26844200D414859049402D9CDA64BDEF3C4E623331FBCCA3E4DFBBFC79E4004DE96FC3B1EC6DE4298D5A1C8F98E45266745B382040191D0034539682F4E5A0B527FEB018029277C88E0039937D8ACCC6256092004165D36586CC013A008625A2D7394A5B1DE16C0E3004A8035200043220C5B838200EC4B8E315A6CEE6F3C3B9FFB8100994200CC59837108401989D056280803F1EA3C41130047003530004323DC3C860200EC4182F1CA7E452C01744A0A4FF6BBAE6A533BFCD1967A26E20124BE1920A4A6A613315511007A4A32BE9AE6B5CAD19E56BA1430053803341007E24C168A6200D46384318A6AAC8401907003EF2F7D70265EFAE04CCAB3801727C9EC94802AF92F493A8012D9EABB48BA3805D1B65756559231917B93A4B4B46009C91F600481254AF67A845BA56610400414E3090055525E849BE8010397439746400BC255EE5362136F72B4A4A7B721004A510A7370CCB37C2BA0010D3038600BE802937A429BD20C90CCC564EC40144E80213E2B3E2F3D9D6DB0803F2B005A731DC6C524A16B5F1C1D98EE006339009AB401AB0803108A12C2A00043A134228AB2DBDA00801EC061B080180057A88016404DA201206A00638014E0049801EC0309800AC20025B20080C600710058A60070003080006A4F566244012C4B204A83CB234C2244120080E6562446669025CD4802DA9A45F004658527FFEC720906008C996700397319DD7710596674004BE6A161283B09C802B0D00463AC9563C2B969F0E080182972E982F9718200D2E637DB16600341292D6D8A7F496800FD490BCDC68B33976A872E008C5F9DFD566490A14'
in08 = 'C200B40A82'
in09 = '04005AC33890'
in10 = '880086C3E88112'
in11 = 'CE00C43D881120'
in12 = 'D8005AC2A8F0'
in13 = 'F600BC2D8F'
in14 = '9C005AC2F8F0'
in15 = '9C0141080250320F1802104A08'

print('Result for Test-0 Puzzle:', acd16(in00))
print('Result for Test-1 Puzzle:', acd16(in01))
print('Result for Test-2 Puzzle:', acd16(in02))
print('Result for Test-3 Puzzle:', acd16(in03))
print('Result for Test-4 Puzzle:', acd16(in04))
print('Result for Test-5 Puzzle:', acd16(in05))
print('Result for Test-6 Puzzle:', acd16(in06))
print('Result for Puzzle:', acd16(in07))
print('Result for Test-8 Puzzle:', acd16(in08))
print('Result for Test-9 Puzzle:', acd16(in09))
print('Result for Test-10 Puzzle:', acd16(in10))
print('Result for Test-11 Puzzle:', acd16(in11))
print('Result for Test-12 Puzzle:', acd16(in12))
print('Result for Test-13 Puzzle:', acd16(in13))
print('Result for Test-14 Puzzle:', acd16(in14))
print('Result for Test-15 Puzzle:', acd16(in15))
