import csv
filteritems = []
with open('Ladder Faculty List_AY15-16.csv', 'rb') as csvfile:
    namereader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in namereader:
         filteritems += ["([BIB_TEXT] contains '" + row[0] + ', ' +  row[1] + "' or [BIB_TEXT] contains '" + row[1] + ' ' + row[0] + "')"]
            
' or '.join(filteritems)
