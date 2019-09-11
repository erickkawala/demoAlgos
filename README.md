## Python Algos
Compression_algo_pseudo contains the pseudocode for compression_algo.py. Currently not functional.

construct_submatrix_2D, 3D are benchmarked:
	2D: 10M executions in 2.1273080479999997 seconds
	3D: 10M executions in 7.822783686999999 seconds

size_of.py is a command line script that takes one object parameter.

py_pkg_which.py <python_module> => where arg is a python package and you have a python env setup, prints location of python package argument.

## Elixir Phoenix Seed Scripts

See www.github.com/erickkawa/phx-hello for project with schemas to test seed scripts.

seed_all_users.ex seeds a database with user schema fields for username and name while seeding birth_year, birth_month, birth_day, country, subregion, and city. Number of iterations is set with n_stop parameter in calling function at bottom of file. Average insert operation time reports between 3ms and 4ms, but I found that this is actually a lot higher than the actual time. Also, region list item names are not equal, skewing average time.

seed_all_random.ex seeds user schema fields for regions randomly and uses a random displacement buffer to birth_year, birth_month, and birth_day.

seed_all_IO.ex prints all schema fields at the command line, instead of inserting them.

time.ex prints out the days of the year with leap years, used to seed user's birth_year, birth_month, and birth_day, starting at 1900. Can be changed to work with more recent years.

## misc
simplex_algo.ex is a maximization or minimization of an objective function-- the linear programming simplex solution.
(currently incomplete, may do python)

## JS
reverseOnDiagonals.js is code used for a codefight on codefights.com. Now, codesignal.com. Reverses the diagonals of a square 2D array.

