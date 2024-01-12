import sys

in0 = '''start-A
start-b
A-c
A-b
b-d
A-end
b-end'''

in1 = '''dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc'''

in2 = '''fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW'''

in3 = '''EO-jc
end-tm
jy-FI
ek-EO
mg-ek
jc-jy
FI-start
jy-mg
mg-FI
jc-tm
end-EO
ds-EO
jy-start
tm-EO
mg-jc
ek-jc
tm-ek
FI-jc
jy-EO
ek-jy
ek-LT
start-mg'''

def cpaths0(cave_joints, count, cv0, path):
    for cv1 in cave_joints[cv0]:
        if cv1.islower() and cv1 in path:
            continue
        if cv1 == 'end':
            #print(path)
            count[0] += 1
            continue
        path.append(cv1)
        cpaths0(cave_joints, count, cv1, path)
        path.pop()

def cpaths1(cave_joints, count, cv0, path):
    for cv1 in cave_joints[cv0]:
        if cv1.islower():
            if path.count(cv1) == 1:
                chk = False
                for p in path:
                    if p.islower() and path.count(p) == 2:
                        chk = True
                        break
                if chk:
                    continue
            if path.count(cv1) == 2:
                continue
        if cv1 == 'end':
            #print(path)
            count[1] += 1
            continue
        path.append(cv1)
        cpaths1(cave_joints, count, cv1, path)
        path.pop()

def p1(inp):
    cave_joints = {}
    for lyn in inp.split('\n'):
        ls = lyn.split('-')
        if ls[1] != 'start' and ls[0] != 'end':
            if not ls[0] in cave_joints:
                cave_joints[ls[0]] = [ls[1]]
            else:
                cave_joints[ls[0]].append(ls[1])
        if ls[0] != 'start' and ls[1] != 'end':
            if not ls[1] in cave_joints:
                cave_joints[ls[1]] = [ls[0]]
            else:
                cave_joints[ls[1]].append(ls[0])
    count = [0, 0]
    path = []
    cpaths0(cave_joints, count, 'start', path)
    cpaths1(cave_joints, count, 'start', path)
    return count

# Won't work if there are loops in paths

print('Soltions of Test Puzzle 1:', p1(in0))
print('Soltions of Test Puzzle 2:', p1(in1))
print('Soltions of Test Puzzle 3:', p1(in2))
print('Soltions of Puzzle:', p1(in3))
