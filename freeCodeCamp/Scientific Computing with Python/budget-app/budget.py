class Category:
    def __init__(self, category = ''):
        self.name = category
        self.ledger = []
        self.balance = 0
    def __str__(self):
        s = '*' * ((31-len(self.name)) // 2) + self.name + '*' * ((30-len(self.name)) // 2) + '\n'
        for t in self.ledger:
            s += t['description'][:23].ljust(23) + '{:.2f}'.format(t['amount']).rjust(7) + '\n'
        s += 'Total: {:.2f}'.format(self.balance)
        return s
    def check_funds(self, amount):
        return amount <= self.balance
    def deposit(self, amount, description = ''):
        self.ledger.append({'amount' : amount, 'description' : description})
        self.balance += amount
        return True
    def withdraw(self, amount, description = ''):
        if self.check_funds(amount):
            self.ledger.append({'amount' : -amount, 'description' : description})
            self.balance -= amount
            return True
        else:
            return False
    def get_balance(self):
        return self.balance
    def transfer(self, amount, catg):
        if self.check_funds(amount):
            self.balance -= amount
            catg.balance += amount
            self.ledger.append({'amount' : -amount, 'description' : f'Transfer to {catg.name}'})
            catg.ledger.append({'amount' : amount, 'description' : f'Transfer from {self.name}'})
            return True
        else:
            return False

def create_spend_chart(categories):
    nc = len(categories)
    ws = [sum([t['amount'] for t in c.ledger if t['amount'] < 0]) for c in categories]
    sum_ws = sum(ws)
    wsp = [int(10 * w / sum_ws) * 10 for w in ws]    # i think it should be round() instead of int(), as per original problem
    s = 'Percentage spent by category\n'
    for k in range(100, -1, -10):
        s += f'{k:>3}| ' + ''.join(['o  ' if wsp[i] >= k else '   ' for i in range(nc)]) + '\n'
    s += '    -' + '-' * 3 * nc + '\n'
    cns = [len(c.name) for c in categories]
    for j in range(max(cns)):
        cs = ''
        for i in range(nc):
            if j < cns[i]:
                cs += categories[i].name[j] + '  '
            else:
                cs += '   '
        s += '     ' + cs + '\n'
    return s[:-1]

food = Category("Food")
entertainment = Category("Entertainment")
business = Category("Business")
food.deposit(900, "deposit")
entertainment.deposit(900, "deposit")
business.deposit(900, "deposit")
food.withdraw(105.55)
entertainment.withdraw(33.40)
business.withdraw(10.99)
print(create_spend_chart([business, food, entertainment]))
