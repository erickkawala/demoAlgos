# this is some recursive try to check_right recursively and preserve with globals and idk

p_origin = [0]
p_target = [0]
ans_string = "

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

                if matrix[z][y][x] == ""
                    pass # its compressed
                ans_string = ""
                right_ans = ""

                # check_all(matrix, z, y, x)
                try target = matrix[z][y][x+1]:
                    origin = matrix[z][y][x]
                                #               ALL MESSED UP HERE, TRY CATCH X+ , this is a waste of time
                    n = count_right(o_z, o_x, o_y matrix, t_z, t_y, t_x, 0)
                    char = matrix[z][y][x]
                    origin = str(matrix[z][y][x]*n)
                    matrix2[x][y][z] = right_ans
                except IndexError:
                    

def count_right(matrix, n):
    n = 1
    target = matrix[z][y][x+n]
    origin = matrix[z][y][x]
    if target != origin:
        return # no matches, next index thru auto loop
    elif target == origin:
        n+=1
        target = matrix[z][y][x+n]
        origin = matrix[z][y][x]
    else:
        return
        target = matrix[z][y][x+n]
        origin = matrix[z][y][x+n+1]

# num indices to 0 out, target indices,              stop at origin indices
#    from count_right
def right_backfill(n, target_z, target_y, target_x, origin_z, origin_y, origin_x):
    # we checked right for matches and had more than 0
    #   so backfill >> LEFT <<  
    # if n starts at 1, break at 1.  starts at 0, break at 0, redundant
    if target_x == origin_x:
        return
    else:
        matrix[target_z][target_y][target_x] = ""   # compressing this, make it empty string, size of 37. None is 38
        
        target_x-=1  # if i check_right, i take target_x left
    #       recurse                           go back one step in X
    right_backfill( n-1 , target_z, target_y, target_x-1, origin_z, origin_y, origin_x):


def down_backfill(n, target_z, target_y, target_x, origin_z, origin_y, origin_x):
    # we checked down for matches and had more than 0 - Y negative direction
    #   so backfill in the UP direction - Y positive direction
    # if n == 1:  havent figured this out yet
    # if n starts at 1, break at 1.  starts at 0, break at 0, redundant
    if target_y == origin_y:
        return
    else:
        matrix[target_z][target_y][target_x] = ""
        
        target_y+=1
    #       recurse                           go back one step in X
    down_backfill( n-1 , target_z, target_y, target_x-1, origin_z, origin_y, origin_x):

matrix = [ \
    [ \
        [1, 1, 1, 1, 1],  # 1R4 => ["1R4D3F2",0,0,0,0]
        [1, 1, 1, 1],  # 1R3 => [0,0,0,0]
        [1, 1, 1]  # 1R2 => [0,0,0]
    ]
]

matrix2 = matrix

compress(matrix2)



def read_symbol_map:
    pass

def symbol_map_freq
    # map most freq symbols to 0-9
    # IRL, map to a bitfield of 0->2^n-1, c++
