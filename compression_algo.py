import pprint as pp


def check_all(matrix):

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
                    ans_string = check_right(z, y, x,
                                             matrix, z, y, x+1, 0)
                    matrix[z][y][x] = ans_string
                    # ans_string += check_down
                    # ans_string += check_forward
                    print("ans_string", ans_string)
                    matrix[z][y][x] = ans_string


def check_right(origin_z, origin_y, origin_x, matrix, new_z, new_y, new_x, counter):
    try:
        origin = matrix[origin_z][origin_y][origin_x]
        target = matrix[new_z][new_y][new_x]
        if origin == target:
            # print(matrix[z][y][x], matrix[z][y][x+1])
            counter += 1
            target = ""
            try:
                check_right(origin_z, origin_y, origin_x, matrix,
                            new_z, new_y, new_x+1, counter)

            except IndexError:
                if counter == 0:
                    print('origin', origin)
                    return str(origin)

                elif counter > 0:
                    ans_string = str(origin)+"R"+str(counter)
                    print("ans_string", ans_string)
                    return ans_string

        elif target != origin and counter > 0:
            ans_string = str(origin)+"R"+str(counter)
            print("ans_string: ", ans_string)
            try:
                check_right(new_z, new_y, new_x+1, matrix,
                            new_z, new_y, new_x+1, 0)
            except IndexError:
                ans_string = str(origin)+"R"+str(counter)
                return ans_string

        elif target != origin and counter == 0:
            return origin
        # we want to let the calling loop call check right itself
        #     try:
        #         check_right(origin_z, origin_y, origin_x+1, matrix, new_z, new_y, new_x+1, 0)
        #     except IndexError:
        #         return str(origin)
        else:
            return str(origin)

    # origin != target:
    except IndexError:
        if counter == 0:
            return origin

        elif counter > 0:
            ans_string = str(origin)+"R"+str(counter)
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
