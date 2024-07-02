import unittest
import sys
def matrix_chain_multi(dimensions:list[int]):
    n = len(dimensions) -1
    opt_multi = [[None for i in range(n)] for i in range(n)]

    sel_barrieer = [[None for i in range(n-1)] for i in range(n-1)]
    for i in range(n):
        opt_multi[i][i] =0
    for chain_length in range(1,n):
        for i in range(n-chain_length):
            j = i +chain_length
            min_multi = sys.maxsize
            for k in range(i+1,j+1):
                current_multi = (
                    opt_multi[i][k-1]+
                    opt_multi[k][j]+
                    dimensions[i] * dimensions[k] * dimensions[j+1]
                )
                if current_multi < min_multi :
                    min_multi = current_multi
                    opt_multi[i][j] =min_multi
                    sel_barrieer[i][j-1] = k
    return opt_multi[0][n-1]
class TestBruteforceRecursiveMatrixChainMultiplication(unittest.TestCase):

    def test_bruteforce_recursive_matrix_chain_multiplication(self):
        dimensions = [5, 4, 6, 2, 7]
        expected = 158
        self.assertEqual(matrix_chain_multi(dimensions), expected)
if __name__ == "__main__":
    unittest.main()