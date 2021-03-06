﻿# TOPSIS Package

TOPSIS stands for **T**echnique for **O**der **P**reference by **S**imilarity to **I**deal **S**olution.

It is a method of compensatory aggregation that compares a set of alternatives by identifying weights for each criterion, normalising scores for each criterion and calculating the geometric distance between each alternative and the ideal alternative, which is the best score in each criterion. An assumption of TOPSIS is that the criteria are monotonically increasing or decreasing.
In this Python package *Vector Normalization* has been implemented.


## Installation

$ python3 -m pip install TOPSIS_package
> Link for installation has also been provided above

## Usage

Step 1:  >>>python3 
Step 2:  >>> import TOPSIS_package as tp
Step 3:  >>>tp.topsis(*InputDataFile*,*weights*,*Impacts*)
>Note: This package will work for the Python interactive interpreter or any of the Python editor. This package will not work as command line solution. For the command line solution email at: jsunishka@gmail.com

The result will be displayed as the row number having the maximum rank. This is the result after preprocessing the data, calculating Normalized Decision Matrix, then calculating Weighted Normalized Decision Matrix, calculation of best and worst value for every feature, then calculating the *Euclidean Distance* of every row from the best and the worst ideal ideal solution followed by calculation of performance and rank.

Alongwith with the row number having best rank, the ranks for all labels(rows) is also displayed.
