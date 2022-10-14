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
    a_list[a] = (input())
    a_list[a_list == ''] = 0
    # Convert a_list to matrix
    a_sub_lists = [a_list[i:i + size] for i in range(0, len(a_list), size)]
    a_matrix = np.asarray(a_sub_lists, dtype=object)

# clear b_list so we can re-use it
b_list = []
# generate bn value for b_list
for b in range(size):
    b_list.append(f"b{b+1}")

# ask user for each value of vector
for b in range(size):
    # clear screen
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    # show current vector setup to user
    p_vector(b_list)
    # ask user for input to specific variable, and assign it
    print(f"\n{b_list[b]} = ?")
    b_list[b] = input()


print("Provide initial guess")
init_guess = int(input())

# create init_value x0 list
x = []
for i in range(size):
    x.append(init_guess)

# convert to float
a_matrix = a_matrix.astype(float)
b_list = np.array(b_list)
b_list = b_list.astype(float)

# create D and R matrix
D = np.diag(a_matrix)
R = a_matrix - np.diagflat(D)

# compute x(k)
for i in range(25):
    x = (b_list - np.dot(R, x)) / D
    print(f"iteration {i+1}: {x}")

print(f"\nFinal: {x}")
