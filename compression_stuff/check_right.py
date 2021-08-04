# from prettyprint import pp

def compress(matrix):
    for frame in matrix:
        # check forward, back here
        for row in frame:
            # check up, down here
            for col in row:
                # check left, right
                z = matrix.index(frame)
                print(z)
                y = frame.index(row)
                print(y)
                x = row.index(col)
                print(x)
                ans_string = ""
                right_ans = ""
                # check_all(matrix, z, y, x)
                target = matrix[z][y][x+1]
                print("target:", target)
                origin = matrix[z][y][x] #set origin xyz and target xyz below:
                print("origin:", origin)
                o_z = matrix[frame]
                o_y = matrix[row]
                o_x = matrix[col]
                t_z = matrix[frame]
                t_y = matrix[row]
                t_x = matrix[col]

                

                                #origin  matrix3D-paged-in-data  target  ele to right                     #match_ctr
                check_right(o_z, o_y, o_x, matrix, t_z, t_y, t_x+1, 0)
                if n == 0:
                    pass
                else:
                    char = matrix[z][y][x]
                    origin = str(matrix[z][y][x]*n)
                    matrix2[x][y][z] = right_ans

# doing 2d array, check right matches, then turn matches into "", put compress symbol into current ele
                                                    #n is match counter
def check_right(o_z, o_y,o_x, matrix, t_z, t_y, t_x, n):
    n = 0
    target = matrix[z][y][x+n]
    origin = matrix[z][y][x]
    if target != origin:             # and frame_ctr != frame_len:
        try: check_right(o_z, o_y, o_x, matrix, t_z, t_y, o_x, 0)
        except IndexError: #no more columns left, go to next row, set match_ctr to 0
            
            check_right(o_z, o_y, o_x, matrix, t_z, t_y+1, o_x, 0) # go to next z,y+1,x 0,1,0
    elif target == origin:
        n+=1
        try:
            target = matrix[z][y][x+n]
            origin = matrix[z][y][x]
            if target == origin:
                n+=1
                print(n)
            check_right(o_z, o_y, o_x, matrix, t_z, t_y, o_x+n, n)
            # check_right(o_z, o_y, o_x, matrix, t_z, t_y, o_x+n, n)
            # right_backfill(o_z, o_y, o_x, matrix, t_z, t_y, o_x, 0) 
        except IndexError:
            check_right(o_z, o_x, o_y, matrix, t_z, t_y, o_y+1, 0) # go to next z,y+1,x 0,1,0
    else:

        target = matrix[z][y][x+n]
        origin = matrix[z][y][x+n+1]
#                  how many matches from check right to back_fill, n-1 times
#                                     
def right_backfill(n, target_z, target_y, target_x, origin_z, origin_y, origin_x):
    n-=1

    if n == 0:
        return 0
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

matrix2 = matrix

compress(matrix2)