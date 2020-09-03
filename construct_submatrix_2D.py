import pprint as pp


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
