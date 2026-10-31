# OCR transcription

> Transcribed from the scanned pages of [1952-charnes.pdf](1952-charnes.pdf). Page breaks are marked below. OCR preserves the text as recognized; original typography, tables, and mathematical notation may not be represented exactly.

## Printed page 135

ECONOMETRICA

VOLUME 20 APRIL, 1952 NUMBER 2

BLENDING AVIATION GASOLINES—A STUDY IN
PROGRAMMING INTERDEPENDENT ACTIVITIES IN AN
INTEGRATED OIL COMPANY¹

By A. CHARNES, W. W. COOPER, AND B. MELLON
SUMMARY

THE TECHNIQUES of linear programming are here explained in a
commercial application—blending aviation gasolines. Blending is crit-
ically important to almost all other areas of programming in an inte-
grated oil company. Intelligent programming of production, transporta-
tion, manufacturing, or marketing generally requires solution of blending
problems as an initial or integral part of the whole process for it is in
blending that the final outputs are determined.

In the first part of the paper, questions of optimum programming in a
given technological and institutional structure are explored. Computa-
tions are executed primarily by means of the simplex technique of
Dantzig [4]. Because of the presence of multiple degeneracy and the
absence of a general method (at the time these computations were made)’
of handling such problems, it was not possible to rest securely on the
simplex method. Alternative methods of computation were, therefore,
explored and bounding techniques were employed to discover possible
divergences from optimality. Finally, to test the validity of the results,
calculations undertaken by a company programming official were ob-
tained for purposes of check and comparison.

A relatively simple program is first calculated and more than one
optimal program obtained. These results are then extended to more
complex problems. Finally, the sensitivity of the matrix to possible
changes in the coefficients is studied.

The problem of linear programming may be stated as follows: A

1 This study is a modified version of 2 paper presented at the Conference on
Linear Inequalities (1951) sponsored jointly by the U.S. Department of the Air
Forces and National Bureau of Standards. The research for this paper was par-
tially supported by grants from the U.S. Department of the Air Forces to the
Carnegie Institute of Technology, to the School of Industrial Administration
for research in intrafirm behavior, and to the Department of Mathematics for
research in applied mathematics. Grateful acknowledgment is made to Mr. Carl
Lemke who supervised the computations and to Mr. T. Sainsbury and Mr. T. T.
Kwo who assisted him. Professor David Rosenblatt made numerous helpful
suggestions.

2 Shortly after this study was completed, Charnes [1] developed a general
method for handling degeneracy.

135

## Printed page 136

136 A. CHARNES, W. W. COOPER AND B. MELLON

set of m equations in n unknowns is specified. This may be written in the
form pee iP; = Po, where the P; and Po represent column vectors,
each with m components. The problem then is to find a set of A; 2 0
which satisfies these equations and which maximizes a linear functional
fay) = hs \,.c;. The c; may correspond to any set of relevant cri-
teria but, by the nature of the problem here, they are restricted to
prices of outputs or products.

The sensitivity problem revolves around variation in the components
of the P; . The results of these variations may be studied in terms either
of consequent variation in physical program composition (via the new
activity levels so obtained) or of consequent variation in the value of
the functional, or both. Because of the explicit relevance of profits to
business activity, attention is here centered on the changes in profit
position resulting from such structural variation. Finally, the possible
consequences of variation in the vector Po (which corresponds to levels
of expected inputs) and the prices c; are also discussed. Changes in
coefficients of the matrix correspond to changes in the technology.
Hence, the effects of programs of applied research may be examined in
terms of the relative profitability of the improvements which the re-
search proposes to effect.

INTRODUCTION

The purpose of this paper is to investigate applications of linear
programming and related techniques to planning problems in business
enterprise, to obtain comparisons with current commercial practice,
and to explore possible extensions and simplifications of linear pro-
gramming techniques. This study, it should be borne in mind, is oriented
toward planning or programming rather than execution of operations.
It is oriented toward the type of activity undertaken by a central office
planning group such as a budgetary committee. No attempt is made to
introduce such phenomena as “‘initial” or “boundary” conditions,
feedback reporting design and interpretation, and agent behavior and
control phenomena of the type which would have to be considered at
the operating level, as distinct from the programming level.’ These
problems have been reserved for separate study. At the outset, the
indebtedness that all workers in this field owe to T. C. Koopmans,
George Dantzig, Marshall Wood, and Wassily Leontief [6, 7] should
be acknowledged.

Programming inputs and outputs in an oil refinery was selected for
study because it was possible to obtain the necessary coefficients with-
out undertaking large-scale empirical surveys. The advanced stage of
chemical work and developed standards of classification in petroleum

> For a more detailed discussion of points of difference between programming
and execution, see Cooper [3].

## Printed page 137

BLENDING AVIATION GASOLINES 137

refining make it possible to avoid difficult problems of aggregation,
which are present in may other types of industrial processes.

To avoid the necessity of employing high speed electronic computing
equipment, which was not available for this work, no attempt was made
to study programming for an entire refinery. Only one process—blending
aviation gasolines—was studied. This restriction of the area of study
added the further convenience of avoiding problems of storing, lead
times, make-ready times, etc., which would be encountered in a large
study. In short, the problem was restricted to the flow of components
in the blending process.

Blending, rather than other phases of refinery operations, was se-
lected for study because (a) it represents an important distinct phase
of such operations and hence of programming, and (b) it has essential
characteristics that make it typical not only of refining problems, but
of chemical manufacture in general. Pressure, volume conditions, and
even the action of catalytic agents are present in this problem with the
usual complex interactions between physical, chemical, economic, tech-
nological, and managerial considerations. The model though simplified
has thus a real and important counterpart for a wide range of problems
in physical operations and business planning. These criteria—operational
significance and importance—have been borne in mind in the choice of
simplifying assumptions in the model constructed for use in this study.

ELEMENTS OF THE PROBLEM—TECHNOLOGICAL BACKGROUND

Only material costs and quantities were considered. Capital, labor,
and other elements of cost were omitted. Given the refinery and blend-
ing equipment, such costs are not variable.’ Labor costs are largely fixed
by the refinery operations as a whole, the blending activity having only
an insignificant effect on these costs. The same is true of overhead and
related costs.

A few words should be said to clarify terminology and to explain some
of the considerations involved in blending. As is well-known, when crude
oil is refined various products may be formed, such as gasoline, kerosene,
distillate fuels, light and heavy lubricating oils, tar, etc. The exact
proportions of each product depend not only on the characteristics of
the crude oil and the design of the refinery but upon the methods em-
ployed as well. Variations in temperature and pressure, introduction of

4A possible exception would be selling and distribution costs which are not
relevant to refinery operations. It should be noted that, apart from decisions to
close down major units of the refinery, labor requirements are rather rigidly
fixed by technological characteristics. Even with major shutdowns, relatively
large groups of skilled labor must often be employed since technology and capital
considerations make it inadvisable to depend on ready availability of such labor
jn the free market.

## Printed page 138

138 A. CHARNES, W. W. COOPER AND B. MELLON

chemical agents or catalysts, and numerous other devices may be em-
ployed to effect these proportions.

