# **CHAPTER 3**

A Maximum Profit Running Plan Problem

Running plans that will assure maximum possible profit can be prepared by the simplex method of linear programming. An example pertaining to a special form of the running plan problem was prepared by Charnes, Cooper, and Mellon (6) in their integrated oil company study. An example of the general form of preparing a running plan is given herewith.  
A refinery has four different crudes available in stated quantities and wishes to meet given requirements for four different products. One of the crudes can be run alternately either for fuel products or for lube distillate. The product yields and the profit for each crude operation are given. The objective is to make a selection of crude oils which will meet product requirements with maximum possible profit.

### **TABLEAU I**

| Basis | A | B | C1 | C2 | D | XA | XB | XC | XD | XG | XH | XL | XF | Z | Q   |
| :---- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| **XA** | 1 |  |  |  |  | 1 |  |  |  |  |  |  |  |  | 100 |
| **XB** |  | 1 |  |  |  |  | 1 |  |  |  |  |  |  |  | 100 |
| **XC** |  |  | 1 | 1 |  |  |  | 1 |  |  |  |  |  |  | 200 |
| **XD** |  |  |  |  | 1 |  |  |  | 1 |  |  |  |  |  | 100 |
| **XG** | 0.6 | 0.5 | 0.4 | 0.4 | 0.3 |  |  |  |  | 1 |  |  |  |  | 170 |
| **XH** | 0.2 | 0.3 | 0.2 | 0.1 | 0.3 |  |  |  |  |  | 1 |  |  |  | 85 |
| **XL ←** |  |  |  | 0.2 |  |  |  |  |  |  |  | 1 |  |  | 20 |
| **XF** | 0.2 | 0.2 | 0.1 | 0.2 | 0.3 |  |  |  |  |  |  |  | 1 |  | 85 |
| **Z** | \-10 | \-20 | \-15 | \-25 ↓ | \-7 |  |  |  |  |  |  |  |  | 1 | 0 |

Tableau I contains a complete statement of the problem. The four crudes, A, B, C, and D, are available in quantities Q of 100, 100, 200, and 100 Mbpw respectively. The desired products, G, H, L, and F, have requirements of 170, 85, 20, and 85 Mbpw respectively. The yields for each crude are shown as decimal fractions and the negative profit as cents per barrel listed in the column for each crude. The vectors XA, XB, XC, and XD represent the respective crudes not run, and the vectors XG, XH, XL, and XF represent the respective product requirements not met. The matrix table is a basic feasible solution and indicates that no crudes are being run and no product requirements are met. The profit Z is 0\.  
The next feasible solution (No. 2\) of the problem is selected by introducing the column showing the largest negative Z value as a row in the matrix. This is column C2 with a Z value of \-25. The row in the first matrix which is to be replaced is determined by the minimum ratio of Q to C2, using only positive values. This is row XL with a ratio of 20/0.2 \= 100\. Column C2 and row XL are marked with arrows. This means that crude operation C2 will be run to meet all of the lube distillate requirements. This is done preferentially because it is the most profitable operation. The new matrix is set up as follows, with identity columns for the common vectors.

| Basis | A | B | C1 | C2 | D | XA | XB | XC | XD | XG | XH | XL | XF | Z | Q   |
| :---- | :---- | :---- | :---- | ----- | :---- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| **XA** | .... | .... | .... | .... | .... | 1 | .... | .... | .... | .... | .... | .... | .... | .... | .... |
| **XB** | .... | .... | .... | .... | .... | .... | 1 | .... | .... | .... | .... | .... | .... | .... | .... |
| **XC** | .... | .... | .... | .... | .... | .... | .... | 1 | .... | .... | .... | .... | .... | .... | .... |
| **XD** | .... | .... | .... | .... | .... | .... | .... | .... | 1 | .... | .... | .... | .... | .... | .... |
| **XG** | .... | .... | .... | .... | .... | .... | .... | .... | .... | 1 | .... | .... | .... | .... | .... |
| **XH** | .... | .... | .... | .... | .... | .... | .... | .... | .... | .... | 1 | .... | .... | .... | .... |
| **C2** | .... | .... | .... | 1 | .... | .... | .... | .... | .... | .... | .... | 5 | .... | .... | 100 |
| **XF** | .... | .... | .... | .... | .... | .... | .... | .... | .... | .... | .... | .... | 1 | .... | .... |
| **Z** | .... | .... | .... | .... | .... | .... | .... | .... | .... | .... | .... | .... | .... | 1 | .... |

