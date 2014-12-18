# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import csv
import string

# <codecell>

filetext = open('list.txt', 'r')
itemlist = []
filterlist = []
counter = 0

# <codecell>

for line in filetext:
    item = line.split()
    itemlist += item
    counter = counter + 1
    if counter > 998:
        thinglist = []
        for item in itemlist:
            #print string.zfill(item, 9)
            thinglist.append(string.zfill(item, 9))
        #filterlist += ["([BIB_DOC_ID] in ('" + "', '".join(itemlist) + "'))"]
        filterlist += ["([BIB_DOC_CHAR] in ('" + "', '".join(thinglist) + "'))"]
        itemlist = []
        counter = 0
filtertext = ' or '.join(filterlist)

# <codecell>

print filtertext

# <codecell>


