import numpy as np
import scipy.linalg
#Your optional code here
#You can import some modules or create additional functions

def lu(A,b):
    # Edit here to implement your code
    LU = scipy.linalg.lu_factor(A)
    sol = scipy.linalg.lu_solve(LU,b)

    return list(sol)

def sor(A, b):
    L = -1*np.tril(A,-1)
    D = np.diag(np.diag(A))
    U = -1*np.triu(A,1)
    
    K_j = np.linalg.inv(D).dot(L+U)
    SR = max(abs(i) for i in np.linalg.eigvals(K_j))
    omega = 2 * (1-np.sqrt(1-SR**2)) / SR**2
    
    Q = D/omega - L
    K = np.linalg.inv(Q).dot(Q-A)
    c = np.linalg.inv(Q).dot(b)
    sol = np.zeros_like(b)
    for i in range(20): #iteration limit = 20
        sol = K.dot(sol) + c
    return list(sol)

def solve(A, b):
    #condition = np.all(np.linalg.eigvals(A) > 0) # Check: eigenvalues are all positive
    #condition = True   
    if np.all(np.linalg.eigvals(A) > 0):
        print('Solve by sor(A,b)')
        return sor(A,b)
    else:
        print('Solve by lu(A,b)')
        return lu(A,b)

if __name__ == "__main__":
    ## import checker
    ## checker.test(lu, sor, solve)

    A = [[2,1,6], [8,3,2], [1,5,1]]
    b = [9, 13, 7]
    sol = solve(A,b)
    print(sol)
    
    A = [[6566, -5202, -4040, -5224, 1420, 6229],
         [4104, 7449, -2518, -4588,-8841, 4040],
         [5266,-4008,6803, -4702, 1240, 5060],
         [-9306, 7213,5723, 7961, -1981,-8834],
         [-3782, 3840, 2464, -8389, 9781,-3334],
         [-6903, 5610, 4306, 5548, -1380, 3539.]]
    b = [ 17603,  -63286,   56563,  -26523.5, 103396.5, -27906]
    sol = solve(A,b)
    print(sol)
