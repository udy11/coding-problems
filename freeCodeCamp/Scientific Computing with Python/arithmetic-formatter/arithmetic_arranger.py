def arithmetic_arranger(problems, ans = False):
    if len(problems) > 5:
        return "Error: Too many problems."
    if ans:
        s = ['', '', '', '']
    else:
        s = ['', '', '']
    g = 0
    for p in problems:
        q = p.split()
        if not q[1] in ('-', '+'):
            return "Error: Operator must be '+' or '-'."
        if not (q[0].isnumeric() and q[2].isnumeric()):
            return "Error: Numbers must only contain digits."
        n = max(len(q[0]), len(q[2]))
        if n > 4:
            return "Error: Numbers cannot be more than four digits."
        s[0] += ' ' * (g+2) + q[0].rjust(n)
        s[1] += ' ' * g + q[1] + ' ' + q[2].rjust(n)
        s[2] += ' ' * g + '-' * (n+2)
        if ans:
            s[3] += ' ' * g + str(eval(p)).rjust(n+2)
        g = 4
    if ans:
        return s[0] + '\n' + s[1] + '\n' + s[2] + '\n' + s[3]
    else:
        return s[0] + '\n' + s[1] + '\n' + s[2]