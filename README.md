# Graph Theory and Algorithms
## PhD in Computer Science



## Exercise 1

Let us consider the following algorithm to compute the optimal multicut in trees (Algorithm 18.4, https://doi.org/10.1007/978-3-662-04565-7).

1.  $f\gets 0$, $D\gets \emptyset$
2.  For each vertex $v$ in nonincreasing order of depth
    
    a.    For each pair $(s_i, t_i)$ such that $lca(s_i, t_i) = v$, greedily route integral flow from $s_i$ to $t_i$
    
    b.    Add to $D$ all edges that have been saturated at the previous step

3.  $e_1, \ldots , e_l \gets$ the ordered list of edges in $D$
4.  For $j=l$ downto $1$

    c.    If $D-\{e_j\}$ is a multicut in $G$, then $D\gets D-\{e_j\}$

5.  Output $D$


Prove that, if step b is modified so that only one edge is added to $D$, then the resulting $D$ is not guaranteed to be a multicut

## Exercise 2

Prove that, if steps 4 and c are removed, then the approximation factor is unbounded.

## Exercise 3

Consider the algorithm for Max Independent Set for graphs with bounded twin-width described in http://arxiv.org/abs/2007.14161

Provide a complete description of an algorithm to solve Max *Weighted* Independent Set and prove its correctness (you also have to prove that it computes an optimal independent set.
