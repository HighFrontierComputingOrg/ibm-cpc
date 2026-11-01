**ECONOMETRICA**

VOLUME 20   \|   APRIL, 1952   \|   NUMBER 2

# **BLENDING AVIATION GASOLINES—A STUDY IN PROGRAMMING INTERDEPENDENT ACTIVITIES IN AN INTEGRATED OIL COMPANY**

**BY A. CHARNES, W. W. COOPER, AND B. MELLON1**

## **SUMMARY**

THE TECHNIQUES of linear programming are here explained in a commercial application—blending aviation gasolines. Blending is critically important to almost all other areas of programming in an integrated oil company. Intelligent programming of production, transportation, manufacturing, or marketing generally requires solution of blending problems as an initial or integral part of the whole process for it is in blending that the final outputs are determined.

In the first part of the paper, questions of optimum programming in a given technological and institutional structure are explored. Computations are executed primarily by means of the simplex technique of Dantzig \[4\]. Because of the presence of multiple degeneracy and the absence of a general method (at the time these computations were made) of handling such problems, it was not possible to rest securely on the simplex method. Alternative methods of computation were, therefore, explored and bounding techniques were employed to discover possible divergences from optimality. Finally, to test the validity of the results, calculations undertaken by a company programming official were obtained for purposes of check and comparison.

A relatively simple program is first calculated and more than one optimal program obtained. These results are then extended to more complex problems. Finally, the sensitivity of the matrix to possible changes in the coefficients is studied.

The problem of linear programming may be stated as follows: A set of *m* equations in *n* unknowns is specified. This may be written in the form ∑*i*\=1*n* λ*iPi* \= *P*0, where the *Pi* and *P*0 represent column vectors, each with *m* components. The problem then is to find a set of λ*i* ≥ 0 which satisfies these equations and which maximizes a linear functional *f*(λ*i*) \= ∑*i*\=1*n* λ*ici*. The *ci* may correspond to any set of relevant criteria but, by the nature of the problem here, they are restricted to prices of outputs or products.

The sensitivity problem revolves around variation in the components of the *Pi*. The results of these variations may be studied in terms either of consequent variation in physical program composition (via the new activity levels so obtained) or of consequent variation in the value of the functional, or both. Because of the explicit relevance of profits to business activity, attention is here centered on the changes in profit position resulting from such structural variation. Finally, the possible consequences of variation in the vector *P*0 (which corresponds to levels of expected inputs) and the prices *ci* are also discussed. Changes in coefficients of the matrix correspond to changes in the technology. Hence, the effects of programs of applied research may be examined in terms of the relative profitability of the improvements which the research proposes to effect.

1 This study is a modified version of a paper presented at the Conference on Linear Inequalities (1951) sponsored jointly by the U.S. Department of the Air Forces and National Bureau of Standards. The research for this paper was partially supported by grants from the U.S. Department of the Air Forces to the Carnegie Institute of Technology, to the School of Industrial Administration for research in intrafirm behavior, and to the Department of Mathematics for research in applied mathematics. Grateful acknowledgment is made to Mr. Carl Lemke who supervised the computations and to Mr. T. Sainsbury and Mr. T. T. Kwo who assisted him. Professor David Rosenblatt made numerous helpful suggestions.  
Shortly after this study was completed, Charnes \[1\] developed a general method for handling degeneracy.

## **INTRODUCTION**

The purpose of this paper is to investigate applications of linear programming and related techniques to planning problems in business enterprise, to obtain comparisons with current commercial practice, and to explore possible extensions and simplifications of linear programming techniques. This study, it should be borne in borne in mind, is oriented toward planning or programming rather than execution of operations.2 It is oriented toward the type of activity undertaken by a central office planning group such as a budgetary committee. No attempt is made to introduce such phenomena as "initial" or "boundary" conditions, feedback reporting design and interpretation, and agent behavior and control phenomena of the type which would have to be considered at the operating level, as distinct from the programming level. These problems have been reserved for separate study. At the outset, the indebtedness that all workers in this field owe to T. C. Koopmans, George Dantzig, Marshall Wood, and Wassily Leontief \[6, 7\] should be acknowledged.

Programming inputs and outputs in an oil refinery was selected for study because it was possible to obtain the necessary coefficients without undertaking large-scale empirical surveys. The advanced stage of chemical work and developed standards of classification in petroleum refining make it possible to avoid difficult problems of aggregation, which are present in many other types of industrial processes.

To avoid the necessity of employing high speed electronic computing equipment, which was not available for this work, no attempt was made to study programming for an entire refinery. Only one process—blending aviation gasolines—was studied. This restriction of the area of study added the further convenience of avoiding problems of storing, lead times, make-ready times, etc., which would be encountered in a large study. In short, the problem was restricted to the flow of components in the blending process.

Blending, rather than other phases of refinery operations, was selected for study because (a) it represents an important distinct phase of such operations and hence of programming, and (b) it has essential characteristics that make it typical not only of refining problems, but of chemical manufacture in general. Pressure, volume conditions, and even the action of catalytic agents are present in this problem with the usual complex interactions between physical, chemical, economic, technological, and managerial considerations. The model though simplified has thus a real and important counterpart for a wide range of problems in physical operations and business planning. These criteria—operational significance and importance have been borne in mind in the choice of simplifying assumptions in the model constructed for use in this study.

2 For a more detailed discussion of points of difference between programming and execution, see Cooper \[3\].

## **ELEMENTS OF THE PROBLEM TECHNOLOGICAL BACKGROUND**

Only material costs and quantities were considered. Capital, labor, and other elements of cost were omitted.3 Given the refinery and blending equipment, such costs are not variable. Labor costs are largely fixed by the refinery operations as a whole, the blending activity having only an insignificant effect on these costs. The same is true of overhead and related costs.

A few words should be said to clarify terminology and to explain some of the considerations involved in blending. As is well-known, when crude oil is refined various products may be formed, such as gasoline, kerosene, distillate fuels, light and heavy lubricating oils, tar, etc. The exact proportions of each product depend not only on the characteristics of the crude oil and the design of the refinery but upon the methods employed as well. Variations in temperature and pressure, introduction of chemical agents or catalysts, and numerous other devices may be employed to effect these proportions.

Not all gasolines, even when produced from the same crude stock, are of uniform quality. The properties may be changed or adjusted by blending different gasolines in suitable proportions and subjecting them to chemical treatment. Aviation gasolines are blended from carefully selected straight-run gasolines, catalytically cracked gasolines, and special components synthesized from other refinery products. With the addition of appropriate amounts of tetraethyl lead (TEL) and other chemicals and dyes, the final products aviation gasolines are blended.

Of course, not all components that are usable in producing aviation gasolines will be devoted exclusively and exhaustively to that purpose. Economic, technological (e.g., storage limitations), and other considerations may make it desirable to divert some of these components to production of other products. For this study, all components not completely consumed in the production of aviation gasolines are assumed to be blended into premium automotive gasoline.4

