Compression_algo_pseudo contains the pseudocode for compression_algo.py. Currently not functional.

construct_submatrix_2D, 3D are benchmarked:
	2D: 10M executions in 2.1273080479999997 seconds 
	3D: 10M executions in 7.822783686999999 seconds


See www.github.com/erickkawa/phx-hello for project with schemas to test seed scripts.

seed_all_users.ex seeds a database with user schema fields for username and name while seeding birth_year, birth_month, birth_day, country, subregion, and city. Number of iterations is set with n_stop parameter in calling function at bottom of file.
Average insert operation time reports between 3ms and 4ms, but I found that this is actually higher than the actual time in a test of 8.7 million. Also, region list item names are not equal, skewing average time.

seed_all_uneven_regions.ex seeds users table with country, subregion, and city with list lengths 203, 202 and 201 respectively.

seed_all_uneven_regions_time.ex seeds user schema fields for regions unevenly and adds a random displacement buffer to birth_year, birth_month, and birth_day.

time.ex prints out the days of the year with leap years, used to see user's birthday year, month, and day, starting at 1900.  Can be changed to work with more recent years.


size_of.py is a command line script that takes one object parameter.

simplex_algo.ex is a maximization or minimization of an objective function-- the linear programming simplex solution.
(currently incomplete)