Row C2 is also completed by dividing each element in the XL row of matrix 1 by XLC2, thus obtaining 0.2/0.2 \= 1, 1/0.2 \= 5 and 20/0.2 \= 100 respectively for the C2, XL and Q elements in matrix 2\.  
The columns C2, XL, and Q now require correction. Since column C2 is an identity vector, all other elements in this column are 0\. Column XL is corrected as follows:  
(XAXL)2 \= (XAXL)1 \- (C2XL)2 (XAC2)1 \= 0 \- 5 × 0 \= 0  
(XBXL)2 \= (XBXL)1 \- (C2XL)2 (XBC2)1 \= 0 \- 5 × 0 \= 0  
(XCXL)2 \= (XCXL)1 \- (C2XL)2 (XCC2)1 \= 0 \- 5 × 1 \= \-5  
(XDXL)2 \= (XDXL)1 \- (C2XL)2 (XDC2)1 \= 0 \- 5 × 0 \= 0  
(XGXL)2 \= (XGXL)1 \- (C2XL)2 (XGC2)1 \= 0 \- 5 × 0.4 \= \-2  
(XHXL)2 \= (XHXL)1 \- (C2XL)2 (XHC2)1 \= 0 \- 5 × 0.1 \= \-0.5  
(XFXL)2 \= (XFXL)1 \- (C2XL)2 (XFC2)1 \= 0 \- 5 × 0.2 \= \-1

(ZXL)2 \= (ZXL)1 \- (C2XL)2 (ZC2)1 \= 0 \- 5 × (-25) \= 125  
and column Q is corrected as follows:  
(XAQ)2 \= (XAQ)1 \- (C2Q)2 (XAC2)1 \= 100 \- 100 × 0 \= 100  
(XBQ)2 \= (XBQ)1 \- (C2Q)2 (XBC2)1 \= 100 \- 100 × 0 \= 100  
(XCQ)2 \= (XCQ)1 \- (C2Q)2 (XCC2)1 \= 200 \- 100 × 1 \= 100  
(XDQ)2 \= (XDQ)1 \- (C2Q)2 (XDC2)1 \= 100 \- 100 × 0 \= 100  
(XGQ)2 \= (XGQ)1 \- (C2Q)2 (XGC2)1 \= 170 \- 100 × 0.4 \= 130  
(XHQ)2 \= (XHQ)1 \- (C2Q)2 (XHC2)1 \= 85 \- 100 × 0.1 \= 75  
(XFQ)2 \= (XFQ)1 \- (C2Q)2 (XFC2)1 \= 85 \- 100 × 0.2 \= 65  
(ZQ)2 \= (ZQ)1 \- (C2Q)2 (ZC2)1 \= 0 \- 100(-25) \= 2500  
All other columns remain unchanged. The new matrix for feasible solution No. 2 is completed as follows:

### **TABLEAU II**

| Basis | A | B | C1 | C2 | D | XA | XB | XC | XD | XG | XH | XL | XF | Z | Q   |
| :---- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| **XA** | 1 |  |  |  |  | 1 |  |  |  |  |  |  |  |  | 100 |
| **XB ←** |  | 1 ↓ |  |  |  |  | 1 |  |  |  |  |  |  |  | 100 |
| **XC** |  |  | 1 |  |  |  |  | 1 |  |  |  | \-5 |  |  | 100 |
| **XD** |  |  |  |  | 1 |  |  |  | 1 |  |  |  |  |  | 100 |
| **XG** | 0.6 | 0.5 | 0.4 |  | 0.3 |  |  |  |  | 1 |  | \-2 |  |  | 130 |
| **XH** | 0.2 | 0.3 | 0.2 |  | 0.3 |  |  |  | .... |  | 1 | \-0.5 |  |  | 75 |
| **C2** |  |  |  | 1 |  |  |  |  |  |  |  | 5 |  |  | 100 |
| **XF** | 0.2 | 0.2 | 0.1 |  | 0.3 |  |  |  |  |  |  | \-1 | 1 |  | 65 |
| **Z** | \-10 | \-20 | \-15 |  | \-7 |  |  |  |  |  |  | 125 |  | 1 | 2500 |

