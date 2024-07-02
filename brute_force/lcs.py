def longest_common_sequence(str1,str2,i,j):
    if i >=len(str1) or j >=len(str2):
        return 0
    elif str1[i] ==str2[j] :
        return 1 + longest_common_sequence(str1,str2,i+1,j+1)
    else:
        return max(longest_common_sequence(str1,str2,i+1,j),longest_common_sequence(str1,str2,i,j+1))
def longest_common_sequence_with_seq(str1,str2,i,j):
    if i >=len(str1) or j >=len(str2):
        return ""
    elif str1[i] ==str2[j] :
        val = str1[i] + longest_common_sequence_with_seq(str1,str2,i+1,j+1)
        return val
    else:
        val1 =  longest_common_sequence_with_seq(str1,str2,i+1,j)
        val2 =longest_common_sequence_with_seq(str1,str2,i,j+1)
        if len(val1)> len(val2):
            return val1
        else :
            return val2


if __name__ == "__main__":
    str1 = "presidentpresidentpresident"
    str2 ="providenceprovidenceprovidence"
    print(longest_common_sequence(str1,str2,0,0))