Not all gasolines, even when produced from the same crude stock,
are of uniform quality. The properties may be changed or adjusted by
blending different gasolines in suitable porportions and subjecting them
to chemical treatment. Aviation gasolines are blended from carefully
selected straight-run gasolines, catalytically cracked gasolines, and spe-
cial components synthesized from other refinery products. With the
addition of appropriate amounts of tetraethyl lead (TEL) and other
chemicals and dyes, the final products—aviation gasolines—are blended.

Of course, not all components that are usable in producing aviation
gasolines will be devoted exclusively and exhaustively to that purpose.
Economic, technological (e.g., storage limitations), and other considera-
tions may make it desirable to divert some of these components to
production of other products. For this study, all components not com-
pletely consumed in the production of aviation gasolines are assumed to
be blended into premium automotive gasoline.

This simplifying assumption is not far removed from realities of the
current situation. Aviation stocks can technologically be used in pro-
ducing automotive fuels and under current demand conditions, such
diversions would prove economical. It should be realized, however, that
the process of diversion to other final products can be continued to
further lengths, that materials not used to produce premium automotive
gasoline can be absorbed in the production of regular grade automotive
gasoline and sold directly to other refiners as stocks, etc.’ It should be
further noted that it is also assumed that the increment over scheduled
production of automotive gasolines resulting from diversion of com-
ponents in the avaition blending program would not be sufficiently
large to have an adverse effect on price or other marketing and distribu-
tion considerations for such fuels. This assumption is justified by the
relative magnitude of the figures for the various programs. Even if this
had not proved to be the case, it would have been possible to extend
the calculations without fundamentally affecting the principles involved.

Given the properties of the components, the blending operation must
be directed in a manner to insure that certain quality specifications are

‘Fortunately, company policy and the requirements of simple profit maxi-
mization coincided at the time of this study. Premium automotive fuels repre-
sent the next highest priced product line to aviation grades. Company policy on
this point pivots about grades of gasoline which have to be purchased from other
producers in order to ‘‘balance”’ its own programs. Premium grades at the time
of this study were being purchased from other companies. If lower priced ‘‘regu-
lar’? or “house grades’’ were being purchased instead, company policy would
have required their substitution for premium automotive fuels in order to deter-
mine the relative desirability of diversion of ‘‘stocks’”’ from the aviation program.

## Printed page 139

BLENDING AVIATION GASOLINES 139

satisfied. Of these specifications, the two most important are ignition
properties, as measured by octane ratings or performance numbers, and
volatility as measured by Reid Vapor Pressure. These two specifications
usually govern blending considerations within ordinary ranges of opera-
tion, although other considerations may become dominant under less
usual conditions.

Reid Vapor Pressure, (RVP), is determined by standard specific
trials with given gauges and containers under stipulated temperature
conditions. Higher than permitted pressures are undesirable, and even
dangerous in aviation gasolines, because of the tendency to boil and
produce vapor lock under high temperature and altitude operating
conditions. Indeed, for considerations of maximum operating efficiency,
airplane fuel systems are specifically designed to operate with fuels of
maximum RVP of 7.0 Ibs./sq. in. Generally, it is prudent to blend for
a maximum RVYP of 6.9 lbs./sq. in., and the blending coefficients used in
this study are based on this assumption.

Aircraft engines are generally designed to operate satisfactorily pro-
vided the fuels used meet minimal octane or ‘‘antiknock”’ requirements.
“Knocking” in aircraft engines is a more serious matter than in automo-
bile engines. Unless these minimal octane requirements are met, the
engine will not perform satisfactorily and destruction or damage to the
engine may result. On the other hand, use of excessively high octane
rated fuels results in greater expense with no comparable benefit in
operating performance.

Closely related to octane ratings are performance numbers (PN),
generally specified on aviation gasoline contracts.° Two important con-
siderations in the properties of a fuel for aircraft operations are (1)
full power for takeoff and (2) maximum mileage per gallon under normal
cruising conditions. Best performance on takeoff is attained with a
“rich mixture” or high fuel/air ratio; maximum fuel economy, 1.e.,
condition (2), is attained with a “lean mixture” or low fuel/air ratio.

Standard methods of testing have been devised for measuring these

* Octane ratings represent a method of objectively and quantitatively deter-
mining antiknock properties. The octane number or rating is defined as the per
cent of iso-octune in an iso-octane normal-heptane mixture which has the same
knock rating as the gasoline being rated in the test engine. The greater the per
cent of iso-octane, the higher the octane number and the greater the antiknock
properties of the gasoline.

Concomitant with the evolution of modern aircraft design, it became essential
to develop gasolines with higher antiknock ratings than 100 per cent iso-octane.
Consequently a new rating scale, the so-called PN scale, was developed to indi-
eate Maximum-potential-performance level of the fuel. There is a unique cor-
respondence between octane rating and PN up to 100 octane; beyond this level
PN is determined, relative to the amount of TEL which must be added to iso-
octane, to achieve the same antiknock rating as the fuel being tested.

## Printed page 140

140 A. CHARNES, W. W. COOPER AND B. MELLON

fuel properties by means of appropriately designed single cylinder
engines which are operated under carefully specified conditions. The
first, or rich mixture PN, is rated by what is known as the 3-c test;
the second, or lean mixture PN, is rated by what is known as the l-c
test.

This study was conducted in two stages: First, program calculations
were made on the assumption that only the 1-c PN was specified;
second, both l-c and 3-c specifications were simultaneously imposed.
By this means it was possible both to simplify the initial calculations
and facilitate insight into the character of the problem. It was decided
to study the problem in this particular sequence for other reasons as
well. Prior to World War II, it was common practice to specify only
the 1-c quality restriction. Hence, it was possible, also, by this means,
to conform to the historical sequence of practice and to obtain estimates
of the economic cost of the additional quality restriction.

As was previously noted, properties of the final products can be al-
tered not only by blending gasolines but also by chemical treatment,
e.g., by the addition of TEL (tetraethyl lead). The blending indexes for
Reid Vapor Pressures are independent of the grades of gasoline, but the
octane and performance number blending indexes are functions of the
amount of TEL in the product. Hence, there can be more than one
blending index for any component. In general, the greater the amount
of TEL the higher the blending index—in economic terms, the tech-
nological coefficients are increased by application of this factor. Given
the structure of relative factor prices used,’ it would be advantageous
to apply more of the factor TEL in order to increase yields from the
given stocks. But because of undesirable properties, including the poi-
sonous character of unduly high concentrations of TEL, maximum
limits are imposed on its use either by specification or by law.* In this
study, the maximum amount of TEL permitted was assumed to be
employed. This makes the problem conform not only to the usual as-
sumptions of profit maximization but to general practice in the industry
as well.

7 Estimates of market prices of TEL as of March, 1950, were employed in the
study, although these were not necessarily the prices paid by the company on
firm, or open-end contract amounts.

8 Higher amounts of TEL may be used in military gasolines than in civilian
gasolines. In civilian aviation gasolines maximum permitted TEL is 4.0 ce/gal.;
military aviation gasolines permit a maximum of 4.6 cc/gal. The effect of the
additional TEL permitted is to add two additional grades of product with four
additional blending coefficients. The problem considered was restricted to civil-
ian gasoline in order to reduce the number of computations. Numerical magni-
tudes of the results are, therefore, affected but not the basic techniques or
principles.

## Printed page 141

BLENDING AVIATION GASOLINES 141