As the tableau shows, the profit for running 100 Mbpw of crude C to meet the 20 Mbpw of lube distillate requirements is 2500 (1000/100) \= \$25,000 per week.

Remaining are 400 Mbpw of available crudes and requirements for G, H, and F products of 130, 75, and 65 Mbpw respectively. The next feasible solution is determined by inspection of the matrix table. Column B contains the largest negative Z value of \-20, and row XB shows the smallest Q to B ratio of 100/1 \= 100\. The new matrix, Tableau III, is set up as before.  
As shown, the profit for running 200 Mbpw of crudes B and C is 4500 (1000/100) \= \$45,000 per week. Remaining are 300 Mbpw of crudes A, C, and D and requirements for G, H, and F products of 80, 55, and 45 Mbpw respectively. Column C1 is introduced next (ZC1 \= \-15) and row XC is removed (Q/C1 \= 100). Tableau IV, the new matrix, is set up as before.

### **TABLEAU III**

| Basis | A | B | C1 | C2 | D | XA | XB | XC | XD | XG | XH | XL | XF | Z | Q   |
| :---- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| **XA** | 1 |  |  |  |  | 1 |  |  |  |  |  |  |  |  | 100 |
| **B** |  | 1 |  |  |  |  | 1 |  |  |  |  |  |  |  | 100 |
| **XC ←** |  |  | 1 ↓ |  |  |  |  | 1 |  |  |  | \-5 |  |  | 100 |
| **XD** |  |  |  |  | 1 |  |  |  | 1 |  |  |  |  |  | 100 |
| **XG** | 0.6 |  | 0.4 |  | 0.3 |  | \-0.5 |  |  | 1 |  | \-2 |  |  | 80 |
| **XH** | 0.2 |  | 0.2 |  | 0.3 |  | \-0.3 |  |  |  | 1 | \-0.5 |  |  | 55 |
| **C2** |  |  |  | 1 |  |  |  |  |  |  |  | 5 |  |  | 100 |
| **XF** | 0.2 |  | 0.1 |  | 0.3 |  | \-0.2 |  |  |  |  | \-1 | 1 |  | 45 |
| **Z** | \-10 |  | \-15 |  | \-7 |  | 20 |  |  |  |  | 125 |  | 1 | 4500 |

### **TABLEAU IV**

| Basis | A | B | C1 | C2 | D | XA | XB | XC | XD | XG | XH | XL | XF | Z | Q   |
| :---- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| **XA** | 1 |  |  |  |  | 1 |  |  |  |  |  |  |  |  | 100 |
| **B** |  | 1 |  |  |  |  | 1 |  |  |  |  |  |  |  | 100 |
| **C1** |  |  | 1 |  |  |  |  | 1 |  |  |  | \-5 |  |  | 100 |
| **XD** |  |  |  |  | 1 |  |  |  | 1 |  |  |  |  |  | 100 |
| **XG ←** | 0.6 ↓ |  |  |  | 0.3 |  | \-0.5 | \-0.4 |  | 1 |  |  |  |  | 40 |
| **XH** | 0.2 |  |  |  | 0.3 |  | \-0.3 | \-0.2 |  |  | 1 | 0.5 |  |  | 25 |
| **C2** |  |  |  | 1 |  |  |  |  |  |  |  | 5 |  |  | 100 |
| **XF** | 0.2 |  |  |  | 0.3 |  | \-0.2 | \-0.1 |  |  |  | \-0.5 | 1 |  | 25 |
| **Z** | \-10 |  |  |  | \-7 |  | 20 | 15 |  |  |  | 50 |  | 1 | 6000 |

As shown, the profit for running 300 Mbpw of crudes B and C is 6000 (1000/100) \= \$60,000 per week. Remaining are 200 Mbpw of crudes A and D and requirements for G, H, and F products of 40, 25, and 25 Mbpw respectively. Column A is introduced next (ZA \= \-10), and row XG is removed (Q/A \= 67). The new matrix is set up as before.  
As Tableau V shows, the profit for running 367 Mbpw of crudes A, B, and C is 6667 (1000/100) \= \$66,670 per week. Remaining are 133 Mbpw of crudes A and D and requirements for H and F products of 12 and 18 Mbpw respectively. Column D is introduced (ZD \= \-2), and row XH is removed (Q/D \= 58). The new matrix is set up as before.

