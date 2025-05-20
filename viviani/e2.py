# /usr/bin/env python3
# author: Mattia Sgro
# lecture 2
# implementation of Compressed Sparse Row to matrix and vice-versa

def mateq(a, b):
    na = len(a)
    nb = len(b)
    ma = len(a[0])
    mb = len(b[0])
    if (na != nb):
        return False
    if (ma != mb):
        return False
    for x in range(na):
        for y in range(ma):
            if a[x][y] != b[x][y]:
                return False
    return True

def getnnz(mat):
    c = 0
    for x in range(len(mat)):
        for y in range(len(mat[0])):
            if mat[x][y] != 0:
                c += 1
    return c


def csr2mat(csr):
    nnz = len(csr[0])
    assert len(csr[0]) == len(csr[1])
    n = len(csr[2]) - 1

    m = max([i for i in csr[1]])

    nmat = [[0 for _ in range(m+1)] for _ in range(n)]
    ri = 1
    vi = 0
    for rows in range(n):
        elems = csr[2][ri] - csr[2][ri-1]
        for i in range(elems):
            nmat[rows][csr[1][vi]] = csr[0][vi]
            vi +=1
        ri +=1

    

    return nmat


def mat2csr(mat):
    n = len(mat)
    m = len(mat[0])

    nnz = getnnz(mat)

    csr = [
        [None for _ in range(nnz)],  # v array
        [None for _ in range(nnz)],  # c array
        [None for _ in range(n + 1)],  # r array
    ]
    csr[2][0] = 0

    vci = 0
    ri = 1

    for x in range(n):
        for y in range(m):
            val = mat[x][y]
            if val != 0:
                csr[0][vci] = val
                csr[1][vci] = y
                vci += 1
        csr[2][ri] = vci
        ri += 1

    return csr


def main():
    mat = [
        [0, 2, 0, 0, 1, 0, 0, 0],
        [0, 8, 0, 0, 0, 0, 2, 0],
        [2, 0, 3, 0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 8, 0],
    ]
    print("input mat is:\t", mat)

    csr = mat2csr(mat)
    print("csr(mat) is:\t", "v:",csr[0], " c:", csr[1], " r:", csr[2])

    mat2 = csr2mat(csr)
    print("mat(csr) is:\t", mat2)
    if mateq(mat,mat2):
        print("ok!")
    else:
        print("WARN: without knowing the length of each row, mat(csr) will truncate (from the right) any column full of zeros")
        print("Truncated!")

    print("-------------------")
    mat = [
        [0, 2, 0, 0, 1, 0, 0, 0],
        [0, 8, 0, 0, 0, 0, 2, 0],
        [2, 0, 3, 0, 1, 1, 0, 1],
        [0, 0, 0, 0, 0, 0, 8, 0],
    ]
    print("input mat is:\t", mat)

    csr = mat2csr(mat)
    print("csr(mat) is:\t", "v:",csr[0], " c:", csr[1], " r:", csr[2])

    mat2 = csr2mat(csr)
    print("mat(csr) is:\t", mat2)
    if mateq(mat,mat2):
        print("ok!")
    else:
        print("WARN: without knowing the length of each row, mat(csr) will truncate (from the right) any column full of zeros")
        print("Truncated!")

if __name__ == "__main__":
    main()
