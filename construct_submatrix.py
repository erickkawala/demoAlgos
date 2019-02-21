def construct_submatrix_inclusion (matrix, include_rows, include_columns):
    ans_ary = []

    # SEE construct_submatrix_3d.py for comments / pseudocode
    for row in matrix:
        if check_include_rows(include_rows,matrix.index(row)):
            # ans_ary.append([])
			# just need to append a row and push good cols when check_rows==1
            row_t = []
            for col in row:
                if check_include_columns(include_columns, row.index(col)):
                    row_t.append(col)
            ans_ary.append(row_t)
			
    print(ans_ary)

				
def check_include_rows(include_rows, target_row_index):
    for row in include_rows:
        if row == target_row_index:
                return True
    

def check_include_columns(include_columns, target_column_index):
    for column in include_columns:
        if column == target_column_index:
            return True


include_rows1=[2]
include_columns1=[2]

matrix1 = \
[
 [1,2,3],
 [4,5,6],
 [7,8,9]
]

construct_submatrix_inclusion(matrix1,include_rows1,include_columns1)

# =>  [9]
# exclusive is harder... or not
