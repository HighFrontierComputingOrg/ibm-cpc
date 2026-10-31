# Linear Programming: The Solution of Refinery Problems

> OCR-assisted verbatim transcription of [1955-symonds.pdf](1955-symonds.pdf). PDF page breaks are retained. Tables and mathematical notation are represented in plain text where Markdown cannot preserve their original layout; verify uncertain OCR characters against the scan.

## PDF page 1

*[Blank page]*

## PDF page 2

Walter A. Lawrence

WITHDRAWN
BATES COLLEGE LIBRARY

BATES COLLEGE LIBRARY
WESTERN MAINE
PRESENTED BY
WALTER A. LAWRENCE
Professor of Chemistry
Bates College

## PDF page 3

*[Blank page]*

## PDF page 4

*[Blank page]*

## PDF page 5

Linear Programming:

The Solution of Refinery Problems

GIFFORD H. SYMONDS

Executive Secretary, Manufacturing Technical Committee
Esso Standard Oil Company

1955
Esso Standard Oil Company, New York, N.Y.

## PDF page 6

Permission to reproduce material contained herein may be secured from the copyright owners. For
information address Public Relations Department, Esso Standard Oil Company, 15 West 51 Street,
New York 19, New York.

Copyright, 1955, by Esso Standard Oil Company

Library of Congress Catalog Card Number: 55-11950

Printed in United States of America

## PDF page 7

PREFACE

The material in this book originated in 1953 as a series of
intracompany memoranda intended to illustrate the appli-
cation of linear programming to the solution of refinery
problems. In view of the advantages of exchanging this
type of information with others, some of the applications
were presented as papers at the IBM Petroleum Confer-
ence in Endicott, N. Y., during October, 1953, at the
Econometric Society Meeting in Washington, D. C., dur-
ing December, 1953, and at the Society for Advancement
of Management Meeting in New York City during Jan-
uary, 1954. The requests for copies of these papers led to
the suggestion that the pertinent material be published in
book form.

The author is deeply indebted to Professors A. Charnes
and W. W. Cooper of the Carnegie Institute of Technology
for their instruction in linear programming and for their
helpfulness in reviewing this work. Chapter 7 was prepared
by Mr. Meyer A. Efroymson of the Process Research Divi-
sion, Esso Laboratories, of our associate Esso Research
and Engineering Company and with his permission has
been incorporated into the volume.

GIFFORD H. SYMONDS

## PDF page 8

*[Blank page]*

## PDF page 9

Table of Contents

PAGE

CHAPTER ONE: Introduction ........................................ 1

CHAPTER TWO: A Maximum Profit Fuel Oil Blending Problem Showing the
Rudiments of the Mathematical Procedure .......................... 4

CHAPTER THREE: A Maximum Profit Running Plan Problem ............ 12

CHAPTER FOUR: A Problem in Blending Aviation Gasoline for Maximum
Profit .......................................................... 18

CHAPTER FIVE: A Refinery Improvement Program Under Competitive
Conditions ...................................................... 25

CHAPTER SIX: Optimum Production Rates and Inventory to Meet Uncertain
Seasonal Requirements ........................................... 37

CHAPTER SEVEN: Planning an Experimental Program ................. 47

CHAPTER EIGHT: A Transportation Problem ........................ 54

CHAPTER NINE: A Crude Allocation Problem ....................... 63

References ..................................................... 74

## PDF page 10

*[Blank page]*

## PDF page 11

CHAPTER 1

Introduction

Linear programming is a new mathematical method for solving problems concerned
with decision-making. It is, therefore, of great interest to management people and
their staff advisers. The method is useful in the fields of management science, opera-
tions research, and economics. The quantitative aspects of problems such as optimum
inventories, production schedules, sales efforts, pricing policies, business expansion,
direction of research, evaluation of alternative projects, and economic factors are
subject to analysis by linear programming. The qualitative aspects of these problems
cannot be handled by linear programming, but with ingenuity many of the qualitative
factors can be expressed by quantitative terms. Thus, for example, the quality or
appearance of a product, expressed in an arbitrary scale, may be related to its sales
demand, price, and production cost.

Linear programming is essentially a method for making systematic selections. The
statement of a problem for solution by linear programming involves (1) an objective
and (2) a set of restrictions. Thus, in the simplest of examples, let

X, = amount of product we will sell,

X,» = amount.of product we will not sell,
100 = maximum capacity for sefling product,

$2 = unit profit for selling product.

Our objective is to make the maximum profit

Z = 2X, (max)
and our restriction is the selling capacity

X,+ X2= 100.
We also require that X, and X. not be negative:

X,=0;X2=0.

The solution, of course, is obvious with only a one-dimensional system. Thus
X, = 100
X,=0

and Z = $200.

## PDF page 12

2 Linear Programming: The Solution of Refinery Problems

The solution mechanism by linear programming is as follows:

Step 1 State restrictions X, + X2= 100 (X, = 0).
Step 2 State objective Z = 2X; (max)
Step 3 Determine null case, let 26 =O,
Therefore X_g=100=— X14 Xe
and Z= 0=-2X, + Z.
Step 4 Determine improvement AZ/AX, = 2.
Step 5 Make substitution, let X,= 0.
Therefore X,—100=X,+ Xz
and Z=200= 2X2+Z.

No further improvement in the objective is possible in this case, and an optimal
solution is reached. For such a simple case no mathematical formulation is needed,
but for the usual problem with many restrictions and a complicated objective func-
tion, the method of linear programming may offer the most efficient solution.

In order to apply linear programming to a problem, it is necessary to state the
relationships between the variables as a set of linear equations. The variables must be
otherwise independent and must exceed the number of equations. Thus, mathe-
matically,

LayX; = by (= 1,2-++m; j= 1,2+++n; n> m)
where the sum of the coefficient a, times the value of each variable X; equals a re-
quirement 5; in the ith equation. These equations are the familiar simultaneous equa-
tions such as those used in blending problems. An important difference, of course, is
the requirement that the number of variables must exceed the number of equations so
that an infinite number of solutions can be obtained and the best one selected. Another
requirement is that no quantity can be negative. Thus, mathematically,

X; = 0 and b= 0.

This requirement will assure that only useful answers will be considered.

The solution of the problem by linear programming also requires a directing force
or objective which will be maximized (or minimized) during the solution. This is stated
mathematically

jc,X; = max
where c; is the profit (or cost) per unit of X; used. The solution is carried out by an
iterative process, which at each stage of calculation assigns either zero or positive
values to all X, variables. These values will meet the constraints of the linear equa-
tions and will tend to increase the maximizing function at each stage of calculation.

## PDF page 13

Introduction 3

If a solution is possible, a maximum profit case will definitely be reached and other
cases with lower profit cari dlso be evaluated.

Linear programming has been applied to the solution of certain refinery problems
such as blending available components into required products for maximum profit,
optimum crude allocation to several refineries, and optimum inventory and production
rate for a seasonal product. Illustrative problems have been set up and solved for these
and other problems, Although the values in the illustrative problems are fictional, the
real problems are of considerable economic importance and the linear programming
solution methods have practical significance.

The most widely applicable method of linear programming is the simplex method,
invented by George Dantzig”) and described by Charnes and Cooper‘®) in their In-
troduction to Linear Programming, 1953. This method is suitable for blending and
scheduling problems involving different products, operations, and feed supplies where
a profit motive can be reduced to terms susceptible to mathematical formulation.
Linear programming has also been applied to the solution of game theory problems,
both the two-player zero-sum game type‘®) and the one-player vs. probability game
type. This method is suitable for evaluation of new business ventures or new facil-
ities and for planning optimum inventories against a variable demand. Another
application of linear programming is the transportation model,‘®) a procedure that
applies to optimum distribution of homogeneous material and will solve problems of
minimum-cost transportation and maximum-profit allocation.

A simplex-method problem involving a 25 by 50 matrix can be solved on a desk
computer in about 4 hours per iteration. Solution of the same problem on the IBM
604 multiplier requires about 1 hour per iteration, and on the CPC it is estimated
that 25 to 30 minutes per iteration would be required. However, the greatest efficiency
may be obtained by using the IBM general solution of the simplex method on its 701
Computer which would require only about 30’seconds per iteration for the 25 by 50
problem. The maximum size simplex method problem currently programmed by IBM
is a 50 by 100 matrix. Solutions of the simplex method problems have also been
worked out on other high-speed computers such as the CRC and the Univac. The
number of iterations required will generally be between m and 2m, where m is the
number of rows in the matrix. Calculations for the transportation model are very
simple since only addition and subtraction steps are required. Problems using this
model can be solved easily on a desk computer, unless they are very large.

The illustrative material gathered in this volume shows how these problems are set
up and solved by the various methods of linear programming. All of the calculations
are indicated so that other problems may be set up and solved in similar manner.

## PDF page 14

CHAPTER 2

A Maximum Profit Fuel Oil Blending Problem

Showing the Rudiments of the Mathematical Procedure

A refinery produces, on the average, 1000 gallons per hour of virgin pitch in its crude
distillation operation. This pitch may be blended with flux stock to make commercial
fuel oil, or it may be sent in whole or in part to a visbreaker unit.

1000 P
yee Pelee
Foy

The visbreaker produces an 80 per cent yield of tar which may also be blended with
flux stock to make commercial fuel oil. The visbreaking operation is economically
break-even if the pitch and the tar are given no value—i.e., the value of the overhead
products equals the cost of the operation. The commercial fuel oil brings a realization
of 5 cents per gallon, but the flux stock has a cracking value of 8 cents per gallon. This
information, together with the viscosity and gravity blending numbers and product
specifications, appears in the table below. It is desired to operate for maximum profit.

FUEL OIL BLENDING PROBLEM

Quan. Avail. Value
GPH cPG Vise. BI. No. Grav. BI. No.
Pitch P= 1000 —V 0 5 8
Visbreaker feed Vv 0 oa ae
Tar T=0.8V 0 1t 7
Flux F = any 8 37 24
Fuel oil PLiTitF 5 21 min 12 min

This information may be expressed in the following equations and inequations:

## PDF page 15

Maximum Profit Fuel Oil Blending Problem, Rudiments of Mathematical Procedure 5

Viscosity requirement 5P + 11T -+ 37F =21(P +7 +P).
Gravity requirement “8P 4- 774 24F = 12(P+7+4+F).

Material balances P+V= 1000
T = 0.8V.
Profit will be Z=S(P + T + F) — 8F cents per hour.

Since there are four relations with four unknowns covering the quality and mate-
rial requirements, these may be solved directly. The answer will give the quantities of
pitch, tar, and flux required to meet the minimum viscosity and gravity specifications
of the product. The equations may be restated as follows:

(5 — 21)P 4+- (11 — 21)(0.8V) + (37-2) F = 0
(8 — 12)P + ( 7 — 12)(0.8V) + (24-12)F = 0.

—2P _V42F=0
—P—V13F=—0.

Adding P+V = 1000
gives three simultaneous equations, which may be solved:

—P +42F = 1000

3F = 1000
P= Fey
P = —333
V = 1333
T = 1067.

This solution is impossible, since negative quantities are not permissible. The
method of simultaneous equations will not guard against negative quantities. In fact,
when there are many variables, some negative quantities are almost certain to result.
The usual procedure at this point is to look over the requirements to discover what is
causing the trouble. Here it is obvious that minimum viscosity and minimum gravity
cannot be met at the same time with positive quantities. There must be some give-
away in one or both of these qualities. How can maximum profit operation be assured
in this situation? This is exactly what linear programming can do. Of course, for
small-scale problems, the optimum operation can be surmised or even determined
by comparing all the known alternatives; for any size problem it can be calculated
unfailingly by linear programming.

One of the basic features of linear programming is that no quantity may be nega-
tive. The procedure assures that all requirements will be met and that the maximum

## PDF page 16

6 Linear Programming: The Solution of Refinery Problems

objective will be reached. For a simplified example of linear programming the reader
is referred to a paper by A. W. Tucker given at the 1953 ASOQC Convention. In
this example the requirements are the quality and material balances. The objective is
maximum profit. '

To solve this problem by the simplex method of linear programming, it is neces-
sary to restate the three simultaneous equations on page 5 as three inequalities:

2P4+V—2F= 0
PLV—3F= 0
P+V <= 1000.

The inequalities allow for possible giveaway in viscosity, gravity, or quantity,
should this prove to be desirable. These inequalities are changed to equations by
adding “giveaway factors.” Thus:

2P+ V—2F4+X, = 0
P+ V—3F 4X, = @
Ptv + Xs = 1000.

The profit function is expressed in terms of the same variables.

Profit = 5P + 4V —3F Zz
or —SP —4V 4 3F+Z = 0.

Il

A basic case is set up, involving the maximum giveaway so that the maximum
profit case may be built up in logical order. This basic case may be expressed in tabu-
lar form as follows:

TABLEAU |

P v F X X2 X3 Zz Q
Xi 2 1 —2 1 on 0
X2 1 1 =3 1 0
X3 1 1 = _ - 1 1000
Zz ~5 —4 3 a — oo 1 0

It will be noted that this matrix table consists of the coefficients in the preceding
equations listed under the appropriate column for each variable. The columns X;, Xo,
X;, and Z are “identity columns,” since the only element in each is a single -|-1. The
row corresponding to cach of these unity coefficients is known by the same designa-
tion as the column, and the quantity Q is the actual value assigned to this variable. The
variables X,, X», Xz, and Z are therefore ‘‘in the basis,” and the variables P, V, and F

## PDF page 17

Maximum Profit Fuel Oil Blending Problem, Rudiments of Mathematical Procedure q

are not in the basis and have zero values. The profit function 5P + 4V —3F is shown
as the negative in order to include Z in the basis, indicating that these values are only
potential at this time.

Variable P has the greatest associated profit and should be used first. P must replace
X; since the smallest positive ratio of Q to P is necessary to avoid negative quantities.
The tableau will be transformed to put P into the basis as follows:

TABLEAU It

P Vv F Xi X2. X3 Z 2

Divide equation X, by 2 and replace in this
position as equation P.

P 1 1/2 -1 f2 0
Next subtract this new equation from the
X, and X; equations to obtain the new X,
and X,; equations:

M2... 1/2 —2 -1/2 1... ... 0

Xo. «1/2 1-1/2... 1... 1000
Then multiply the new P equation by 5 and
add to the Z equation to obtain the new Z

equation.
Z ... 3/2 —-2 S/2 .. 2. 1 0

We have now put P into the basis, removing Xi. (Column P is now an identity
column and column _X, is not an identity column.) The quantity associated with P is
zero, since, of course, P will not meet the quality requirements unless some flux is
used, The desirability of using this flux is shown by the high potential profit under the
F column. F must replace X, since negative Q to F ratios must be avoided.

Though the method of subtracting equations can be used to transform the tableau,
it is simpler to use formulas or “algorithms” for this purpose. The algebraic form of
these algorithms is derived as follows:

## PDF page 18

8 Linear Programming: The Solution of Refinery Problems

where

X, is the row to be replaced,

X, is any other row vector,

X,, is the column coming into the basis,
and —_-X, is any other column vector.

First divide the equation in
row X, by a,,

Next multiply this equation
by @,, and subtract from
the equation in row X,

a,; becomes a’;,; since X;, replaces X, in the basis.):

a,
@ yy = aE.
Ry Gn
a ;
and Wy = ay——! ay, Gb),
Ox

where
a’, == any new element in the row replacing the row removed
a’; = any other new element
a == corresponding old element
d,, == Old element in the same column and in the row removed
a, = old element in the same row and in the column entering
a,x, — old clement in the row removed and in the column entering.

The third tableau may now be prepared by use of the algorithms. The new F row
should be calculated first and should replace the old X3 row.

