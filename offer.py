with open('C:\\Users\\nitekumar\\Downloads\\data.txt','r') as f:
    lines = f.read().split('\n')
offer_id={}
cellid={}
for i in range(0,len(lines)):
    oid=''
    cell=''
    event=''
    lines[i]=lines[i].split('&')
    for j in range(len(lines[i])):
        if 'oid=' in lines[i][j]:
           oid=lines[i][j]
        elif 'cell' in lines[i][j]:
            cell=lines[i][j]
        elif 'tracking_event' in lines[i][j]:
            event=lines[i][j].split('=')[1]
    if not(oid in offer_id.keys()):
        offer_id[oid]={'event':{}}
    if cell not in offer_id[oid].keys():
        offer_id[oid][cell]={}
    

    if event not in offer_id[oid][cell].keys():
        offer_id[oid][cell][event]=1
    else:
        offer_id[oid][cell][event]+=1


        
    if event not in offer_id[oid]['event'].keys():
        offer_id[oid]['event'][event]=1
    else:
        offer_id[oid]['event'][event]+=1

    if not (cell in cellid.keys()):
                   cellid[cell]={'ctr':0}
    if event not in cellid[cell].keys():
        cellid[cell][event]=1
    else:
        cellid[cell][event]+=1
        

print "*********************************************"        
for x in offer_id.keys():
    for y in offer_id[x].keys():
        if  y  not in ['event']:
            try:
                offer_id[x][y]['ctr']=float(offer_id[x][y]['cl'])/float(offer_id[x][y]['im'])*100
            except:
                offer_id[x][y]['ctr']=0
        else:
            try:
                offer_id[x][y]['ctr']=float(offer_id[x][y]['cl'])/float(offer_id[x][y]['im'])*100
            except:
                offer_id[x][y]['ctr']=0
                                                                    
    
    print x,offer_id[x]
print "*********************************************"
for y in cellid.keys():
    try:
        cellid[y]['ctr']=((float)(cellid[y]['cl'])/(float)(cellid[y]['im']))*100
        print y,cellid[y]
    except:
        print y,cellid[y]
        continue
