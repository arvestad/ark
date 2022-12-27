import numbers
from tabulate import tabulate

class Ark:
    def __init__(self, rows=None, headers=None):
        self._headers = headers
        self._rows = rows

    def __iter__(self):
        return ArkRowIterator(self)

    def __getitem__(self, key):
        '''
        `key` is a header name or index
        '''
        if self._headers and key in self._headers:
            col_idx = self._headers.index(key)
            return Ark(rows=list(map(lambda lst: [lst[col_idx]], self._rows)), headers=[self._headers[col_idx]])
        elif type(key) == int:
            if self._headers:
                head = [self._headers[key]]
            else:
                head = None
            print('rows:', self._rows)
            rows = list(map(lambda lst: [lst[key]], self._rows))
            return Ark(rows=rows, headers=head)
        else:
            raise IndexError('Not a column header/index')

    def __repr__(self):
        return f'<Ark>'

    def __str__(self):
        return tabulate(self._rows, headers=self._headers, showindex=True, tablefmt='simple')

    def __len__(self):
        return len(self._rows)

    def get_row(self, idx):
        return ArkRow(self._rows[idx], headers = ark._headers, ark=self)

    def add_col(self, data, header=None):
        pass

    @classmethod
    def read_csv(cls, filename, headers=None, delimiter=','):
        rows = list()
        
        with open(filename) as h:
            if headers == None:
                line = h.readline().rstrip()
                headers = line.split(delimiter)

            for line in h:
                row = line.split(delimiter)
                rows.append(row)

            # Check all rows have same number of columns
            # and that types agree, and that headers match
        return Ark(rows, headers)
    
    
class ArkRow:
    '''
    '''
    def __init__(self, row, headers=None, ark=None):
        '''
        The ark that the row is extracted from is referenced.
        '''
        self._ark = ark
        self._headers = headers
        self._row = row
        
    def __str__(self):
        if self._ark:
            return tabulate([self._row], headers=self._ark._headers, tablefmt='simple')
        else:
            return tabulate([self._row])
        

    def __getitem__(self, key):
        '''
        `key` is a header name or index
        '''
        if self._headers and key in self._headers:
            col_idx = self._headers.index(key)
            return self._row[col_idx]
        elif type(key) == int:
            return self._row[key]
        else:
            raise IndexError('Not a column header/index')

    def __len__(self):
        return len(self._row)

    def __eq__(self, other):
        return self._rows == other._rows

    def __add__(self, other, dest=None):
        if isinstance(other, numbers.Number):
            other = ArkRow([other] * len(self._row), headers=self._headers)
        if dest is None:
            dest = ArkRow([None] * len(self._row), headers=self._headers)
        for idx, (a, b) in enumerate(zip(self._row, other._row)):
            dest._row[idx] = a + b
        return dest
    
    def __iadd__(self, other):
        return self.__add__(other, self._row)

    def __radd__(self, other):
        res = self.__add__(other)
        return res

    def items(self):
        if self._headers:
            for head, elem in zip(self._headers, self._roq):
                yield head, elem
        else:
            for idx, elem in enumerate(self._row):
                yield idx, elem


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


