import re

def add_time(start, duration, day = ''):
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    h0, m0, ap = re.split(':| ', start)
    t0 = int(h0) * 60 + int(m0)
    if ap.lower() == 'pm':
        t0 += 720
    dh, dm = re.split(':', duration)
    dt = int(dh) * 60 + int(dm)
    t1 = t0 + dt
    h1, m1 = divmod(t1, 60)
    nd, h1 = divmod(h1, 24)
    if h1 < 12:
        if h1 == 0: h1 = 12
        s = f'{h1}:{m1:02} AM'
    else:
        if h1 > 12: h1 = h1 - 12
        s = f'{h1}:{m1:02} PM'
    if day:
        s += ', ' + days[(days.index(day.title()) + nd) % 7]
    if nd > 1:
        s += f' ({nd} days later)'
    elif nd == 1:
        s += ' (next day)'
    return s
