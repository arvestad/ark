import numbers
from tabulate import tabulate

class Ark:
    def __init__(self, rows=None, headers=None):
        '''
        Using `rows` parameter: instantiate object from an iterable of rows. 
                                This may be from CSV reader object or simply 
                                a list of rows.
        The `header` parameter is None by default, meaning no headers are 
        inferred. If a list of strings, then those are used as headers. If a 
        non-negative integer, then that is taken as the row with headers and
        rows before are ignored. 
        '''
        if type(rows) != list:
            rows = list(rows)
        if type(headers) == int: # Assume this is the line containing row headers.
            self.headers = rows[headers]
            first_data_line = headers + 1
            self._rows = rows[first_data_line:]
        else:
            self.headers = headers
            self._rows = rows
            

    def __iter__(self):
        return ArkRowIterator(self)

    def __getitem__(self, key):
        '''
        `key` is a header name or index
        '''
        if self.headers and key in self.headers:
            col_idx = self.headers.index(key)
            return Ark(rows=list(map(lambda lst: [lst[col_idx]], self._rows)), headers=[self.headers[col_idx]])
        elif self.headers and (type(key) == list or type(key) == tuple):
            col_indices = []
            for k in key:
                if k in self.headers:
                    col_indices.append(self.headers.index(k))
                elif type(k) == int:
                    k_idx = int(k)
                    if k_idx < 0 or k_idx > len(self.headers):
                        raise IndexError(f'Not a column header/index: {key}')
                    col_indices.append(k_idx)
                else:
                    raise IndexError(f'Not a column header/index: {key}')
            return Ark(rows=list(map(lambda lst: [lst[idx] for idx in col_indices], self._rows)),
                       headers=key)
        elif type(key) == int:
            if self.headers:
                head = [self.headers[key]]
            else:
                head = None
            print('rows:', self._rows)
            rows = list(map(lambda lst: [lst[key]], self._rows))
            return Ark(rows=rows, headers=head)
        else:
            raise IndexError(f'Not a column header/index: {key}')


    def __str__(self):
        return tabulate(self._rows, headers=self.headers, showindex=True, tablefmt='simple')

    def __repr__(self):
        return str(self)


    def __len__(self):
        return len(self._rows)


    def head(self, n_rows=10):
        return Ark(rows=self._rows[:n_rows], headers=self.headers)


    def get_row(self, idx):
        return ArkRow(self._rows[idx], headers = self.headers, ark=self)

    def add_col(self, data, header=None):
        pass


    def column(self, idx, numeric=False):
        '''
        Convenience function for creating a function accessing row elements.

        The `numeric` flag replaces empty strings and `None` values with 0.
        '''
        def isnumeric(val):
            if val == '' or val == None:
                return 0
            else:
                return val
        if numeric:
            return lambda row: isnumeric(row[idx])
        else:
            return lambda row: row[idx]
    

    def groupby(self, by, accumulator):
        '''
        Sort and group, in SQL style rather than itertools style.

        `by` - Function to group by. Consider using the `column` method.
        `accumulator` - Function that summarizes lists (etc), like `mean` and `max`.
        '''
        rows = sorted(self._rows, key=by)
        pass
        
        
    # @classmethod
    # def import(self, rows):
    #     '''Return an Ark object from an iterable of rows. This may be from CSV reader object
    #     or simply a list of rows.'''
        

    # def read_csv(cls, filename, headers=None, delimiter=','):
    #     rows = list()
        
    #     with open(filename) as h:
    #         if headers == None:
    #             line = h.readline().rstrip()
    #             headers = line.split(delimiter)

    #         for line in h:
    #             row = line.split(delimiter)
    #             rows.append(row)

    #         # Check all rows have same number of columns
    #         # and that types agree, and that headers match
    #     return Ark(rows, headers)
    
    
class ArkRow:
    '''
    '''
    def __init__(self, row, headers=None, ark=None):
        '''
        The ark that the row is extracted from is referenced.
        '''
        self._ark = ark
        self.headers = headers
        self._row = row
        self._accumulated_errors = [] # Used for collecting problems during row+row operations
        
    def __str__(self):
        if self.headers:
            table = tabulate([self._row], headers=self.headers, tablefmt='simple')
            footnotes = '\n'.join(self._accumulated_errors)
            return table + '\n' + footnotes
        else:
            return tabulate([self._row])

    def __repr__(self):
        return f'<ArkRow {self._row} headers={self.headers}>'

    def __getitem__(self, key):
        '''
        `key` is a header name or index
        '''
        if self.headers and key in self.headers:
            col_idx = self.headers.index(key)
            return self._row[col_idx]
        elif type(key) == int:
            return self._row[key]
        else:
            raise IndexError('Not a column header/index')

    def __len__(self):
        return len(self._row)

    def __eq__(self, other):
        return self._row == other._row


    def __add__(self, other, dest=None):
        if isinstance(other, numbers.Number):
            other = ArkRow([other] * len(self._row), headers=self.headers)
        if dest is None:
            dest = ArkRow([None] * len(self._row), headers=self.headers)
        for idx, (a, b) in enumerate(zip(self._row, other._row)):
            try:
                dest._row[idx] = a + b
            except TypeError:
                dest._register_error(idx, f'Cannot add types {type(a)} and {type(b)} ({a} + {b})')
                dest._row[idx] = 'N/A'
            except:
                dest._register_error(idx, f'Cannot add {a} and {b}')
                dest._row[idx] = 'N/A'                
        return dest
    
    def __iadd__(self, other):
        return self.__add__(other, self)

    def __radd__(self, other):
        res = self.__add__(other)
        return res

    
    def __truediv__(self, other, dest=None):
        if isinstance(other, numbers.Number):
            other = ArkRow([other] * len(self._row), headers=self.headers)
        if dest is None:
            dest = ArkRow([None] * len(self._row), headers=self.headers)
        for idx, (a, b) in enumerate(zip(self._row, other._row)):
            try:
                dest._row[idx] = a / b
            except TypeError:
                dest._register_error(idx, f'Cannot divide types {type(a)} and {type(b)} ({a} + {b})')
                dest._row[idx] = 'N/A'
            except:
                dest._register_error(idx, f'Cannot divide {a} by {b}')
                dest._row[idx] = 'N/A'
        return dest

    def __itruediv__(self, other):
        return self.__truediv__(other, self._row)
   
    

    def items(self):
        if self.headers:
            for head, elem in zip(self.headers, self._roq):
                yield head, elem
        else:
            for idx, elem in enumerate(self._row):
                yield idx, elem

    def _register_error(self, idx, msg):
        '''
        Collect error messages
        '''
        self._accumulated_errors.append(f'Error in column {idx}: {msg}')
        


class ArkRowIterator:
    def __init__(self, ark):
        self._ark = ark
        self._row_idx = 0

    def __next__(self):
        try:
            row = self._ark.get_row(self._row_idx)
            self._row_idx += 1
            return row
        except IndexError:
            raise StopIteration