(FVY =XV/X,F = 1/2+1=1/2

(FFY = X3F/X3F = ijl
(PX = X3X)/X4F = -1/2 +1 = —-1/2
(PXaY = X3X3/X2F = 1+-1=1

(FQ) = X;Q/X;F = 1000 + 1 = 1000

## PDF page 19

Maximum Profit Fuel Oil Blending Problem, Rudiments of Mathematical Procedure 9

Only the columns V, F, X1, Xs, and Q will require transformation since these have
ratio values. Column F, of course, will change to an identity column. The calculations
for the other columns are given as follows:

(PVY =PV — (X2V/X;F) (PF) = 1/2—1/2(-1)= 1
QQVY = XV — (X3V/X2F)(X2F) = 1/2 —1/2(—-2)= 3/2
(ZVY =ZV —(X3V/X2F) (ZF) = —3/2 — 1/2 (—2) = —1/2

(PXY = PX, — (XeX1/XF)(PF) = 1/241/2(-)= 90
(KeXiy = XX — (X3X1/XeF) (KF) = —1/2 + 1/2 (—2) = —3/2
(ZX) = ZX, —(X3X1/X3F) (ZF) 5/2 4+1/2(-2)= 3/2

I!

(PX3¥ = PX, — (X3X3/X3F) (PF) = O—1(~1) = |]
(XX) = X2Xg — (XgX3/XeF) (Xo) = 0 — 1 (--2) = 2
(ZX3)' =ZX, —(X2X2/XsF) (ZF) = 0-1 (—2) = 2
(POY =PQ —(X:0/X:F) (PF) = O—1000(—1) = 1000
(X20Y = X20 — (X3:0/X3F)(X2F) = 0O-— 1000(—2) = 2000
(ZQY =ZQ —(X3Q0/X2F)(ZF) = 0—1000(—2) = 2000
Columns P, X2, and Z are unchanged. The new tableau may be written:
TABLEAU JI!
P Vv FE Xi Xo X3 z Q
P 1 1 — a a 1 1000
X2 ai 3/2 — —3/2 1 2 2000
F : 1/2 1 -1/2 1... 1000
1/2... 3/2 2 1 2000

This tableau or matrix table pictures the situation where 1000 gph of pitch and
1000 gph of flux are blended to make a fuel oil meeting the minimum viscosity speci-
fication (X, = 0) and giving away 4 points on gravity. No pitch is being visbroken,
and the profit is 2000 cents per hour ($480 per day). This is not the maximum profit
case, however, since some potential profit is shown in the V column. V should enter
the basis, replacing P, since the Q to V ratio of 1000 is the smallest.

The calculations are made as follows:

wey =1/1 = 1
(yy =-1/1 = 1
VXyY -1/1 = 1

(vey = 1000/1 = 1000

## PDF page 20

Linear Programming: The Solution of Refinery Problems

10
(X2PY =O0—1( 3/2) = —3/2
(FPY =0—1( 1/2)= —1/2
(ZPy =0-1(-1/2)= 1/2
(XoX3) =2—-1( 3/2)= 1/2
(FXsy =1—1( 1/2)= 1/2
(ZX, =2—-1(—1/2)= 5/2
(X,0Y —2000—1000( 3/2)= 500
(FEY =1000—1000¢ 1/2)= 500
(ZOY = 2000 — 1000 (—1/2) = 2500

Column V is transformed into an identity column. Columns F, X;, X2, and Z are
unchanged. The new tableau may be written as follows:

A

TABLEAU IV
P v F xX Xe. Xs z Q
v 1 _ — 1 1000
X2 3/2 —3/2 1 1/2 500
F =i//2 1 =il/n 1/2 500
Zz 1/2 3/2 5/2 1 2500
PLANE OF P-=: 0 PLANE OF V = 0 anor
= 2000
Ly <— <_—j /
Vv +P © 1000 v2o] —_> V+P = 1000
PROFIT —> <j | p20 a
= 2000 iN —> / mW
\ _ N F /
eee \ \ pRorit PROFIT 1
5 Ho «&
4,

1000 v

1000

## PDF page 21

Maximum Profit Fuel Oil Blending Problem, Rudiments of Mathematical Procedure V1

The above case represents the maximum possible profit in this operation since there
is no potential profit (no negative value in the Z row) to be obtained by using any other
variable in the basis. This case includes visbreaking all of the pitch (1000 gph) and
blending the tar (800 gph) with 500 gph of flux. The minimum viscosity specifica-
tion is exactly met, but there is a giveaway of about 1.5 points in gravity. The maxi-
mum profit is 2500 cents per hour ($600 per day).

A geometrical representation of this solution may be seen at the bottom of page 10.

The three-dimensional diagram indicates the constraints due to viscosity, gravity,
and availability of pitch, with the constant profit lines shown for each plane. The
quantity of flux stock is minimized by the maximal value of the profit functional when
all available pitch is used. The gravity constraint is not limiting and could have been
eliminated from the set.

## PDF page 22

CHAPTER 3
A Maximum Profit Running Plan Problem

Running plans that will assure maximum possible profit can be prepared by the
simplex method of linear programming. An example pertaining to a special form
of the running plan problem was prepared by Charnes, Cooper, and Mellon“ in their
integrated oil company study. An example of the general form of preparing a running
plan is given herewith.

A refinery has four different crudes available in stated quantities and wishes to
meet given requirements for four different products. One of the crudes can be run
alternately either for fuel products or for lube distillate. The product yields and the
profit for each crude operation are given. The objective is to make a selection of crude
oils which will meet product requirements with maximum possible profit.

TABLEAU I

A B Cy Co D Xx Xp Xe Xp Xo Xu Xt Xr Z Q
Xo 06 #05 04 04 O38 2 we OD a oe 2 170
Xe Ot 02 O02 02 O38 eo Lo. | 85
Zz —10 —20 -15 -—25 0 -Fo ee 0

Tableau I contains a complete statement of the problem. The four crudes, A, B, C,
and D, are available in quantities Q of 100, 100, 200, and 100 Mbpw respectively.
The desired products, G, H, L, and F, have requirements of 170, 85, 20, and 85
Mbpw respectively. The yields for each crude are shown as decimal fractions and the
negative profit as cents per barrel listed in the column for each crude. The vectors
X4, Xp, Xc, and Xp represent the respective crudes not run, and the vectors Xg, Xn,

## PDF page 23

Maximum Profit Running Plan Problem 13

X,, and Xy represent the respective product requirements not met. The matrix table
is a basic feasible solution and indicates that no crudes are being run and no product
requirements are met. The profit Z is 0.

The next feasible solution (No. 2) of the problem is selected by introducing the
column showing the largest negative Z value as a row in the matrix. This is column Cz
with a Z value of —25. The row in the first matrix which is to be replaced is deter-
mined by the minimum ratio of Q to Co, using only positive values. This is row Xz,
with a ratio of 20/0.2 = 100. Column C, and row X;, are marked with arrows, This
means that crude operation C2 will be run to meet all of the lube distillate require-
ments. This is done preferentially because it is the most profitable operation. The new
matrix is set up as follows, with identity columns for the common vectors.

A B C, GC D Xa Xe Xe Xp Xo Xn MXM Xe Z Q
Xa coo | ones anon | ec
Xp coao | pono coun | coe) eS
Xb cow ofc Ga, «RES, 2) co

Row Cz is also completed by dividing each element in the X;, row of matrix 1 by
X,Co, thus obtaining 0.2/0.2 = 1, 1/0.2 = 5, and 20/0.2 = 100 respectively for the
Cz, Xz, and Q elements in matrix 2.

The columns C2, X,, and Q now require correction. Since column C; is an identity
vector, all other elements in this column are 0, Column X;, is corrected as follows:

(XuXn)2 = (KaXy)1 — (C2X1)o(XsC2)1 =O -5 K 0 = 0
(XeX po = (XeX1)1 — (CoXz)o(X eC.) =9—5 XK 0 = 0
(XcX1)2 = (XcXz)1 — (C2X 7) AX oCoh = 0-—5xX1 = =5
(XpXp)2= (XpXp)1 — (C2Xz)a{XnC2). = 0-5 XO = 0
(X@X zo = (XeXr)1 — (CaXDlXeC2)1 =O-5K04 = —2
(XeXne= (XnXp)1 — (C2X1)(XyC21 =O-3 KO1 = —05

(XpXp)o = (XpXq)1 — (CoX1)(XrC)1 =O-SKO2 = —-1
(ZXn)o = (ZX1)1 — (CoX1)A{ZC2. =0—5 X(—25)= 125

## PDF page 24

14 Linear Programming: The Solution of Refinery Problems

and column Q is corrected as follows:
(X4Q). = (X4Q)1 — (CoQ)o(X4C2)1 = 100-100 x0 = 100
(X2Q)2 = (XQ). — (C2Q)e(XyC2), = 100 — 100 x 0 100
(XoQ)e = (XeQh — (CiQ)AXeCs)1 = 200 — 100 K 1 100
(XpQ)2 = (XQ) — (CoO)2(XvC2)1 = 100 — 100 KO = 100
(XeQ)e =(X¢Q)1 — (C.Q)AXeC2): = 170 — 100K 0.4= 130
(XnQ)» = (XxQ)1 — (CoQ)of(XuCo, = 85 —100K01= 75
(X7rQ)o = (XrQ). — (CeQ)f{XrC2). = 85—100K02= 65
(ZQ)2 =(ZQ)1 —(C2Q)(ZC2), = 0 — 100(—25) = 2500

All other columns remain unchanged. The new matrix for feasible solution No. 2
is completed as follows:

TABLEAU II

A B Cc; C2 D Xa Xp Xe Xp Xo Xu Xi Mp Z Qa
Xe 1 a a |) ne wee ee 100
Xe 06 #O5 04 .. O03 2. we ne ne TO, 2... os 130
Xi 00.2 02 O03 O03 2.0 a ue 2 AOS, 15 -
Xr 0.12 #02 O02 2... OO] Le ee -1 1... 65
Z2 -10 -20 -15 2.00 -Fou ee ee 1250, 1S 25000

As the tableau shows, the profit for running 100 Mbpw of crude C to meet the 20
Mbpw of lube distillate requirements is 2500 (1000/100) == $25,000 per week.
Remaining are 400 Mbpw of available crudes and requirements for G, H, and F
products of 130, 75, and 65 Mbpw respectively. The next feasible solution is deter-
mined by inspection of the matrix table. Column B contains the largest negative Z
value of —20, and row Xz shows the smallest Q to B ratio of 100/1 = 100. The new
matrix, Tableau III, is set up as before. '

As shown, the profit for running 200 Mbpw of crudes B and C is 4500 (1000/100)
— $45,000 per week. Remaining are 300 Mbpw of crudes A, C, and D and require-
ments for G, H, and F products of 80, 55, and 45 Mbpw respectively. Column C, is
introduced next (ZC, = —15) and row X¢ is removed (Q/C, = 100). Tableau IV,
the new matrix, is set up as before.

## PDF page 25

Maximum Profit Running Plan Problem 15
TABLEAU II!
A & i Co D Xa Xe Xc Xp Xq Xu Xi Xe Z a

Xa 1 a 1 a 100
Xo... 1 1... —5 100
Xd — ran 1 ae 1 a 100
Xe 0.6 0.4 0.3 —0.5 1 —2 80
Xu 0.2 03°... 0.3 —0.2 1 -0.5 55
Xr 0.1 0.2 0.3 OLA, —1;-1 45
Zz —10 —15 =i 20 125 1 4500
TABLEAU IV

A | C D Xa Xp Xc Xp Xo Xu XL. Ar Z Q

‘
Xa 1 I , 100
Cc; 1 an 1 : —5 100
Xp a 1 an we Low. 100
Xe 0.6 0.3 -0.5 —0.4 1 = 40
Xx 0.2 .. 0,3 02 03) i 1 25
Xr O14 0.3 0.2 -0.2 2. wt ae TD. 28
Zz —10 7... 20 SB .. .. 650. 16000

As shown, the profit for running 300 Mbpw of crudes B and C is 6000
(1000/100) = $60,000 per week. Remaining are 200 Mbpw of crudes 4 and D and
requirements for G, H, and F products of 40, 25, and 25 Mbpw respectively. Column
A is introduced next (ZA == —10), and row Xq is removed (Q/A = 67). The new
matrix is set up as before.

As Tableau V, page 16, shows, the profit for running 367 Mbpw of cnides A, B,
and C is 6667 (1000/100) = $66,670 per week. Remaining are 133 Mbpw of crudes
A and D and requirements for H and F products of 12 and 18 Mbpw respectively.
Column D is introduced (ZD = —2), and row Xx is removed (Q/D = 58). The new
matrix is set up as before.

Since there are no negative values in the Z row, Tableau VI, this case represents a

## PDF page 26

16 Linear Programming: The Solution of Refinery Problems
TABLEAU V
A B Ci && Xa Xp Xo Xp Xo My Xt Xr Z a
Xa -0.5 1 5/6 2/3 —5/3 33
8 1 H oe 7 100
0 ee 1... SS, 100
XD ee es 7 a I FP 000 8b 100
A 1 05 5/6  -—2/3 3/3 67
MWe 0.2 -1/30 —1/6 -1/3 1 1 12
Cp 1 a . . 5 100
Xr 0.25 —7/60 —2/15 1/6 .. .. 1 18
Zz —2 35/3 25/3 50/3... 50 1 6667
TABLEAU VI
A B C; CG D Xa, Xp Xe Xp Xs Xy Xi Xe Z Qa

Xa i 3/4 1/4... —2.5 2.5 Be) ooo 62
BE 1 1 . a . 100
qi Pou... 7 i. a 7, So. 100
XD ee ee 1/6 5/6 1 5/3 —5 —-5 . 42
A feo coon coon) ARE —3/4 —1/4 .... 2.5 —-2.55 —2.5 .. 38
De 1 —-1/6 —5/6 .... —5/3 5 3 oxen 58
Grow we De = = es 7 5... 1... 100
Me —3/40 3/40 1/4 —5/4 —5/4 1... 4
ZR ey... 34/3 20/3 40/3 10 60 ... 1 6783

maximum profit feasible solution. The profit is 6783(1000/100) = $67,830 per
week. The following table shows the disposition of available crudes in this solution.

Products G
Mbpw A
L
F
Crude not used
Total crude

Crudes Mbpw

A B C1 Co D
22 «50 40 40 18
7 20 30 10 18
ee
4 2 2 2 17
2 oOo 0 oO 4
100 100 100 100 100

Product
Not Made

0

0
0
4

Total
Required

170
85
20
85

## PDF page 27

Maximum Profit Running Plan Problem 17

With the given crude slate the requirements for products G, H, and L are met, but it
is not economical to meet quite all of the requirements for product F. Of course,
more of crude D could be used to displace the other crudes in order to increase the
yield of product F with some loss of profit. Other methods would include the use of
different crudes having high F yield, the purchase of product F for resale, and reduc-
ing the percentage of product F required.

## PDF page 28

CHAPTER 4

A Problem in Blending Aviation Gasoline

for Maximum Profit

Blending problems are very well adaptable for solution by the simplex method of
linear programming. Some studies on blending aviation gasoline have been made
available by Charnes, Cooper, and Mellon‘’). The example given herewith gives
the general solution and illustrates some simplicity in handling the data.

It is desired to blend five available refinery streams for the requirements of Grade
100/130 and Grade 115/145 aviation gasoline to make maximum profit. A study
of the past shipments indicates that only three inspections are critical for each grade,
namely 1C +4.6 lean octane (performance number, or PN), 3C +4.6 rich octane
(PN), and Reid vapor pressure (RVP). The inspections used in this study are linear
blending values (BL) including tolerances. Neglecting the noncritical inspections is
one way of simplifying the blending problem. Complete inspections for the final blends
can be calculated to be sure that product quality will be satisfactory in all respects.
The critical inspections, cost, and availability of the refinery streams are shown as
follows:

BL PN BL PN BL Cost Avail
Stream 10 44.6 3044.6 RVP epg bpd
No. 1 122.0 158.3 3.0 17.7 750
No, 2 109.0 145.0 4.0 16.0 800
No. 3 Oar 110.0 5.0 14.5 857
No. 4 90.0 125.0 7.0 13.0 1000
No. 5 114.0 145.0 19.0 11.0 Any

In view of its low cost and high quality, it is obvious that the maximum amount of
stream 5 should be used in the blends as limited by the RVP specification of 7 on
each grade. Thus, the RVP inspection and stream 5 can be eliminated from the prob-

## PDF page 29

Problem in Blending Aviation Gasoline for Maximum Profit 19

lem by blending streams 1 to4.up to 7 RVP with stream 5. This procedure is another

way of simplifying the blending problem. The resulting preliminary blends are shown
as follows:

BL PN BL PN BL Cost Avail
Component 1€+4.6 3€+44.6 RVP cpg bpd
A 120.0 155.0 7 16.0 1000
B 110.0 145.0 7 15.0 1000
c 100.0 115.0 7 14.0 1000
D 90.0 125.0 7 13.0 1000

The specifications, refinery prices, and requirements of the products are shown as
follows:

BL PN BL PN BL Price Required
Product 10446 3C446 RVP ¢pg bpd
M 100 130 7 16.0 2000
N 115 145 7 18.0 2000

The linear equations are developed from this information.
The quantity of each component used plus the amount of product not made equals
the requirement.

Ay + By + Cy + Dy + Xy = M = 2000
Ay + By + Cy + Dy + Xy =N = 2000

The quantity of each component used plus the amount not used equals the avail-
ability.

Ay + Ay + X4=A = 1000
By + By + Xz = B = 1000
Cy + Cy + Xe =C = 1000
Dy + Dy + Xp = D = 1000

The quality relationships are expressed as inequalities to allow for possible product
quality giveaway.

120 Ay + 110 By -+ 100Cy+ 90 Dy = 100 (M — Xu)
155 Ay + 145 By -} 115 Cy + 125 Dy = 130 (M — Xy)
120 Ay + 110 By +100Cy + 90 Dy == 115 (NV — Xx)
155 Ay 4- 145 By + 115 Cy + 125 Dy == 145 (N — Xy)

## PDF page 30

20 Linear Programming: The Solution of Refinery Problems

These relationships can be expressed as differential inequalities as follows:

20 Ay + 10 By — 10Dy=0
25Ay + 1SBy— 15Cy— 5Dy=0
SAy~ 5SBy— 15Cy— 25Dy==0
10 Ay — 30€y— 20Dy =0.

These inequalities can be simplified and expressed as equations:

=i bh + Dy+Xp=0
—5d4y—- 3Byt 3Cy+ Du+Xe=0
— Ayt+ Byt+ 3Cy+ SDy+Xe2=0
— Ay 4+ 3Cy+ 2Dy+Xs=0.

The equation for profit can be written as follows:
Za=2Ay+ By +3 By4+2Cy+4Cy 4+ 3 Dy +5 Dy.

Since it is desired to maximize this function, the negative value is used in the matrix.
The basic feasible solution and the ten substituted cases are shown on pages 22-24.
The maximum profit feasible solution can be summarized as follows:

Compo- M N
nent 100/130 115/145 Not Used Avail
A 0 1000 0 1000
B 750 250 0 1000
¢c 500 250 250 1000
D 750 0 250 1000
Not Made 0 500
Required 2000 2000

The maximum profit for this case is 7750(42/100) = $3255 per day. The require-
ment for Grade 100/130 is met, and preliminary blends A and B are used entirely;
it is not economical, however, to meet all of the requirement for Grade 115/145 with
the available refinery streams. Part of preliminary blends C and D are not used and
would be available for motor gasoline.

The critical inspections of the final blends are determined as shown in the table at
the top of page 21.

The product quality giveaway of 1.7 PN on Grade 115/145 is the best arrange-
ment for maximum profit with the existing situation. Refinery process changes which
would economically increase the ratio of 1C to 3C rating of the blending stocks
slightly would be worth investigating to avoid this giveaway.

## PDF page 31

Problem in Blending Aviation Gasoline for Maximum Profit 21

CRITICAL INSPECTIONS OF THE FINAL BLENDS

Product M(100/130) Product N(115/145)
inspect BL PN Inspect BL PN
Component %inBlend 1C +4.6 3C +4.6 %inBlend 1C +-4.6 3C +4.6
A a _ on 66.7 120.0 155.0
B 37.5 110.0 145.0 16.7 110.0 145.0
c 25.0 100.0 115.0 16.7 100.0 115.0
D 37.5 90.0 125.0 — an on
100 100.0 130.0 100 115.0 146.7

(Note Xg = 250; A3C = 250(10/1500) = 1.7 PN)

If it is necessary to make the maximum amount of Grade 115/145 regardless of
cost, the highest octane components should be blended.

BL PN BL PN BL Cost Avail

Component 1C +-4.6 3C +4.6 RVP tpg bpd
A 120.0 135.0 7 16.0 1000
B 110.0 145.0 7 15.0 1000
Max. 115/145 115.0 150.0 7 15.5 2000
Excess 95.0 120.0 7 13.5 2000

Tn this case the requirement of 2000 bpd for Grade 115/145 is met with 5 PN 3C
+-4.6 octane giveaway. The excess blending stock of 2000 bpd must be returned to
motor gasoline since it will not make any Grade 100/130 because of low octane qual-
ity. The profit with this method is 2000 (18.0 — 15.5) (42/100) = $2100 per day.
This, of course, is far below the maximum profit of $3255 per day for the case deter-
mined by linear programming.

It should be pointed out that it is possible to convert all 4000 bpd of the preliminary
blends A to D into 1333 bpd of Grade 115/145 and 2667 bpd of Grade 100/130
aviation gasoline. Since the requirement for Grade 100/130 is only 2000 bpd, the
excess of 667 bpd would have to be returned to motor gasoline. The profit in this
case would be [1333 (18 — 15.5) -} 2000 (16 — 14.0)} (42/100) = $3080 per day.
This is less than the maximum profit of $3255 per day for the case determined by
linear programming.

## PDF page 32

22 Linear Programming: The Solution of Refinery Problems

Basic Feasible Solution
Tableau |

ay Ay By By oy Cy By Dn Xa Xe Ae % Mn Bu He Xo mM 2 @

Tableau II

ay Ay By BN Sy Cy DN X, Xp Xo Xp XW XN Xp XQ Me Ms 2 @

br oe 1900
Xs 1 1000
a ee - 1000
yoo 8 1 1000
My on el 1 2000
Ro. (8 » 2000
Mpeo-2 .. i 1 -
% 5. 3 1

Dy. 1/5 7

Xo. 8/5. = i

z = a4 2a S 1

ay By BN Cy Cy Oy Dy XQ Xe Xo XD XM IN XPRQ XR Ae Z

iL --- 1000

1 1 a . 1000

a . = 1 1 1000

VW 1 —1/5 a HS -» 1000

6/5 2/5 - 2000
V5 3/5
—3/5 9/5

3 1

ay By BN Sy *N Dy Dy Xq Xp Xe a
9/10 1/2 1/10 B00
th i com ~» 1000

3 cnc x0 1 . 1000
V0 1/2 —1/10 500
—3/10 1/2 3/10 1 3 500
5 AB. vw» 2000
1/5 -Vs . 1000
. 3/10 —3/10 1500
V5. 5 i

3/5 —2/5

12/5 —1  —13/5 1 3000

## PDF page 33

Problem in Blending Aviation Gasoline for Maximum Profit 23
Tableau V¥ -
Ay mN By BN Suey Dy Dy X, Xp Xo Xp XN Xp XqQ Xp Nye Z a
Kae a —1/2 1/6 . —1/2 1/2 V6
Xp on 1 a -
Xe va foo 2/9 : 2/9
Any 1/2 —1/6 mo WA. —1/6
Xm ww 1/2 1/2 . 3/2 1/72
cw 4/3 8/9 » 1/9
Bay 2 1B 1 13
Xo —1/2 —1/2 3/2 1/2
Dy ms CD 1/3 3 bcs Vg
LNT . —1/3 we B/G —2/9
Zz —10/3 —1 —20/9 —2 .... —2/9
Tableau VI
Am fn Ba BN SM SN OM ON X_ XB Xe XD Xm XN Xp XQ HR
Ay 1-1/2 1/6 1/6
ie 1 1° .
Xe Ve 1/6 V6
Any 1 1/2 —1/6 6 1/6 500
My v2 1/2 1/2 —1/2 500
XN 2/8 2/3-
Dy ne 1/3
XQ —1/2 —1/2 1/72 1/2 1500
By 5 -. V3 . V3 —1/3 coxa
oy —1/6 —1/6 —VY6 172 ... 167
z —8/3 —8/3 a1 1 4667
Tableau Vil
Ay Ay By By fy Sy DM DN Xy XR Xo Xp Xm XN Xp XqQ Xe Xs 2 w
Ay la. 2/3 1 1/2 ... —1/2 . 1000
1 ee ee 1000
—1l/3 -1/6 1 V6 667
-V2.. 2 om
—12 ... —3/2 cxp
an —2/3 2/3 667
1/3 co 1 . 1000
= 1/2 3/2 2000
= 1/6 ... —1/6 333
8/3 4f 7333
Tableau Vit!
Ay An By By Sy Sy Dy Dy Xq Xp Xp Ng Xp Xs Zz @
1 V2... 1/2... 1/6 —1/6 1000
1/3 1/3 . —2/3 —1/3 667
1/2 .. . 1/2 1/6
we 1/2... ~ Y2.. V2 on
A/2 —2/3 ... —2/3 1/3 667
& ax a —1/3 1900
2 _ —4 2 2000
173 1/6 .... 1/6 ... —1/6 339
10/3 5/3... 8/3... 4/3 1 7333

## PDF page 34

24 Linear Programming: The Solution of Refinery Problems
Tableau IX
Ay Ay By x Ca SN Dm Dy Xa Xa Xe Xp Xm AN Xp XqQ Xe kyo 2 A
1000
... 1000
5/9. 667
1/3.
—2/ 667
1000
... 2000
-1/3 . ,
5/9... 333
6/9 1 7333
Tabieau X
a
. 1000
1000
667
667
w 1900
. 2000
20/3 10/3 7333
Maximum Profit Feasible Solution
Tableau X1
By AN By By Cy Cy Dy Dy Xp TULA bth SH a
Ay 8 Sh en 1 : ims he
By 3/2 : _ a 1/44 —1/8 ow
Xe 5/6 . 5/3 1/9 7/12 -—§/24 —1/3
i WA. 1 = 3/4 1/8
7 . -172 1/4
Xy -1/3 . . 2/3 —4/3 —1/6 —1/12 —1/3
Dy —l/2 . exp v4 —1/8
Xs —3/2 3 1/4 1/8 —1
By —-32. an 4 1/8 a
¢, 5/6 5/3 «1/3 aa —V1l2 —1/24 1/3
z 5/6 5/3 10/3 5/3... 17/12 «5/24 «4/3

## PDF page 35

CHAPTER 5

A Refinery Improvement Program

Under Competitive Conditions

For illustrative purposes this chapter presents the solution of a refinery problem in
operations research by the use of the game theory solved by linear programming.
The relationship between game theory and linear programming is discussed by Gale,
Kuhn, and Tucker‘) and by George B. Dantzig. One of the most appropriate
reference books is Introduction to the Theory of Games by J. C. C. McKinsey.)

A refinery, X, produces insufficient yields of gasoline and distillate fuel to meet its
requirements, while producing distress residual fuel. Refinery X must pay 10 cents
per barrel excess transportation costs on products requiring shipment into or out of
the marketing area in order to meet product demands. Four different proposals have
been prepared for changing product distribution, which would result in increasing
profit from 30 cents per barrel to 35, 39, 42, and 44 cents per barrel, respectively,
including reductions in excess transportation costs from 10 cents per barrel to 6, 3, 1,
and 0 cents per barrel respectively. Each proposal is economically justified if optimum
operation is maintained. It seems obvious that the proposal showing the maximum
profit should be adopted. However, the assumption made in this study was that a
major competitor, refinery Y, who also has poor product distribution, would do noth-
ing about improving its operation. It was possible to show that if refinery Y carried
out the same type of improvement projects a reduction in excess transportation costs
to refinery X, also, would result. This condition is due to the fact that the two refineries
X and Y are sharing a fixed market demand, and any improvement in product yields
at either refinery would decrease the excess transportation costs for both refineries.
On the other hand, if both refineries carried out the maximum improvement program,
the maldistribution of products would be overcorrected. Their combined products
would again be out of balance, and both refineries would again incur excess trans-
portation costs. Thus the excess transportation costs of refinery X depend upon the

## PDF page 36

26 Linear Programming: The Solution of Refinery Problems

strategies adopted by both refinery X and refinery Y. In this situation a profit matrix
can be set up for five alternate strategies of X vs. the same five alternate strategies of
Y. The problem of determining the best strategy for X can be solved by Jinear pro-
gramming using the simplex method applied to a game theory problem. This method
is described by Robert Dorfman in Koopmans, Activity Analysis of Production and
Allocation.®) The solution to the problem will also consider the possibilities of
“mixed strategies,” i.c., X may process part of its crude in one manner and part in
another. The solution will show which methods will be best for refinery Y after X has
adopted its best procedure and what the resulting profit for refinery X will be. If the -
profit matrix is correct, the answer will be certain to provide the best profit regard-
less of the competitor’s intentions.

Given

Profit in cents per barrel at refinery X for each of five alternate strategies (no change
and four proposals) depends upon the same five strategies at refinery Y. The follow-
ing table shows the excess transportation costs.

Xy X2 X3 X Xs
Yi 10 6 3 1 0
Y2 6 3 1 0 2
Y3 3 1 0 2 3
Y4 1 0 2 5 a)
Ys 0 2 5 9 14

In addition to these excess transportation costs, refinery X will increase its profit
by 0, 1, 2, 3, and 4 cents per barrel by adopting strategies X, X2, X3, X4, and X;, re-
spectively. The net effect of these changes on the current profit of 30 cents per barrel
is shown in a profit table as follows:

PROFIT* TO X
XX X2 X% X Xs
Ni 30 35 39 42 44
Yo 34 38 41 43 42
Y3 37 40 42 41 39
Y4 39 41 40 38 35
Y5 40 39 37 34 30

*In cents per barrel.

## PDF page 37

Refinery Improvement Program Under Competitive Conditions 27

Required

Determine the best strategies for X to maximize profit. Also determine the best
responding strategies for Y and the resulting profit for X.

Development of the Mathematical Model
The profit for X will depend upon the strategy adopted by Y. Thus for any given y,:

Z, = Byayx, (x20; 3x, D,
and for all values of y;:
Z = 3s Baur; (y=; Sy, = 1)

where x; and y, are the corresponding fractions of the strategies of X and Y, respec-
tively, and a, are the specific profits to X for these strategies. The objective for X,
of course, is to maximize Z. It will be assumed in this study that the objective for
Y is to minimize Z. This assumption is based upon the direct competition of X and Y
to share a fixed market demand. Thus, Z is the profit to X which is maximized by
X and minimized by Y. Therefore:

Z—-Z=b;

where b, is the excess of profit to X, if any, for selected strategy y;. The best strategies
for Y resulting in minimum profit to X will be obtained when 5; = 0.
Combining equations gives:

ByXy — b, = Z.
Dividing by Z gives
Byayx;/Z — b/Z= 1.

Substituting new variables X; for x,/Z and Y; for b;/Z results in a set of linear
equations:
3yayX;— Y¥i= 1
where the objective for X is
3X, 1/Z=min (Z = max)

and the objective for Y is
Y¥,=0 (b, = 0).

Thus the desirable strategies for X will be in the basis and will have values

x;== ZX;,

## PDF page 38

28 Linear Programming: The Solution of Refinery Problems

while the desirable strategies for Y occur when Y; — 0 and therefore will not be in
the basis. They will have values

yy = —Z E,;(—AX,/ AY)
where (—AX;/AY,) are coefficients for X in the basis and Y not in the basis.

This expression is equivalent to

(%) = —(—AEX/AY)

where 2X = min
or yy = —-AZ/AD,
where Z = max.

This relationship is obtained from the duality theorem of linear programming as
discussed by Charnes and Cooper'?) and by Dantzig and Dorfman“) where, at the
solution of the game theoretic problem for all strategies in the basis,

Ljaayx;* = Syayy.* = Z.*

Solution of the Problem

Construct a payoff matrix by subtracting a number (29) from each element in the
profit table to reduce the minimum element to 1.

Xx X2 X3 X4 X5
Y) 1 6 10 13 15
Yo 5 9 12 14 13
Y3 8 il 13 12 10
Y4 10 12 11 9 6
Ys 11 10 8 5 1

Construct a problem matrix by attaching X) = 1 and negative Y identity columns
to the payoff matrix.

Xo Xy X2 X3 X X5 %1 Y2 Y3 Y4 Ys
(¥1) 1 1 6 10 13 15 —1 0 0 0 0
(Yo) 1 9 12 14 13 0 —1 0 0 0
(Ys) 1 8 11 13 12 10 ie) —1 0 0
(Ya) 1 10 12 il 9 6 0 Oo —-1 0
(Ys) 1 Mt 10 8 5 1 0 0 0 Oo —-I1

## PDF page 39

Refinery Improvement Program Under Competitive Conditions 29

The problem matrix does not constitute a feasible solution because of the absence
of identity vectors. Instead, there is a set of negative unit vectors forming a negative
unit submatrix, In order to obtain a basic feasible solution it is necessary to convert
the matrix to the usual form containing a unit submatrix. This can be done when mak-
ing the first transformation to include an X in the basis. The first X to enter the basis
should be selected with the largest minimum payoff. Thus if X selects strategy X3, Y
will select strategy Y; and the payoff to X will be 8. This is the best apparent single
strategy. It will be noted that the Y; to be excluded from the basis is determined by the
maximum X /X\, in order to maintain all Xy=0. The transformation is completed
by use of the simplex algorithm for a’,; and the negative simplex algorithm for all
other a’, Thus

ar}
Org =
OK

and

ay, 5
ay a, —a;, GAR.

These algorithms will definitely convert the Y vectors to unit vectors which to-
gether with the substituted X vector will form a unit submatrix and thus provide a
basis for the feasible solution.

The basic feasible solution is expressed in the following matrix form.

Xo Xi X2 X3 X4 X5 Yi Yo Ys Ya Ys
Xs 0.125 1375 1.25 1 0.625 0.125 0 0 0 O —0,125
vi 0.250 12,75 6.50 0 —6.75 —13.75 1 0 O O —1,25
Y2 0.500 11.50 6.00 0 —6.50 —11.50 0 1 #O O —1.50
Ys 0.625 9875 5.25 0 —3.875 -8375 0 0 1 O —1.625
Y4 0.375 5.125 1.75 0 —2.125 4.625 0 0 O 1 —1.375
=x 0.125 1375 1.25 1 0.625 0.125 0 0 O O —0.125

The row =X is the same as row X; since only a single strategy is involved in this
solution. The value of the game to X by adopting strategy X is 1/2X in the Xo col-
umn or 1/0.125 = 8.0. The profit to X is 29 4 8.0 = 37.0 cents per barrel. The
value of the game to Y by adopting responding strategy Ys is 1/2X in the Y columns
or 1/—0.125 = —8.0. (The profit to X is considered a loss to Y.)

Jn order to be a maximum profit solution, 2X must be not higher than 1 in any
of the X¥ columns and not higher than 0 in any of the Y columns. All of the =X ele-
ments meet these requirements except in the X, and Xz columns where &X is 1.375

## PDF page 40

30 Linear Programming: The Solution of Refinery Problems

and 1.25, respectively. Strategy X1 is chosen, therefore, to enter the next feasible
solution (No. 2). The row to omit from the new matrix is determined as usual by the
smallest ratio of its element in the X» column to its element in the X; (new strategy)
column. The smallest ratio is in the Y; row (0.250/12.75 = 0.0196) and the Y, row
is therefore omitted from the new matrix. This means that Y, becomes one of Y’s
responding strategies in feasible solution No. 2.

The matrix for feasible solution No. 2 may be completed by use of the regular
simplex algorithms:

Xo Xr X2 Xe X Xs Yi Yo Ya Ya Ys XY
X 0.0196 1 0.510 0 —0.529 —1.078 0.0784 0 0 0 —0.0980
Xs 0.0980 0 0.549 1 1.353 1.608 —0.1078 0 0 O 0.0098
Yo 0.275 © 0.135 0 —0412 0.902 -0.902 1 0 0 —0.373
Ys 0.431 O 0.214 0 1.353 2.275 —-0.775 0 1 0 —0.657
Y4 0.275 0 ~0.864 0 0.588 0.902 —0.402 0 O 1 —0.873
=x 0.1176 1 1.059 1 0.824 0,530 —0.294 0 0 0 —0.0882 —0.1176

In this solution X uses strategy X; for (0.0196/0.1176)100 = 16.7 per cent of its
crude and strategy X, for (0.0980/0.1176)100 = 83.3 per cent of its crude. Y uses
responding strategies Y, for (—0.0294/—0.1176)100 = 25.0 per cent of its crude
and Y; for (—0.0882/—0.1176)100 — 75.0 per cent of its crude. The value of the
game to X is 1/0.1176 = 8.50, corresponding to a profit of 29-++ 8.50 — 37.50 cents
per barrel. However, this solution is not a maximum profit feasible solution since 2X
in the X~ column is greater than 1, indicating that the X, strategy should be used in a
new feasible solution. Since the ratio of Xo to Xz in the X, row of 0.0196/0.510 =
0.0385 is the smallest ratio, strategy X, should be omitted from the new feasible
solution.

The matrix for feasible solution No. 3 may be completed.

Xo Xr Xe Xs Xs Xs Yr Ya ¥3 Ys Y5 zy
M2. 0.0385 1.961 1 0 —0.137 —2.114 0.1535 0 0 O W—0.1920
Xa 0.0770 —1.076 0 1 1.923 - 2.768 —0.1920 0 0 O 0.1150
Y2 0.269 —0.265 0 O —0.272 1.187 —0.923 1 0 O —0.347
Ys 0.423 —0.419 0 0 1.575 2.726 —0.807 0 1 O —0,616
Ya 0,308 1.686 0 0 —0.307 —0.923 —0.270 0 0 1 —1.039
=X 0.1155 0.885 1 1 0.886 0.654 —0.0385 0 0 0 —0.0770 —0.1155

## PDF page 41

Refinery Improvement Program Under Competitive Conditions 31

Since 2X is not more than 1 in.any X column and not more than 0 in any Y column,
solution No. 3 becomes a maximum profit feasible solution. The optimum strategies
for X are X» for (0.0385/0.1155)100 = 33.3 per cent of its crude and X, for
(0.7700/0.1155)100 = 66.7 per cent of its crude. The optimum responding strategies
for Y are Y; for (—0.0385/—0.1155)100 = 33.3 per cent of its crude and Y, for
(—0.0770/—0.1155)100 = 66.7 per cent of its crude. The value of the game to X
will be 1/0.1155 = 8.66 corresponding to a profit of 29 + 8.66 — 37.66 cents per
barrel which is the maximum profit possible with the profit table given in this problem.

This problem can also be solved with refinery Y as the maximizing player. It is
necessary fo restate the problem matrix to include a payoff matrix to Y recoded so
that the largest payoff to X will be —1 (equivalent to +-1 to Y). By subtracting 45
from the original profit table and transposing the negative matrix, the following payoff
matrix to Y is obtained.

v) Y2 ¥3 Y4 Y5
Xx 15 11 8
Xa 10 7 5
X3 6 4 3 5
X4 3 ra 4 7 il
X5 1 3 6 10 15

In the first transformation Y,; should replace X1. The optimal solution, of course,
is identical with that of the problem maximizing the profit to refinery X.

In the event that the information in the profit table may not be completely known
by both competitors, there may be considerable advantage in computing responding
(defensive) strategies based upon an estimate of competitor’s knowledge of the payoff
matrix. Since the offensive strategies are always based upon the best strategies for the
defensive, any defect in knowledge of the offensive side will result in extra profit for
the defensive side.

A Two-Player Non-Zero-Sum Game Theory Problem

In many cases, the two-player zero-sum game theoretic method cannot be used for
two sets of strategies because, though the strategies are related, the profit matrices for
the two players are not opposite. Such a situation is illustrated below for two business
competitors who have separate alternate but interrelated plans for improving the
profit from their respective businesses.

## PDF page 42

32 Linear Programming: The Solution of Refinery Problems

PROFIT* TO X PROFIT* TO Y¥
x x2 x3 x4 yl y2 y3 y4
yl 1 2 3 5 xT 4 3 2) 1
y2 2 1 2 3 x2 3 2 1 2
y3 3 2 1 2 x3 2 1 2 4
¥4 4 3 2, 1 Xa 1 2 4 7

*In thousarids of dollars per day.

Each problem is set up for solution by linear programming, giving the following
solution matrices.

For the X game
Xx] x2 x3. OX by; bo b3 bg bs Zx Q
bi on =e 1 2. @ 3p 3/2 12 ae 2
zx 1 tow .. 1/2 2... 5/2 1 5/2
x4 oe _ 1 1 bee =i1y/2 1/2 ey 1/2
x) 1 1 re 1/2) 20 2

and for the Y game
v1 y2 ys ya by bp bs bys zy Q
y4 a 2/3 1... 173 -1/3 .. 13 .. 173
bg ws 2 YB me om 4/3 -7/3 1 41/3 .. 41/3
v1 1 1 WS mm om = 1/3 2/3 2/3
zy - 1 4B 2/3 1/3... 8/3 1 8/3
by ee 4B 5B 2/3... 173 1/3

The minimax profit* for X is 5/2 ($2500 per day) for strategies x; = 1/2 and
X4 = 1/2, and the minimax profit for Y is 8/3 ($2667 per day) for strategies y, = 2/3
and y, = 1/3. It will be noted that X would lose 1 ($1000 per day) for the adoption
of either x2 or x, strategies and that Y would lose 1 ($1000 per day) for the adoption
of yz strategy or 4/3 ($1333 per day) for the ys strategy. It may safely be assumed,
therefore, that X will adopt x, and x, strategies and Y will adopt y; and y, strategies.

In view of these results, it is advisable to set up reduced games for the x;, x4, y:, and
Yy4 Strategies having the following profit matrices.

*That is, the maximum of the alternate minimum values.

## PDF page 43

Refinery Improvement Program Under Competitive Conditions 33

STRATEGIES OF X.. STRATEGIES OF Y
x1 x4 Yt Y4
Yl 1 5 x] 4 1
y4 4 1 x4 1 7

The solution of these games results in the following solution matrix for X (reduced
game);

xT x4 by bg bs zx Q
Fy a _ 3/7 4/7 19/7 1 19/7
x4 a 1 =i 1/7 3/7 _ 3/7
x1 1 . 1/7 1/7 4/7 - 4/7

and for Y (reduced game)

v1 v4 by by bs zy Q
7) . 1 1/9 -1/9 1/3 . 1/3
Zy oe — 2/3 I) 3 1 3
v1 1 . ~1/9 1/9 2/3 : 2/3

