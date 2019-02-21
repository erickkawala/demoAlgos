import pprint as pp

def construct_submatrix_3d (matrix, include_frames, include_rows, include_columns):
    ans_ary = []

    # if frame index in matrix matches from include_frames ary, push new frame
    for frame in matrix:
        if check_include_frames(include_frames,matrix.index(frame)):
            frame_t = []

            # if row index in matrix matches from include_rows ary, push new row to frame_t
            for row in frame:
                if check_include_rows(include_rows,frame.index(row)):
                    row_t = []

                    # if col index in matrix matches from include_columns, push matrix[frame[row[col]]] row_t
                    for col in row:
                        if check_include_columns(include_columns, row.index(col)):
                            row_t.append(col)
                
                    # when done pushing columns to row, push row to frame.  continue for all rows in frame.
                    frame_t.append(row_t)
            
            # when done pushing columns to rows and rows to frame, push frame to ans_ary
            # this should probably be ans_ary = frame_t, but this works...
            ans_ary.append(frame_t)
			
    pp.pprint(ans_ary)

# these could all be the same arbitrary function
# if current index exists in array of target indices, return true:
def check_include_frames(include_frames, target_frame_index):
    for frame in include_frames:
        if frame == target_frame_index:
            return True
				
def check_include_rows(include_rows, target_row_index):
    for row in include_rows:
        if row == target_row_index:
            return True

def check_include_columns(include_columns, target_column_index):
    for column in include_columns:
        if column == target_column_index:
            return True


# frames, rows, column indices to include:
include_rows1=[0,1]
include_columns1=[0,1]
include_frames1=[0,1]

matrix1 = \
    [\
        [\
            [1, 2, 3],\
            [4, 5, 6],\
            [7, 8, 9]\
        ],\
        [\
            [1, 11, 12],\
            [13, 14, 15],\
            [16, 17, 18]\
        ],\
        [\
            [19, 20, 21],\
            [22, 23, 24],\
            [25, 26, 27]\
        ]\
    ]

matrix2 = \
    [[[1, 2], [4, 5]], [[1, 11], [13, 14]]]

# matrix before
print("\nMatrix1 is: \n")
pp.pprint(matrix1)
print("\n")

# correct answer
print("Answer should be: \n")
pp.pprint(matrix2)
print("\n")

# actual result after processing matrix
print("... Running. Answer is:\n")
construct_submatrix_3d(matrix1, include_frames1, include_rows1, include_columns1)
print("\nDone.\n")



# output is:
# [[[1, 2], [4, 5]], [[1, 11], [13, 14]]]
# => correct.
