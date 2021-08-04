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
                target = matrix[z][y][x+1]
                origin = matrix[z][y][x]
                                #               
                n = check_right(o_z, o_x, o_y matrix, t_z, t_y, t_x, 0)
                if n == 0:
                    pass
                else:
                    char = matrix[z][y][x]
                    origin = str(matrix[z][y][x]*n)
                    matrix2[x][y][z] = right_ans

def check_right(matrix, n):
    n = 1
    target = matrix[z][y][x+n]
    origin = matrix[z][y][x]
    if target != origin:
        return 
    elif target == origin:
        n+=1
        target = matrix[z][y][x+n]
        origin = matrix[z][y][x]
    else:
        return
        target = matrix[z][y][x+n]
        origin = matrix[z][y][x+n+1]

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