This simplifying assumption is not far removed from realities of the current situation. Aviation stocks can technologically be used in producing automotive fuels and under current demand conditions, such diversions would prove economical. It should be realized, however, that the process of diversion to other final products can be continued to further lengths, that materials not used to produce premium automotive gasoline can be absorbed in the production of regular grade automotive gasoline and sold directly to other refiners as stocks, etc. It should be further noted that it is also assumed that the increment over scheduled production of automotive gasolines resulting from diversion of components in the aviation blending program would not be sufficiently large to have an adverse effect on price or other marketing and distribution considerations for such fuels. This assumption is justified by the relative magnitude of the figures for the various programs. Even if this had not proved to be the case, it would have been possible to extend the calculations without fundamentally affecting the principles involved.

Given the properties of the components, the blending operation must be directed in a manner to insure that certain quality specifications are satisfied. Of these specifications, the two most important are ignition properties, as measured by octane ratings5 or performance numbers,6 and volatility as measured by Reid Vapor Pressure. These two specifications usually govern blending considerations within ordinary ranges of operation, although other considerations may become dominant under less usual conditions.

Reid Vapor Pressure, (RVP), is determined by standard specific trials with given gauges and containers under stipulated temperature conditions. Higher than permitted pressures are undesirable, and even dangerous in aviation gasolines, because of the tendency to boil and produce vapor lock under high temperature and altitude operating conditions. Indeed, for considerations of maximum operating efficiency, airplane fuel systems are specifically designed to operate with fuels of maximum RVP of 7.0 lbs./sq. in. Generally, it is prudent to blend for a maximum RVP of 6.9 lbs./sq. in., and the blending coefficients used in this study are based on this assumption.

Aircraft engines are generally designed to operate satisfactorily provided the fuels used meet minimal octane or "antiknock" requirements. "Knocking" in aircraft engines is a more serious matter than in automobile engines. Unless these minimal octane requirements are met, the engine will not perform satisfactorily and destruction or damage to the engine may result. On the other hand, use of excessively high octane rated fuels results in greater expense with no comparable benefit in operating performance.

Closely related to octane ratings are performance numbers (PN), generally specified on aviation gasoline contracts. Two important considerations in the properties of a fuel for aircraft operations are (1) full power for takeoff and (2) maximum mileage per gallon under normal cruising conditions. Best performance on takeoff is attained with a "rich mixture" or high fuel/air ratio; maximum fuel economy, i.e., condition (2), is attained with a "lean mixture" or low fuel/air ratio. Standard methods of testing have been devised for measuring these fuel properties by means of appropriately designed single cylinder engines which are operated under carefully specified conditions. The first, or rich mixture PN, is rated by what is known as the 3-c test; the second, or lean mixture PN, is rated by what is known as the 1-c test.

This study was conducted in two stages: First, program calculations were made on the assumption that only the 1-c PN was specified; second, both 1-c and 3-c specifications were simultaneously imposed. By this means it was possible both to simplify the initial calculations and facilitate insight into the character of the problem. It was decided to study the problem in this particular sequence for other reasons as well. Prior to World War II, it was common practice to specify only the 1-c quality restriction. Hence, it was possible, also, by this means, to conform to the historical sequence of practice and to obtain estimates of the economic cost of the additional quality restriction.

As was previously noted, properties of the final products can be altered not only by blending gasolines but also by chemical treatment, e.g., by the addition of TEL (tetraethyl lead). The blending indexes for Reid Vapor Pressures are independent of the grades of gasoline, but the octane and performance number blending indexes are functions of the amount of TEL in the product. Hence, there can be more than one blending index for any component. In general, the greater the amount of TEL the higher the blending index—in economic terms, the technological coefficients are increased by application of this factor. Given the structure of relative factor prices used, it would be advantageous to apply more of the factor TEL in order to increase yields from the given stocks.7 But because of undesirable properties, including the poisonous character of unduly high concentrations of TEL, maximum limits are imposed on its use either by specification or by law.8 In this study, the maximum amount of TEL permitted was assumed to be employed. This makes the problem conform not only to the usual assumptions of profit maximization but to general practice in the industry as well.

The complete list of products entering into actual company programming as well as maximum RVP, ignition qualities (in terms of PN), and TEL assumptions are given in Table I. Of these products, the first three aviation grades indicated by parentheses along with premium automotive fuels were selected for study. The last three, or military grades, were eliminated from study. With appropriate computational equipment it is, of course, easily possible to extend the calculations for programming all categories.

Similar simplifications were introduced for the components. A tabulation of the components used in this study, along with relevant chemical and physical properties, is displayed in Table II. From this list the items denoted by parentheses were selected for study.

3 A possible exception would be selling and distribution costs which are not relevant to refinery operations. It should be noted that, apart from decisions to close down major units of the refinery, labor requirements are rather rigidly fixed by technological characteristics. Even with major shutdowns, relatively large groups of skilled labor must often be employed since technology and capital considerations make it inadvisable to depend on ready availability of such labor in the free market.

4 Fortunately, company policy and the requirements of simple profit maximization coincided at the time of this study. Premium automotive fuels represent the next highest priced product line to aviation grades. Company policy on this point pivots about grades of gasoline which have to be purchased from other producers in order to "balance" its own programs. Premium grades at the time of this study were being purchased from other companies. If lower priced "regular" or "house grades" were being purchased instead, company policy would have required their substitution for premium automotive fuels in order to determine the relative desirability of diversion of "stocks" from the aviation program.

5 Octane ratings represent a method of objectively and quantitatively determining antiknock properties. The octane number or rating is defined as the per cent of iso-octane in an iso-octane normal-heptane mixture which has the same knock rating as the gasoline being rated in the test engine. The greater the per cent of iso-octane, the higher the octane number and the greater the antiknock properties of the gasoline.

6 Concomitant with the evolution of modern aircraft design, it became essential to develop gasolines with higher antiknock ratings than 100 per cent iso-octane. Consequently a new rating scale, the so-called PN scale, was developed to indicate maximum-potential-performance level of the fuel. There is a unique correspondence between octane rating and PN up to 100 octane; beyond this level PN is determined, relative to the amount of TEL which must be added to iso-octane, to achieve the same antiknock rating as the fuel being tested.

7 Estimates of market prices of TEL as of March, 1950, were employed in the study, although these were not necessarily the prices paid by the company on firm, or open-end contract amounts.

8 Higher amounts of TEL may be used in military gasolines than in civilian gasolines. In civilian aviation gasolines maximum permitted TEL is 4.0 cc/gal.; military aviation gasolines permit a maximum of 4.6 cc/gal. The effect of the additional TEL permitted is to add two additional grades of product with four additional blending coefficients. The problem considered was restricted to civilian gasoline in order to reduce the number of computations. Numerical magnitudes of the results are, therefore, affected but not the basic techniques or principles.

**TABLE I — LIST OF PRODUCTS**

| Symbols Used In Study | Gasolines (Aviation Grade) | Specifications |  |  | Maximum TEL, cc/gal. |
| :---: | :---- | :---: | :---: | :---: | :---: |
|  |  | Maximum RVP | Minimum 1-c PN | Minimum 3-c PN |  |
| M | 80 L | (7.0) | (80.0)b | (...) | (0.5) |
| N | 91 C | (7.0) | (91.0) | (96) | (4.0) |
| Q | 100 C | (7.0) | (100.0) | (130) | (4.0) |
| — | 91 M | 7.0 | 91.0 | 96 | 4.6 |
| — | 100 M | 7.0 | 100.0 | 130 | 4.6 |
| — | 115/145 | 7.0 | 115.0 | 145 | 4.6 |
| Z | Premium motor | a | a | a | 3.0 |

