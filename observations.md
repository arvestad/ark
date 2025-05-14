# Observations on implementing a Pythonic dataframe

## The statistics module is closed

I expected `statistics` to be implemented in an open-closed^[1] manner.
However, this module expects to work on iterables containing elements of type `int`, `float`,
`Fraction`, and `Decimal`. If one supplies another type, even if following the Python data model^[2], 
an exception is created.
This prohibits this module from being applied to a dataframe. 



[1] The open-closed principle, https://en.wikipedia.org/wiki/Open–closed_principle
[2] Data model. Python 3.11.1 documentation, https://docs.python.org/3/reference/datamodel.html