### **TABLEAU V**

| Basis | A | B | C1 | C2 | D ↓ | XA | XB | XC | XD | XG | XH | XL | XF | Z | Q   |
| :---- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| **XA** |  |  |  |  | \-0.5 | 1 | 5/6 | 2/3 |  | \-5/3 |  |  |  |  | 33 |
| **B** |  | 1 |  |  |  |  | 1 |  |  |  |  |  |  |  | 100 |
| **C1** |  |  | 1 |  |  |  |  | 1 |  |  |  | \-5 |  |  | 100 |
| **XD** |  |  |  |  | 1 |  |  |  | 1 |  |  |  |  |  | 100 |
| **A** | 1 |  |  |  | 0.5 |  | \-5/6 | \-2/3 |  | 5/3 |  |  |  |  | 67 |
| **XH ←** |  |  |  |  | 0.2 |  | \-1/30 | \-1/15 |  | \-1/3 | 1 | 0.5 |  |  | 12 |
| **C2** |  |  |  | 1 |  |  |  |  |  |  |  | 5 |  |  | 100 |
| **XF** |  |  |  |  | 0.25 |  | \-7/60 | \-2/15 |  | \-1/6 |  | \-0.5 | 1 |  | 18 |
| **Z** |  |  |  |  | \-2 |  | 35/3 | 25/3 |  | 50/3 |  | 50 |  | 1 | 6667 |

Since there are no negative values in the Z row, Tableau VI, this case represents a maximum profit feasible solution. The profit is 6783 (1000/100) \= \$67,830 per week.

### **TABLEAU VI (Optimal Solution)**

| Basis | A | B | C1 | C2 | D | XA | XB | XC | XD | XG | XH | XL | XF | Z | Q   |
| :---- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| **XA** |  |  |  |  |  | 1 | 3/4 | 1/4 |  | \-2.5 | 2.5 | 2.5 |  |  | 62 |
| **B** |  | 1 |  |  |  |  | 1 |  |  |  |  |  |  |  | 100 |
| **C1** |  |  | 1 |  |  |  |  | 1 |  |  |  | \-5 |  |  | 100 |
| **XD** |  |  |  |  |  |  | 1/6 | 5/6 | 1 | 5/3 | \-5 | \-5 |  |  | 42 |
| **A** | 1 |  |  |  |  |  | \-3/4 | \-1/4 |  | 2.5 | \-2.5 | \-2.5 |  |  | 38 |
| **D** |  |  |  |  | 1 |  | \-1/6 | \-5/6 |  | \-5/3 | 5 | 5 |  |  | 58 |
| **C2** |  |  |  | 1 |  |  |  |  |  |  |  | 5 |  |  | 100 |
| **XF** |  |  |  |  |  |  | \-3/40 | 3/40 |  | 1/4 | \-5/4 | \-5/4 | 1 |  | 4 |
| **Z** |  |  |  |  |  |  | 34/3 | 20/3 |  | 40/3 | 10 | 60 |  | 1 | 6783 |

The following table shows the disposition of available crudes in this solution:

| Products Mbpw | Crudes Mbpw |  |  |  |  | Product Not Made | Total Required |
| :---- | :---: | :---: | :---: | :---: | :---: | ----- | ----- |
|  | A | B | C1 | C2 | D |  |  |
| **G** | 22 | 50 | 40 | 40 | 18 | 0 | 170 |
| **H** | 7 | 20 | 30 | 10 | 18 | 0 | 85 |
| **L** | 0 | 0 | 0 | 20 | 0 | 0 | 20 |
| **F** | 4 | 20 | 20 | 20 | 17 | 4 | 85 |
| **Crude not used** | 62 | 0 | 0 | 0 | 42 |  |  |
| **Total crude** | 100 | 100 | 100 | 100 | 100 |  |  |

With the given crude slate the requirements for products G, H, and L are met, but it is not economical to meet quite all of the requirements for product F. Of course, more of crude D could be used to displace the other crudes in order to increase the yield of product F with some loss of profit. Other methods would include the use of different crudes having high F yield, the purchase of product F for resale, and reducing the percentage of product F required.