a No bearing on computations since premium motor fuel is to be blended to specification with other components.

b 80 L is a result of mobilization changes to conserve aviation components. Normally an 80 octane aviation gasoline does not contain TEL.

**TABLE II — AVIATION GASOLINE STOCKS**

| Symbols Used in Study | Component | RVP | Blending Indexes |  |  |  |  |
| :---: | :---- | :---: | :---: | :---: | :---: | :---: | ----- |
|  |  |  | PN 1 | 1-c |  | 3-c |  |
|  |  |  | TEL cc/gal → 0.5 | 4.0 | 4.6 | 4.0 | 4.6   |
| A | Alkylate I | (5.0) | (94.0) | (107.5) | 108.0 | (148.0) | 151.0 |
| B | Catalytic gasoline A | (8.0) | (83.0) | (93.0) | 93.3 | (106.0) | 110.0 |
| D | Straight-run gasoline mix A | (4.0) | (74.0) | (87.0) | 88.8 | (80.0)a | 84.0 |
| — | Straight-run gasoline mix B | 5.9 | 77.0 | 89.0 | 91.0 | 95.0 | 99.0 |
| — | Outside isomers | 9.2 | 85.0 | 97.7 | 98.3 | 112.1 | 115.1 |
| — | Catalytic gasoline B | 8.8 | — | — | — | 92.0 | 108.0 |
| — | Alkylate II | 4.8 | — | — | 106.0 | — | 149.0 |
| — | Toluene | 1.0 | — | — | 102.0 | — | 230.0 |
| F | Isopentane | (20.5) | (95.0) | (108.0) | 107.04 | (140.0) | 141.00 143.0 |

a Two blending indexes available

## **MATHEMATICAL STATEMENT OF THE PROBLEM**

With this background, it is now possible to proceed with a mathematical statement of the problem. As noted in the summary at the outset of this paper, the linear programming problem requires specification of a set of *m* equations in *n* unknowns. In equivalent vector form this may be written ∑*i*\=1*n* λ*iPi* \= *P*0 where the *Pi* and *P*0 represent column vectors, each with *m* components. It is required to find a set of λ*i* ≥ 0 that satisfies these equations and simultaneously maximizes a linear functional *f*(λ*i*) \= ∑*i*\=1*n* λ*ici*.

Tables I and II supply the necessary information for mathematical formulation of the problem. Each of the aviation gasolines, M, N, and Q, have stipulated minimal PN and maximal RVP ratings. Each of the inputs, A, B, D, and F, have certain technological ratings relative to these outputs for stipulated amounts of TEL. This information may be utilized to form the following set of inequations:

| 94.0λ11 \+ 83.0λ12 \+ 74.0λ13 \+ 95.0λ14 ≥ 80M 5.0λ11 \+ 8.0λ12 \+ 4.0λ13 \+ 20.5λ14 ≤ 6.9M 107.5λ21 \+ 93.0λ22 \+ 87.0λ23 \+ 108.0λ24 ≥ 91N 5.0λ21 \+ 8.0λ22 \+ 4.0λ23 \+ 20.5λ24 ≤ 6.9N 107.5λ31 \+ 93.0λ32 \+ 87.0λ33 \+ 108.0λ34 ≥ 100Q 5.0λ31 \+ 8.0λ32 \+ 4.0λ33 \+ 20.5λ34 ≤ 6.9Q | (1) |
| :---- | ----: |

where, by definition

| M \= λ11 \+ λ12 \+ λ13 \+ λ14 N \= λ21 \+ λ22 \+ λ23 \+ λ24 Q \= λ31 \+ λ32 \+ λ33 \+ λ34 | (1a) |
| :---- | ----: |

The convention to be followed is that the first subscript on the λ's refers to the output and the second to the input. Thus, the first output, M in (1a), is composed of the four inputs λ1*i*, *i* \= 1, 2, 3, 4, where the second subscripts refer successively to the bracketed items in Table II; that is, the inputs, A, B, D, and F which go into the makeup of M. (Some of the λ*ij* may, of course, be zero.) The inequations refer by pairs to each of the aviation grade gasolines specifying PN and RVP properties, respectively. Referring to M, for example, the first two inequations stipulate that M shall have an octane (PN) rating of at least 80 and vapor pressure (RVP) of not more than 6.9 lbs./sq. inch. Although the terms on the right-hand side can be viewed as components of the requirements vector, *P*0, it is better first to reduce the set (1) to equations by introducing additional nonnegative quantities, appropriately defined. This will be done at a later stage.

Associated with each of the variables λ*ij* in (1) is a vector with components representing elements in the given structure. Reference to Table III may serve to make the meaning of this statement clear. Under the column headed *P*11 are structural components representing the properties of alkylate going into the makeup of M. Per unit used, the former contributes 94.0 units, 94 − 80 \= 14 units in excess of minimal requirements, to the latter's PN rating (at the specified TEL level). Alkylate contributes 5.0 units, or 6.9 − 5.0 \= 1.9 units below maximum permitted RVP of M. The technological properties of alkylate relative to M are independent of its properties relative to N or Q in terms of the given structure as indicated by the zeros (represented by blanks in the matrix) for the succeeding four rows of *P*11. In short, the outputs are tied together only through the policy restrictions on availability (shortly to be discussed) indicated in the last four rows of Table III.

To construct the program matrix, it is first desirable to simplify the set of inequations (1). Before doing so, however, it will be well to state the policy restrictions in mathematical form. As a result of company policies and programming in other parts of the refinery, the various inputs are expected to flow into the storage tanks at certain average rates, in barrels per calendar day. To eliminate the need for constructing additional storage capacity it is desired that these "stocks" or inputs be consumed, on the average, at exactly these rates.9 Stated in mathematical form, this policy restriction becomes:

| A \= λ11 \+ λ21 \+ λ31 \+ λ41 \= 3800 B \= λ12 \+ λ22 \+ λ32 \+ λ42 \= 2652 D \= λ13 \+ λ23 \+ λ33 \+ λ43 \= 4081 F \= λ14 \+ λ24 \+ λ34 \+ λ44 \= 1300 | (1b) |
| :---- | ----: |

where the λ4*i*, *i* \= 1, 2, 3, 4, are the amounts of A, B, D, and F not employed in making M, N, or Q. These values may be regarded as inputs to a new product, Z, which is subject to no technological restrictions in the aviation program. Z is, of course, premium automotive fuel.

The total daily inflows amount, on the average, to 11,833 barrels per calendar day as indicated by the numbers on the right-hand side of (1b), which enter as components in the vector *P*0 (see Table III). Stated in this form, company policy is seen to be equivalent to treating these inputs as fixed factors. The price of these inputs is, therefore, irrelevant to programming calculations. Their valuation (like the valuation of any fixed factor under strict definition of alternative costs) proceeds entirely from the receipts side in terms of possible alternative employments.10

Upon combining and simplifying, the relations specified in (1), (1a), and (1b) become:

