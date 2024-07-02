class NQueens:
    def __init__(self,queens) -> None:
        self.queens = queens
        self.placements =[0 for i in range(queens+1)]
    def backTrack(self,k):
        for i in range(1,self.queens):
            if self.place(k,i):
                self.placements[k]=i
                if k == self.queens  :
                    print("Solutions",self.placements)
                    a=10
                else:
                    self.backTrack(k+1)
    def place(self,k,i):
        for j in range(1,k):
            if (self.placements[j]==i) or (abs(self.placements[j]-i) == abs(j-k)):
                return False
        return True
    
if __name__ == "__main__":
    prob = NQueens(4)
    prob.backTrack(1)
