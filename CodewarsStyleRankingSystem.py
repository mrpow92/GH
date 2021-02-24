class User:

    def __init__(self):
        self.rank = -8
        self.progress = 0


    def inc_progress(self, rank):
        if rank>8 or rank<-8 or rank == 0: 
            raise Exception('Wrong rank!!!')
        print(self.rank, rank, self.progress)
        if not self.rank == 8:

            if rank == self.rank:
                self.progress += 3
            elif rank+1 == self.rank:
                self.progress += 1
            elif rank+1 < self.rank:
                self.progress += 0
            if rank==-1 and self.rank ==1:
                self.progress +=1
            if rank > self.rank:
                d = rank - self.rank
                if self.rank < 0 and rank > 0: d-=1
                self.progress += (10*d*d)
            while self.progress >= 100:
                self.update_rank()  

            print(self.rank, rank, self.progress)
        #print("progress", self.progress,"rank:", self.rank)

    def update_rank(self):
        
        if self.progress>=100 and self.rank<8:
            self.rank+=1
            self.progress-=100
        if self.rank == 0:
            self.rank = 1
        if self.rank == 8:
            self.progress = 0 




user = User()
user.rank = -1
print(user.progress)
user.inc_progress(4)
#user.inc_progress(-1)
print(user.progress)
print(user.rank)
user.inc_progress(-1)
print(user.progress)
print(user.rank)