| 14λ11 \+ 3λ12 − 6λ13 \+ 15λ14 ≥ 0 1.9λ11 − 1.1λ12 \+ 2.9λ13 − 13.6λ14 ≥ 0 16.5λ21 \+ 2λ22 − 4λ23 \+ 17λ24 ≥ 0 1.9λ21 − 1.1λ22 \+ 2.9λ23 − 13.6λ24 ≥ 0 7.5λ31 − 7λ32 − 13λ33 \+ 8λ34 ≥ 0 1.9λ31 − 1.1λ32 \+ 2.9λ33 − 13.6λ34 ≥ 0 λ11 \+ λ21 \+ λ31 \+ λ41 \= 3800 λ12 \+ λ22 \+ λ32 \+ λ42 \= 2652 λ13 \+ λ23 \+ λ33 \+ λ43 \= 4081 λ14 \+ λ24 \+ λ34 \+ λ44 \= 1300 | (2) |
| :---- | ----: |

Reference to the right-hand side of (1) reveals that the coefficients of the three aviation grades represent the minimal PN (octane) ratings and maximal RVP ratings that each of the aviation grades M, N, and Q is required to meet. As previously noted (see Table I and accompanying discussion), M must rate at least 80, N at least 91, and Q at least 100 on the PN scale for the 1-c test. Of course, statement of these conditions in the form of inequalities permits overfulfillment of requirements if profits can be increased in that manner. That is, M, for example, may be produced with a final PN in excess of 80\. So long as it remains below 91, it will not bring a higher price. Nevertheless, it may prove more profitable (as will later be shown) to overfulfill than to meet requirements exactly. Imposing the condition that requirements must be met exactly would, of course, necessitate restatement of (1) in the form of a set of equations, replacing the inequality signs by equality signs.11

The first six inequations in (2) may be reduced to a set of equivalent equations by introducing an appropriate set of new nonnegative unknowns, i.e., λ1, λ2, λ3, λ4, λ5, and λ6 on the right-hand side. The subscript in each of these unknowns refers to the number of the inequation in which it is to be introduced. In the terminology of the Air Forces, the λ's so introduced are referred to as pseudo variables \[8\].

Corresponding to each of these pseudo variables is an "artificial activity," *P*1, *P*2, *P*3, *P*4, *P*5, and *P*6 with components as listed under the headings in Table III. While meaning need not always be attached to these "artificial activities," (i.e., they may be introduced only for the purpose of facilitating computations), they have in this problem a definite physical meaning. Here a nonzero value for any of the pseudo variables represents an overfulfillment of requirements (extra octane or reduced RVP) in the product to which it refers. (See *infra*, the notes under Table VIII).

Upon executing the indicated operation, the relations (2) become

| 14λ11 \+ 3λ12 − 6λ13 \+ 15λ14 − λ1 \= 0 1.9λ11 − 1.1λ12 \+ 2.9λ13 − 13.6λ14 − λ2 \= 0 16.5λ21 \+ 2λ22 − 4λ23 \+ 17λ24 − λ3 \= 0 1.9λ21 − 1.1λ22 \+ 2.9λ23 − 13.6λ24 − λ4 \= 0 7.5λ31 − 7λ32 − 13λ33 \+ 8λ34 − λ5 \= 0 1.9λ31 − 1.1λ32 \+ 2.9λ33 − 13.6λ34 − λ6 \= 0 λ11 \+ λ21 \+ λ31 \+ λ41 \= 3800 λ12 \+ λ22 \+ λ32 \+ λ42 \= 2652 λ13 \+ λ23 \+ λ33 \+ λ43 \= 4081 λ14 \+ λ24 \+ λ34 \+ λ44 \= 1300 | (3) |
| :---- | ----: |

This set of 10 equations in 22 unknowns represents the basic set of technological and policy restrictions.12 A feasible solution (or program) must provide a set of nonnegative values which will simultaneously satisfy all of these relations.

The problem is to maximize the net receipts function subject to these restrictions. Such a function is formed by introducing the appropriate set of prices for each of the outputs M, N, Q, and Z; thus defining a receipts functional

| *R* \= 4.96*M* \+ 5.846*N* \+ 6.451*Q* \+ 4.830*Z*    − 0.05177*M* − 0.409416(*N* \+ *Q*) − 0.281862*Z* | (4) |
| :---- | ----: |

where the positive coefficients represent dollars-per-barrel receipts,13 and the negative coefficients correspond to the cost of TEL at maximum permitted concentration.14

Since premium automotive fuel enters only as a residual in the aviation program,

| *Z* \= 11,833 − *M* − *N* − *Q* | (5) |
| :---- | ----: |

Inserting this expression, (4) becomes

| *R* \= 0.36*M* \+ 0.889*N* \+ 1.494*Q* \+ \$53,818 | (6) |
| :---- | ----: |

In this form the equation of net receipts is stated in incremental value terms, relative to the price per barrel of Z. The constant, \$53,818, then represents the minimum level of receipts obtained by diverting all components to the next best alternative, the production of Z. This level of receipts must be attained if it is worth (on an alternative cost basis) producing any gasoline at all of aviation grade under the stipulated restrictions. Clearly, this functional will be a maximum if

| *z*0 \= 0.36*M* \+ 0.889*N* \+ 1.494*Q* | (7) |
| :---- | ----: |

is a maximum. For the program calculations, therefore, only this last expression, (7), need be used.

Thus the problem is to maximize the linear functional, *z*0, as given in (7), subject to the side conditions (3). Since only nonnegative solutions are admissible, the solutions must satisfy the additional restrictions:

| λ*ij* ≥ 0,    (*i, j* \= 1, 2, 3, 4\) λ*k* ≥ 0,    (*k* \= 1, 2, 3, 4, 5, 6\) | (8) |
| :---- | ----: |

where the terms with double subscripts represent the level of "real activities" and the terms with single subscripts the level of "artificial activities," respectively.15, 16 Thus, all solutions must lie within the positive orthant.17 The 22 conditions (8) plus the 10 conditions (3) and the statement of the linear form (7), which is to be maximized subject to these conditions, constitute the complete model for solution of the 1-c specification problem.

9 This was not immediately apparent to various company officials with whom the problem was discussed. It was their feeling that, in any event, it was better to avoid the need for additional storage capacity, probably because such capacity problems would have to be dealt with under company procedure outside the normal routine of programming calculations.

10 One such alternative would be possible diversion to premium automotive fuel. It should be clear that restatement of (1b) as inequations would set either (a) minimum levels of (fixed) costs or (b) upper limits to variable costs, depending on which way the inequality signs were turned.

11 Such restatement may also introduce contradictory conditions. The program is then said to be infeasible. Such indeed proves to be the case when exact requirements are imposed on the full 1-c and 3-c programs. The reasons for this are evident. It will be recalled that the 1-c and 3-c tests refer to cruising and take-off properties of the same gasoline. Thus, for Q with PN's of 100 and 130, respectively, the 1-c test may yield a value below 100 and the 3-c test may yield a value above 130\. Attempts to alter one of the ratings will, in general, drive the other in the same direction. Much attention apparently centers on this problem, referred to as "giving away octanes," in the manufacturing division. In conversations with company officials it was admitted that such double requirements on a single product might be impossible to fulfill exactly. Company officials stated that in such cases they preferred to overblend on the "low" in order to meet the "high" exactly. But in actual calculations (for the problems discussed in this paper) it was noted that the programming officer overblended on both the low and the high.