The complete list of products entering into actual company program-
ming as well as maximum RVP, ignition qualities (in terms of PN), and
TEL assumptions are given in Table I. Of these products, the first three
aviation grades indicated by parentheses along with premium automo-
tive fuels were selected for study. The last three, or military grades,
were eliminated from study. With appropriate computational equip-
ment it is, of course, easily possible to extend the calculations for pro-
gramming all categories.

Similar simplifications were introduced for the components. A tabula-
tion of the components used in this study, along with relevant chemical
and physical properties, is displayed in Table II. From this list the
items denoted by parentheses were selected for study.

TABLE I—List or Propvucrts

Gasolines Specifications
Symbols — =e ni ae i
Usedin | Aviation Grade | Maximum | Minimum | Minipym | rma
M 80 L (7.0) (80.0) tics) (0.5)®
N 91 C (7.0) (91.0) (96) (4.0)
Q 100 C (7.0) (100.0) (130) (4.0)
91 M 7.0 91.0 96 4.6
100 M 7.0 100.0 130 4.6
115/145 7.0 115.0 145 4.6
Z Premium motor s a | @ 3.0

* No bearing on computations since premium motor fuel is to be blended to specification with other
com ponents.

5 80 L is a result of mobilization changes to conserve aviation components. Normally an 80 octane
aviation gasoline does not contain TEL.

MATHEMATICAL STATEMENT OF THE PROBLEM

With this background, it is now possible to proceed with a mathe-
matical statement of the problem. As noted in the summary at the
outset of this paper, the linear programming problem requires specifica-
tion of a set of m equations in n unknowns. In equivalent vector form
this may be written >°2.,\.P; = Po where the P; and Py represent
column vectors, each with m components. It is required to find a set
of \; 2 0 that satisfies these equations and simultaneously maximizes a
linear functional f(A;) = gat AiC; -

Tables I and II supply the necessary information for mathematical
formulation of the problem. Each of the aviation gasolines, M, N, and
Q, have stipulated minimal PN and maximal RVP ratings. Each of
the inputs, A, B, D, and F, have certain technological ratings relative to

## Printed page 142

142 A. CHARNES, W. W. COOPER AND B. MELLON

TABLE II—Aviation Gasouine Stocks

Blending Indexes
Symbols
ued Component RVP PN — l-o 3-c
i lp 7045 4.0 4.6 4.0 4.6
A Alkylate I (5.0) (94.0) (07. 5) | 108.0 | (148.0) | 151.0
B Catalytic gas-| (8.0) (83.0) (93.0) | 93.3 | (106.0) | 110.0
oline A
D Straight-run (4.0) (74.0) (87.0) | 88.8 | (80.0) | 84.0
gasoline mix
A
Straight-run 5.9 77.0 89.0 91.0 95.0 99.0
gasoline mix
B
Outside iso- 9.2 85.0 97.7 98.3 | 112.1 | 115.1
mers
Catalytic gas- 8.8 a Lae Las 92.0 | 108.0
oline B
Alkylate IT 4.8 -_ a 106.0 _ 149.0
Toluene 1.0 ee — 102.0 ais 230.0
r | Isopentane | (20.8) (95.0) | (108.0) ee (140.0) ite 4

® Two blending indexes available

these outputs for stipulated amounts of TEL. This information may be
utilized to form the following set of inequations:

94.0\n + 83.0A2 + 74.0013 + 95.0Au > 80M
5.0\n + 8.0\2 + 4.0013 + 20.5\4 < 6.9M
(1) 107.5da1 + 93.0Ae + 87.0r23 + 108.0r\% > 91N
5.0r\n + 8.02 + 4.03 + 20.5r\u < 6.9N
107.5ds1 + 93.032 + 87.0Az0 + 108.0A% > 100Q
5.0r\n + 8.02 + 4.0% + 20.5ru < 6.99

where, by definition

I

Mo = Xn + Awe + Ais + Aa
(1a) N = Yar + Aaa + Avs + Aaa
Q = dar + Ase + Ass + Aza

The convention to be followed is that the first subscript on the ’s
refers to the output and the second to the input. Thus, the first output,
M in (la), is composed of the four inputs \;;, 7 = 1, 2, 3, 4, where the

## Printed page 143

BLENDING AVIATION GASOLINES 143

second subscripts refer successively to the bracketed items in Table IT;
that is, the inputs, A, B, D, and F which go into the makeup of M.
(Some of the A,;; may, of course, be zero.) The inequations refer by pairs
to each of the aviation grade gasolines specifying PN and RVP proper-
ties, respectively. Referring to M, for example, the first two inequations
stipulate that M shall have an octane (PN) rating of at least 80 and
vapor pressure (RVP) of not more than 6.9 Ibs./sq. inch. Although the
terms on the right-hand side can be viewed as components of the re-
quirements of vector, Po, it is better first to reduce the set (1) to equa-
tions by introducing additional nonnegative quantities, appropriately
defined. This will be done at a later stage.

Associated with each of the variables ;; in (1) is a vector with com-
ponents representing elements in the given structure. Reference to
Table III may serve to make the meaning of this statement clear. Under
the column headed Py are structural components representing the
properties of alkylate going into the makeup of M. Per unit used, the
former contributes 94.0 units, 94 — 80 = 14 units in excess of minimal]
requirements, to the latter’s PN rating (at the specified TEL level).
Alkylate contributes 5.0 units, or 6.9 — 5.0 = 1.9 units below maximum
permitted RVP of M. The technological properties of alkylate relative
to M are independent of its properties relative to N or Q in terms of
the given structure as indicated by the zeros (represented by blanks in
the matrix) for the succeeding four rows of P,,. In short, the outputs
are tied together only through the policy restrictions on availability
(shortly to be discussed) indicated in the last four rows of Table ITI.

To construct the program matrix, it is first desirable to simplify the
set of inequations (1). Before doing so, however, it will be well to state
the policy restrictions in mathematical form. As a result of company
policies and programming in other parts of the refinery, the various
inputs are expected to flow into the storage tanks at certain average
rates, in barrels per calender day. To eliminate the need for construct-
ing additional storage capacity it is desired that these ‘“‘stocks” or in-
puts be consumed, on the average, at exactly these rates. Stated in
mathematical form, this policy restriction becomes:

A = An + Aa + An + An = 3800
B = daz + Azz + Ase + Awe = 2652

D = Xs + Avs + Ass + Ags = 4081

where the \y;, 7 = 1, 2, 3, 4, are the amounts of A, B, D, and F not
employed in making M, N, or Q. These values may be regarded as in-
puts to a new product, Z, which is subject to no technological restric-

(1b)

## Printed page 144

144 A. CHARNES, W. W. COOPER AND B. MELLON

tions in the aviation program. Z is, of course, premium automotive
fuel.

The total daily inflows amount, on the average, to 11,833 barrels per
calendar day as indicated by the numbers on the right-hand side of
(1b), which enter as components in the vector Py (see Table III). Stated
in this form, company policy is seen to be equivalent to treating these
inputs as fixed factors.’ The price of these inputs is, therefore, irrelevant
to programming calculations. Their valuation (like the valuation of
any fixed factor under strict definition of alternative costs) proceeds
entirely from the receipts side in terms of possible alternative employ-
ments.”

Upon combining and simplifying, the relations specified in (1),
(la), and (1b) become:

144 An +3 Awvn— 6 Agt15 Ay 20
1.9Au — 1.12 + 2.913 — 13.6A4 2 0
16.5r2 +2 Aw— 4 Awst17 Ay 20
1.921 — 1.1dA2 + 2.9A23 — 13.6rA% 2 0
7.5 — 7 Ag — 13 Ag+ 8 Au 2 O
1.9As — 1.1Ag2 + 2.9A33 — 13.6Au 2 0

(2)
Au + Aa ++ Ast + Au. = 3800

Au + Azo + Ase + Ae = 2652
Au + No + Au + Aa 1300

Reference to the right-hand side of (1) reveals that the coefficients
of the three aviation grades represent the minimal PN (octane) ratings
and maximal RVP ratings that each of the aviation grades M, N, and
Q is required to meet. As previously noted (see Table I and accompany-
ing discussion), ! must rate at least 80, N at least 91, and Q at least
100 on the PN scale for the 1l-c test. Of course, statement of these

* This was not immediately apparent to various company officials with whom
the problem was discussed. It was their feeling that, in any event, it was better
to avoid the need for additional storage capacity, probably because such capacity
problems would have to be dealt with under company procedure outside the
normal routine of programming calculations.

10 One such alternative would be possible diversion to premium automotive
fuel. It should be clear that restatement of (1b) as inequations would set either
(a) minimum levels of (fixed) costs or (b) upper limits to variable costs, depend-
ing on which way the inequality signs were turned.

## Printed page 145

BLENDING AVIATION GASOLINES 145

conditions in the form of inequalities permits overfulfillment of require-
ments if profits can be increased in that manner. That is, M, for exam-
ple, may be produced with a final PN in excess of 80. So long as it re-
mains below 91, it will not bring a higher price. Nevertheless, it may
prove more profitable (as will later be shown) to overfulfill than to meet
requirements exactly. Imposing the condition that requirements must
be met exactly would, of course, necessitate restatement of (1) in the
form of a set of equations, replacing the inequality signs by equality
signs.”

The first six inequations in (2) may be reduced to a set of equivalent
equations by introducing an appropriate set of new nonnegafive un-
knowns, 1e., Ar, Az, A3, Ag, As, and A, on the right-hand side. The subscript
in each of these unknowns refers to the number of the inequation in
which it is to be introduced. In the terminology of the Air Forces, the
\’s so introduced are referred to as pseudo variables [8].

Corresponding to each of these pseudo variables is an “artificial
activity,” P:, P2, Ps, Ps, Ps, and Ps with components as listed under
the headings in Table III. While meaning need not always be attached
to these ‘‘artificial activities,” (i.e., they may be introduced only for the
purpose of facilitating computations), they have in this problem a
definite physical meaning. Here a nonzero value for any of the pseudo
variables represents an overfulfillment of requirements (extra octane
or reduced RVP) in the product to which it refers. (See infra, the notes
under Table VIII).

Upon executing the indicated operation, the relations (2) become

1.9rn — 1.1Ai2 + 2-9A13 — 13.6Au — Az = 0

11 Such restatement may also introduce contradictory conditions. The pro-
gram is then said to be infeasible. Such indeed proves to be the case when exact
requirements are imposed on the full 1-c and 3-c programs. The reasons for this
are evident. It will be recalled that the 1-c and 3-c tests refer to cruising and
take-off properties of the same gasoline. Thus, for Q with PN’s of 100 and 130,
respectively, the l-c test may yield a value below 100 and the 3-c test may yield
a value above 130. Attempts to alter one of the ratings will, in general, drive
the other in the same direction. Much attention apparently centers on this prob-
lem, referred to as ‘“‘giving away octanes,’”’ in the manufacturing division. In
conversations with company officials it was admitted that such double require-
ments on a single product might be impossible to fulfill exactly. Company offi-
cials stated that in such cases they preferred to overblend on the ‘‘low’’ in order
to meet the “high” exactly. But in actual calculations (for the problems dis-
cussed in this paper) it was noted that the programming officer overblended on
both the low and the high.

## Printed page 146

146 A. CHARNES, W. W. COOPER AND B. MELLON

(3)
Aun + An + Aa + At = 3800
Aw + Ae + Ase + Aaa = 2652
Ait = Aw + Ass + Nas = 4081
Au + Az + As + Aus = 1300

This set of 10 equations in 22 unknowns represents the basic set of
technological and policy restrictions.” A feasible solution (or program)
must provide a set of nonnegative values which will simultaneously
satisfy all of these relations.

The problem is to maximize the net receipts function subject to these
restrictions. Such a function is formed by introducing the appropriate
set of prices for each of the outputs M, N, Q, and Z; thus defining a
receipts functional

(4) R = 4.96M + 5.846N + 6.451Q + 4.830Z
— 0.05177M —0.409416(N + Q) — 0.281862Z

where the positive coefficients represent dollars-per-barrel, receipts,”
and the negative coefficients correspond to the cost of TEL at maxi-
mum permitted concentration.”

Since premium automotive fuel enters only as a residual in the avia-
tion program,

12 Without the simplifying assumptions—elimination of military aviation
gasolines and the 3-c test—the system would have yielded 22 equations in 62
unknowns.

18 Tt may be worth noting that the “‘prices’’ used in the receipts functional
are not necessarily market prices. They represent a mixture of quotations, mar-
ket prices, and internal prices which have been adjusted to preserve company
confidentiality.

4 It will be recalled that the blending coefficients were set on the assumption
that maximum-permitted TEL would be used. Although by alteration of blend-
ing proportions, the amount of TEL could be reduced and quality restrictions
still satisfied, the increased introduction of TEL represents the cheapest method
of securing the results. (Of course, alteration of the amount of TEL would
change the blending coefficients). Hence, TEL, which the operating officials are
free to vary within specification limits, represents a variable cost as determined
by the amount used and price. In economic terms it is the ‘‘cost of maintaining
the plant at the legally permitted optimum level.’’ In budgetary control terms,
the increased cost of using alternative methods of satisfying requirements repre-
sents a penalty for not utilizing the best methods available.

## Printed page 147

BLENDING AVIATION GASOLINES 147

(5) Z = 11,838 — M— WN — Q.
Inserting this expression, (4) becomes
(6) R = 0.36M + 0.889N + 1.4940 + 53,818.

In this form the equation of net receipts’ is stated in incremental
value terms, relative to the price per barrel of Z. The constant, $53,818,
then represents the minimum level of receipts obtained by diverting
all components to the next best alternative, the production of Z. This
level of receipts must be attained if it is worth (on an alternative cost
basis) producing any gasoline at all of aviation grade under the stipu-
lated restrictions. Clearly, this functional will be a maximum if

(7) z = 0.36M + 0.889N + 1.4940

is a maximum. For the program calculations, therefore, only this last
expression, (7), need be used.

Thus the problem is to maximize the linear functional, z , as given
in (7), subject to the side conditions (3). Since only nonnegative solu-
tions are admissible, the solutions must satisfy the additional restric-
tions.

where the terms with double subscripts represent the level of “real
activities” and the terms with single subscripts the level of ‘‘artificial
activities,” respectively.” Thus, all solutions must lie within the posi-
tive orthant.’’ The 22 conditions (8) plus the 10 conditions (3) and

(8)

