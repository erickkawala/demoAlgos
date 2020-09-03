import pprint as pp


def construct_submatrix_3d(matrix, include_frames, include_rows, include_columns):
    ans_ary = []

    for frame in matrix:
        if check_include_ary(include_frames, matrix.index(frame)):
            frame_t = []

            for row in frame:
                if check_include_ary(include_rows, frame.index(row)):
                    row_t = []

                    for col in row:
                        if check_include_ary(include_columns, row.index(col)):
                            row_t.append(col)

                    frame_t.append(row_t)

            ans_ary.append(frame_t)

    pp.pprint(ans_ary)

# could all be rewritten arbitrarily: if target_index exists in include_ary
#       return true
# def check_include_frames(include_frames, target_frame_index):
#     for frame in include_frames:
#         if frame == target_frame_index:
#             return True


def check_include_ary(include_ary, target_ary_index):
    for row in include_ary:
        if row == target_ary_index:
            return True


# def check_include_columns(include_columns, target_column_index):
#     for column in include_columns:
#         if column == target_column_index:
#             return True


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

# matrix2 = \
#     [
#         [
#             [1, 2, 3]
#         ]
#     ]\

print("matrix1 before is: \n")
pp.pprint(matrix1)
print("\n")

construct_submatrix_3d(matrix1, include_frames1, include_rows1, include_columns1)

# print("matrix1 is now: \n")
# pp.pprint(matrix1)
# print("\n")

# print("matrix1 should be: \n")
# pp.pprint(matrix2)
# print("\n")

# print("... Running: \n")
# construct_submatrix_3d(matrix1, include_frames1,
#                        include_rows1, include_columns1)


### Uncomment the below code for benchmarking ###

# import timeit
# setup = "from __main__ import construct_submatrix_3d,\
#     matrix1,include_frames1,include_rows1,include_columns1"
# time = timeit.timeit("construct_submatrix_3d(matrix1, include_frames1,\
# include_rows1, include_columns1)", setup=setup)
# # print(time)
# average = time/1000000
# print("\n10M executions in "+str(time)+" seconds \n")
# print("average: "+str(average)+" seconds \n")

# print("\nDone.")