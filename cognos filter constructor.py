# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import csv
filetext = open('list.txt', 'r')
textlist = []
filterlist = []
counter = 0

# <codecell>

for line in filetext:
    item = line.split()
    #print item
    textlist += item
    counter = counter + 1
    if counter > 998:
        counter = 0
        filterlist += ["[BIB_DOC_ID] in ('" + "', '".join(textlist) + "')"]
        textlist = []

# <codecell>

filtertext = ' or '.join(filterlist)

# <codecell>

filtertext

# <codecell>