As a result of restricting the responding strategies, the profit for X has increased
from 5/2 to 19/7 ($2714 per day) and the profit for Y has increased from 8/3 to 3
($3000 per day). When using the values of x1 =: 4/7, x, = 3/7, y1 = 2/3, and
ys = 1/3, the following minimax profits result:

PROFIT TO X PROFIT TO ¥
ayy, 4/7 X 2/3 X1= 8/21 xy, 4/7X 2/3 x 4 = 32/21
x4yq 3/7 X 2/3 XK 5 = 30/21 x41 3/7 X 2/3 X1= 6/21
xy_ 4/7 X 1/3 x 4= 16/21 aye 4/7X 1/3 X1= 4/21
xq 3/7 X1/3X1= 3/21 xgyq 3/7 X 1/3 X T= 21/21
Total Z, = 19/7 Total Z, 2 3

It is desired to select strategies which will assure at least the minimax profits to X
and Y. In fact, when using the strategies indicated in the solution matrices for the
reduced games, no other profits can result. This is shown as follows:

Profit to X Profit to Y
yz=1 or y,=1 4=1 or m=1
“= 4/7 4/7 x1 4/7 x4 y= 2/3 2/3 X4 2/3 x1
Xe=3/7 393/7KX5 3/71 ya 1/3 13x11  1/3x7

