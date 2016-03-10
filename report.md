UECM3033 Assignment #2 Report
========================================================

- Prepared by: ** Lee Hui Si**
- Tutorial Group: T3

--------------------------------------------------------

## Task 1 --  $LU$ Factorization or SOR method

The reports, codes and supporting documents are to be uploaded to Github at: 

[https://github.com/LeeHuiSi/UECM3033_assign2](https://github.com/LeeHuiSi/UECM3033_assign2)

Explain your selection criteria here.

LU factorization is one of the direct methods to obtain solution of linear systems. It only work for any square matrix. SOR is iterative method which under stationary method work when the matrix has positive diagonal elements if and only if the matrix is positive definite.

To speed up the computation, iteration methods such as SOR method are required. The successful convergence of iterative methods may be dependent on the positive definite property of the coefficient matrix, but checking this property is as costly as solving it. However, some conditions affecting convergence, such as positive diagonal elements and symmetry are easy to verify. Usually, both symmetric and positive definite of a matrix can only guarantee for rapid convergence. But for non-symmetric systems, SOR may still be successful. So in this assignment, the only special property of matrix to be concerned is positive diagonally and by checking whether all the eigenvalues are positive with the condition below.

np.all(np.linalg.eigvals(A) > 0)

If it is true, then SOR method will be implement, else LU decomposition.

---------------------------------------------------------

## Task 2 -- SVD method and image compression

Put here your picture file 

![fruit.jpg] (fruit.jpg)

How many non zero element in Sigma?

There are 800 non-zero elements in matrix Sigma.

Put here your lower and better resolution pictures. Explain how you generate
these pictures from `task2.py`.

Here are my lower resolution image.

![LowerResolution.jpg] (LowerResolution.jpg)

![LowerResolution.png] (LowerResolution.png)



Here are my better resolution image.

![BetterResolution.jpg] (BetterResolution.jpg)

![BetterResolution.png] (BetterResolution.png)



First, the RGB matrices are obtained from the ¡°fruit.jpg¡±. Then decompose the R,G and B matrices into S,U,V by using np.linalg.svd. After that, create 3 zero matrices that has the same dimensions as S. To compress the lower resolution image, only keep the first 30 diagonal value of sigma matrix and let the remaining element become zero. For the better resolution image, keep the first 200 diagonal value of sigma matrix and let the remaining element become zero. Lastly, combine S, U, V into R, G and B matrices again.

What is a sparse matrix?
In numerical analysis, a sparse matrix is a matrix in which most of the elements are zero. Sparse storage can be using to save memory. For instance, lower the resolution by letting more elements of matrix to become zero and it can be save the memory to store inside our computer or mobile phone.
-----------------------------------

<sup>last modified: 11Mar2016 here</sup>


