COMPRESS


def getMaxAdjacentMatches():
    GET OPTIMAL PAGE/FRAME SIZE
    def iteratePageSize(matrix_in),pageX,pageY,pageZ):
        

get optimal page size, take all symbols in,
determine if 1,2,1,3,1, then index-i%2
WRT TO OPTIMAL STARTING POINT, diff w diff page sizes

GET OPTIMAL ROW/COLUMN SIZE? can have diff sized rows, columns, need map to reverse it then

if many 1R4's then map 1R4 to 0,
append symbol=>number seq at end
delimited small way

wanna go 10 ways? upLeft, upRight,
downLeft, downRight, 
ULF, ULB
URF, URB

DLF, DLB
DRF, DRB

4 - 3COORD DIAGONALS ^^ CHECK FUNCTIONS, PER PAGE SIZE / W VARIABLE PAGE SIZES

9*3-1
1 is the self, center index

9 adjacent/diagonal indices in Yaxis above it
9 adjacent/diagonal indices in Yaxis below it
8 adjacent indices in Yaxis of index
26 D directions to compress in, at N 3D indices to start compressing in, at Z*X*Y page sizes
total permutations/checks:  D*N*Z*Y*X


unless you can determine an optimal page size and order that can be appended or prepended
to the compress file / special delimited, like:
    page size 2x2, order 1,5,3,4,2 for:
        15342\


4 dimensions to get more adjacent indices?
wrt to page size, where number of total adjacent, BUT goal is max Adjacent Matches


4 R,L,F,B,U,D



3! = 6
3! = 6

lol

start middle, 1R1L2U3D4F5B6
etc

FREQ MAP to BIT FIELD
either freq map symbols or freq map 1R4s
highest frequency symbols have 0-9...n

if many 1R2s, map to bitfield = 0 in c++
if 2nd most 1R3s, map to 1.. etc

look for contiuous 1R4s..1D4s...1F4s...
find the optimal combination of 

go diagonally... say 1RDF4... for 1,1,1 to 4,4,4
doesnt matter what codes are, get mapped to symbols





## 4D?