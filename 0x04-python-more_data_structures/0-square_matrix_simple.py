#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    nmat = []

    for i in matrix:
        temp = []
        for j in i:
            temp.append(j ** 2)
        nmat.append(temp)
    return nmat
