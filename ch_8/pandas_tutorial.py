import pandas as pd
from StringIO import StringIO

df = pd.DataFrame({
    'name': ['Albert Einstein', 'Marie Curie', 'William Faulkner'],
    'category': ['Physics', 'Chemistry', 'Literature']
})

df = pd.DataFrame([
    {'name': 'Albert Einstein', 'category': 'Physics'},
    {'name': 'Marie Curie', 'category': 'Chemistry'},
    {'name': 'William Faulkner', 'category': 'Literature'}
])

data = " `Albert Einstein`| Physics \n`Marie Curie`| Chemistry"

df = pd.read_csv(StringIO(data),
                 sep='|',
                 names=['name', 'category'],
                 skipinitialspace=True, quotecar="`")