15 The functionals used here are not identical with net profits but may be
made so by subtraction of the total fixed costs as defined by the accounting
process. These costs are omitted because they do not affect the composition of
the program.

16 The following definitions adopted from [8] will prove useful in succeeding
discussion: (1) Model—a set of simultaneous equations or inequations which
describe the interrelationships within an operation. (2) Activity—a subdivision
of an operation identified by principal output and a particular combination of
input factors. (3) Item—a good or service, or an aggregate thereof, produced by
or required for the performance of an activity. (4) Level of activity—the rate
of production of the principal output item of an activity per unit time period.
(5) Artificial activity—an activity having no exact counterpart in reality, which
is introduced into the formulation as a deliberate construct for conceptual or
computational convenience. (6) Plan—a schedule of required outputs or activity
levels for a specified set of items which are taken as the objective of an operation.
(7) Program—a combined schedule of the levels of all activities and of the inputs
and outputs of all items involved in an operation.

17 Geometrically the solutions thus form a convex polyhedron, i.e., a convex
set with a finite number of ‘‘corners.’’ See Charnes [1].

## Printed page 148

148 A. CHARNES, W. W. COOPER AND B. MELLON

the statement of the linear form (7), which is to be maximized subject
to these conditions, constitute the complete model for solution of the
1-c specification problem.

COMPUTATIONAL PROCEDURE

To facilitate systematic computations, it is well to array the coeffi-
cients of the ten equations and twenty-two unknowns (3) in matrix
form, as shown in Table III, where Po is the vector whose components
represent the requirements specified on the right-hand side of the equa-
tion (3).

If suitable computation machinery were at hand to provide solutions
for a system of ten equations in ten unknowns,” then a certain set of
solutions could be obtained in terms of which every solution could be
expressed as a per cent combination. Among this set would be the solu-
tions which maximize 2 ; of course, there may be more than one such
maximal set. In the absence of such computational facilities, recourse
was had to the simplex method of Dantzig [4] and the elimination
method of Dines [5].

The elimination method is impracticable for the system in toto be-
cause of (1) the size of the system of inequalities and (2) the difficulty
of determining the distinguished set of solutions from the various pos-
sible solutions provided by the elimination process.” In the simplex

18 For the “complete program” involving both the 1-c and 3-c tests and mili-
tary aviation gasolines as well, solutions for twenty-two equations in twenty-
two unknowns would be required.

19 The title “elimination method”’ is used here because of certain natural
analogies with the usual process of elimination of variables in solving sets of
algebraic equations. Suppose the system of inequalities is written in the form:

Des a,j7; + by = 0 (@ = 1,2, --+ , m).
If the coefficient of z; is positive for, say, 7 = 1, --- , tp and negative for, say,
t = tp41,°** , m, then by multiplying one of the ‘‘positive’’ inequations by

minus the coefficient of z; in a ‘‘negative’’ inequation, and similarly multiplying
the ‘‘negative’’ inequation by the coefficient of z; in the ‘‘positive’’ inequation,
and adding the two inequations so formed, the variable z; would be eliminated
from that pair.

The total number of new inequations that could be formed in this manner
would be equal to the number of ‘“‘positive’’ times the number of ‘‘negative’”’
inequations. It is necessary to form all of these possible new inequations at each
stage in order to retain a system equivalent to the initial one. Thus, starting
with m inequations, as many as (m?/4) inequations may result at the second
stage, (m*/16) at the third stage, and so on. (In practice, this maximum rate of
increase is not generally attained).

At the end of this process a system of k unknowns remains (if the J-rank of
the matrix, determined by the existence of a column of coefficients all of the
same sign, is k > 0) and & — 1 of the variables may be assigned values at pleas-
ure. (Moreover, an J-rank, k > 0, is a necessary and sufficient condition for the

## Printed page 149

TABLE III—PROGRAM MATRIX, 1-c TEST

The columns are grouped by output as \(M\), \(N\), \(Q\), \(Z\), and artificial
activities. The ten entries shown for each column are the coefficients in
rows 1–10, in order. \(P_0\) is the requirements column.

| Column | Rows 1–10 |
|---|---|
| \(P_{11}\) | \(14,\ 1.9,\ 0,\ 0,\ 0,\ 0,\ 1,\ 0,\ 0,\ 0\) |
| \(P_{12}\) | \(3,\ -1.1,\ 0,\ 0,\ 0,\ 0,\ 0,\ 1,\ 0,\ 0\) |
| \(P_{13}\) | \(-6,\ 2.9,\ 0,\ 0,\ 0,\ 0,\ 0,\ 0,\ 1,\ 0\) |
| \(P_{14}\) | \(15,\ -13.6,\ 0,\ 0,\ 0,\ 0,\ 0,\ 0,\ 0,\ 1\) |
| \(P_{21}\) | \(0,\ 0,\ 16.5,\ 1.9,\ 0,\ 0,\ 1,\ 0,\ 0,\ 0\) |
| \(P_{22}\) | \(0,\ 0,\ 2,\ -1.1,\ 0,\ 0,\ 0,\ 1,\ 0,\ 0\) |
| \(P_{23}\) | \(0,\ 0,\ -4,\ 2.9,\ 0,\ 0,\ 0,\ 0,\ 1,\ 0\) |
| \(P_{24}\) | \(0,\ 0,\ 17,\ -13.6,\ 0,\ 0,\ 0,\ 0,\ 0,\ 1\) |
| \(P_{31}\) | \(0,\ 0,\ 0,\ 0,\ 7.5,\ 1.9,\ 1,\ 0,\ 0,\ 0\) |
| \(P_{32}\) | \(0,\ 0,\ 0,\ 0,\ -7,\ -1.1,\ 0,\ 1,\ 0,\ 0\) |
| \(P_{33}\) | \(0,\ 0,\ 0,\ 0,\ -13,\ 2.9,\ 0,\ 0,\ 1,\ 0\) |
| \(P_{34}\) | \(0,\ 0,\ 0,\ 0,\ 8,\ -13.6,\ 0,\ 0,\ 0,\ 1\) |
| \(P_{41}\) | \(0,\ 0,\ 0,\ 0,\ 0,\ 0,\ 1,\ 0,\ 0,\ 0\) |
| \(P_{42}\) | \(0,\ 0,\ 0,\ 0,\ 0,\ 0,\ 0,\ 1,\ 0,\ 0\) |
| \(P_{43}\) | \(0,\ 0,\ 0,\ 0,\ 0,\ 0,\ 0,\ 0,\ 1,\ 0\) |
| \(P_{44}\) | \(0,\ 0,\ 0,\ 0,\ 0,\ 0,\ 0,\ 0,\ 0,\ 1\) |
| \(P_1\)–\(P_6\) | Each column has \(-1\) in its corresponding row 1–6 and \(0\) elsewhere. |
| \(P_0\) | \(0,\ 0,\ 0,\ 0,\ 0,\ 0,\ 3800,\ 2652,\ 4081,\ 1300\) |

The rows of the matrix are, respectively, the three PN conditions, the
three RVP conditions, and the availability equations for \(A\), \(B\), \(D\),
and \(F\).

## Printed page 150

150 A. CHARNES, W. W. COOPER AND B. MELLON

technique of Dantzig the calculations proceed in a straightforward man-
ner, starting from a distinguished feasible solution toward an optimum.
This technique rests on an assumption of “nondegeneracy,” which is
not fulfilled in this problem.”

However, since the tableaus involved in Dantzig’s method provide an
efficient means of systematically examining some of the vast range of
possibilities,” it was decided to begin with this approach and check the
solutions obtained by other methods. The simplex method is relatively
simple and straightforward. An expression is required of Py in terms
of a linear combination with positive coefficients (the \) of 10 linearly
independent column vectors selected from the set of twenty-two such
vectors displayed in Table ITI, and an expression of the remaining P’s
in terms of these ten. In this manner the initial \’s may be determined.
The solutions so obtained do not necessarily provide a maximum for
the functional. But by means of the criteria developed by Dantzig [4|
it 1s possible at each stage of the calculations, provided degeneracy is not
present, to determine whether (a) further calculations are required,
(b) a maximum has been obtained, or (c) no finite maximum exists.
When condition (a) occurs (and degeneracy is not present) the solu-
tions themselves provide a simple means of improving the value of the
functional at the next stage of calculations. Moreover, examination of
Dantzig’s proof of optimality of the solution attained by his technique
disclosed a test for optimality of any solution regardless of “degeneracy”’

existence of a solution of the system of linear inequalities so that the method
provides a check on consistency conditions).

Bearing in mind the above (at worst) possible increase of the number of in-
equations in the system, it can be readily seen that the method rapidly becomes
impractical as m increases. It is clear, also, that the final number of unknowns
which may be assigned values at pleasure is not independent of the order of
elimination used. Many variants may result. From these numerous solutions it
is dificult to select those sets among which the maximum solutions must lie.

20 Cf. Dantzig [4, p. 3]: ‘‘Nondegeneracy assumption: Every subset of m
points from the set (Pa, P:, P:,-:+: , P,) is linearly independent’’—where m
represents the number of elements in a column vector, n, the number of un-
knowns, and P,), the constants on the right-hand side, as in Table III.