12 Without the simplifying assumptions—elimination of military aviation gasolines and the 3-c test—the system would have yielded 22 equations in 62 unknowns.

13 It may be worth noting that the "prices" used in the receipts functional are not necessarily market prices. They represent a mixture of quotations, market prices, and internal prices which have been adjusted to preserve company confidentiality.

14 It will be recalled that the blending coefficients were set on the assumption that maximum-permitted TEL would be used. Although by alteration of blending proportions, the amount of TEL could be reduced and quality restrictions still satisfied, the increased introduction of TEL represents the cheapest method of securing the results. (Of course, alteration of the amount of TEL would change the blending coefficients). Hence, TEL, which the operating officials are free to vary within specification limits, represents a variable cost as determined by the amount used and price. In economic terms it is the "cost of maintaining the plant at the legally permitted optimum level." In budgetary control terms, the increased cost of using alternative methods of satisfying requirements represents a penalty for not utilizing the best methods available.

15 The functionals used here are not identical with net profits but may be made so by subtraction of the total fixed costs as defined by the accounting process. These costs are omitted because they do not affect the composition of the program.

16 The following definitions adopted from \[8\] will prove useful in succeeding discussion: (1) Model—a set of simultaneous equations or inequations which describe the interrelationships within an operation. (2) Activity—a subdivision of an operation identified by principal output and a particular combination of input factors. (3) Item—a good or service, or an aggregate thereof, produced by or required for the performance of an activity. (4) Level of activity—the rate of production of the principal output item of an activity per unit time period. (5) Artificial activity—an activity having no exact counterpart in reality, which is introduced into the formulation as a deliberate construct for conceptual or computational convenience. (6) Plan—a schedule of required outputs or activity levels for a specified set of items which are taken as the objective of an operation. (7) Program—a combined schedule of the levels of all activities and of the inputs and outputs of all items involved in an operation.

17 Geometrically the solutions thus form a convex polyhedron, i.e., a convex set with a finite number of "corners." See Charnes \[1\].

## **COMPUTATIONAL PROCEDURE**

To facilitate systematic computations, it is well to array the coefficients of the ten equations and twenty-two unknowns (3) in matrix form, as shown in Table III, where *P*0 is the vector whose components represent the requirements specified on the right-hand side of the equation (3).

If suitable computation machinery were at hand to provide solutions for a system of ten equations in ten unknowns,18 then a certain set of solutions could be obtained in terms of which every solution could be expressed as a per cent combination. Among this set would be the solutions which maximize *z*0; of course, there may be more than one such maximal set. In the absence of such computational facilities, recourse was had to the simplex method of Dantzig \[4\] and the elimination method of Dines \[5\].19

18 For the "complete program" involving both the 1-c and 3-c tests and military aviation gasolines as well, solutions for twenty-two equations in twenty-two unknowns would be required.

19 The title "elimination method" is used here because of certain natural analogies with the usual process of elimination of variables in solving sets of algebraic equations. Suppose the system of inequalities is written in the form: ∑*j*\=1*n* *aijxj* \+ *bi* ≥ 0 (*i* \= 1, 2, ..., *m*). If the coefficient of *xi* is positive for, say, *i* \= 1, ..., *ip* and negative for, say, *i* \= *ip*\+1, ..., *m*, then by multiplying one of the "positive" inequations by minus the coefficient of *xi* in a "negative" inequation, and similarly multiplying the "negative" inequation by the coefficient of *xi* in the "positive" inequation, and adding the two inequations so formed, the variable *xi* would be eliminated from that pair.  
The total number of new inequations that could be formed in this manner would be equal to the number of "positive" times the number of "negative" inequations. It is necessary to form all of these possible new inequations at each stage in order to retain a system equivalent to the initial one. Thus, starting with *m* inequations, as many as (*m*2/4) inequations may result at the second stage, (*m*4/16) at the third stage, and so on. (In practice, this maximum rate of increase is not generally attained).  
At the end of this process a system of *k* unknowns remains (if the I-rank of the matrix, determined by the existence of a column of coefficients all of the same sign, is *k* \> 0\) and *k* − 1 of the variables may be assigned values at pleasure. (Moreover, an I-rank, *k* \> 0, is a necessary and sufficient condition for the existence of a solution of the system of linear inequalities so that the method provides a check on consistency conditions).  
Bearing in mind the above (at worst) possible increase of the number of inequations in the system, it can be readily seen that the method rapidly becomes impractical as *m* increases. It is clear, also, that the final number of unknowns which may be assigned values at pleasure is not independent of the order of elimination used. Many variants may result. From these numerous solutions it is difficult to select those sets among which the maximum solutions must lie.

**TABLE III — PROGRAM MATRIX 1-C TEST**

| M |  |  |  | N |  |  |  | Q |  |  |  | Z |  |  |  | Artificial Activities |  |  |  |  |  | Requirements *P*0 |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | :---: |
| *P*11 | *P*12 | *P*13 | *P*14 | *P*21 | *P*22 | *P*23 | *P*24 | *P*31 | *P*32 | *P*33 | *P*34 | *P*41 | *P*42 | *P*43 | *P*44 | *P*1 | *P*2 | *P*3 | *P*4 | *P*5 | *P*6 |  |
| 14 | 3 | \-6 | 15 |  |  |  |  |  |  |  |  |  |  |  |  | \-1 |  |  |  |  |  | 0 |
| 1.9 | \-1.1 | 2.9 | \-13.6 |  |  |  |  |  |  |  |  |  |  |  |  |  | \-1 |  |  |  |  | 0 |
|  |  |  |  | 16.5 | 2 | \-4 | 17 |  |  |  |  |  |  |  |  |  |  | \-1 |  |  |  | 0 |
|  |  |  |  | 1.9 | \-1.1 | 2.9 | \-13.6 |  |  |  |  |  |  |  |  |  |  |  | \-1 |  |  | 0 |
|  |  |  |  |  |  |  |  | 7.5 | \-7 | \-13 | 8 |  |  |  |  |  |  |  |  | \-1 |  | 0 |
|  |  |  |  |  |  |  |  | 1.9 | \-1.1 | 2.9 | \-13.6 |  |  |  |  |  |  |  |  |  | \-1 | 0 |
| 1 |  |  |  | 1 |  |  |  | 1 |  |  |  | 1 |  |  |  |  |  |  |  |  |  | 3800 |
|  | 1 |  |  |  | 1 |  |  |  | 1 |  |  |  | 1 |  |  |  |  |  |  |  |  | 2652 |
|  |  | 1 |  |  |  | 1 |  |  |  | 1 |  |  |  | 1 |  |  |  |  |  |  |  | 4081 |
|  |  |  | 1 |  |  |  | 1 |  |  |  | 1 |  |  |  | 1 |  |  |  |  |  |  | 1300 |

The elimination method is impracticable for the system in toto because of (1) the size of the system of inequalities and (2) the difficulty of determining the distinguished set of solutions from the various possible solutions provided by the elimination process. In the simplex technique of Dantzig the calculations proceed in a straightforward manner, starting from a distinguished feasible solution toward an optimum. This technique rests on an assumption of "nondegeneracy," which is not fulfilled in this problem.20

