import re

ifl = open('12_input.txt', 'r')
dt = ifl.read().strip()    # storing all the input
ifl.close()

# Part 1
print(sum([int(x) for x in re.findall(r'\-?\d+', dt)]))

# For part 2, any substring in curly brackets {} containing red
# is removed from dt and integers are then summed as in part 1
k = 0
while k < len(dt) - 2:
    if dt[k:k+3] == 'red':    # search for brackets start whenever 'red' is found in dt
        i0 = k-1    # i0 and i1 will contain positions of '{' and '}'
        cbs = []    # to store curly brackets
        sbs = []    # to store square brackets
        chsb = False    # keeps track if 'red' is contained in square brackets
        while i0 >= 0:    # brackets that open and close before/after 'red' are not considered, this is achieved using append and pop on cbs and sbs
            if dt[i0] == '{':
                if not cbs:
                    break
                else:
                    cbs.pop()
            elif dt[i0] == '}':
                cbs.append(dt[i0])
            elif dt[i0] == '[':
                if not sbs:
                    chsb = True
                    break
                else:
                    sbs.pop()
            elif dt[i0] == ']':
                sbs.append(dt[i0])
            i0 -= 1
        if not chsb and i0 >= 0:    # proceeds to find position of '}', if chsb is False and '{' was found
            n = len(dt)
            i1 = k+3
            cbs = []
            while i1 < n:
                if dt[i1] == '}':
                    if not cbs:
                        break
                    else:
                        cbs.pop()
                elif dt[i1] == '{':
                    cbs.append(dt[i1])
                i1 += 1
            dt = dt[:i0] + dt[i1+1:]    # removing substring {...red...} from dt
            k = i0
            continue
        else:
            k += 3
    else:
        k += 1

print(sum([int(x) for x in re.findall(r'\-?\d+', dt)]))
