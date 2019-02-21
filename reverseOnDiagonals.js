
function reverseOnDiagonals(matrix)
{

var matrix1 = matrix;
var diag1Len = matrix[0].length;
var diag2Len = 0;

var diag1 = [];
var diag2 = [];
  
  // used to pass all checks on codefights
  
  //get Diag2Len
  for (var i = 0; i <= matrix[0].length-1; i++)
  {
    diag2Len++;
  }

  console.log('matrix length: ', matrix.length);

  console.log('get diag 1\n');
  // get diag1 and push to new array: diag1

  for (var i = 0; i <= diag1Len-1; i++)
  {
    // console.log(i)
    diag1.push(matrix[i][i]);
  }
  
  // console.log(diag1);


  //get diag2 and push to new array: diag2
  console.log('get diag 2\n');

  for (var t = 0; t <= matrix[0].length-1; t++)
  {
    // console.log(matrix[0]+'\n');

    var buffer = 1;

    for (var k = matrix[t].length-1; k >= 0 ; k--)
    {
          if (k == matrix[t].length-1 && t == 0)
          {
            diag2.push(matrix[t][k]);
          }
          if (k == matrix[t].length - t)
          {
            diag2.push(matrix[t][k-buffer]);
            buffer++;
          }
    }
  buffer++;

  }


  console.log('diag1', diag1);
  console.log('diag2', diag2);

  var diag2Rev = diag2.reverse();
  // console.log('diag2Rev', diag2Rev);
  var diag1Rev = diag1.reverse();

  console.log('matrix1',matrix1);
    // rewrite diagonal 1
    console.log('rewrite diagonal 1...')
    for (var i = 0; i <= matrix.length-1; i++)
    {
        matrix1[i][i] = diag1Rev[i];
    }
    console.log(matrix1);


    // rewrite diagonal 2

    console.log('rewrite diagonal 2...');
    for (var t = 0; t <= matrix[0].length-1; t++)
    {
        var row = matrix1[t];
        for (var k = row.length-1; k >= 0 ; k--)
        {
            if (k == row.length-1 && t == 0)
            {
              matrix1[t][k] = diag2Rev[t];
              buffer++;
            }
            else if (k == row.length-1 - t && t > 0)
            {
              matrix1[t][k] = diag2Rev[t];
              buffer++;
            }
            else {
              continue;
            }
        }
        buffer++;
    }
    console.log(matrix1);
    return matrix1;
}

matrix2 =
    [
      [0, 1, 2, 3],
      [4, 5, 6, 7],
      [8, 9, 10, 11],
      [12, 13, 14, 15]
    ]

var matrix =
    [ 
      [1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]
    ]



reverseOnDiagonals(matrix);


reverseOnDiagonals(matrix2);
// console.log('matrix2 ans:' + '\n', matrix2)

// matrix3 = [[1,2,3]]
// reverseOnDiagonals(matrix3);
// console.log('matrix3 ans:', matrix3)
// reverseOnDiagonals(matrix1);
