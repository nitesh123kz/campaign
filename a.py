with open('C:\\Users\\nitekumar\\Downloads\\data.txt','r') as f:
    lines = f.read().split('\n')
cellid={}
total=0
cust={}
for i in range(0,len(lines)):
    #print i
    lines[i]=lines[i].split('&')
    event=''
    cell=''
    customer=''
    for j in range(len(lines[i])):
            if 'tracking_event' in lines[i][j]:
                event=lines[i][j].split('=')[1]
            elif  'cell' in  lines[i][j]:
                cell=lines[i][j]
            '''elif 'custno=' in  lines[i][j]:
                customer=lines[i][j].split('=')[1]
            '''
    if not (cell in cellid.keys()):
                   cellid[cell]={'total':0}
    if event not in cellid[cell].keys():
        cellid[cell][event]=1
        cellid[cell]['total']+=1
        total+=1
    else:
        cellid[cell][event]+=1
        cellid[cell]['total']+=1
        total+=1

    
print  cellid
print len(cellid.keys()),total
'''if customer not in cust.keys():
        cust[customer]=[]
    if cell not in cust[customer]:
        cust[customer].append(cell)
for   key in  cust.keys():
    print  key,  cust[key]'''
                    

