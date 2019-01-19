from math import sqrt, cos, sin, radians, degrees
def calculate_a_times_b (mtrx_1, mtrx_2, current_row_a, current_col_b, num_col_a):
    total = 0
    for current_col_a in range(num_col_a):
        mult = mtrx_1[current_row_a][current_col_a] * mtrx_2[current_col_a][current_col_b]
        total = total + mult
    return total

def matrix_multiply_universal (mtrx_1, mtrx_2):
    num_row_a = len(mtrx_1)
    num_col_a = len(mtrx_1[0])
    num_row_b = len(mtrx_2)
    num_col_b = len(mtrx_2[0])
    C = list()
    for current_row_a in range (num_row_a):
        c_row = list()
        for current_col_b in range(num_col_b):
            total = calculate_a_times_b(mtrx_1, mtrx_2, current_row_a, current_col_b, num_col_a)
            c_row.append(total)
        C.append(c_row)
    return C

def transpose_zero_fill (mtrx_1):
    C = list()
    for row_zeros in range(len(mtrx_1[0])):
        c_row = list()
        for col_zeros in range(len(mtrx_1)):
            c_row.append(0)
        C.append(c_row)

    return C


def transpose_fill (mtrx_1):
    C = transpose_zero_fill(mtrx_1)
    #print(C)
    for row in range(len(mtrx_1)):
        for col in range(len(mtrx_1[0])):
            C[col][row] = mtrx_1[row][col]
    return C




def rotate_n_degrees(theta, vector_init):
    theta_radians = radians(theta)
    mtrx_rotate = [[cos(theta_radians), -sin(theta_radians)],[sin(theta_radians), cos(theta_radians)]]
    mtrx_rotate_output = matrix_multiply_universal(mtrx_rotate, vector_init)
    mtrx_rotate_output_int = list()
    for row in range(len(mtrx_rotate_output)):
        row_list = list()
        for col in range(len(mtrx_rotate_output[0])):
            value = int(mtrx_rotate_output[row][col])
            row_list.append(value)
        mtrx_rotate_output_int.append(row_list)

    return mtrx_rotate_output_int
