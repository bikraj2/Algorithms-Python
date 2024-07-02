import math
import sys
import unittest

def matrix_chain_multi(dimensions:list[int]):
    n = len(dimensions) -1
    opt_operations =[[None for i in range(n)] for i in range(n)]
    #   2 3 4
    # 1 - - -
    # 2 - - -
    # 3 - - -
    sel_barrier = [[None for i in range(n-1)] for i in range(n-1)]
    for i in range(n):
        opt_operations[i][i] =0
    for chain_length in range(1,n):
        for i in range(n - chain_length):
            j = i+chain_length
            min_multi = sys.maxsize
            for k in range(i+1,j+1):
                    opt = (
                        opt_operations[i][k-1] + 
                         opt_operations[k][j] + 
                        dimensions[i]*dimensions[k]*dimensions[j+1] 
                    )
                    if opt < min_multi :
                        min_multi = opt
                        opt_operations[i][j] = min_multi
                        sel_barrier[i][j-1] = k
    return opt_operations[0][n-1]
if __name__ =="__main__":
    print(matrix_chain_multi([5,4,6,2,7]))

def brute_force_chain_multi(dimension:list[int],i:int|None,j:int | None):
    if i ==None:
        i = 0
    if j == None:
        j = len(dimension)-2
    if i==j:
        return 0
    min_multi = sys.maxsize
    for k in range(i+1,j+1):
        current_multi = (
            brute_force_chain_multi(dimension,i,k-1) +
            brute_force_chain_multi(dimension,k,j) +
            dimension[i] *dimension[k] *dimension[j+1]
        )
        if current_multi <min_multi :
            min_multi =current_multi
    return min_multi


def dynamic_memo_matrix_chain_multiplication(
    dimensions: list[int], i: int | None = None, j: int | None = None, memo=None
):
    if memo is None:
        i = 0
        n = len(dimensions) - 1
        j = n - 1
        memo = [[None for _ in range(n)] for _ in range(n)]

    if i == j:
        return 0

    if memo[i][j] is not None:
        return memo[i][j]

    min_multiplications = sys.maxsize
    for k in range(i + 1, j + 1):
        current_multiplications = (
            dynamic_memo_matrix_chain_multiplication(dimensions, i, k - 1, memo)
            + dynamic_memo_matrix_chain_multiplication(dimensions, k, j, memo)
            + dimensions[i] * dimensions[k] * dimensions[j + 1]
        )
        if current_multiplications < min_multiplications:
            min_multiplications = current_multiplications
            memo[i][j] = min_multiplications

    return min_multiplications

class TestDynamicTabulationMatrixChainMultiplication(unittest.TestCase):

    def test_dynamic_tabulation_matrix_chain_multiplication(self):
        dimensions = [5, 4, 6, 2, 7]
        expected = 158

        self.assertEqual(dynamic_memo_matrix_chain_multiplication(dimensions), expected)


class TestBruteforceRecursiveMatrixChainMultiplication(unittest.TestCase):

    def test_bruteforce_recursive_matrix_chain_multiplication(self):
        dimensions = [5, 4, 6, 2, 7]
        expected = 158

        self.assertEqual(brute_force_chain_multi(dimensions,None,None), expected)


class TestDynamicRecursiveMatrixChainMultiplication(unittest.TestCase):

    def test_dynamic_recursive_matrix_chain_multiplication(self):
        dimensions = [5, 4, 6, 2, 7]
        expected = 158

        self.assertEqual(matrix_chain_multi(dimensions), expected)


if __name__ == "__main__":
    unittest.main()