Total Z, 19/7 or 19/7 Total Z, 3 or 3

## PDF page 44

34 Linear Programming: The Solution of Refinery Problems

However, if X uses the responding strategies in the Y reduced game or if Y uses
the responding strategies in the X reduced game, additional profits for either X or
Y can be obtained. The possible increased profit for X by varying Y strategies can be
shown as follows:

Profit to X Profit to Y
yx=1 or yy=i x, =2/3  x,=1/3 TotalZ,
3, = BiB PAYS Sx Ml 2/3 «4 yyp=l 2/3x4 1/31 3
or or
Bq = NyB 1/3 x 5 1/3 x1 yYe=l 2/3 x1 1/3 x7 3
Total Z, 7/3 or 3

Thus if X adopts the responding strategies x, = 2/3 and x, = 1/3, player Y can
then vary his strategies without loss to Y. If Y can be induced under this situation to
adopt strategies y, = 0 and y, = 1, then the profit for X will be increased from
19/7 to 3 ($3000 per day).

Similarly, the possible increased profit for Y by varying X strategies can be shown
as follows:

Profit to X Profit to Y
y,=3/7 yg= 4/7 Total Z, x,=1 or x,=1
a Sil 3/7 x1 4/7 x4 19/7 y, = 3/7 3/7 x4 3/7 X1
or or
Ba = Wl 3/7 x 5 4/7 xX 1 19/7 ye 4/7 4/7 x1 4/7 X7

TotalZ, 16/7 or 31/7

Thus if Y adopts the responding strategies y; — 3/7 and y4 — 4/7, player X can
then vary his strategies without loss to X. If X can be induced under this situation to
adopt strategies x, — 0 and x, — 1, then the profit for Y will be increased from 3 to
31/7 ($4429 per day).

An incentive can be provided by either X or Y changing his responding strategies
slightly so that his opponent will select a strategy resulting in maximum profit. Thus,
by changing X’s responding strategies by 1/21 the situation outlined at the top of
page 35 results.

In the case below, it is desired, of course, to induce Y to adopt strategies y, = 0
and y, = 1, Incentive is provided for this move when X increases strategy x, slightly
above the responding value of 1/3. By increasing x, to 8/21 and decreasing x, to
13/21, there is a distinct profit incentive in the value of 69/21 ($3286 per day) for

## PDF page 45

Refinery Improvement Program Under Competitive Conditions 35

Profit to X Profit to Y
y=1 or yz=l 4% = 13/21 x,= 8/21 total Z,
%j= 13/21 13/211 13/21 x4 Yi=1 13/21x%4 8/21%1 60/21
or or

a = sya 8/21 x 5 8/21 xX 1 ys=1 13/211 8/21K7 69/21
Total Z, 53/21 or 20/7

Y to adopt strategy y; = 1. This results in a profit to X of 20/7 ($2857 per day)
compared with a minimax value of 19/7 ($2714 per day) and a maximum value
(without incentive or loss to Y) of 3 ($3000 per day).

Incentive for X to adopt a strategy most favorable to Y can be provided if Y should
change his responding strategies by 1/21 resulting in the following situation:

Profit to X Profit to Y
yy; = 10/21 yg=11/21 Total Z, %,=1 or x41
xy=1 10/21 x1 11/21 x 4 - 18/7 y, =10/21 10/21 4 . 10/21 xt
or or
X,= 1 10/21X5 11/211. 61/21) yg=11/21 11/21K1 11/21«K7
Total Z, 17/7 or 29/7

In this case Y has increased strategy y, by 1/21 from 3/7 to 10/21, thus causing
the profit to X to increase from 19/7 ($2714 per day) to 61/21 ($2905 per day) and
the resulting profit to Y to increase to 29/7 ($4143 per day) compared with a mini-
max value of 3 ($3000 per day) and a maximum value (without incentive or loss to
X) of 31/7 ($4429 per day).

A summary of these various strategies is shown on page 36.

It can be seen that, if both X and Y adopt responding strategies, the profit to each
is the same as the minimax profit for the reduced games without the safeguard pro-
vided by the minimax strategies. Either player could suffer loss in his profit if his
opponent altered his strategy to bring this about. If both players alter their respond-
ing strategies slightly to induce their opponents to select more favorable strategies,
the result would be only a slight change from the minimax profits. In this example
it is obvious that Y can offer more inducement to X than X can offer to Y so that
the final best arrangement of strategies would be X¥, = 0 and X, = 1 for X and
approximately Y, = 10/21 and Y, = 11/21 for Y to provide profits considerably
over the minimax profits for both X and Y. It is possible, of course, to select single
strategies for the players which will give more profit to one player or to both players

## PDF page 46

36 Linear Programming: The Solution of Refinery Problems

SUMMARY OF VARIOUS STRATEGIES