However, since the tableaus involved in Dantzig's method provide an efficient means of systematically examining some of the vast range of possibilities,21 it was decided to begin with this approach and check the solutions obtained by other methods. The simplex method is relatively simple and straightforward. An expression is required of *P*0 in terms of a linear combination with positive coefficients (the λ) of 10 linearly independent column vectors selected from the set of twenty-two such vectors displayed in Table III, and an expression of the remaining *P*'s in terms of these ten. In this manner the initial λ's may be determined. The solutions so obtained do not necessarily provide a maximum for the functional. But by means of the criteria developed by Dantzig \[4\] it is possible at each stage of the calculations, provided degeneracy is not present,22 to determine whether (a) further calculations are required, (b) a maximum has been obtained, or (c) no finite maximum exists.

When condition (a) occurs (and degeneracy is not present) the solutions themselves provide a simple means of improving the value of the functional at the next stage of calculations. Moreover, examination of Dantzig's proof of optimality of the solution attained by his technique disclosed a test for optimality of any solution regardless of "degeneracy" of the system or how the solution is obtained.23 What is required is an expression of *P*0 (see Table III) in terms of ten linearly independent *P*'s, some of whose weights (λ) may be zero, expression of the *P*'s in terms of this set and continued computation of the remaining quantities in the "simplex table."

20 Cf. Dantzig \[4, p. 3\]: "Nondegeneracy assumption: Every subset of *m* points from the set (*P*0, *P*1, *P*2, ..., *Pn*) is linearly independent" where *m* represents the number of elements in a column vector, *n*, the number of unknowns, and *P*0, the constants on the right-hand side, as in Table III.

21 By this method it is possible to examine 1 \+ *m*(*n* − *m*) possibilities at each stage of computation. In this problem it was thus possible to examine 121 possibilities at each step.

22 Since these computations were made, Charnes has developed a rigorous and general method of applying the simplex technique, regardless of degeneracy, which does not require an initial feasible solution or consideration of conditions of dependence and independence, and by means of which all possible optimal solutions may be obtained. The details of this method and the three criteria referred to in the text may be found in Charnes \[2\].

23 A proof of this proposition as developed by C. E. Lemke, may be found in Charnes \[1\].

## **OPTIMUM PROGRAMS COMPLETE SYSTEM**

In the simplex calculations, a degeneracy effect appeared after the first computation; i.e., a solution was obtained involving only eight *P*'s and no M.24 These were, however, sufficient to investigate the N-Q-Z system. Upon executing the calculations, an optimal *z*0 \= \$15,249 (and total net receipts, *R* \= \$69,067) per calendar day was obtained. This level of receipts was achievable for the two alternative programs presented in Tables IV and V. In addition, of course, any percentage combinations of these two programs which meet the availability restrictions25 will also yield the same maximum net receipts.

**TABLE IV**

INPUT-OUTPUT TABLE FOR OPTIMUM FEASIBLE PROGRAM—1-C TEST  
(BBLS/C.D.) *z*0 \= \$15,249

| Inputs | Outputs |  |  |  | Total |
| :---- | ----- | ----- | ----: | ----- | ----: |
|  | M | N | Q | Z |  |
| A |  | 60 | 3740 |  | 3800 |
| B |  |  | 2652 |  | 2652 |
| D |  | 3023 | 1058 |  | 4081 |
| F |  | 653 | 534 | 113 | 1300 |
| **Total** |  | **3736** | **7984** | **113** | **11833** |

It should, perhaps, be expressly stated that the programs presented in Tables IV and V meet the optimality test referred to in footnote 26 for the complete system, *M-N-Q-Z*. The simplified system, *N-Q-Z*, however, presented an opportunity to secure comparisons of maximum receipts obtained with M present and absent under various policy restrictions, to investigate other aspects of the problem, and to establish bounds which could be utilized to check the solutions obtained. For establishing such bounds, the principle that the maximum of a functional does not decrease as its domain is extended was employed. The bounds so obtained assured that the final solutions could differ at most insignificantly from their possible maxima.26

24 This type of degeneracy effect is implied not only by the mathematical but also by the technological structure since each product, such as M, is stated in terms of two equations—vapor pressure and octane (or PN) ratings.

25 See equations (1b).

26 The complementary principle (the maximum of a functional is not increased as its domain is contracted) indicated that, in general, the company method of programming does not obtain a maximum feasible solution. Moreover, if the stated company method of programming were strictly carried out—maximizing output of the highest priced product, then the next highest priced, and so on—it would be impossible to produce, apart from a small quantity of Z, any of the other products. Calculation according to a strict interpretation of this procedure showed that for the simplified problem, net receipts of \$12,110 per calendar day, or a diminution of \$3,139 from the calculated optimum would be obtained. However, the company method is tempered in application by judgment and experience (See Table VI).  
As a check on the calculations, one of the officials responsible for company programming was asked to program in terms of the problem as stated in this paper and to match his results against those reached here; it was felt also that by this means insight would be obtained on actual programming methods used. After a rather involved series of calculations, tempered at each stage by judgment and experience, he concluded a program, the composition of which constituted a convex combination of the alternate 1-c solutions presented here. This resulted, of course, in the same net receipts, *z*0 \= \$15,249.  
The method employed was, in many respects, vaguely similar to methods employed in the transportation problem (see Koopmans, \[6\]) but without benefit of an explicit and rigorous step-by-step procedure. Also missing was, of course, an optimality criterion which in this case was supplied, as a target, by the alternate solutions presented above. In the 1-c and 3-c program, for example, only a preliminary set of estimates was available from this study and the official stopped calculating as soon as he surpassed these figures, but while still nearly \$200 per day away from the final optimum.  
These computations were also independently checked by L. Goldstein of the U.S. Department of the Air Forces by means of the simplex technique and ignoring degeneracy. He secured a unique optimum with a program whose composition, up to rounding errors, was identical with the one displayed in Table IV, the difference in final result being within three dollars. The program of Table V was found by him to be less than four dollars lower than optimal, the discrepancy again resulting from rounding errors in the computations.

**TABLE V**

INPUT-OUTPUT TABLE FOR ALTERNATIVE OPTIMUM FEASIBLE PROGRAM—1-C TEST  
(BBLS/C.D.) *z*0 \= \$15,249

| Inputs | Outputs |  |  |  | Total |
| :---- | ----- | ----- | ----: | ----- | ----: |
|  | M | N | Q | Z |  |
| A |  |  | 3800 |  | 3800 |
| B |  | 1279 | 1373 |  | 2652 |
| D |  | 2111 | 1970 |  | 4081 |
| F |  | 347 | 840 | 113 | 1300 |
| **Total** |  | **3737** | **7983** | **113** | **11833** |

Noting that M, the lowest priced product (see equation 4\) would not be produced at all in the final program, it was decided to determine the effects of possible policy restrictions in this direction.27 For this purpose it was decided to eliminate N, the medium priced gasoline entirely and investigate two alternative policies with respect to M: (1) a requirement that at least 500 barrels per calendar day of M be produced, and (2) a requirement that exactly 500 bbls/c.d. of M be produced. The first policy resulted in an average total reduction of net receipts by \$2,090 (*z*0 \= \$13,159), and the second in a reduction of \$2,999 (*z*0 \= \$12,250) per calendar day.

