import numpy as np


def p_vector(vector):
    for value in vector:
        if value == vector[0]:
            print(f"[['{value}']")
        elif value == vector[-1]:
            print(f" ['{value}']]")
        else:
            print(f" ['{value}']")


a_list = ['a11', 'a12', 'a13', 'a12', 'a22', 'a23', 'a13', 'a23', 'a33']  # example square matrix
size = 3  # size for both square matrix and b vector
# below list comprehension converts list into square matrix
a_sub_lists = [a_list[i:i + size] for i in range(0, len(a_list), size)]

b_list = ['b1', 'b2', 'b3']  # example b vector

a_matrix = np.asarray(a_sub_lists)
print(f"When asked, provide an A matrix and b vector that fills the following form:\n(note, it does not have to be "
      f"size 3, any square matrix will work)\nsize =\n{size}\nA = \n{a_matrix},\nb =")
p_vector(b_list)

# Get size of array from user
print("size: ")
size = int(input())

# get full size of matrix from size variable
nxn = size * size

# clear a_list so we can re-use it
a_list = []
# generate anm value for a_list

for i in range(size):
    for j in range(size):
        a_list.append(f"a{i+1}{j+1}")

# Convert a_list to matrix
a_sub_lists = [a_list[i:i + size] for i in range(0, len(a_list), size)]
a_matrix = np.asarray(a_sub_lists, dtype=object)

# ask user for each value of matrix
for a in range(nxn):
    # clear screen
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    # show current matrix setup to user
    print(f"A =\n{a_matrix}")
    # ask user for input to specific variable, and assign it
    print(f"\n{a_list[a]} = ?")
    a_list[a] = int(input())
    # Convert a_list to np.matrix
    a_sub_lists = [a_list[i:i + size] for i in range(0, len(a_list), size)]
    a_matrix = np.asarray(a_sub_lists, dtype=object)

# clear b_list so we can re-use it
b_list = []
# generate bn value for b_list
for b in range(size):
    b_list.append(f"b{b+1}")
# convert list to np.matrix (vector)
b_vector = np.array(b_list)

# ask user for each value of vector
for b in range(size):
    # clear screen
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    # show current vector setup to user
    p_vector(b_list)
    # ask user for input to specific variable, and assign it
    print(f"\n{b_list[b]} = ?")
    b_list[b] = int(input())
    b_vector = np.array(b_list)


print("Provide initial guess")
init_guess = int(input())
x = []
for i in range(size):
    x.append(init_guess)


# convert to matrix to float
A = a_matrix.astype(float)
print(f"A:\n{A}")
b = b_vector.astype(float)
print(f"b:\n{b}")
# create D and R matrix, as type float
D = np.diag(np.diag(a_matrix)).astype(float)
print(f"D:\n{D}")
N = D - A
print(f"N:\n{N}")
D_inverse = np.linalg.inv(D)
print(f"D_inverse:\n{D_inverse}")

print("\nFormula: xk+1 = D^-1[(N)*xk+b]\n")

print(f"x0={x}")
for i in range(3):
    Nx = N.dot(x)
    print(f"Nx={Nx}")
    Nxb = Nx + b
    print(f"Nxb={Nxb}")
    x = D_inverse.dot(Nxb)
    print(f"d_inv*Nxb={x}")
    x = np.diag(x)
    print(f"Iteration {i+1}: x={x}\n")
    x = x.tolist()

print(f"jacobi solution: {np.diag(x)}")

x = np.zeros_like(b)
for it_count in range(3):
    x_new = np.zeros_like(x)
    print(f"Iteration {it_count}: {x}")
    for i in range(A.shape[0]):
        s1 = np.dot(A[i, :i], x_new[:i])
        s2 = np.dot(A[i, i + 1:], x[i + 1:])
        x_new[i] = (b[i] - s1 - s2) / A[i, i]
    if np.allclose(x, x_new, rtol=1e-8):
        break
    x = x_new

print(f"gauss-seidel solution: {x}")
