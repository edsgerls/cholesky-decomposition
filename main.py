import numpy as np
import math


# A == AT and zT·A·z > 0
# Compute if matrix is symmetric, positive-definite, if it is not: use exceptions if possible
def check_SymmPosDefinite(mat):
    if np.allclose(mat, mat.T, rtol=1e-05, atol=1e-05):
        if len([eigval for eigval in np.linalg.eigvals(A) if eigval <= 0]) == 0:
            return True  # meaning it must have only positive eigenvalues
        else:
            return False


if __name__ == '__main__':
    A = np.array([[2, 1], [1, 2]])

    m, n = np.shape(A)

    # Check for a square matrix
    if m == n:
        # Before anything, compute if matrix is symmetric, positive-definite (real matrices only)
        if check_SymmPosDefinite(A):
            print('Matrix A is symmetric, positive definite')



        # L = np.linalg.cholesky(A)
        # print(L)

        m,n = np.shape(A)

        R = np.zeros((n,n))

        # TODO: I do not like subtracting 1 to each term as in R[i-1,i-1], refactorize
        for j in range(1,n+1):
            print('j:',j)
            for i in range(1,j+1):
                print('i:', i)
                if i == j:
                    sq_sum = 0
                    for k in range(1,(j+1)-1):
                        sq_sum += math.pow(R[k-1,j-1],2)
                    R[i-1,i-1] = math.sqrt(A[i-1,i-1] - sq_sum)
                    print(R[i-1,i-1])

                elif j > i:
                    pr_sum = 0
                    for k in range(1,(i+1)-1):
                        pr_sum += R[k-1,i-1]*R[k-1,j-1]

                    R[i-1,j-1] = (A[i-1,j-1] - pr_sum)*(1/R[i-1,i-1])
                    print(R[i-1,j-1])


        print(R)
        print(np.matmul(np.transpose(R),R))

        # Compute the determinant as: det(A) = det(R)^2
        diag = np.diag(R)
        #print(diag)

        detR = 1
        for element in diag:
            detR *= element

        detR_squared = math.pow(detR,2)
        #print('Determinant of A:', detR_squared)


