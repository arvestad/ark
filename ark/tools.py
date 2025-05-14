'''
Supply tools for Ark.
'''

from itertools import groupby

def collect_by(a, by):
    '''
    Sort and group, in SQL style rather than itertools style.

    `a`  - an ark to work on.
    `by` - Function to group by. Consider using the `column` method.
    
    Returns an iterator containing pairs, where item 0 are the elements
    that have been returned by `by` and item 1 is an iterable containing
    rows.

    In contrast to itertools.groupby, `collect_by` is looking at all elements,
    not just adjacent elements.
    '''
    # selector = lambda r: (by(r), r) # Returns keys and rows
    # pairs = sorted(map(selector, a), key=lambda x: x[0])

    ordered = sorted(a, key=by)
    return groupby(ordered, key=lambda pair: pair[0])


        
    