All figures refer, of course, to maximum feasible programs. Thus, the second policy is much more restrictive, resulting in a reduction of net receipts nearly \$1,000/c.d. greater than the first, despite the fact that it insures that an "excessive" amount of the lowest priced material will not be produced.28 The equality condition, *M* \= 500, provides less opportunity for taking advantage of technological and other conditions. Mathematically, it is obvious that the condition that the solution must lie on a line, or in a hyperplane, is more restrictive with respect to range of possible variation than is the condition that the solution lie within a region bounded by and including that line or hyperplane.

Inspection of the matrix in Table III makes clear (as previously noted) that the products *M-N-Q-Z* are linked together only through the availability restrictions specified in equation (3). Since the major products, M, N, and Q, are linked only in this manner, it is possible to construct reduced systems involving only one major product and Z, and obtain feasible programs having the same diversion of components of A-B-D-F into this one major product. Therefore, it is possible to approximately examine the probable consequences of changes of structure in the complete system, *A-B-D-F* → *M-N-Q-Z*, by studying the effects of such changes on optimal solutions in the reduced systems. Percentage combinations of optimal solutions for the reduced systems obviously also constitute feasible solutions for the complete system.29

27 M, the lowest priced aviation gasoline, it was discovered, is produced by the company partly as a goodwill or service gesture. It is of interest to note that the company official referred to in the preceding footnote immediately dropped M from his calculations as soon as he understood that the problem as one of simple profit maximization.

28 Such a policy might be imposed, e.g., to insure that certain contractual commitments are met or that a certain market position is maintained, without "sacrificing" too much production of higher priced products. Under the first policy, *M* ≥ 500, nearly 3,900 bbls per calendar day of M is produced which might seem to be too large a diversion to the lowest priced product, but the fixing of exact limits actually results in a much greater reduction of receipts than occurs when the diversion is allowed. It is, perhaps, worth noting that differential repricing of M at \$0.904, or slightly in excess of N, \$0.889, would result in net receipts equal to the N-Q-Z program.  
Calculations for the complete system, *M-N-Q-Z*, however, resulted in approximately equivalent maxima, *z*0 \= \$15,032, for both *M* \= 500 and *M* ≥ 500 so that from the point of view of profit maximization the two policies are equivalent when the restriction *N* \= 0 is removed.

29 It is of interest to note that the solutions for Q, the highest price product, in the reduced systems are all fairly close to the amount produced in the complete system, nearly 8,000 bbls per day. Since the reduced system, *Q-Z*, gives the maximum feasible value for Q, 8,106 bbls/c.d., these solutions provide insight into stated company policy of attempting to maximize the higher octane rated products at the expense of lower rated products. The programs for *N-Z* and *M-Z* involved large values for pseudo variables: λ2 \= 71,870 and λ1 \= 54,461, respectively. Pseudo variables need have no physical (operational) meaning, but in this problem they may be interpreted as overfulfillments of stated requirements for vapor pressure and octanes, respectively.

## **OPTIMUM PROGRAMS REDUCED SYSTEMS**

It was decided to calculate maximum feasible programs for the reduced systems: Q-Z, N-Z, M-Z. The results of these calculations are given in Tables VI, VII, and VIII.

The reduced systems can also be used to establish rough upper bounds for the complete system by utilizing the principle, already noted, that the maximum of a functional does not decrease as its domain is extended. The reduced systems, of course, impose fewer restrictions on each major product and thus yield upper bounds for the amount of each major product which can be produced under the given structure. With the stated technology (and availabilities), the maximum amounts obtainable for each major product (see preceding tables) are: *M* \= 11,720 bbls/c.d., *N* \= 11,720 bbls/c.d., *Q* \= 8,106 bbls/c.d.

To obtain an upper bound for the functional, *z*0, consider the reduced system Q-Z. The optimal solution yields the maximum amount of Q which can be produced under the stated restrictions. If N is then freed of all restrictions—other than availability—the domain of the functional is thereby extended, and the value of *z*0 \= 1.494(8106*Q*) \+ \$0.889(3727*N*) \= \$15,423 provides an upper bound for the complete system. That is, to establish this bound it is assumed that the inputs, 3727 barrels (see Table VI), which would otherwise be diverted to Z can be used to produce N. This bound may be further adjusted by requiring the N so introduced to satisfy its technological restrictions as given by the N-Z program (see Table VII). With this adjustment *z*0 \= 1.494(8106*Q*) \+ 0.889(11,720/11,833) × 3727*N* \= \$15,391 is obtained. These same methods can be applied to the optimum N-Q-Z program to obtain even better upper bounds. Thus, *z*0 \= \$1.494(7984*Q*) \+ \$0.889(3736*N*) \+ \$0.36(11,720/11,833 × 113*M*) \= \$15,289 an upper bound which exceeds the program maximum as determined from the optimality criterion by only \$40.30

30 See footnote 23, above.

**TABLE VI**

PRODUCTION OF Q-Z ONLY (BBLS/C.D.) *z*0 \= \$12,110 MAXIMUM

| Outputs | Inputs |  |  |  | Total |
| :---- | ----- | ----- | ----: | ----: | ----: |
|  | A | B | D | F |  |
| Q | 3800 | 2652 | 1103 | 551 | 8106 |
| Z |  |  | 2978 | 749 | 3727 |
| **Total** | **3800** | **2652** | **4081** | **1300** | **11833** |

**TABLE VII**

PRODUCTION OF N-Z ONLY (BBLS/C.D.) *z*0 \= \$10,419 MAXIMUM

| Outputs | Inputs |  |  |  | Total |
| :---- | ----- | ----- | ----- | ----: | ----: |
|  | A | B | D | F |  |
| N | 3800 | 2652 | 4081 | 1187 | 11720 |
| Z |  |  |  | 113 | 113 |
| **Total** | **3800** | **2652** | **4081** | **1300** | **11833** |

**TABLE VIII**

PRODUCTION OF M-Z ONLY (BBLS/C.D.) *z*0 \= \$4,219 MAXIMUM

| Outputs | Inputs |  |  |  | Total |
| :---- | ----- | ----- | ----- | ----: | ----: |
|  | A | B | D | F |  |
| M | 3800 | 2652 | 4081 | 1187 | 11720 |
| Z |  |  |  | 113 | 113 |
| **Total** | **3800** | **2652** | **4081** | **1300** | **11833** |

## **PROGRAM COMPARISONS: 1-C AND 1-C AND 3-C PN'S**

The reduced systems can also, as previously noted, be used to estimate approximately the effects of changes in the matrix. Indeed, it is so simple to trace through these effects by use of the reduced systems that, to save computations, it was decided to make these estimates for the combined 1-c and 3-c programs, rather than to study each in isolation. Before discussing the sensitiveness of the matrix to changes in coefficients, it may be well to present the result of computations for the additional 3-c restrictions.31

