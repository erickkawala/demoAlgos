import pprint as pp
import timeit
def construct_submatrix_inclusion(matrix, include_rows, include_columns):
    ans_ary = []

    for row in matrix:
        if check_include_ary(include_rows, matrix.index(row)):
            # ans_ary.append([])
			# just need to append a row and push good cols when check_rows==1
            row_t = []
            for col in row:
                if check_include_ary(include_columns, row.index(col)):
                    row_t.append(col)
            ans_ary.append(row_t)

    pp.pprint(ans_ary)

# could all be rewritten arbitrarily: if target_index exists in include_ary
#       return true
def check_include_ary(include_rows, target_row_index):
    for row in include_rows:
        if row == target_row_index:
                return True


# def check_include_columns(include_columns, target_column_index):
#     for column in include_columns:
#         if column == target_column_index:
#             return True


include_rows1 = [1]
include_columns1 = [1]

matrix1 = \
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

pp.pprint(matrix1)

construct_submatrix_inclusion(matrix1, include_rows1, include_columns1)

### Uncomment the below code for benchmarking ###

# setup = "from __main__ import construct_submatrix_inclusion,\
#     matrix1,include_rows1,include_columns1"
# time = timeit.timeit("construct_submatrix_inclusion(matrix1,\
# include_rows1, include_columns1)", setup=setup)

# average = time/1000000
# print("\n10M executions in "+str(time)+" seconds \n")
# print("average: "+str(average)+" seconds \n")
