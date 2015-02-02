import csv
import string

filetext = open('list.txt', 'r')
itemlist = []
filterlist = []
#inverted_name_list = []
#direct_order_name_list = []

for line in filetext:
    item = line.strip().split(',')
    inverted_name = line.strip()
    direct_order_name = item[-1] + ' ' + ' '.join(item[:-1])
    #inverted_name_list += [inverted_name.strip()]
    #direct_order_name_list += [direct_order_name.strip()]
    filterlist += ["([BIB_TEXT] contains '" + inverted_name.strip() + "' or [BIB_TEXT] contains '" + direct_order_name.strip()+ "')"]

filtertext = ' or '.join(filterlist)

print filtertext