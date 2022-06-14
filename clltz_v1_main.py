class clltz():
    def __init__(self, var = int):
        self.itrs = self.mul = self.div = 0 #iterations, multiplication, division
        self.ini = int(var)
        self.var = int(var)
    def assign(self, var = int):
        var = int(var)
        self.var += var - int(self.var)
        self.ini += var - int(self.ini)
        self.itrs = self.mul = self.div = 0
    def execute(self):
        self.var = int(self.var)
        if self.var == 0:
            return
        while self.var != 1:    
            if self.var%2 == 0:
                self.var/= 2
                self.div+=1
            else:
                self.var = 3*self.var+1
                self.mul+=1
            self.itrs+=1
    def results(self):
        return print(f'{self.ini} took {self.itrs} iterations to get to {self.var}.\nThe n/2 formula was executed {self.div} times.\nThe 3n+1 formula was executed {self.mul} times.\n\n')