21 By this method it is possible to examine 1 + m(n — m) possibilities at each
stage of computation. In this problem it was thus possible to examine 121 pos-
sibilities at each step.

22 Since these computations were made, Charnes has developed a rigorous and
general method of applying the simplex technique, regardless of degeneracy,
which does not require an initial feasible solution or consideration of conditions
of dependence and independence, and by means of which all possible optimal
solutions may be obtained, The details of this method and the three criteria
referred to in the text may be found in Charnes [2].

## Printed page 151

BLENDING AVIATION GASOLINES 151

of the system or how the solution is obtained.” What is required is an
expression of Py) (see Table III) in terms of ten linearly independent
P’s, some of whose weights (A) may be zero, expression of the P’s in
terms of this set and continued computation of the remaining quantities
in the “simplex table.”

OPTIMUM PROGRAMS—COMPLETE SYSTEM

In the simplex calculations, a degeneracy effect appeared after the
first computation; i.e., a solution was obtained involving only eight
P’s and no M.™ These were, however, sufficient to investigate the
N—Q—Z system. Upon executing the calculations, an optimal 2 =
$15,249 (and total net receipts, R = $69,067) per calender day was ob-
tained. This level of receipts was achievable for the two alternative

TABLE IV
Input-Output TABLE FOR OpTiMuM FEASIBLE PROGRAM—l-c TEST
(BBLS/C.D.) zo = $15,249

Outputs
M N q é Total
Inputs
A 60 3740 ita 3800
B ia 2652 ata 2652
D wie 3023 1058 eat 4081
F a 653 534s 118 | 1300

Total........... .. $736 7984 113 | 41833

programs presented in Tables IV and VY. In addition, of course, any
percentage combinations of these two programs which meet the avail-
ability restrictions” will also yield the same maximum net receipts.
It should, perhaps, be expressly stated that the programs presented
in Tables IV and V meet the optimality test referred to in footnote 26
for the complete system, M—-N—Q—Z. The simplified system, N—Q—Z,
however, presented an opportunity to secure comparisons of maximum
receipts obtained with M present and absent under various policy re-
strictions, to investigate other aspects of the problem, and to establish

*% A proof of this proposition as developed by C. E. Lemke, may be found
in Charnes [1].

** This type of degeneracy effect is implied not only by the mathematical but
also by the technological structure since each product, such as M, is stated in
terms of two equations—vapor pressure and octane (or PN) ratings.

25 See equations (1b).

## Printed page 152

152 A. CHARNES, W. W. COOPER AND B. MELLON

bounds which could be utilized to check the solutions obtained. For
establishing such bounds, the principle that the maximum of a func-
tional does not decrease as its domain is extended was employed. The

TABLE V

InrputT-—OvutTrut TABLE FoR ALTERNATIVE OpriMuM FEASIBLE PRoGRAM—1-c TEST
(BBLS/C.D.) zo = $15,249

Outputs
M N Q Zz Total
Inputs

A Las 3800 Les 3800

B ee 1279 1373 _ 2652

D naa 2111 1970 wee 4081

PF 347 840 113 1300

POLL is pewsews as 3737 7983 113 11833

bounds so obtained assured that the final solutions could differ at most
insignificantly from their possible maxima.”

26 The complementary principle (the maximum of a functional is not increased
as its domain is contracted) indicated that, in general, the company method of
programming does not obtain a maximum feasible solution. Moreover, if the
stated company method of programming were strictly carried out—maximizing
output of the highest priced product, then the next highest priced, and so on—
it would be impossible to produce, apart from a small quantity of Z, any of the
other products. Calculation according to a strict interpretation of this procedure
showed that for the simplified problem, net receipts of $12,110 per calendar day,
or a diminution of $3,139 from the calculated optimum would be obtained. Iow-
ever, the company method is tempered in application by judgment and ex-
perience (See Table VI).

As a check on the calculations, one of the officials responsible for company
programming was asked to program in terms of the problem as stated in this
paper and to match his results against those reached here; it was felt also that
by this means insight would be obtained on actual programming methods used.
After a rather involved series of calculations, tempered at each stage by judg-
ment and experience, he concluded a program, the composition of which con-
stituted a convex combination of the alternate 1-c solutions presented here.
This resulted, of course, in the same net receipts, z = $15,249.

The method employed was, in many respects, vaguely similar to methods
employed in the transportation problem (see Koopmans, [6]) but without bene-
fit of an explicit and rigorous step-by-step procedure. Also missing was, of course,
an optimality criterion which in this case was supplied, as a target, by the alter-
nate solutions presented above. In the 1l-c and 3-c program, for example, only
a preliminary set of estimates was available from this study and the officia
stopped calculating as soon as he surpassed these figures, but while still nearly
$200 per day away from the final optimum.

These computations were also independently checked by L. Goldstein of the

## Printed page 153

BLENDING AVIATION GASOLINES 153

Noting that M, the lowest priced product (see equation 4) would not
be produced at all in the final program, it was decided to determine the
effects of possible policy restrictions in this direction.”’ For this purpose
it was decided to eliminate N, the medium priced gasoline entirely and
investigate two alternative policies with respect to Af: (1) a require-
ment that at least 500 barrels per calender day of M be produced, and
(2) a requirement that eractly 500 bbls/c.d. of be produced. The
first policy resulted in an average total reduction of net receipts by
$2,090 (20 = $13,159), and the second in a reduction of $2,999 (2 =
$12,250) per calendar day.

