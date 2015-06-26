import os
import fnmatch

def processlines(filetext):
    itemlist = []
    filterlist = []
    counter = 0

    for line in filetext:
        item = line.split()
        itemlist += item
        counter += 1

        if counter > 998:
            thinglist = []
            for item in itemlist:
                thinglist.append(str.zfill(item, 9))
            filterlist += ["([BIB_DOC_CHAR] in ('" + "', '".join(thinglist) + "'))"]
            itemlist = []
            counter = 0

    if counter > 0:
        thinglist = []
        for item in itemlist:
            thinglist.append(str.zfill(item, 9))
        filterlist += ["([BIB_DOC_CHAR] in ('" + "', '".join(thinglist) + "'))"]
        itemlist = []
        counter = 0

    filtertext = '\nOR\n'.join(filterlist)
    return filtertext

for file in os.listdir('.'):
    if (fnmatch.fnmatch(file, '*.txt')) and not (fnmatch.fnmatch(file, '*output.txt')):
        filetext = open(file, 'r')

        cognos = open(file[0:-4]+"_output.txt", "w")
        cognos.write(processlines(filetext))
        cognos.close()