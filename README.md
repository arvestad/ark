# ark: Experiments with a "pythonic" dataframe

Pandas is huge black box that (in my opinion) does not sit well within the rest of Python. While it
is integrating various modules (matplotlib, for example), one cannot easily just apply functions to
a pandas dataframe like one does with lists and dicts. I am constantly surprised that expressions I
write are not working as expected and a lot of panda programming (mine as well as others) seems to
depend on frequent internet searching and trial and error.

In this project, I investigate whether it is possible to design a dataframe
that feels like an addition to lists, dicts, etc, rather than a universe in
itself.

"ark" is the Swedish word for "sheet" (as in spreadsheet). 

## Goals

The main design goal is to get a datastructure that behaves and feels like any other
datastructure in Python. Efficiency is (as I understand it) a design goal for other
dataframes, but efficiency is subordinate to working well with Python's standard
modules.

* Iteration over rows and columns should be easy.
* Use of functional programming constructs (`map`, `filter`, `reduce`, `groupby`, etc) should mostly just work.
* Standard operations like `sum`, `min`, `mean`, etc, should work.
* If a function/method works on lists, it ought to work on ark.
* The ark dataframe should only define a small number of methods. 

I would like to be able to write expressions like below.

```
from ark import Ark
import csv

with open('file.csv') as h:
	df = Ark.import(h)
print(mean(df))

m = mean(groupby(df, column(3))
print(m)
```