xi x4 PROFIT TO X* yt y4 PROFIT TO Y*
FULL GAMES .
Minimax for X 1/2 1/2 2500 would play y. and y,
Minimax for Y would play x2 and x3 2/3 1/3 2667
REDUCED GAMES .
Minimax for X 4/1 3/7 2714 1 or 1
Minimax for Y 1 or 1 2/3 1/3 3000

USING RESPONDING STRATEGIES

Minimum to X 2/3 1/3 2333 1 0 3000
Maximum to X 2/3 1/3 3000 0 1 3000
With inducement to Y 13/21 8/21 2857 0 1 3286
Minimum to Y 1 0 2714 3/7 4/7 2286
Maximum to Y 0 1 2714 3/7 4/7 4429
With inducement to X 0 1 2905 10/21 11/21 4143
Both X and Yresponding 2/3 1/3 2714 3/7 4/7 3000

WITH COLLUSION

Maximum profit to X 0 1 5000 1 9 1000
Maximum profit to Y 0 1 1000 0 1 7000
*In dollars per day.

together, but this will require collusion since both individual interests cannot be
served simultaneously by adopting single strategies.

With the information obtained from the game theoretic analysis of a competitive
situation as outlined here, decisions can more easily be made to adopt strategies
that will assure minimax profits regardless of the competitor’s actions, or to adopt
strategies that will take advantage of any increased profits made available by com-
petitor’s selection of non-minimax strategies.

## PDF page 47

CHAPTER 6

Optimum Production Rates and Inventory to Meet
Uncertain Seasonal Requirements

The selection of production rates and inventory to meet a variable seasonal require-
meat for u product such as heating fuel may have a major effect upon the profit or
loss of the operation. In general, variations in the production rate are uneconomical
and may be reduced by increasing inventory. Large inventories are also costly, how-
ever, because of the operating expense and interest on the marginal capital tied up
in the storage facilities and in the stock.

The production cost curve for heating fuel passes through the minimum value at
an average production rate which is equal to the average requirement. This condition
has been brought about by expansion of the heating fuel market in relation to other
products as long as the unit production cost could be decreased, The extra cost at
low production rates is due to uneconomical processing methods to dispose of the
surplus and the extra cost at high production rates is due to diversion of more valu-
able components to heating fuel.

For this illustrative study the heating season has been divided into two equal
periods of 90 days each, denoted as period A and period B. The remainder of the
year is denoted as period C. It is necessary to decide what is the maximum size of
the inventory to be accumulated before period A, denoted as inventory 1, and the
production rates to run during periods A, B, and C. The requirements for the product
have been found to vary in almost random fashion above and below the average for
each of periods A and B. No significant effect of requirement A has been found in
requirement B. A more complete study of this problem would divide the heating
season into many parts, and in this case it would be necessary to consider the per-
sistence of requirements from one period to the next as well as the process lag in
changing from one production rate to another. It is also possible that the inventory
and production rate may have some specific effects upon the requirements.

The possibility of failing to meet requirements was considered; but because the
method of evaluating political and good will effects was not known this case was not

## PDF page 48

38 Linear Programming: The Solution of Refinery Problems

included in the model, The variability of the requirements considered in the model
covers about 99.7 per cent of the expected occurrences in requirements. The extreme
cases not considered would not affect optimum operating practice. For all other cases
production rates were allowed to vary only within limits of meeting possible expected
requirements. The production rate during period B was never allowed to fall below
the average rate during period C since with a low production rate necessary to meet
requirement the inventory would not be critical and a more even production rate
during periods B and C would be economical. In this case the average production
rate could only be approximated until the requirement in period B had developed
sufficiently.

The realization price of the heating fuel was assumed to be constant for period A
and also for period B except where greatest deviation in requirement was found in
period A. A 25 per cent deviation in requirement in period A was accompanied by a
5 per cent change in price in period B. These cases constitute no more than 5 per
cent of the occurrences in either direction. In a more complete study the possible
effect of inventory and production rate on the price-requirement relationship would
be investigated.

Development of the Mathematical Model

It was decided to formulate this problem as a constrained game for solution by
linear programming. (Professor A. Charnes has excellent notes for several lectures on
constrained games‘1*).) This method will allow for incorporation of additional factors
in the complete problem. After some preliminary study, six proposed alternate strat-
egies were included for evaluation, involving two different sets of production rates at
each of three different maximum inventories. Thirteen different probable occurrences
of requirements for periods A and B were included, with restrictions placed on these
occurrences in accordance with the histogram shown on Chart I, page 39. The payoff
matrix was built up from the preduction rate and inventory cost and price data shown
on Chart II, page 39. The linear equations were developed as follows:

The profit to the refiner is Z. In order to allow for negative profit (loss to refiner)

Z>=Xn41 — X42

where the non-negative variables x,,1 and x,<2 are profit and loss, respectively.

The constraints in this problem include the limiting probabilities on nature’s
strategies

Lue (for certain x,)
and the payoff matrix
DjGdigt; + by = Z.
Since nature is the maximizing player in this game, the objective will be to maximize

## PDF page 49

Optimum Production Rates and Inventory to Meet Uncertain Seasonal Requirements 39

CHART |

>
Ss)
z
Fa
J
g
Ke
re
&
1516 #417 18 #19 20 21 22 23 24 25 2 27 28. 29 30
HALF SEASON REQUIREMENTS
CHART II
fs
g 2.00
S 1.50 \
5 \
a IN
B 1.00.
& a TINe
# 0.50 \ AVERAGE PRICE aes EES NDEDIRRICES
go ees
& DEPRESSED ace \ | ea
zo. a
AVERAGE [A
169 REQUIREMENT
' UNIT COST OF MAXIMUM INVENTORY
aga OR UNIT COST OF AVERAGE INVENTORY

i] 50

106

150

200

PRODUCTION RATE

250

300

## PDF page 50

40 Linear Programming: The Solution of Refinery Problems

(—Z). In addition, an artificial vectort with a unit profit of —M will be used to force
=x; = 1. Thus
Sxjy-+-w=1 (wd).
The profit functional to nature therefore becomes
f (—Z) = ~Xn41 + Xn42 — Mw = max.
In the basic problem matrix, this functional has the value
f(-Z) = —M

since w=1 in the null case. The equation for the f (--Z) row in the problem matrix
therefore becomes

—M = f (—Z) —M Xxy + Xn41 — Xn+2

The unit vector for f (—Z) which will not be excluded from the basis has been
omitted from the attached problem and solution matrices but is implied. The variable
w will be excluded from the basis in the optimal solution because of its —M unit
profit. This gives an optimal value

PK—)s=—*,

The optimal refinery strategy will be obtained when b; — 0. Positive b; values indi-
cate the decrease from profit Z for the other strategies.

The method of building up the payoff matrix can be illustrated as follows for Re-
finery Strategy y1, and Nature’s Strategy x2o

Quantity Cost (above normal)

Max inventory1 24 8.64
ve Production A 10.5 0.13
Br Requirement A 16.5

Requirement B 22.5

Inventory 2 18

Possible requirement 28.5

Production B 10.5 0.13

Inventory 3 6

Production C 18 1.67

Avg. inventory 15 3.40

Total production 39 15.97

Normal realization oe) 19.50

Price depression 22.5 —4.50

Profit —0.97

#See Charnes and Cooper, Introduction to Linear Programming® for a discussion of the arti-
ficial vector.

## PDF page 51

Optimum Production Rates and Inventory to Meet Uncertain Seasonal Requirements 41

The complete calculations for the payoff matrix are shown on Tables I and II.

The restrictions on nature’s 13 strategies were derived from a study of past re-
quirements. It was estimated that no more than 25 per cent of the occurrences of the
half-season requirements will be significantly below the normal of 22.5 and no more
than 25 per cent will be significantly above the normal. Most of these deviations will
average about -+ 3 from the normal and not more than 20 per cent of them will aver-
age about + 6. The linear equations for these restrictions were developed as follows:

Probability of half-season deviation of 3 or more Pp = 0.25
Probability of half-season deviation of 6 or more Pop = 0.05
Probability of half-season deviation of 3 plus

half-season deviation of 3 or more (Pp — Dov) (Pp) = 0.05
Probability of normal half-season plus half-season

deviation of 3 or more (1.0 — 2pp) (pp) = 0.125
Probability of normal half-season plus half-season

deviation of 6 or more (1.0 — 2pp) (pep) = 0.025

Nature’s strategies, x20 to x32 shown in the problem matrix, Table III, include prob-
able occurrences in various combinations of requirements A and B restricted by the
above inequalities.

Solution of the Problem

The solution of this problem was carried out by the IBM 701 Computer. The
matrix for the optimal feasible solution is shown in Table TV. A summary of this
solution follows:

Refinery Strategy Inventory 1 Production A Probable Profit
Vis 27 10.5 3.786 — 0 = 3.786
Yi 27 13.5 3.786 — 0.164 — 3.622
Yis 30 10.5 3.786 — 0.252 — 3.534
Y15 24 13.5 3.786 — 0.965 = 2.821
Yio 30 13.5 3.786 — 1.822 = 1.964
Yia 24 10.5 3.786 — 2.919 = 0.867

The best of the refinery strategies included in this study is obviously y1s with a
probable profit of 3.786. The effect of varying inventory 1 and production A can be
determined by comparing the cases. Thus increasing production A from 10.5 to 13.5
with inventory 1 at 27 would decrease probable profit by 0.164. However, with in-
yentory 1 at 24 the optimum production A would be 13.5, and the decrease in prob-

## PDF page 52

42

Linear Programming: The Solution of Refinery Problems

TABLE !: Inventories and Production Rates Needed to Meet
Various Requirements

Refinery
Strategy

7”
=

P.

P.

Nature’s Strategy

Requirement A
Requirement B

Inv. 1 Prod. A
24° «(10.5
24 13.5
27) (10.5
27) 13.5
30 «10.5
30 «13.5

P,

20, Pay Pap Pag Pog = Pag Pag) Poy) Pow 30 Pay Pag
16.5 195 195 19.5 22.5 228 225 225 225 25.5 25.5 25.5 28.5
22.8 195 22.5 25.5 18.5 19.5 22.5 25.5 28.5 19.5 22.5 255 22.5
Inv. 2 18 15 15 15 12 12 12 12 12 9 9 9 6
Prod.B 10.5 «13.5 (13.5 135 16.5 165 165 165 165 19.5 19.5 19.5 22.5
Inv. 3 6 9 6 3 1 #$§ 6 3, 89 9 6 4 6
ProdC 8 «18S 158k BCs 2Hi—i‘ia“H Sk
Avg.inv. 15 165 15 135 18 165 18 138 12 165 15 135 15
Inv. 2 21 #18 #18 #18 15 15 15 15 15 i2 2 12 9
Prod. B 85 105 105 105 335 135 125 135 13.5 165 16.5 168 19.5
Inv. 3 7 9 6 3 2 9 6 3 0 § 6 3 6
Prod. G 7 15 18 21 12 #415 18 21 2 18 18 21 18
Avg.Inv. 15.5 165 15 135 18 165 15 195 12 165 15 135 18
Inv. 2 2118 «#18 #418 15 15 15 15 15 12 12 12 9
Prod, B 95 10.5 105 115 135 13.5 195 135 19.5 165, 16.5 16.5 19.5
Inv. 3 8 9 6 4 2 #8 & 3 0 8 6 3 6
Prod. C 1@ 18 «2k 2315182 1d.
Avg. Inv, 17.5 18 16.5 155 19.5 18 165 15 135 18 165 15 165
Inv. 2 m4 21 21 2] 18 18 18 18 ig 18 18 15 12
Prod. B 85 85 95 105 105 105 105 115 125 195 135 135 165
Inv. 3 1 1 8 B 2 8 G6 4 2 9 8 3 6
Prod.c 17 17) 18° «210 18821238
Avg.Iny. 185 185 175 165 195 38 165 155 145 18 16.5 15 165
Inv. 2 2 21 2 2) 18 1B 618) «6B 8s B58
Prod. B 95 95 10.8 115 10.5 105 115 125 135 135 135 135 165
Inv. 3 MOS fb bs 55 G 5 a
Prod. ¢ 190 19 2) 23) BOL 2a
Avg.Inv. 20.5 20.5 195 185 21 195 185 175 165 19.5 18 165 18
Inv. 2 27 24 «(8A dss sisCKles«C«‘dK;C«é‘WS
Prod. B 85 85 95 10.5 88 98 105 115 125 15 15 125 135
Inv. 3 OVO i om O 7 fb S 7 8 BG
Prod. ¢ wy o17) «190219228 HM
Avg. tn, = 21.5 215 205 195 215 205 195 185 17.5 19.5 185 17.5 18

## PDF page 53

Optimum Production Rates and Inventory to Meet Uncertain Seasonal Requirements 43
TABLE HH: Cost and Profit Data for Inventories, Production
Rates and Requirements
Nature's Strategy Poo Poy Por Pas Pog Pos Pag 1 Pop Pag 9 Pop Pag Pay Pag
BR Requirement A 16.5 195 195 195 22.5 225 22.5 225 225 25.5 25.5 25.5 28.5
EZ Requirement 5 22.5 195 22.5 25.8 165 19.5 22.5 25.8 28.5 19.5 22.5 25.5 22.5
@& tnv.1 Prod.
Pig 24 «10.5. Prod.A = 0.13 0.13 0.13 0.13 0.13 0.13 0.19 013 0.13 0.13 0.13 0.13 0.13
Prod,B 131.02 1.02 1.02 4.30 4.30 4.30 4.30 4.30 9.44 9,44 9.44 14.58
Prod.C «1.67 4.29 1.67 0.26 7.48 4.29 1.67 0.26 0.19 4.29 1.67 0.26 1.67
Max, Inv, 8.64 8.64 8,64 8.64 3.64 8.64 8.64 8.64 8.64 8.64 8.64 8.64 8.64
Avg.Inv. 5.40 5.94 5.40 4.86 6.48 5.94 5.40 4.86 4.32 5.94 5.40 4.86 5.40
Cost 15.97 20.02 16.86 14.61 27,03 23.30 20.14 18.19 17.58 28.44 25.28 23.33 30.42
Price 15,00 19.50 21.00 22.50 19.50 21.00 22.50 24.00 25.50 22.50 24,00 25.50 30.00
Profit —0.97-0.52 4.14 7.59—7.53-2.30 2.36 581 7.92—5.94—1.28 2.17 0.42
Pi; 24 135 Prod.A 1.02 1.02 1.02 1.02 1.02 1.02 1.02 1.02 102 102 102 1.02 1.02
Prod.B 0.86 0,13 0.13 0.13 102 1.02 102 1.02 1.02 4.30 4.30 4.30 9.44
Prod.C = 2.22 4.29 1.67 0.26 7.48 4.29 1.67 0.26 0.19 4.29 1.67 0.26 1.67
Max. Inv. 8.64 8.64 8.64 8.64 8.64 8.64 8.64 8.64 8.64 8.64 8.64 8.64 8.64
Avg. inv, 5.58 5.94 5.40 4.86 6.48 5.94 5.40 4.86 4.92 5.94 5.40 4.86 5.40
Cost 18.32 20.02 16.86 14.91 24.64 20.91 17.75 15.80 15.19 24.19 21,03 19.08 26.17
Price 16.00 19.50 21.00 22.50 19.50 21,00 22.50 24,00 25,50 22.50 24.00 25.50 30.00
Profit 3.32052 4.14 7595.14 0.09 4.75 8.20 10.31-1.69 2.97 642 3.83
Pig 27 «10.5 «Prod.A = 0.18 0.13 0.13 0.13 0.13 0.13 0.13 0.13 0.13 0.13 013 013 0.13
Prod.B 9.40 0.19 0.13 0.10 2.02 1.02 1.02 1.02 102 4.30 4.30 4.30 9.44
Prod,C = «112 «1.67 0.26 «=O 4.29 1.67 0.26 0.19 1.59 1.67 0.26 0.19 0.26
Max. Inv. 9.72 9.72 9.72 9.72 9.72 9.72 9.72 9.72 9.72 9.72 972 9.72 9.72
Avg. inv, 6.30 6.48 5,94 5.58 7.02 648 5.94 5.40 4.86 648 5.94 5.40 5.94
Cost 17.67 18.13 16.18 15.53 22.18 19.02 17.07 16.46 17.32 22.30 20.35 19.74 25.49
Price 15.00 19,50 21.00 22.50 19.50 21.00 22.50 24.00 25,50 22.50 24.00 25.50 30.00
Profit —2.67 1.37 4.82 6.97—2.63 198 643 7.54 818 0.20 3.65 5.76 4.51
Pi, 27 «13.5 Prod.A = 1.02 «1.02 1.02 1.02 1.02 1.02 1.02 1.02 1.02 102 1.02 1.02 102
Prod.B 0.86 0.86 9.40 0.13 0.13 0.13 0.13 O10 0.42 1.02 1.02 1.02 4.30
Prod.C «2.22 2.22 112 0.26 4.29 167 0.26 0 0.53 167 0.26 0.19 0.26
Max. inv. 9.72 9,72 $.72 9.72 9.72 972 9.72 9.72 9.72 9.72 972 972 9.72
Avg. inv. 6.66 6.66 6.30 5.94 7.02 648 5.94 5.58 5.22 648 5.94 5.40 5.94
Cost 20.48 20.48 18,56 17.07 22.18 19.02 17.07 16.42 16.91 19.91 17.96 17.35 21.24
Price 15.00 19.50 21.00 22.50 19.50 21.00 22.50 24.00 25.50 22.50 24.00 25.50 30.00
Profit, 5.48098 244 5.43268 1.98 543 7.58 859 2.59 6.04 815 8.76
Pyg 30:10. ProdA ©1319 0.13 0.13 0.13 0.13 0.13 0.13 0.13 0.13 0.13 0.18 0.13
Prod.B 0.40 0.40 0.13 0.10 0.23 0.13 0.10 0.42 1.02 1.02 102 1.02 4.30
Prod. C 112 112 0.26 0 167 0.26 0 0.53 159 0.26 0.19 159 0.19
Max, Inv. 10.80 10.80 10.80 10.80 10.80 10.80 10.80 10.80 10.80 10.80 10.80 10.80 10.80
Avg. Inv. 7.38 7.38 7.02 666 7.56 7.02 6.66 6.30 5.94 7.02 648 5.94 6.48
Cost 49.83 19.83 18.34 17.69 19.29 18.34 17.69 18.18 19.48 19.23 18.62 19.48 21.90
Price 15.00 19.50 21.00 22.50 19.50 21.00 22.50 24,00 25.50 22.50 24.00 25.50 30.00
Profit  —4.83—0.33 2.66 4.81 0.21 2.66 4.81 5.82 602 3.27 5.38 602 8.10
Pip 3013.5 Prod. A 1.02 102 1.02 1.02 102 1.02 1.02 1.02 102 102 1.02 1.02 1.02
Prod.B 0.86 «0.86 0.40 0.13 0.86 0.40 0.13 O10 042 0.13 0.10 0.42 1.02
Prod. 2.22 -2.22 142 0,26 2.22 112 026 0 053 0.26 0 0.53 0.19
Max. Inv, 10.80 10.80 10.80 10.80 10.80 10.80 10.80 10.80 10,80 10.80 10.80 10.80 10.80
Avg. Inv. 7.74 7.74 7.38 7.02 7.74 7.38 7.02 6.66 6.30 7.02 6.66 6.30 6.48
Cost 22.64 22.64 20.72 19.23 22.64 20.72 19.23 18.58 19.07 19.23 18.58 19.07 19.52
Price 15.00 19.50 21.00 22.50 19.50 21.00 22.50 24,00 25.50 22.50 24.00 25.50 30.00
Profit  —7.64—3.14 0.28 3.27 3.14 0.28 3.27 5.42 6.43 3.27 5.42 6.43 10.49

