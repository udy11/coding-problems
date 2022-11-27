# First, all operators are replaced to the corresponding ones in
# python, like AND is replaced with &. Keywords is, in, if and as
# are also replaced. Every statement is then rearranged in a
# dict dts where keys are variables to be assigned and values are
# the expressions they correspond to, for example {'ai' : 'af & ah'}.
# Then those expressions are evaluated that only contain operators
# and digits in values, these evaluated values are then replaced
# with corresponding variables in all other entries. This process
# is repeated until no evaluatable expression is left.

# FAILED IDEA 1:
# Originally I thought to define each statement as a function
# Like ai = lambda af() & ah()
# And then simply evaluate a() to get the answer
# but somehow this takes a lot of time, which could be
# because function search is slow? would like to know
# the actual reason.

# FAILED IDEA 2:
# Another idea was that starting from the expression
# of a, just keep replacing variables with their
# expressions until the expression contains only
# operators and numbers, but unfortunately the expression
# grows very quickly and further computation becomes slow

import re

def p1(dts):
    while True:
        vrs = {}
        check = True
        for d0 in dts:
            if not re.findall(r'[a-z]+', dts[d0]):
                check = False
                exec(d0 + '=' + dts[d0])
                vrs[d0] = str(locals()[d0])
        for v0 in vrs:
            del dts[v0]
            for d1 in dts:
                dts[d1] = re.sub(f'\\b{v0}\\b', vrs[v0], dts[d1])
        if check:
            break
    return locals()['a']

ifl = open('07_input.txt', 'r')
dt = ifl.read()
ifl.close()

reps = {'AND' : '&',
        'OR' : '|',
        'LSHIFT' : '<<',
        'RSHIFT' : '>>',
        'NOT' : '~',
        'is' : 'isis',
        'in' : 'inin',
        'if' : 'ifif',
        'as' : 'asas'}
for r in reps:
    dt = dt.replace(r, reps[r])

dts = {}
for d in dt.strip().split('\n'):
    eqn, var = d.split('->')
    dts[var.strip()] = eqn.strip()
del dt

print(p1(dict(dts)))
dts['b'] = '956'
print(p1(dts))
