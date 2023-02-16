

def compress(matrix):
    for frame in matrix:
        # check forward, back here
        for row in frame:
            # check up, down here
            for col in row:
                # check left, right
                z = matrix.index(frame)
                y = frame.index(row)
                x = row.index(col)
                ans_string = ""
                right_ans = ""
                # check_all(matrix, z, y, x)


                # n = 1
                #count matches to the right
                count_right(o_z, o_y, o_x, matrix, t_z, t_y, t_x, 1)
                
                
                                #               
                n = count_right(o_z, o_y, o_x, matrix, t_z, t_y, t_x, 0)
                char = matrix[z][y][x]
                origin = str(matrix[z][y][x]*n)


                matrix2[x][y][z] = right_ans

#                                                     1
def count_right1(o_z, o_x, o_y, matrix, t_z, t_y, t_x, n):
    # n = 1
    try target = matrix[o_z][o_y][o_x+n]:
    origin = matrix[t_z][t_y][t_x]
    if target != origin:
        return  # nothing to compress
    elif target == origin:
        n+=1
        target = matrix[z][y][x+n]
        origin = matrix[z][y][x]
    else:
        return
        target = matrix[z][y][x+n]
        origin = matrix[z][y][x+n+1]

    # call right_backfill

#                                                     n
def count_right2(o_z, o_x, o_y, matrix, t_z, t_y, t_x, 0):
    if (n == 1):
        try target = matrix[z][y][x+n]:
            origin = matrix[z][y][x]
            if target != origin and n == 0:
                pass
            elif target != origin and n > 0:
                right_backfill()
                pass # go to next index, check_right(), 
                        # ^pass is return if check_right() called in loop
            elif target == origin:
                n+=1
                # silent pass to next item
                # target = matrix[z][y][x+n]
                # origin = matrix[z][y][x]
            else:  # target != origin and n > 0:
                target = matrix[z][y][x+n+1]
                origin = matrix[z][y][x+n]
                return n
        except IndexError:
            ## handle IndexError when no matches, so dont backfill ##
            return
    else: #(n > 1):
        try target = matrix[z][y][x+n]:
            origin = matrix[z][y][x]
            if target != origin and n == 0:
                pass
            elif target != origin and n > 0:
                right_backfill()
                pass # go to next index, check_right(), 
                        # ^pass is return if check_right() called in loop
            elif target == origin:
                n+=1
                # silent pass to next item
                # target = matrix[z][y][x+n]
                # origin = matrix[z][y][x]
            else:  # target != origin and n > 0:
                target = matrix[z][y][x+n+1]
                origin = matrix[z][y][x+n]
                return n
        except IndexError:
            print("n > 1 - index error, here n is match counter")
            return
            ## handle IndexError when no matches ##
            ## n is the match counter, so if n!==0, then call right_backfill, @line 54
            right_backfill(t_z, t_y, t_x, o_z, o_y, o_x, n)
        

#      num matches n, target z y x,  origin z y x
def right_backfill(n, t_z, t_y, t_x, o_z, o_y, o_x):
    # n is current number of matches to turn to empty string ""
    # going from 
    if n == 0:
        return
    else:
        matrix[z][y][x]
        
        x-=1

matrix = [ \
    [ \
        [1, 1, 1, 1, 1],  # 1R4 => ["1R4D3F2",0,0,0,0]
        [1, 1, 1, 1],  # 1R3 => [0,0,0,0]
        [1, 1, 1]  # 1R2 => [0,0,0]
    ]
]

compress(matrix)