All figures refer, of course, to maximum feasible programs. Thus, the
second policy is much more restrictive, resulting in a reduction of net
receipts nearly $1,000/c.d. greater than the first, despite the fact that
it insures that an “excessive” amount of the lowest priced material
will not be produced.” The equality condition, M = 500, provides less
opportunity for taking advantage of technological and other conditions.
Mathematically, it is obvious that the condition that the solution must
lie on a line, or in a hyperplane, is more restrictive with respect to range
of possible variation than is the condition that the solution lie within
a region bounded by and including that line or hyperplane.

Inspection of the matrix in Table III makes clear (as previously
noted) that the products M@—N—Q—Z are linked together only through

U.S. Department of the Air Forces by means of the simplex technique and ig-
noring degeneracy. He secured a unique optimum with a program whose com-
position, up to rounding errors, was identical with the one displayed in Table IV,
the difference in final result being within three dollars. The program of Table V
was found by him to be less than four dollars lower than optimal, the discrepancy
again resulting from rounding errors in the computations.

27 M, the lowest priced aviation gasoline, it was discovered, is produced by
the company partly as a goodwill or service gesture. It is of interest to note
that the company official referred to in the preceding footnote immediately drop-
ped M from his calculations as soon as he understood that the problem as one of
simple profit maximization.

28 Such a policy might be imposed, e.g., to insure that certain contractual com-
mitments are met or that a certain market position is maintained, without ‘‘sacri-
ficing’’ too much production of higher priced products. Under the first policy,
M > 500, nearly 3,900 bbls per calender day of M is produced which might seem
to be too large a diversion to the lowest priced product, but the fixing of exact
limits actually results in a much greater reduction of receipts than occurs when
the diversion is allowed. It is, perhaps, worth noting that differential repricing
of M at $0.904, or slightly in excess of N, $0.889, would result in net receipts equal
to the N—Q—Z program.

Calculations for the complete system, M—N—Q—Z, however, resulted in ap-
proximately equivalent maxima, z» = $15,032, for both M = 500 and M > 500
so that from the point of view of profit maximization the two policies are equiv-
alent when the restriction N = 0 is removed.

## Printed page 154

154 A. CHARNES, W. W. COOPER AND B. MELLON

the availability restrictions specified in equation (3). Since the major
products, M, N, and Q, are linked only in this manner, it is possible to
construct reduced systems involving only one major product and Z, and
obtain feasible programs having the same diversion of components of
A—B—D—F into this one major product. Therefore, it is possible to
approximately examine the probable consequences of changes of struc-
ture in the complete system, A—-B—D—F — M—N—Q—Z, by study-
ing the effects of such changes on optimal solutions in the reduced sys-
tems. Percentage combinations of optimal solutions for the reduced
systems obviously also constitute feasible solutions for the complete

29
system.
OPTIMUM PROGRAMS—REDUCED SYSTEMS

It was decided to calculate maximum feasible programs for the re-
duced systems: Q—Z, N—Z, M—Z. The results of these calculations
are given in Tables VI, VII, and VIII.

The reduced systems can also be used to establish rough upper bounds
for the complete system by utilizing the principle, already noted, that
the maximum of a functional does not decrease as its domain is extended.
The reduced systems, of course, impose fewer restrictions on each major
product and thus yield upper bounds for the amount of each major
product which can be produced under the given structure. With the
stated technology (and availabilities), the maximum amounts obtain-
able for each major product (see preceding tables) are: M = 11,720
bbls/c.d., N = 11,720 bbls/c.d., Q@ = 8,106 bbls/c.d.

To obtain an upper bound for the functional, z) , consider the reduced
system Q—Z. The optimal solution yields the maximum amount of Q
which can be produced under the stated restrictions. If N is then freed
of all restrictions—other than availability—the domain of the func-
tional is thereby extended, and the value of z = 1.494(8106Q) +
$0.889(3727N) = $15,423 provides an upper bound for the complete
system. That is, to establish this bound it is assumed that the inputs,
3727 barrels (see Table VI), which would otherwise be diverted to Z
can be used to produce N. This bound may be further adjusted by

29 It is of interest to note that the solutions for Q, the highest price product, in
the reduced systems are all fairly close to the amount produced in the complete
system, nearly 8,000 bbls per day. Since the reduced system, Q—Z, gives the
maximum feasible value for Q, 8,106 bbls/c.d., these solutions provide insight
into stated company policy of attempting to maximize the higher octane rated
products at the expense of lower rated products. The programs for N—Z and
M—2Z involved large values for pseudo variables: \, = 71,870 and A, = 54,461,
respectively. Pseudo variables need have no physical (operational) meaning, but
in this problem they may be interpreted as overfulfillments of stated requirements
for vapor pressure and octanes, respectively.

## Printed page 155

BLENDING AVIATION GASOLINES 155

requiring the N so introduced to satisfy its technological restrictions
as given by the N—Z program (see Table VII). With this adjustment
2 = 1.494(8106Q) + 0.889(11,720/11,833) * 3727N = $15,391 is ob-
tained. These same methods can be applied to the optimum N—Q—Z

TABLE VI
Propuction or Q—Z Onty (BBLS/C.D.) zo = $12,110 Maximum

Inputs | |
A B D F Total
Outputs

|
|

Q 3800 2652 1103 551 8106

Z cease 2978749 8727

Tilsen 3800 2652 4081 1300 , 11833
TABLE VII

Propuction or N—Z Onty (BBLS/C.D.) zp = $10,419 Maximum

!
‘

Inputs
| A B D F Total
Outputa
N 3800 2652 4081 1187 11720
Z ok a, 113 113
Total........... 3800 2652 4081 1300 | 11833
TABLE VIII

Propuction or M—Z Onty (BBLS/C.D.) zo = $4,219 Maximum

Inputs |
A B D P | Total

Outputs |
M | 3800 2652 4081 1187 | 11720
Z | “— 113 | 113
Total........... | 3800 2652 4081 1300 | 11833

program to obtain even better upper bounds. Thus, z + $1.494(7984Q)
+ $0.889(3736N) + $0.36(11,720/11,833 * 118M) = $15,289, an upper
bound which exceeds the program maximum as determined from the
optimality criterion” by only $40.

30 See footnote 23, above.

## Printed page 156

156 A. CHARNES, W. W. COOPER AND B. MELLON

PROGRAM COMPARISONS: 1-c AND 1-c AND 3-C PN’S

The reduced systems can also, as previously noted, be used to esti-
mate approximately the effects of changes in the matrix. Indeed, it is
so simple to trace through these effects by use of the reduced systems
that, to save computations, it was decided to make these estimates for
the combined 1-c and 3-c programs, rather than to study each in isola-
tion. Before discussing the sensitiveness of the matrix to changes in
coefficients, it may be well to present the result of computations for the
additional 3-c restrictions.

Noting that no M was produced in the complete l-c program com-
parative estimates were obtained by calculating the effect of the addi-
tional restriction on the production of N—Q—Z. This yielded a figure

TABLE IX
ProcrRaAM CoMPaRISON BETWEEN l-c AND 1-c AND 3-c REQUIREMENTS

Program | Zand: | BBLS/C.D. Receipts ($)
1-c | @q@ | 8, 106 12,110
l-c and 3-e 6,979 10,427
l-c | oN 11,720 10,419
l-c and 3-c¢ 11,720 10,419
l-e M 11,720 4,219
l-c and 3-c 11,720 4,219
l-e i N—Q 3726 N + 7985 Q 15, 249
l-c and 3-e 5516 N + 6204 Q 14,172

