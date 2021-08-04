import pprint as pp


# think about going 4D with pages, pointers?

# eventually, y_length and z_length can be arrays
# used with counters in check_right that contain
# the number of rows in each frame to know when to
# go to the next frame, and last frame IndexError can be handled the same way
#  ary rows_len [0] represents the number of rows in the first frame
#  int frames_len represents number of frames to iterate, indices frames_len-1

# THINK PYTHON NEEDS 2.5 OR 2.6? OR 2.7 FOR THIS TO WORK!
# THIS DOES NOT WORK ON BASE CONDA ENV!

def check_all(): # matrix param removed
    matrix = \
    [
        [1, 1, 1, 1, 1],  # 1R4 => ["1R4D3F2",0,0,0,0]
        [1, 1, 1, 1],  # 1R3 => ["1R3",0,0,0]
        [1, 1, 1]  # 1R2 => ["1R",0,0]
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
    columns, rows, frames = 0

    for frame in matrix:
        frames += 1
        for row in frame:
            rows +=1
            for col in row:
                columns +=1
                z = matrix.index(frame)
                y = frame.index(row)
                x = row.index(col)
                
                print(str(matrix[z][y][x]))
                
                # if matrix[z][y][x] == "":
                #     pass
                # else:
                #     # when check_right returns, next ary element is pushed through
                #     # matrix[z][y][x], so don't have to increment from check_right
                #     #           origin          target    matchctr  y_ctr z_ctr
                #     check_right(z, y, x, matrix, z, y, x+1, 0,      0,    0)
                #     # ans_string = ""
                #                     # origin z, y, x, next is z, y, x+1
                #                     # if match, recurse calls next z, y, x+1
                #     # check_right(z, y, x+1, matrix, z, y, x+2, 0)
                #     # check_down, check forward
                #     #   # ideally, start in the middle, check L,R,Forward,Back,Up,Down
                #     # matrix[z][y][x] = ans_string
                #     # ans_string += check_down
                #     # ans_string += check_forward
                #     # print("ans_string", ans_string)

def check_right(origin_z, origin_y, origin_x, matrix, target_z, target_y, target_x, 
                match_counter, y_counter, z_counter):
    try:
        origin = matrix[origin_z][origin_y][origin_x]
        target = matrix[target_z][target_y][target_x]
        if target == origin:
            match_counter += 1
            target = ""
            ans_string = str(origin)+"R"+str(match_counter)
            print("ans_string: ", ans_string)
            try:
                check_right(origin_z, origin_y, origin_x, matrix,
                            target_z, target_y, target_x+1, 0, y_counter, z_counter)

            # first row index error, increment y_counter
            except IndexError:
                if match_counter == 0:
                    check_right(origin_z, origin_y+1, origin_x, matrix,
                                target_z, target_y+1, target_x+1, 0, y_counter+1, z_counter)

                elif match_counter > 0:
                    print(origin)
                    ans_string = str(origin)+"R"+str(match_counter)
                    # print out the same ans_string again on IndexError
                    print("IndexError:", "ans_string", ans_string)
                    return ans_string

        elif target != origin:
            if match_counter == 0:
                # could potentially do a check_right that wraps to the next row here
                # check 
                
                # if y_counter = rows_len:
                # go to next frame by incrementing origin_z, target_z
                # increment z_counter

                try:
                    origin = matrix[target_z, target_y, target_x+1]

                    check_right(target_z, target_y, target_x, matrix,
                                target_z, target_y, target_x+1, 0, y_counter+1, z_counter)
                
                except IndexError:
                    # go to next row
                    check_right(origin_z, origin_y+1, origin_x, matrix,
                                target_z, target_y+1, target_x+1, 0, y_counter+1, z_counter)

            elif match_counter > 0:
                ans_string = str(origin)+"R"+str(match_counter)
                print("ans_string: ", ans_string)
                origin = ans_string

                # try:
                #     check_right(target_z, target_y, target_x, matrix,
                #                 target_z, target_y, target_x+1, 0)
                # except IndexError:
                #     ans_string = str(origin)+"R"+str(match_counter)
                #     return ans_string

        elif target != origin and match_counter == 0:
            return
        # we want to let the calling loop call check right itself
        #     try:
        #         check_right(origin_z, origin_y, origin_x+1, matrix, target_z, target_y, target_x+1, 0)
        #     except IndexError:
        #         return str(origin)
        else:
            return str(origin)

    # origin != target:
    except IndexError:
        if match_counter == 0:
            return origin

        elif match_counter > 0:
            ans_string = str(origin)+"R"+str(match_counter)
            print("ans_string", ans_string)
            return ans_string

        print("")
        print("matrix is:")
        pp.pprint(matrix)
        print("\n compressing \n")
        check_all(matrix)
        pp.pprint(matrix)

# counting rows per frame, storing as indices of array
# in a paginated array of symbols to be comrpessed
def count_frames(matrix):
    frames_len = 0
    for frame in matrix:
        frames_len += 1

# counting rows per frame, storing as indices of array
# in a paginated array of symbols to be comrpessed
def count_rows(matrix):
    # number of rows in each frame,
    # access at indices rows_len_ary[frames_len-1] -> 0...frames_len-1
    row_len_ary = []
    # num rows per frame, 2nd level depth in 3D matrix
    row_len = 0
    for frame in matrix:
        for row in frame:
            row_len += 1

        row_len_ary.append(row_len)

# redundant to encode up and down, because in the loop, after the first iteration
# in a square 3d matrix (paged from original data / symbol set)
matrix = \
    [
        [1, 1, 1, 1, 1],  # 1R4 => ["1R4D3F2",0,0,0,0]
        [1, 1, 1, 1],  # 1R3 => ["1R3",0,0,0]
        [1, 1, 1]  # 1R2 => ["1R",0,0]
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
check_all()
pp.pprint(matrix)