# take in big data array
# page it into a 3D array
# consider 4d array later...

# look for matches at adjacent positions
# recurse and count (counter*direction_code) then add to ans_string
# so if target is 1, and six 1s in a row in X+ direction,
#    then ans_string gets 6R appended, 0 matches X+, just return
# insert ans_string current position, zero all other pos's
# don't look for diagonals... yet
# eventually, do for arbitrary symbol set.  scan thru items, get uniques...

# parse 6R1F2D... pop type algo
# new form: R6F1D2...

# SEE BOTTOM MATRIX VAR
#
#             Directional codes
# [2][2][3] -> right   R : X+
# [2][2][1] -> left    L : X-
# [2][3][2] -> up      U : Y+
# [2][1][2] -> down    D : Y-
# [3][2][2] -> forward F : Z+
# [1][2][2] -> back    B : Z-    ... DR.BLUF! or flub...
# no diagonals FTL

################################################
# only need Right, Forward, and Up. X+, Y+, Z+
# won't be going negative after compressing positive,
# we know there are no matches
################################################


import pprint as pp


# def compress(matrix):
#     for frame in matrix:
#         for row in frame:
#             for col in row:
#                 z = matrix.index(frame)
#                 y = frame.index(row)
#                 x = row.index(col)
#                 ans_string = ""
#                 # check_all(matrix, z, y, x)
#                 target = matrix[z][y][x]
#                 # right_string = check_right(target, matrix, z, y, x, 0)
#                 print(right_string)
#                 # ans_string += right_string
#                 str(matrix[z][y][x])
#                 matrix[z][y][x] = right_string


# x,y,z are positions in the 3D array
# target is the int value at the current position
# iterate frames, rows, cols
# target_zyx is int 1-9 at current matrix position
# also the symbol we want to compress, L/R,U/D,B/F


# def check_all(matrix, z, y, x):
    # run all checks, combine string
    # target_int = matrix[z][y][x]
    # ans_string += check_right(target_int, matrix, z, y, x, 0)
    # ans_string += check_left   (target_int, z, y, x)
    # ans_string += check_up     (target_int, z, y, x)
    # ans_string += check_down   (target_int, z, y, x)
    # ans_string += check_forward(target_int, z, y, x)
    # ans_string += check_back   (target_int, z, y, x)
    # !!!
    # if ans_string == "": return
    # else: str(target_int)
    # matrix[z][y][x] = ans_string , return

    # print(ans_string)
    # str(matrix[z][y][x])
    # matrix[z][y][x] = ans_string
    # print(matrix[z][y][x])

def check_all(matrix):
    # run all checks, combine string

    for frame in matrix:
        for row in frame:
            for col in row:
                z = matrix.index(frame)
                y = frame.index(row)
                x = row.index(col)

                target_int = matrix[z][y][x]

                if target_int == "":
                    return
                else:
                    ans_string = ""
                    ans_string = check_right(z,y,x,\
                                             matrix, z, y, x+1, 0)
                    # ans_string += check_down
                    # ans_string += check_forward
                    print("ans_string", ans_string)
                    matrix[z][y][x] = ans_string

    # ans_string += check_right(target, matrix, z, y, x, 0)
    # matrix[z][y][x] = ""
    # ans_string += check_left   (target, z, y, x)
    # ans_string += check_up     (target, z, y, x)
    # ans_string += check_down   (target, z, y, x)
    # ans_string += check_forward(target, z, y, x)
    # ans_string += check_back   (target, z, y, x)
    # print(matrix[z][y][x])

# need to iterate either +,- frames, rows, cols
# target_zyx is int 1-9 at current matrix position
# also the symbol we want to compress, L/R,U/D,B/F

# dont know if matrix needs to be a param...

# 
def check_right(origin_z, origin_y, origin_x, matrix, new_z, new_y, new_x, counter):
    # shouldnt need next, should be recursively incremented param
    origin = matrix[origin_z][origin_y][origin_x]
    target = matrix[new_z][new_y][new_x]
    # ans_string = ""
    try:
        if origin == target:
            # print(matrix[z][y][x], matrix[z][y][x+1])
            counter += 1
            target = ""
            check_right(origin_z, origin_y, origin_x, matrix, new_z, new_y, new_x+1, counter)
        elif target != origin and counter > 0:
            ans_string = str(origin)+"R"+str(counter)
            print("ans_string", ans_string)
            origin = ans_string
            try:
                check_right(new_z,new_y,new_x,matrix,new_z,new_y,new_x,0)
            except IndexError:
                ans_string = str(origin)+"R"+str(counter)
                return ans_string
        elif target != origin and counter == 0:
            try:
                check_right(origin_z, origin_y, origin_x+1, matrix, new_z, new_y, new_x+1, 0)
            except IndexError:
                return origin

    # origin != target:
    except IndexError:
        if counter == 0:
            print("counter == 0 and IndexError")
            return origin

        elif counter > 0:
            print("counter = ",counter," and IndexError")
            ans_string = str(origin)+"R"+str(counter)
            # ans_string = str(target_int)+"R"+str(counter)
            print("ans_string", ans_string)
            return ans_string

            # keep incrementing counter until IndexError
    else:
            # if right ele is not same, return
        return origin


matrix = \
    [   # new setup is directional code then number of target_int matches
        # [1,1,1,1,1], #1R4 => ["1R4D2F2",0,0,0,0]
        [1, 1, 1, 1, 1],  # 1R4 => ["1R4D3F2",0,0,0,0]
        [1, 1, 1, 1],  # 1R3 => [0,0,0,0]
        [1, 1, 1]  # 1R2 => [0,0,0]
        # but actually,
        # should be:  1R4D2F2
        # target: 1, Right()=4, Down()=2, Forward()=2
        # check_right algo changed to preserve target_int and
        # zero elements that match the current element
        # to be compressed into
    ],\
    [
        [1, 11, 12],
        [13, 14, 15],
        [16, 17, 18]
    ],\
    [
        [1, 20, 21],
        [22, 23, 24],
        [25, 26, 27]
    ]

print("")
print("matrix is:")
pp.pprint(matrix)
print("\n compressing \n")
check_all(matrix)
pp.pprint(matrix)

# check_index(matrix)

# print(matrix[0][0][0])
# matrix[0][0][0][0]="a"