Noting that no M was produced in the complete 1-c program comparative estimates were obtained by calculating the effect of the additional restriction on the production of *N-Q-Z*. This yielded a figure *z*0 \= \$14,172 or a reduction slightly in excess of \$1,000/c.d. resulting from the addition of the 3-c quality restriction. Inspection of the double-product reduced systems, given in Table IX, indicates that the major effect of the additional restrictions are felt in the reduction in output of Q by more than 1,100 bbls/c.d.—from 8106 to 6979 bbls/c.d. Neither N nor M shows any effect from imposition of the 3-c test requirement; indeed, M is entirely free of this restriction (see Table I). The relatively weak technology for production of Q (see the relatively low values for the PN coefficients of Q in Table III) absorbs the entire incremental strain of the additional quality restriction. The two-product systems thus provide insight into effects on the more complete systems such as *N-Q-Z* where N is increased at the expense of a drastic reduction in Q, the highest quality product.32

31 Again the reduced systems can be used to calculate upper bounds for the complete system should this prove desirable.

32 Use of the *N-Q-Z* system assumes no production of M (e.g., for goodwill purposes) is undertaken.

**TABLE IX**

PROGRAM COMPARISON BETWEEN 1-C AND 1-C AND 3-C REQUIREMENTS

| Program | Z and: | BBLS/C.D. | Receipts (\$)   |
| :---- | :---- | ----: | ----- |
| 1-c | Q | 8,106 | 12,110 |
| 1-c and 3-c | Q | 6,979 | 10,427 |
| 1-c | N | 11,720 | 10,419 |
| 1-c and 3-c | N | 11,720 | 10,419 |
| 1-c | M | 11,720 | 4,219 |
| 1-c and 3-c | M | 11,720 | 4,219 |
| 1-c | N-Q | 3726 N \+ 7985 Q | 15,249 |
| 1-c and 3-c | N-Q | 5516 N \+ 6204 Q | 14,172 |

## **PROGRAMMING FOR STRUCTURAL CHANGES**

To explore the sensitivity of the matrix, the following changes suggested by practical considerations were separately investigated: (1) reduction in RVP of D by 1 unit, (2) decrease in PN (octane) requirements of B by 1 unit on the 1-c test and 1.1 units on the 3-c test, (3) diminution of PN (octane) ratings on A by 1 unit on the 1-c test and 2 units on the 3-c test. The results of these investigations are given in Table X.

The particular coefficients studied were selected on the basis of the following criteria: (1) judgment of experienced engineers associated with refinery operations suggested that variation in these coefficients might be expected to produce marked changes in program results (as measured by net profits) and (2) the coefficients were capable of being changed in the manner (if not to the extent) indicated. The expected results did not, however, materialize. Although the changes were, generally, in the expected direction, the quantitative magnitudes were far less than had been anticipated.33

33 This suggests (along with the observations noted in footnote 26\) that so long as conditions remain stable, even under relatively complex conditions, experienced personnel by application of "insight" and "know-how" do surprisingly well in terms of optimal results. Under new or rapidly changing situations, however, even of a more simple kind than that previously experienced, results achieved by such "cut and try" methods are likely (at least for a time) to depart markedly from possible optima. Such a departure from past experience is involved in estimating the possible effects of changing coefficients. Of course, if conditions are very complex (as in programming for the whole company) there is no guarantee that marked deviations from attainable optima are not likely to remain for protracted periods. Thus, programming is likely to offer the greatest net advantage over good commercial practice under very complex or rapidly changing conditions, particularly if such changes require extension beyond the realm of past experience.

**TABLE X**

EFFECTS OF CHANGES IN SELECTED COEFFICIENTS REDUCED SYSTEMS  
1-C AND 3-C TESTS

| Decrease in Coefficients | Change in Receipts (in dollars), ±Δ*z*0 for Programs |  |  |
| :---- | ----- | ----: | ----- |
|  | Z and Q | Z and N | Z and M   |
| RVP of D by 1 | \+84 | \+84 | \+36 |
| Octane of B by 1 on 1-c and 1.1 on 3-c | −101 | 0 | 0 |
| Octane of A 1 on 1-c and 2 on 3-c | −131 | 0 | 0 |

Inspection of Table X shows that the matrix is surprisingly insensitive when compared to the magnitude of the changes which practical experience would seem to indicate might be obtained. Of course, no conclusions as to the desirability of effecting these changes can be reached without introducing additional considerations such as, (1) the incremental costs of effecting the changes and (2) the possible consequences such changes might have for other company policies and programs. It can be said, however, that in some of the cases the possible benefits or penalties are so small in magnitude as to make the problem unlikely to be worthy of extended attention by company officials. Decreasing the RVP index of D by as much as 1 unit, for example, will produce only minor increases in net receipts. On the other hand, reduction in the octane blending indexes of A has important practical operating conveniences which may far well outweigh the relatively small reduction in net receipts.

Obviously these techniques could be used to explore other problems as well. For example, it might be of interest to explore the cost of current scheduling policy. The restrictions (1b) might be changed. As now stated, they imply that program calculations are unaffected by the price (or cost accounting imputations) of these materials. Changing the equations to inequations which specified upper or lower limits to the use of such materials would alter this aspect of the problem. Given the insensitivity of the present matrix resulting from the large amount of slack allowed under current policy, it would also be interesting to explore the effects of price changes on net receipts. It might be expected that results parallel to those found in altering the quality restrictions would occur. Large relative changes in some of the prices might have no noticeable effect on net receipts. To be fully realistic, however, such calculations should include demand as well as cost considerations.

In principle, it is clear such calculations can easily be made if adequate computational facilities are available. The demonstration of this principle, and the illustration and development of methods for conducting such analyses, is the major purpose of this paper. Therefore, little would be gained by pushing the present calculations further for the blending problem presented here. More important, perhaps, than such investigations is the problem of extending the techniques of programming to the area of operations. The "budget as a document" and the "budget as a process"34 are too intimately related in practice to admit of continuous rigid separation in theory.

*Carnegie Institute of Technology*

34 This felicitous terminology was suggested by Mr. John Norton.

## **REFERENCES**

\[1\] CHARNES, A., "Mathematical Background for Linear Programming," Hectographed lecture series prepared for Carnegie Institute of Technology, Department of the Air Forces Research Project in Intra-Firm Behavior.

\[2\] CHARNES, A., "Optimality and Degeneracy," *ECONOMETRICA*, Vol. 20, April, 1952, pp. 160-170.

\[3\] COOPER, W. W., "A Proposal for Extending the Theory of the Firm," *Quarterly Journal of Economics*, Vol. 65, February, 1951, pp. 87-109.

\[4\] DANTZIG, GEORGE B., "Maximization of a Linear Form Whose Variables are Subject to a System of Linear Inequalities," Headquarters, USAAF, Nov. 1, 1949\. Reproduced in *Activity Analysis of Production and Allocation*, Cowles Commission Monograph No. 13, New York: John Wiley and Sons, 1951, pp. 19-32.

\[5\] DINES, LLOYD L., "Systems of Linear Inequalities," *Annals of Mathematics*, 2nd series, Vol. 20, 1918-19, pp. 191-199.

\[6\] KOOPMANS, T. C., ed., *Activity Analysis of Production and Allocation*, Cowles Commission Monograph No. 13, New York: John Wiley and Sons, 1951, 404 pp.

\[7\] LEONTIEF, WASSILY W., *The Structure of the American Economy, 1919-1939* (second edition), New York: Oxford University Press, 1951, 264 pp.

\[8\] WOOD, M. K., "Elements in the Design of Mathematical Models for Programming," U.S. Department of the Air Forces.
