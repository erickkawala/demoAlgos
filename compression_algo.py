import pprint as pp

ans_string = ""

# can iterate through x until IndexError
def get_y_z_length(matrix):
    rows_len = 0
    frames_len = 0
    for frame in matrix:
        for row in frame:
            rows_len += 1

# eventually, y_length and z_length can be arrays
# used with counters in check_right that contain
# the number of rows in each frame to know when to
# go to the next frame, and last frame IndexError can be handled the same way
#  ary rows_len [0] represents the number of rows in the first frame
#  int frames_len represents number of frames to iterate, indices frames_len-1
# at the last frame, last row, check_right should handle IndexError
# but actually, we need to know when to stop... so probably need z_counter
# or see what happens with an unhandled IndexError for check_right target OOB

def check_all(matrix):

    for frame in matrix:
        for row in frame:
            for col in row:
                z = matrix.index(frame)
                y = frame.index(row)
                x = row.index(col)

                if matrix[z][y][x] == "":
                    pass
                else:
                    # when check_right returns, next ary element is pushed through
                    # matrix[z][y][x], so don't have to increment from check_right
                    #           origin          target    matchctr  y_ctr
                    check_right(z, y, x, matrix, z, y, x+1, 0,      0)
                    # ans_string = ""
                                    # origin z, y, x, next is z, y, x+1
                                    # if match, recurse calls next z, y, x+1
                    # check_right(z, y, x+1, matrix, z, y, x+2, 0)
                    # matrix[z][y][x] = ans_string
                    # ans_string += check_down
                    # ans_string += check_forward
                    # print("ans_string", ans_string)

def check_right(origin_z, origin_y, origin_x, matrix, target_z, target_y, target_x, 
                match_counter, y_counter):
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
                            target_z, target_y, target_x+1, 0, y_counter)

            # first row index error, increment y_counter
            except IndexError:
                if match_counter == 0:
                    check_right(origin_z, origin_y+1, origin_x, matrix,
                                target_z, target_y+1, target_x+1, 0, y_counter+1)

                elif match_counter > 0:
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
                # incremen # redundant, last IndexError handles

                try:
                    origin = matrix[target_z, target_y, target_x+1]

                    check_right(target_z, target_y, target_x, matrix,
                                target_z, target_y, target_x+1, 0, y_counter+1)
                
                except IndexError:
                    # go to next row
                    check_right(origin_z, origin_y+1, origin_x, matrix,
                                target_z, target_y+1, target_x+1, 0, y_counter+1)

            elif match_counter > 0:
                ans_string = str(origin)+"R"+str(match_counter)
                print("ans_string: ", ans_string)
                origin = ans_string

                try:
                    check_right(target_z, target_y, target_x, matrix,
                                target_z, target_y, target_x+1, 0, y_counter)
                                                            #  ^^ match counter
                except IndexError:
                    ans_string = str(origin)+"R"+str(match_counter)
                    return ans_string

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

matrix = \
    [
        [1, 1, 1, 1, 1],  # 1R4 => ["1R4D3F2",0,0,0,0]
        [1, 1, 1, 1],  # 1R3 => [0,0,0,0]
        [1, 1, 1]  # 1R2 => [0,0,0]
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
