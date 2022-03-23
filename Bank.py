class AllBranch():
    def __init__(self, cre, deb):
        self.cre = cre
        self.deb = deb
    #
    # def credit(self):
    #     print('Amount Credited')
    #     return 100
    #
    # def debit(self):
    #     print('Amount Debited')
    #     return 100

    def debit(self):
        return self.deb

    def credit(self):
        return self.cre