## PDF page 54

44 Linear Programming: The Solution of Refinery Problems

TABLE ff: Problem Matrix for Heating Fr

Refinery Strategies

Inventary i 24 24 #27 27° 30
Production A 10.5 13.5 10.5 13.5 10.5 °

Vectors =P, =P, Pp Pg Py Pg Py Pg Py Pig Pay Paz Pag Pag Pus Pas Par Pia

PL (0.25
PL (0.25
Py 0.05
P, 0.05
Ps 9.05
Ps 0.05
P, 0.05
P, 0.05
Po 0,125
Pio 0.125
Pi, 0,025
Pip (0,025
Pi, 1.0
Pig

Ps 0

Pig oO

Pi, (8

Pi, 0

Pip i)

Pp, M

TABLE !V: Optimal Solution of the Heating Ft

Refinery Strategies

Inventory | 24 #24 «#+2F 27) 30
Production A 10.5 13.5 10.5 13.5 10.5

Vet Py Pp Pg Pg Pg Pg Pp Pg Pg Pig Pay Paz Pg. Pra Pas Pigs Paz Pie

Pog 0.080 aan are 1

P, 0.100 wt = =

Pog (0.025

Pop 0.050

P, 0,050

Pop 0.150

P,  0.025 .

Pay (0.050 we 1 a . ee

Py, 3.786 1.78 —0.92 —3.45 . 5.49...

Pip 0.125

P,, (0.050

ve 2.39 —2.39 —4.25 ot
. —3.69 2.35 —4.21 —1.30 ... —2.21 ...

Pip 0.1635 2.38 ....

Pip «0.2517 1.54...
Pig 2.919 —2.39 3.070 186 «186 121... O87 ... 3.07 1 ..
Pis 0.965 L2L con Heil O57 .... 0.68 2. 1

—§.23 —3.93 —8.14 —0.46

Pio 1.8215 2.38

[n/c a —1 -1 -1

Py 0.080 ve "

Py, 0.100 = 2) on Coc) f

Pl 3.786 749° 345... 5.23 178 0.92 3.45 M543...

## PDF page 55

Optimum Production Rates and Inventory to Meet Uncertain Seasonal Requirements 45

rentory and Production Rate Problem

Nature's Strategies

165 195 195 195 225 225 225 225 225 255 26.5 25.5 28.5 Requirement A
225 (19.5 225 25.5 165 195 225 25.5 285 195 22.5 25.5 22.6 Requirement B
ectors Pan Poy Pag Pog Pg Pos Paz Pog «= Pay © Pag) Pay Pan Pag Pag
P, 1 1 1 1 ma UU
P, 1 1 1 1
~ 1
Py 7
Ps 1 .
P, 1 .
P, 1 -
P, 1
Py
Bio os
P) 1 .
Pia 1 1 1 1 1 1 1 1 1 1 1 i 1 .
Py, 0.97 052 4.14 7.59 ~753 230 236 5.81 7.92 —5.94 128 217 042 1 1
Pi; 332 052 414 7.59 5.14 0.09 475 820 10.31 169 297 642 3.83 —1 1
Pig —267 137 482 697 268 1.98 5.43 7.54 818 0.20 3.65 5.76 461 —1 1
Pip ~$48 0.98 244 5.43 268 198 543 7.58 859 259 604 815 876 —1 1
Pie 483 0.33 2.66 4.81 0.21 266 4.81 5.82 602 3.27 538 602 810 —1 1
Pio 7.64 314 0.28 9.27 3.14 0.28 3.27 5.42 649 3.27 542 G43 1049 —1 1
Pp, —M —-M —-M -M -M -M -M -—M -M -—M -—M -—M —M 1 -1
ventory and Production Rate Problem
Nature’s Strategies
165 195 195 19.5 225 225 225 22.5 225 25.5 25.5 25.5 28.5 Requirement A
225 195 225 255 165 195 228 255 288 198 22.5 25.5 225 Requirement #
Betors Pg Pay) Pag) Pog) Pag §= Pag) Pog)S Pay) Pog) Pap 0 Pag «Pay Pan Pigg Pea
Pap 1 i
P, 1
24
Pog i
Ps
P,
22
pe i
p —2,11 —2.75 1
33 i
ro
Py 0.04 2.75
Pig , 110 0.41
Pi, 1.34 —1.54
Pis 1.34 2.81
Pio ve 004 2.81
P 1 1 0.41
26
Pro
aM 211 2.75 0.33

## PDF page 56

46 Linear Programming: The Solution of Refinery Problems

able profit for decreasing inventory 1 from 27 to 24 would be 0.965. On the other
hand, the decrease in probable profit for increasing inventory 1 from 27 to 30 would
be 0.252. It is necessary, of course, to study other cases and other factors in order
to determine the optimum operation.

The selection of nature’s strategies is made by the simplex method to inflict the
greatest loss on the refinery operations within the limits of the constraints. This solu-
tion selected the following distribution of requirements: _

Nature’s Strategy Req. A Req. B Total Req. Probability
Xo 16.5 23.5 39 0.05
Xoq 19.5 19.5 39 0.05
Xo9 19.5 22.5 42 0.15
Xo3 19.5 25.5 45 0
Xing 22.5 16.5 39 0.025
Xo5 22.5 19.5 42 0.10
x6 22.5 22.5 45 0.475
Xo7 22.5 25.5 48 Q
Xog 22.5 28.5 51 0
%o9 25.5 19.5 45 0.05
X39 25.5 22.5 48 0.05
X31 25.5 25.5 51 0
Xa 28.5 Oe) 31 0.05

1.00

It is concluded that this distribution is a satisfactory representation of past occur-
rences. However, since the strategies of nature which were omitted in this solution
would tend to increase refiner’s profit, the profit of 3.786 calculated by the linear
programming solution of the constrained game must be considered somewhat pessi-
mistic. This is, of course, a conservative method of planning operations.

## PDF page 57

CHAPTER 7
Planning an Experimental Program*

Introduction

In order to show the use of the constrained game theory, a simplified example has
been chosen which represents alternate methods of selecting an experimental pro-
gram to solve a refinery problem. This example is hypothetical, and fictional costs and
probabilities have been arbitrarily chosen. The study was suggested by the work of
Thomas A. Elkins on geophysical exploration.'*)

Statement of Problem

A refinery has run into difficulty with the color of the lube stock. It has been
necessary to clay filter this stock at an additional cost to the refining operation of
$1,000,000. A suggestion has been made for a modification in the extraction column
which may eliminate the clay filtering. The modification will cost $100,000. There
are several alternate schemes that the refiner can follow in deciding to make this
plant modification. These are:
J. He can make the modification without any preliminary experimental testing.
IL. He can perform a bench scale test and install the modification if the bench scale
test is successful.
III. He can perform a pilot plant test and install the modification if the pilot scale test
is successful.
IV. He can follow scheme III only if satisfactory results have been obtained on the
bench scale test.

The possible results that can be obtained (the strategies of nature) are:
1. The modification will not clean up the Inbe stock and is indicated to be unsatis-
factory by both the bench and pilot tests.
2. The modification will not clean up the lube stock and is indicated to be unsatis-
factory by the pilot test, although satisfactory results are indicated by the bench test.

*This chapter was prepared by Mr. M. A. Efroymson, Process Research Division, Esso Research
and Engineering Company.

## PDF page 58

48 Linear Programming: The Solution of Refinery Problems

3. The modification will not clean up the lube stock, although satisfactory results are
indicated by both the bench and pilot tests.
4. The modification is successful in the plant and is indicated to be satisfactory by
both bench and pilot tests.
5. The modification is successful in the plant and is indicated to be satisfactory by the
pilot plant test, although the bench test indicates it is unsatisfactory.
6. The modification is successful in the plant, although both the bench and pilot
plants indicate it is unsatisfactory.

The payoff is then as below:

Nature 1 2 3 4 5 6
Refinery | —B —B —B A~B A—B A-—B
Refinery Il —C —B—-—C —B-C A-—B-—C -C -—C
Refinery ill —D ~—D —~B-D A-—B-—D A-B-D —D
RefineryIV  —C —C—D —B-C—D A~—B-C-D -C -—C
where A = value of oil clean-up
B = cost of plant modification
C = cost of bench test
D = cost of pilot test.
We can assign values to these as follows:
(a) A successful lube oil clean-up is worth $1,000,000 (4).
(b) The plant modification will cost $100,000 (B).
(c) The bench test will cost $5,000 (C).
(d) The pilot test will cost $35,000 (D).
The payoff is then as befow (in hundreds of thousands of dollars).
Nature 1 2 3 4 5 6
Refinery | —0.1 —0.1 —0.1 0.9 0.9 0.9
Refinery 11 —0.005 —0.105 —0.105 0.895 —0.005 —0,005
Refinery Ill —0.035 —0.035 —0.135 0.865 0.865 —0.035
Refinery IV —0.005 —0.040 —0.140 0.860  —0.005 —0.005

Discussion

If we assign x; to x5 as the percentage of times nature employs strategies 1 through 6,
then the payoff for each of the refiner’s strategies can be written,

## PDF page 59

Planning an Experimental Program 49

Profit for refiner’s strategy _

1=Q:=—0.1x%, —O.1lx. —O.1x3 +0.9x, -+0.9x, + 0.9x5
I= Q2 = —0.005x, — 0.105x2 — 0.105x3 + 0.895x, — 0.005x5 — 0.005x,
Til = Q; = —0.035x, — 0.035x2 — 0.135x3 + 0.865x, + 0.865%; — 0.035x5
IV = Q, = —0.005x, — 0.040x2 — 0.140x3 + 0.860x, — 0.005x; — 0.005x,.

The refiner will choose the maximum Q obtained in these equations above.
If Qo = maximum Q, then Q:1 —Q) = 0; OQ: —Q) = 0; Os —Q. = 0;
Qs, —Qy = 0. Therefore the first equation above can be written

—0.1x, —0.1x2 —0.1x3 -+- 0.9x4 + 0.925 + 0.9x— — Qo<=0.

The other equations will have a similar form.

Since Qo may be either positive (a profit) or negative (a loss), it is desirable to
define Qy as the difference of two non-negative numbers, ie., Qo = x;—xs, where
Xg is zero when Qy is positive and where x; is zero when Qy is negative.

The above equation can then be written

—0.1%; — 0.lx, — 0.1x3 + 0.9x4 -+ 0.9x5 +- 0.926 — x7 4 xg =O
or
—0.1x, — 0.1%, — 0.1%3 + 0.9x4 + 0.9x5 + 0.9x— — x7 + xg X%) =O

where x9 is zero or a positive value which changes the inequality to an equality;
% is called a slack variable, which is defined as a non-negative value that can be in-
serted into an inequation, thus making an equation.

The equation now states that the profit for scheme I

(—0.1x, —0.12 —0.1x + 0.9%4 + 0.9x5 ++ 0.9x9)

minus the profit for the most profitable scheme (x; — xg) plus a slack value (x9)
which is zero or a positive value equals zero.
The other strategies for the refiner can be written as follows:

—0.005x, —0.105x2 —0.105x3 4-0.895x, —0.005x; —0.005x5 — x; + x3 X19 = 0
--0.035x, —0.035x2 —0.135x3 +-0.865x4 +0.865x, —0.035x—— 47+ 43+ %1 =90
—0,005x, —0.040x, —0.140x, +0.860x, —0.005x; —-0.005x5 — x7 -+ Xe-+*12 = 0

where x19, ¥11, and X12 are other slack variables.
The limiting probabilities on the strategies of nature, x1 to xg, are obtained from
our past experience with problems of this type. If they are stated as inequalities,

## PDF page 60

50 Linear Programming: The Solution of Refinery Problems

they should be stated, if possible, so that they establish a minimum value for favor-
able results or a maximum value for unfavorable results. In this particular problem,
the most favorable results are those which are actually tested in the plant and are
successful, and the most unfavorable are those which are actually tested in the plant
and are unsuccessful. This can be stated in another way, namely, that we want the
number of successful plant modifications to be as great as possible, while keeping the
total number of plant modifications as small as possible.

These limiting probabilities on the successful plant modifications can be stated
as follows (based on past experience):

(a) If we used no preliminary testing, there is a 10 per cent or more chance that the
plant modification will clean up the oil.

(b) If the plant modification would clean up the oil, 70 per cent* or more of the
time the bench test will be indicative, and we will install it in the plant.

(c) If the plant modification would clean up the oil, 80 per cent* or more of the
time the pilot test will be indicative, and we will install it in the plant.

These restrictions can be stated algebraically as follows:

(a) x4 + %5 + x6 =10% of x1 +x+%s = 90%
(b) x4/(24 -+ x5 + 0) =70% or ~0.3x, + 0.7x; + 0.7.x, <0
(C) Ga + %5)/(%4 + X5 + %e) = 80% or —O0.2x, — 0.2x5 4 0.8x5 0.

