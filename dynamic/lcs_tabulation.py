
def longest_common_sequence(str1,str2):
    memo = [[0 for i in range(len(str2)+1)] for i in range(len(str1)+1)]
    for i in range(1,len(str1)+1):
        for j in range(1,len(str2) + 1):
            if str1[i-1]==str2[j-1]:
                memo[i][j] = memo[i-1][j-1] +1
            else :
                memo[i][j] = max(memo[i][j-1],memo[i-1][j])
    return memo[-1][-1],memo
def get_seq(str1,str2,memo):
    seq =""
    i = len(memo) - 1
    j = len(memo[0]) - 1
    while i > 0:
        while j > 0:
            if memo[i][j-1] < memo[i][j] and memo[i-1][j]< memo[i][j]:
                i-=1
                j-=1
                seq +=str1[i]
            elif memo[i][j-1] < memo[i][j]:
                i -=1
            else :
                j-=1
            if j ==0:
                i-=1
    return seq
            
if __name__ == "__main__":
    str1 = "presidentpresidentpresident"
    str2 ="providenceprovidenceprovidence"
    memo= [[None for i in range(len(str2))] for i in range(len(str1))]
    length,res = longest_common_sequence(str1,str2)
    print(get_seq(str1,str2,res))
