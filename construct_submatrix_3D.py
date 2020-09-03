import pprint as pp

def construct_submatrix_3d(matrix, include_frames, include_ary, include_columns):
    ans_ary = []

    for frame in matrix:
        if check_include_ary(include_frames, matrix.index(frame)):
            frame_t = []

            for row in frame:
                if check_include_ary(include_ary, frame.index(row)):
                    row_t = []

                    for col in row:
                        if check_include_ary(include_columns, row.index(col)):
                            row_t.append(col)

                    frame_t.append(row_t)

            ans_ary.append(frame_t)

    pp.pprint(ans_ary)

def check_include_ary(include_ary, target_row_index):
    for row in include_ary:
        if row == target_row_index:
            return True



include_rows1 = [1]
include_columns1 = [1]
include_frames1 = [1]

matrix1 = \
[
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ],
    [
        [10, 11, 12],
        [13, 14, 15],
        [16, 17, 18]
    ],
    [
        [19, 20, 21],
        [22, 23, 24],
        [25, 26, 27]
    ]
]

construct_submatrix_3d(matrix1, include_rows1, include_columns1, include_frames1)