The limiting probabilities on the total number of plant modifications (again,
based on past experience) are:

(d) If we used no preliminary testing, we would install the plant modification
100 per cent of the time.

(e) If we use the bench test, the test will have sufficient screening power that we
will install the plant modification only 50 per cent or less of the time.

(f) If we use the pilot test, the test will have sufficient screening power that we
will install the plant modification only 25 per cent or less of the time.
These restrictions can be stated algebraically as follows:

(d) X1 + X2 + xg + 4 + x5 + x6 = fl
{e) X2 + X3 + x4 = 50%
) Xs + X4 + X5 = 25%

These six equations can now be written

*Note: These values are used only to illustrate the mathematical technique and are not neces-
sarily indicative of the sensitivity of this kind of experimental work.

## PDF page 61

Planning an Experimental Program 51

(a) X1 + Xe ++ X3 + Ng = 0.9
(b) —0.3x4 + 0.7x5 + 0.7x6 + x18 =0
(c) —0.2x, — 0.2x5 + 0.8x6 4- X17 =0
(d) Xy + Xe + x3 + Xe + x5 + xp + tg = 1
(e) : X2 -+ X3 + Xa + X14 = 0.5
(f) Xg -+ Xa + 5 + 15 = 0.25

where x1 to x17 are slack variables and x1. is an artificial variable. An artificial vari-
able must have a value of zero in any optimal solution,

A solution is obtained by solving for the x values which satisfy the six equations
above together with the four equations on page 49, which are written in matrix form
as Tableau I in Table 1, page 52. We obtain an optimum solution by maximizing the
function —A—M x1, where A = x;—xg.

The first, second, and last tableaus are shown on Table 1. The remaining steps in
the calculation can be inferred from Table 2, page 52.

From the last tableau, the expected gain from this proposal is $23,500. The
optimum strategy for the refiner is P;2 (performing both bench and pilot tests) with
the optimum strategy for nature being (0.47, 0.26, 0.17, 0.07, 0.01, 0.02).

These are average values based on the probability of each occurrence. As shown
in the payoff matrix on page 48, any one particular effort may cost as much as
$140,000 (nature strategy 3), or may return as much as $860,000 (nature strategy 4).
However, if we made enough decisions of this kind so that the proportion of suc-
cessful and unsuccessful ventures would average out according to the law of proba-
bility, we would realize an average profit of $23,500.

A more complete analysis of the economics of the alternate refinery schemes is
shown in the table below:

ECONOMICS OF ALTERNATE REFINERY SCHEMES

Average Cost

Getta Gata Bench and Plant Total eo) ee
Pilot Tests Modification
No testing = 100,000 100,600 100,000 _ —
Bench testing 5,000 50,000 55,000 70,000 15,000 ON >
Pilot testing 35,000 25,000 60,000 80,000 20,000 33.3
Bench and pilot
testing 23,500 24,000 47,500 70,000 23,500 49.4

The use of bench and pilot tests shows the greatest profit ($23,500) and the

## PDF page 62

The Solution of Refinery Problems

Linear Programming.

52

ee 4b fE SE SE BE Ue Pee
or 2 € ¢ £2 ¢ T payasul 10398,
Xi WA HA IA A AL Ooo nesjqeL =% STAVL
Wtsoo- TO 60 TO 900 0 OT ~ ~ gezo'o— footy
soc0 TO- 6'0~ TO s90'0— ; - : ; gezo'o fai
zo : OT : 20°0 °4 z
ro oo = see 10° Sy =
s0— o1— ~ v0 &4 =
T0'0 s90°0 se00°0 oly z
Ea= OT vo Ma z
TO Pa 7 - 920 tq =
a seo— seaoo ug
£0 : . £00 "4
sero— seo— ~ : sezoro Sa
‘
WwW wro— ed
a = oT ot o om re 4. 8a
oR = - #0 BS RS = a “ly e
= FR £0 £0 f0- aad a OF eS
= OR ~ OT OT - a) ety) 4
= a : - ay an ms tg FA
ae ot Soo'0— so0'o— o9e'a “ gyooro ta iy
a: 7 OT seo'o- sod S980 STe0"0 ily =
7 : ~ soo'o— s000— S680 spooo <| a
ia 0060 ©6060) 06a 60°0 4g
*
5 i . Ba OI- OF w- OW aly
oro a — zo- 0 a =
oe ST OY ~ oT OT Sly 4
7) im | ot OT vla Ps
oi : . be ety =
. O'I— $00':0~ s00':0— 0980 aly =
- OI— SeOo— $980 $98"0 ug
~ O1— sooe— s00'0— saeo og
“= ad OI 0060 0080 006"0 Sa
Bly aly vq Sly Wy el tly tly Oly bq & 4g 9 54 La
= OT OT—

W3180Ud ANOJHL JWVD GINIVULSNOS JO NOILVINSTVD XATdWIS—L F1GVL

## PDF page 63

Planning an Experimental Program 53

lowest total cost ($47,500): It can be noted in all the cases that, compared to no
testing, the value of experimental work, either bench scale or pilot plant, is related

to the lower manufacturing costs (plant modification costs) rather than to any
increase in income.

Practical A pplication

This example is too simplified to have any practical value; it is illustrative of a
method of linear programming and could probably have been solved by conventional
mathematics. The technique, however, can be extended to include all the factors
which are considered in a realistic plan for experimental research, such as avail-
ability of research funds, availability of technical manpower, effect on other research
projects competing for funds, manpower, and equipment, effect of time of comple-
tion on the value of the project, personnel morale, etc. When these other factors are
considered, the problem becomes so complex that it is difficult to obtain an optimum
solution by conventional means and the methods of linear programming will have
the most merit.

## PDF page 64

CHAPTER 8

A Transportation Problem -

Linear programming can also be applied to a minimum cost transportation problem.
The general transportation model is described by George B. Dantzig in his “Simplex
Method Applied to a Transportation Problem.”‘®) Koopmans and Dantzig state that
a transportation problem involving 25 origins and 60 destinations was solved in 9
man days by hand computation techniques. High-speed computers could undoubtedly
solve this problem with very little effort. Henderson and Schlaifer*) also describe
an interesting transportation problem solved by linear programming. Although the
general simplex method can be used for the solution of the transportation problem,
it is more convenient to use a special solution technique applicable only to transpor-
tation and allocation problems.

Herewith is a typical minimum-cost-transportation problem solved by a special
method of linear programming, a study of which has been presented by Charnes and
Cooper in Management Science*), In this example given supplies of No. 2 Heating
Oil are available at five origin points to meet stated requirements at three destination
terminals, The transportation costs for all 15 possible transfers are known. There are
many possible solutions to this problem, and only one of them will be at the minimum
cost.

Development of the Mathematical Model

Let AX; = quantity available at the jth supply point,
Y, = quantity required at the ith destination,
Ay = quantity transferred from j to i,

and Cy = unit cost of this transfer.

The constraints are

DjAy = Yi, i= leoom
and fJalerrn
BiAy = X; Ay=0.

## PDF page 65

A Transportation Problem 55

The objective is
22,CyAy = fC) = minimum.

The general simplex form for this model is illustrated for a 3 by 3 problem as
follows:

Arn. Ariz Aig Azt Azz Azg Ag) Aga Aga f(C) 2 @
1 1 i . os = . = Ye

a 1 . “ 1 - : 1 = Xs
—Cyy —Cyp —Cyg —Cyy —Cog —Cog —Czy —Czg —Cagp 1 = 0

£(C) = minimum

The six equations for Y; and X, contain one redundancy, since 2,Y, = 2,X;. Thus
any Y,; or X; value can be derived from known values of the other five variables.
Therefore one of the equations can be eliminated from the set. Generally m+ 2 — 1
variables will appear in the basis. By eliminating equation X; and rearranging, a
feasible solution may be obtained. If variables 41,, A1e, Az2, Aes, and Az; form a
non-negative basis, the following solution results:

Ay Ai2 © Ala Aa Ao2 A23 A31 Aa2 Az3f(C)

1 t = ae - con an We
. 1 - i =f =i ce Yot¥y—Xo-Xy
1... Lon aes 1 m ©. o xX
ooo ee = flo. 1 1 woe wee RGAE Wp
— —C's Orn won oxo =O C's .. 1

r A. os > A. Yo A ~

si =—Cyg =—Cy ve ae SAHCgy =—Cg.

_ AG, Crp Cry Chey on a HOO HOO ce ox
_ Ch 404 we oe Gp Chy toh _ «
a Comer son one Opel _
where

FO) = CXC yo(V¥1—X1) + Coo(Xa-X1— Y1)-+-Caa(Vot Yi—X2—X1) + Cas Vs.

## PDF page 66

56 Linear Programming: The Solution of Refinery Problems

This solution may be shown as follows:

i
m
; 1 2 3 Sia
1 xX, Y,-X, Ni
2 XetX,-Y, |¥ot+¥;-X2-X,| Ye
3 Ys Ys
DiAij XX x2 x3
Note Xg=¥3+YotYi—X2—X1.

The effect on f(C) of substituting any A,, not in the basis for an A, in the basis is
shown by the new C’,; values (negative coefficients in the f(C) row). Thus, for sub-
stituting 13,

Af(C)/AA 33 = — (—C'r2) = — (—CigtCog—Coo-4 Cyz).

This means that if A1; is increased by one unit, 42, must be decreased by one unit,
Ago increased by one unit, and Ai. decreased by one unit in order to maintain the
required balance as follows:

i 1 2 3
1 -1 +1
2 +1 ~—1
3

These changes will change f(C) accordingly by the original C,, values. If any new
C’y value is positive, a decrease in f(C) can be obtained by substituting the corre-
sponding. Ay. As in the simplex method, the entering 4;; should be large enough so
that one of the Ay values in the basis will become zero.

A method has been developed then for setting up a feasible solution to the trans-

## PDF page 67

A Transportation Problem 57

portation problem and reaching for an optimum by efficient substitution based upon
the general simplex method of linear programming. It will be noted that only addition
and subtraction are used in the transformations, since all coefficients of A, in the
simplex matrix are +1 or —1.

The Heating Oil Transportation Problem
A homogeneous material, available at supply points A, B, C, D, etc. in given
quantities, should be shipped to destinations X, Y, Z, etc. to meet given requirements

at the smallest possible cost. All transportation costs between origins and destinations
are given.

Supplies (No. 2 Heating Oil)

Point of Origin Amount Available Destination Amount Required
(Mbpd) (Mbpd)
A 10 Xx 40
B 20 Y 80
Cc 30 Zz 120
D 80
E 100

Transportation Costs

Point to Point — cpb Point to Point — epb Point to Point — cpb
Atox 37 AtoY 53 AtoZ 58
BtoX 60 BtoY 52 BtoZ 63
CtoxX 55 CtoY 50 CtwoZ 61
DtoxX 54 DtoY 59 DtoZ 56
EtoX 62 EtoY 51 EtoZ 64

Step 1

Arrange table of costs above minimum cost.

A B c D E
x 7 10 5 4 12
Y 3 2 0 9 1

## PDF page 68

58 Linear Programming: The Solution of Refinery Problems

STEP 2
Arrange table of quantities to be transported.
A 8 Cc D Eo Total
x 40
Y - 80
Zz 120
Total 10 20 30 80 100 240

Step 3
Select a basic feasible solution (No. 1), starting in box XA and working down
to box ZE*

A B c B E Total

x 10 20 10 40

Y 20 60 80

Z 20 100 120
Total 10 20 30 80 100 240

The transportation cost for feasible solution No. 1 is $143,800 per day. The cost
calculations are given in Step 8.

Tt is now necessary to determine whether feasible solution No. 1 uses the mini-
mum possible costs. This is done by determining the C’, for the vacant boxes (Ay
not in the basis).

STEP 4
Compute C’,,
C’xn = Cyn — Cyn t+ Cyp —-Cygp = 4-9+4+0-5= —-10
C'xn = Cxn — Coy + Cop — Cyp + Cyg — Cre = 12 —- 144+6-940—5=—10
C’y4 = Cys — Cyo + Cxg — Cry 3-—04+5-7=1
Cyn = Cyn — Cyo + Crp ~ Cxp 2-—04+5-—10=-3
Cyn = Cen — Con + Cun — Cop = 1—144+6-9=-16

Hf

Ul

*N.B. The number of elements filled in the boxes must equal m + n — 1 or the sum of X, Y, Z,
etc. plus A, 8, C, etc. minus 1; thus 3 + 5 — 1 = 7. In some cases it might be necessary to add 0
in one or more boxes.

## PDF page 69

A Transportation Problem 359

Cra = Coa — Coy + Cyp — Oye + Crp — Cog = 8-64+9-045-72=9
Con = Con — Cap + Cyn — Cyo + Cro — Cyn = 13 -649-045—10=11
C'xg = Cag — Cap + Cyn — Cy =11-649-0=14

The cost factor C’yy has the largest negative* value of —16, which is the change in
f(C) for each unit of YE which can be substituted in the basis. The maximum quantity
of YE should be introduced into the basis, protecting non-negativity.

STEP 5
Determine feasible solution No. 2 by adding quantity 6 in box YE and balancing
case.

A B | DB E Total

x 10 20 10 40

Y 20 60-6 @ 80

Zz ’ 20+6 100-9 120
Total 10 20 30 80 100 240

The quantity @ is the minimum value necessary to eliminate one of the elementst
in basic solution No. 1, namely 6 = 60, and YD = 60 —60 and is eliminated. The
new feasible solution No, 2 becomes

A 5 c D E Total

x 10 20 10 40

Y 20 60 80

Zz 80 40 120
Total 10 20 30 80 100 240
The transportation cost for feasible solution No. 2 is $134,200 per day, as shown

in Step 8.
Calculation of the cost factors shows that C’z4 now has the largest negative value
of —7, and ZA should next be introduced into the basis.

*NLB. In case of m tie for the largest negative value of C’,,, the choice for substitution is arbitrary.

+N.B. Ef two of the elements should happen to be eliminated by this procedure, one of them must
be restored as a 0. Special procedure is required as discussed in Koopman’s Activity Analysis of
Production and Allocation.(®)

## PDF page 70

60

Linear Programming: The Solution of Refinery Problems

STEP 6

Determine feasible solution No. 3 by adding quantity @ in box ZA and balancing

case.

x

Y

Zz

Total

A B c D E
10—6 20 10+6
20-4 60+6
6 80 40—6
10 20 30 80 100

Total

40

80

120

240

The minimum value of @ necessary to eliminate one of the elements in solution
No. 2 is 6 = 10. The new feasible solution No. 3 becomes

x

Y

4

Total

A B ¢c D E
20 20
10 70
10 80 30
10 20 30 80 100

Total

40

80

120

240

The transportation cost for feasible solution No. 3 is $133,500 per day, as shown in
Step 8.

Calculation of the cost factors shows that C’z, now has the largest negative value
of —5, indicating that ZB should next be introduced into the basis.

STEP 7
Determine feasible solution No. 4 by adding quantity @ in box ZB and balancing
case.

A B c o E Total

xX 20-6 20+6 40

Y 10-6 70+86 80

Zz 10 6 80 30-6 120
Total 10 20 30 80 100 240

## PDF page 71

A Transportation Problem

61

The minimum value of 6 necessary to eliminate one of the elements in solution
No. 3 is @ = 10. The new feasible solution No, 4 becomes

A 5 c D E Total

x 10 30 40

Y 80 80

Zz 10 10 80 20 120
Total 10 20 30 80 100 240

Calculation of the cost factors shows that none of the C’,, values is negative, indi-
cating that no further reduction in cost can be made by substitution of the Aj; values.

STEP 8
Determine the minimum cost. All cases are calculated to show the magnitude of
the reduction.
CASE 1
A B Cc D E
x 10X7+20x10+10x5 = 320 Cost;=
Y 20x 0+ 609 = 540 (2380 + 50 x 240)
4 20 x 6+ 100 xX 14=1520 1000/100 =
3330 $143,800 pd
CASE 2
A B c D E
xX 10X7+20x10+10x5 = 320 Costz=
Y 20 x 0 + 60X1 = 60 (1420 + 50 x 240)
Z 80x6+ 40x14=1040 1000/100 =
1420 3134,200 pd
CASE 3
A B c D E
x 20 x 10+ 20x 5 = 300 Cost; =
Y 10x 0 +70x1 = 70 (1350 +50 x 240)
z 10x8 +80x6+30x14 = 980 1000/100 =
$133,500 pd

1350

## PDF page 72

62 Linear Programming: The Solution of Refinery Problems

CASE 4
A B ¢c D E
x 10 x 10+ 30 x5 = 250 The minimum cost for
Y 80x 1 = 80 this example becomes
Z 10x8+ 10x 13 + 806+ 20X14 = 970 Costu, =
1300 (1300 + S50 x 240)
1000/100 =
$133,000 pd

Note that the minimum-cost feasible solution Case 4 in this example uses the two
highest transportation costs 64c for E to Z and 63c for B to Z and does not use the
lowest transportation cost 50c for C to Y. No other minimum-cost feasible solution
may be possible in this problem with other transportation arrangements since all
C’y values are positive (negative coefficients in f(C) row). The minimum cost for this
example is $133,000 per day.

## PDF page 73

CHAPTER 9

A Crude Allocation Problem

The transportation model of linear programming can be used to determine an
arrangement for allocating available crudes to several refineries in order to obtain the
maximum possible profit. An illustrative example is presented herewith. In this ex-
ample, ten crudes are available in stated quantities from 10,000 to 30,000 barrels
per day each, with an aggregate availability of 200,000 barrels per day. Three
refineries X, Y, and Z have incremental operations with stated requirements totaling
180,000 barrels per day. Of the available crude, 20,000 barrels per day will not be
used, One of the refineries has two incremental operations, X, and X2, at different
efficiency levels. The net profit or loss for each crude in each refinery operation is
given. It is assumed that the crude evaluations will reflect the resulting product dis-
tribution from these incremental operations. However, if further debits are encoun-
tered in the solution because of lack of product quality or for transportation of
surplus products, suitable corrections can be made in the crude evaluations and the
problem reworked until a realistic solution is obtained. In large-scale problems, the
calculations can be handled easily on high-speed computers.

The mathematical treatment used in this example is similar to the simplex method
applied to a transportation problem described in Chapter 8. However, the crude
allocation problem is worked to maximize the profit, whereas the transportation prob-
lem is worked to minimize the cost. A modified method of selecting the basic case is
introduced. It it is believed that this method will save about one-half of the trials re-
quired for the solution. A new method is also suggested to maintain the required
number of elements in the quantity matrix (necessary for the simplex method), It is
believed that this method, also, will save calculations and will prevent degeneracy of
the solution.

The following calculations are shown in considerable detail so that the method can
be used for the solution of current problems.

## PDF page 74

64 Linear Programming: The Solution of Refinery Problems

Data Given

Crude evaluation, availability and requirement

Crude o b c d e § 9 h i i Required
(Profit or loss of each crude at each refinery cpb) M bpd

Refinery

X% -6 3 17 10 63 34 #15 22 —2 15 30

X2 -—11 -—7 —16 9 49 16 4 10 —8 8 40

Y | —7 3 16 13 60 25 12 19 4 13 50

z —-1 0 13 3 48 #15 7 i7 9 3 60

0 Oo 0 0 0 Oo 0 0 0 0 20 Not Used

Available
M bpd 30 06«30 20 20 10 20 20 10 30 10 200

Solution of Problem

Construct a basic feasible solution in the modified manner. Select the row and
column containing the greatest profit from the table (63 cpb) and place this row X;
and this column e as the first row and column of a new quantity table for the basic
feasible solution. 7

e Total
% 10 30
Total 10

Enter the totals of 30 for X1 and 10 for e. Place the smaller of these two numbers in
box X, e. Thus Crude ¢ is all assigned to refinery X1.

Since refinery Xj requires additional crude, select the next highest profit operation.
This is crude f with a profit of 34 cpb. The second column on the quantity table is f,
and all of crude f is assigned to refinery X,, satisfying its requirements.

## PDF page 75

A Crude Allocation Problem 65

. f Total

x | 10 | 20 a

Total 10 20

A new refinery and a new crude must be selected, again on the basis of greatest
profit. The profit table shows crude # at refinery Y to be the next best operation at
19 cpb. The desired information is placed in the quantity table as before.

2 f h Total
>< 10 20 30
Y 10 50

Total 10 20 10
Additional crude supply is selected for refinery Y on the basis of greatest profit,

namely, crudes c with 16 cpb and d with 13 cpb. This satisfies the crude requirement

at refinery Y.

e f h ro d Total
XI 10 20 30
Y 10 20 20 50

Total 10 20 10 20 20

## PDF page 76

66 Linear Programming: The Solution of Refinery Problems

A new refinery and a new crude must be selected. Crude j at refinery X» is the
next best operation, with a profit of 8 cpb. Crudes g and 6 with profits of 4 epb and
—7 cpb are next in order of preference for refinery X2.

C) f h ro d i g b Total
X 10 20 30
Y 10 20 20 : 50
Xa 10 20 10 40

