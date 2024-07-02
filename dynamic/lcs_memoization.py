memo = None
def longest_common_sequence(str1,str2,i,j):
    if i >=len(str1) or j >=len(str2):
        return 0
    elif memo[i][j] !=None:
        return memo[i][j]
    else :
        if str1[i] ==str2[j] :
            memo[i][j] = 1 +longest_common_sequence(str1,str2,i+1,j+1)
        else :
            memo[i][j]= max(longest_common_sequence(str1,str2,i+1,j),longest_common_sequence(str1,str2,i,j+1))
        return memo[i][j]
def longest_common_sequence_with_seq(str1,str2,i,j):
    if i >=len(str1) or j >=len(str2):
        return ""
    elif memo[i][j] !=None:
        return memo[i][j]
    else:
        if str1[i] ==str2[j] :
            memo[i][j]= str1[i] + longest_common_sequence_with_seq(str1,str2,i+1,j+1)

        else:
            val1 =  longest_common_sequence_with_seq(str1,str2,i+1,j)
            val2 =longest_common_sequence_with_seq(str1,str2,i,j+1)
            if len(val1)> len(val2):
                memo[i][j]= val1
            else :
                memo[i][j]= val2
        return memo[i][j]


if __name__ == "__main__":
    str1 = "presidentpresidentpresident"
    str2 ="providenceprovidenceprovidence"
    memo = [[None for i in range(len(str2))] for i in range(len(str1))]
    print(longest_common_sequence_with_seq(str1,str2,0,0))