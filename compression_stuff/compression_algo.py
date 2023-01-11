import pprint as pp

# think about going 4D with pages, pointers?
# freq map symbols of form ArrayValue Direction MatchCounter

# eventually, y_length and z_length can be arrays
# used with counters in check_right that contain
# the number of rows in each frame to know when to
# go to the next frame, and last frame IndexError can be handled the same way
#  ary rows_len [0] represents the number of rows in the first frame
#  int frames_len represents number of frames to iterate, indices frames_len-1

def check_all(matrix):

    for frame in matrix:
        z = matrix.index(frame)
        print("z", z)
        for row in frame:
            # y = matrix.index(row)
            y = frame.index(row)
            print("y: ", y)
            for col in row:
                # x = matrix.index(col)
                x = row.index(col)
                print("x: ", x)

                
                z = matrix.index(frame)
                y = frame.index(row)
                x = row.index(col)
                print("matrix[z][y][x]")
                print(matrix[z][y][x])
                if matrix[z][y][x] == "":
                    pass
                else:
                    print("for loop else: not empty ary ele",matrix[z][y][x])
                    # when check_right returns, next ary element is pushed through
                    # matrix[z][y][x], so don't have to increment from check_right
                    #           origin          target    matchctr  y_ctr z_ctr
                    check_right(z, y, x, matrix, z, y, x+1, 0,      0,    0)
                    # ans_string = ""
                                    # origin z, y, x, next is z, y, x+1
                                    # if match, recurse calls next z, y, x+1
                    # check_right(z, y, x+1, matrix, z, y, x+2, 0)
                    # check_down, check forward
                    #   # ideally, start in the middle, check L,R,Forward,Back,Up,Down
                    #   # update 2021: it would make more sense to start at 0,0,0 and look for matches
                    #                   but if there were more symbols, it would make sense to start in middle
                                                                        # and check Up Down Left Right Forward Back
                                        # then most frequent symbols the compressed bit fields with index key map+compressed data
                                        # in any language, C/c++, smallest element is replacing the symbol from that data
                    # matrix[z][y][x] = ans_string, say: 1
                    # ans_string += check_down :1, append 1D
                    # ans_string += check_forward, 1, append 1F
                    # print("ans_string", ans_string)

def check_right(origin_z, origin_y, origin_x, matrix, target_z, target_y, target_x, 
                match_ctr, y_ctr, z_ctr):
    print("check_right function called.")
    try:
        origin = matrix[origin_z][origin_y][origin_x]
        target = matrix[target_z][target_y][target_x]
        if target == origin:
            match_ctr += 1
            target = ""
            # turn ary int to str
            ans_string = str(origin)+"R"+str(match_ctr)
            print("ans_string: ", ans_string)
            try:
                check_right(origin_z, origin_y, origin_x, matrix,
                            target_z, target_y, target_x+1, 0, y_ctr, z_ctr)

            # first row index error, increment y_ctr (row) to backfill after no more target==origin
            #                         z_ctr (frame) will help backfill compressed eles to "", see bottom
            except IndexError:
                print("target == origin, except IndexError, match_ctr: ", match_ctr)
                if match_ctr == 0:
                    check_right(origin_z, origin_y+1, origin_x, matrix,
                                target_z, target_y+1, target_x+1, 0, y_ctr+1, z_ctr)

                elif match_ctr > 0:
                    print(origin)
                    ans_string = str(origin)+"R"+str(match_ctr)
                    # print out the same ans_string again on IndexError
                    print("IndexError:", "ans_string", ans_string)
                    return ans_string

        elif target != origin:
            if match_ctr == 0:
                # could potentially do a check_right that wraps to the next row here
                # check_right_wrap (to look back to 0th in row/col)
                
                # if y_ctr = rows_len:
                # go to next frame by incrementing origin_z, target_z
                # increment z_ctr

                try:
                    origin = matrix[target_z, target_y, target_x+1]

                    check_right(target_z, target_y, target_x, matrix,
                                target_z, target_y, target_x+1, 0, y_ctr+1, z_ctr)
                
                except IndexError:
                    # go to next row
                    check_right(origin_z, origin_y+1, origin_x, matrix,
                                target_z, target_y+1, target_x+1, 0, y_ctr+1, z_ctr)

            elif match_ctr > 0:
                ans_string = str(origin)+"R"+str(match_ctr)
                print("ans_string: ", ans_string)
                origin = ans_string

                # try:
                #     check_right(target_z, target_y, target_x, matrix,
                #                 target_z, target_y, target_x+1, 0)
                # except IndexError:
                #     ans_string = str(origin)+"R"+str(match_ctr)
                #     return ans_string

        elif target != origin and match_ctr == 0:
            return
        # we want to let the calling loop call check right itself
        #     try:
        #         check_right(origin_z, origin_y, origin_x+1, matrix, target_z, target_y, target_x+1, 0)
        #     except IndexError:
        #         return str(origin)
        else:
            print(" target != origin and match_ctr == 0:")
            return str(origin)

    # origin != target:
    except IndexError:
        if match_ctr == 0:
            return origin  #pass?

        elif match_ctr > 0:
            ans_string = str(origin)+"R"+str(match_ctr)
            print("ans_string", ans_string)
            return ans_string
        else:
            print("main try/catch error, review control flow")
    else:
        print("end of control flow")
        return
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

matrix = \
    [
        [1, 1, 1, 1, 1],  # 1R4 => ["1R4D3F2","","","",""]
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