Total 10 20 10 20 20 10 20 30

It will be noted that 20 M bpd of crude 6 is left unassigned until all the crudes
available for the next refinery are considered. The remaining refinery-is Z, and the re-
maining crudes in order of preference are i, b, and a with profits of 9, 0, and —1 cpb
respectively. These assignments are made, and the leftover crude is placed in row N.

e f h € d i g 6 i a Total
> 4) 10 20 30
Y 10 | 20 | 20 50
X2 10 20 10 40
z 20 30 10 60
N 20 20

Total 10 20 10 20 20 10 20 30 30 30 200

Since the total number of elements placed in the boxes is only 12 and the number
of elements required to apply the simplex method is n-+-m—1—10+5—1=14, it is
necessary to place 0 in two boxes. For best results, the selections should be made
on the basis of highest profit* and they must “connect” the groups e f and hc d and
ig bia, An inspection of the profit table shows that Ye and Xe satisfy these
requirements. The modified basic feasible solution is now complete.

*Where the profit is equal for two or more competing elements, a definite order of preference
must be established for all elements to be used in the calculations.

## PDF page 77

A Crude Allocation Problem

30°

67
e f hoe d i g b i a Total

Xy 10 20
Y 0 10 20 20 50
X2 0, 10 20 10 40
Zz 20 30 10 60
N 20 20
Total 10 20 10 20 20 10 20 30 30 30 200

tive C’y value should be introduced into the basis.

For convenience, the table of real profits is rearranged to conform with the basic
feasible solution.

e f h c d i g b i a

63 34 22 17 10 15 15 3 —2 —6

60 25 19 16 13 13 12 3 4 —7

49 16 10 |—16 9 8 4 |-7 —8 —i1

48 15 17 13 3 3 7 0 9 -1

0 0 0 0 0 0 0 0 0 ie]

The profit for the basic feasible solution is
e f h e d i g b r)

X 630+ 680 = 1310
Y + 190 + 320 + 260 = 770
X2 + 80 + 80 —70 90
Zz 0+ 270—10= 260
2430

Profit, = 2430(1000/100) = $24,300 per day

To determine whether this is a maximum profit feasible solution, it is necessary
to calculate the C’,, values (negative coefficients in the f(C) row of the simplex
matrix). Since it is desired to maximize the profit function f(C), any A,; with a posi-

Since there are 36 vacant boxes in this problem [(mn — m — n 4- 1) possible

## PDF page 78

68 Linear Programming: The Solution of Refinery Problems

Aj, values not in the basis], it is unnecessary to compute all of the C’,,. Actually the
C’, should be computed in turn until the first positive value appears, and then the
corresponding A,; should be substituted. New C’, can then be computed by con-
tinuing the same order of computation until no more substitution can be made with
increased profit. This procedure will save materially on the amount of computing
over the usual simplex procedure of choosing the largest C’,, for each substitution.
For this case

C’ x04 = Cxoa — Cya + Cy, — Cxne = 9 — 13-4 60 — 49 =7,

indicating that Xd should be introduced into the basis. Therefore, the quantity @
is inserted in the X24 position and the new case is balanced.

e f h € d i g h i a Total
Xi 10 20 30
Y 0+6 10 20 | 20~6 50
X2 er) 6} 10 20 10 40
z 20 30 10 60
N 20 20

Total 10 20 10 20 20 10 20 30 30 30 200

The value of @ is the smallest necessary to eliminate one of the existing elements,
This is 0, and element X,¢ = 0—0 is eliminated. The new feasible solution No, 2
becomes

e f h € da i 9g b i a Total
x 10 20 30
Y 0 10 20 20 50
X2 0 10 20 10 40
z 20 30 10 60
N 20 20

Total 10 20 10 20 20 10 20 30 30 30 200

## PDF page 79

A Crude Allocation Problem 69

The profit for feasible solution No. 2 is the same as for the basic feasible solution,
namely,

Profit, = $24,300 per day.
Continuing the search for positive C’,; reveals that
C’'yy = Cyn — Cray + Cros — Cra = 3-+749—13=6.

Therefore, Yb should be introduced into the basis.
The required adjustment is made by inserting 6 in box Yb and balancing the case,

e f h ry d i 9 b i a Total
X1 10 20 30
Y 0 10 20 | 20-6 6 50
Xo 0+¢ 10 20 10—¢ 40
z 20 | 30 | 10 60
N 20 20
Total 10 20 10 20 20 10 20 30 30 30 200

Feasible solution No. 3 becomes

e f h ¢ d i 9 b i a Total
xi 10 | 20 30
Y 0 10 20 10 10 50
X2 10 10 20 40
z 20 30 10 60
N 20 20
Totai 10 20 10 20 20 10 20 30 30 30 200

The profit for feasible solution No. 3 is

## PDF page 80

70

Linear Programming: The Solution of Refinery Problems

e f h c d i g b i
Xi 630 + 680
Y 0 + 190 + 320 + 130 + 30
X2 + 90+ 80+ 80
Zz

l

+0 +270—-10=

Profits = 2490(1000/100) == $24,900 per day

Continuing the search for positive C’,, reveals that

1310
. 670
250
260

2490

Claig = Cag — Crag + Cx2a— Cra + Cye — Care = 15-4 +9 — 13 +60 —63 = 4.

Therefore, X1¢ should be introduced into the basis, and @ is inserted in box Xyg.

e f h € d i g b i a
X, |10-6} 20 6
¥ 0+¢6 10 20 | 10-6 10
Xo 10+¢@; 10 | 20-9
Z 20 30 10
N 20
Total 10 20 10 20 20 10 20 30 30 30

Feasible solution No. 4 becomes

e f h c d i g b i a
Xi 0 20 10
Y 10 10 20 10
X2 20 10 10
z 20 30 10
N 20
Total 10 20 10 20 20 10 20 30 30 30

Total

30

50

40

60

20

200

Total

30

50

40

60

20

200

Note that 0 has been restored in box X,¢ since this is the highest profit element
which will connect the two groups of elements.

## PDF page 81

A Crude Allocation Problem 7
The profit for feasible solution No. 4 is
e f h © d i g b
% 0 + 680 + 150 830
Y 600 + 190 + 320 + 30 = 1140
Xz + 180+ 80+ 40 = 300
z + 0+270—10= 260
2530
Profit, = 2530(1000/100) = $25,300 per day
The next A,, to be introduced in the basis is X.h since
C’xon = Cron — Cray + Cry — Cyr, = 17-0413 —19= 1,
Therefore, 6 is inserted in box Zh.
e £ h E d i g b i ow Total
X 0 20 10 30
Y 10 10-6} 20 10+¢6 50
X2 20 | 10 | 10 40
Zz ti] 20—6}| 30 10 60
N 20 20
Total 10 20 10 20 20 10 20 30 30 30 200
Feasible solution No. 5 becomes
e f h c d i g b i a Total
xi o | 20 10 30
Y 10 20 20 50
Xa 20 10 10 40
Z 10 10 30 10 60
N 20 20
Total 10 20 10 20 20 10 20 30 30 30 200

## PDF page 82

72

Linear Programming: The Solution of Refinery Problems

The profit for feasible solution No. 5 is

x
y
X2
Zz

0 + 680

600

f

h

+ 170

¢

+ 320

d

g
+ 150

+ 180+ 80+ 40

+ 60

+ 0+ 270—10

Profit; = 2540(1000/100) = $25,400 per day

Wo

830
980
300
430

2540

The search for positive C’,, at this time requires the calculation of all 36 values,
since no positive values can be found. This is therefore an optimal solution. However,
there are two C’,, values which are zero, namely,

C'vg = Cyyg — Cx + Cre — Cre = 12 — 15 + 63 — 60=0

and

Cre = Cae — Can + Cry —Cye = 13 — 04+ 3—16=—0
The substitution of Yg or Ze will result in different but equally profitable solutions
known as alternate optima. These alternate solutions are shown as follows:

alternate solution No. 5A

x

X2

Total

e f h © d i g b i a Total
10 20 30
0 20 10 20 50
20 10 10 40

10 10 30 10 60

20 20

10 20 10 20 20 10 20 30 30 30 200

## PDF page 83

A Crude Allocation Problem

73

and alternate solution No. 5B...
e f h € d i g b i a Total
xX 0 20 10 30
Y 10 10 30 50
Xo 20 10 10 40
Z 10 | 10 30 | 10 60
N 20 20
Total 10 20 10 20 20 10 20 30 30 30 200

Any combination of these solutions would also be at maximal profit; for example, an
equal mixture of all three solutions would be:

e f h c d i g b i a Total
Xi 3 20 7 30
Y 7 i7 3 23 50
X2 20 10 10 40
z 10 3 7 30 10 60
N 20 20
Total 10 20 10 20 10 20 30 30 30 200

20

The selection of the optimal crude allocation, in this case, can be made with some
fiexibility, possibly to improve some other criterion such as service or good will.
The profit will remain at $25,400 per day with any optimal solution,

## PDF page 84

74 Linear Programming: The Solution of Refinery Problems

REFERENCES

(1) George B. Dantzig, Chapter XXI of *Activity Analysis of Production and
Allocation* (T. C. Koopmans, ed.), Cowles Commission for Research in
Economics Monograph No. 13. New York, John Wiley & Sons, Inc., 1951.

(2) A. Charnes, W. W. Cooper, and A. Henderson, *An Introduction to Linear
Programming*. New York, John Wiley & Sons, Inc., 1953.

(3) Robert Dorfman, Chapter XXII of *Activity Analysis of Production and
Allocation*.

(4) Thomas A. Elkins, “An Application of the Theory of Games to Geophysical
Exploration,” unpublished paper. Pittsburgh, Carnegie Institute of Technology,
1953.

(5) George B. Dantzig, Chapter XXIII of *Activity Analysis of Production and
Allocation*.

(6) A. Charnes, W. W. Cooper, and B. Mellon, “A Model for Programming and
Sensitivity Analysis in an Integrated Oil Company,” *Econometrica*, April 1954.

(7) A. Charnes, W. W. Cooper, and B. Mellon, “Blending Aviation Gasolines,”
*Econometrica*, April 1952.

(8) D. Gale, H. W. Kuhn, and A. W. Tucker, Chapter XIX of *Activity Analysis
of Production and Allocation*.

(9) George B. Dantzig, Chapter XX of *Activity Analysis of Production and
Allocation*.

(10) A. W. Tucker, “Linear Programming,” *Proceedings*, Annual Convention of
American Society for Quality Control, May 1953.

(11) J. C. C. McKinsey, *Introduction to the Theory of Games*. New York,
McGraw-Hill Book Company, Inc., 1952.

(12) A. Charnes, “Set-Theoretic Methods in Economic Analysis,” unpublished
lecture notes, Pittsburgh, Carnegie Institute of Technology.

(13) A. Charnes and W. W. Cooper, “The Stepping-Stone Method of Explaining
Linear Programming Calculations in Transportation Problems,” *Management
Science*, October 1954.

(14) A. Henderson and Robert Schlaifer, “Mathematical Programming,” *Harvard
Business Review*, May-June 1954.

## PDF page 85

*[Blank page]*

## PDF page 86

DATE DUE

30 505 JOSTEN’S
'

## PDF page 87

Esso Standard Oil Company

HD 9560.5
.E5

Linear programming: the solution of refinery problems.

DATE | ISSUED TO
--- | ---
 |
 |
 |
 |

HD 9560.5
.E5

## PDF page 88

Linear programming
HD 9560.5 .E5
E 5033 0020 3487 3

*W6-CQC-237*