2) = $14,172, or a reduction slightly in excess of $1,000/c.d. resulting
from the addition of the 3-c quality restriction.” Inspection of the dou-
ble-product reduced systems, given in Table IX, indicates that the
major effect of the additional restrictions are felt in the reduction in
output of Q by more than 1,100 bbls/c.d.—from 8106 to 6979 bbls/c.d.
Neither N nor M shows any effect from imposition of the 3-c test re-
quirement; indeed, is entirely free of this restriction (see Table I).
The relatively weak technology for production of Q (see the relatively
low values for the PN coefficients of Q in Table III) absorbs the entire
incremental strain of the additional quality restriction. The two-product
systems thus provide insight into effects on the more complete systems

31 Again the reduced systems can be used to calculate upper bounds for the
complete system should this prove desirable.

## Printed page 157

BLENDING AVIATION GASOLINES 157
such as N—Q—Z where N is increased at the expense of a drastic reduc-
tion in Q, the highest quality product.”

PROGRAMMING FOR STRUCTURAL CHANGES

To explore the sensitivity of the matrix, the following changes sug-
gested by practical considerations were separately investigated: (1) re-
duction in RVP of D by 1 unit, (2) decrease in PN (octane) require-
ments of B by 1 unit on the 1-c test and 1.1 units on the 3-c test, (3)
diminution of PN (octane) ratings on A by 1 unit on the 1-c test and
2 units on the 3-c test. The results of these investigations are given in
Table X.

The particular coefficients studied were selected on the basis of the
following criteria: (1) judgment of experienced engineers associated with
refinery operations suggested that variation in these coefficients might
be expected to produce marked changes in program results (as measured

TABLE X

EFFrects OF CHANGES IN SELECTED COEFFICIENTS REDUCED SYSTEMS
l-c AND 3-c TESTS

Change in Receipts (in dollars), + A Zoe

Decrease in Coefficients for Programs

Zand@ Zand NV Zand M
Se gerercnveres comenamaacnneumennenas + 84 +84 +36
Octane of B by 1 on 1-c and 1.1 on 3-c........ —101 0 0
Octane of A 1 on 1l-c and 2 on 3-c............. — 131 0 0

by net profits) and (2) the coefficients were capable of being changed
in the manner (if not to the extent) indicated. The expected results
did not, however, materialize. Although the changes were, generally, in
the expected direction, the quantitative magnitudes were far less than
had been anticipated.”

32 Use of the N—Q—Z system assumes no production of M (e.g., for goodwill
purposes) is undertaken.

33 This suggests (along with the observations noted in footnote 26) that so
long as conditions remain stable, even under relatively complex conditions, ex-
perienced personnel by application of “‘insight’’ and ‘“‘know-how”’ do surprisingly
well in terms of optimal results. Under new or rapidly changing situations, how-
ever, even of a more simple kind than that previously experienced, results achieved
by such ‘‘cut and try’’ methods are likely (at least for a time) to depart markedly
from possible optima. Such a departure from past experience is involved in es-
timating the possible effects of changing coefficients. Of course, if conditions
are very complex (as in programming for the whole company) there is no guarantee
that marked deviations from attainable optima are not likely to remain for pro-

## Printed page 158

158 A. CHARNES, W. W. COOPER AND B. MELLON

Inspection of Table X shows that the matrix is surprisingly insensi-
tive when compared to the magnitude of the changes which practical
experience would seem to indicate might be obtained. Of course, no
conclusions as to the desirability of effecting these changes can be
reached without introducing additional considerations such as, (1) the
incremental costs of effecting the changes and (2) the possible conse-
quences such changes might have for other company policies and pro-
grams. It can be said, however, that in some of the cases the possible
benefits or penalties are so small in magnitude as to make the problem
unlikely to be worthy of extended attention by company officials. De-
creasing the RVP index of D by as much as 1 unit, for example, will
produce only minor increases in net receipts. On the other hand, reduc-
tion in the octane blending indexes of A has important practical operat-
ing conveniences which may far well outweigh the relatively small reduc-
tion in net receipts.

Obviously these techniques could be used to explore other problems
as well. For example, it might be of interest to explore the cost of cur-
rent scheduling policy. The restrictions (1b) might be changed. As now
stated, they imply that program calculations are unaffected by the price
(or cost accounting imputations) of these materials. Changing the equa-
tions to inequations which specified upper or lower limits to the use of
such materials would alter this aspect of the problem. Given the insensi-
tivity of the present matrix resulting from the large amount of slack
allowed under current policy, it would also be interesting to explore the
effects of price changes on net receipts. It might be expected that results
parallel to those found in altering the quality restrictions would occur.
Large relative changes in some of the prices might have no noticeable
effect on net receipts. To be fully realistic, however, such calculations
should include demand as well as cost considerations.

In principle, it is clear such calculations can easily be made if ade-
quate computational facilities are available. The demonstration of this
principle, and the illustration and development of methods for con-
ducting such analyses, is the major purpose of this paper. Therefore,
little would be gained by pushing the present calculations further for
the blending problem presented here. More important, perhaps, than
such investigations is the problem of extending the techniques of pro-
gramming to the area of operations. The “budget as a document” and

tracted periods. Thus, programming is likely to offer the greatest net advantage
over good commercial practice under very complex or rapidly changing condi-
tions, particularly if such changes require extension beyond the realm of past
experience,

44 This felicitous terminology was suggested by Mr. John Norton.

## Printed page 159

BLENDING AVIATION GASOLINES 159

the “budget as a process’ are too intimately related in practice to
admit of continuous rigid separation in theory.

Carnegie Institute of Technology
REFERENCES

[1] Charnes, A., “Mathematical Background for Linear Programming,’’ Hecto-
graphed lecture series prepared for Carnegie Institute of Technology,
Department of the Air Forces Research Project in Intra-Firm Behavior.

[2] Charnes, A., “Optimality and Degeneracy,” Econometrica, Vol. 20, April,
1952, pp. 160-170.

[3] Cooper, W. W., ‘‘A Proposal for Extending the Theory of the Firm,’’ Quar-
terly Journal of Economics, Vol. 65, February, 1951, pp. 87-109.

[4] Dantzig, George B., “Maximization of a Linear Form Whose Variables are
Subject to a System of Linear Inequalities,’’ Headquarters, USAAF, Nov.
1, 1949. Reproduced in Activity Analysis of Production and Allocation,
Cowles Commission Monograph No. 13, New York: John Wiley and Sons,
1951, pp. 19-32.

[5] Dines, Lloyd L., “Systems of Linear Inequalities,” Annals of Mathematics,
2nd series, Vol. 20, 1918-19, pp. 191-199.

[6] Koopmans, T. C., ed., Activity Analysis of Production and Allocation, Cowles
Commission Monograph No. 13, New York: John Wiley and Sons, 1951,
404 pp.

[7] Leontief, Wassily W., The Structure of the American Economy, 1919-1939
(second edition), New York: Oxford University Press, 1951, 264 pp.

[8] Wood, M. K., “Elements in the Design of Mathematical Models for Program-
ming,” U. 5. Department of the Air Forces.
