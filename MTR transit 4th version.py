#data
pink=['Disneyland','Sunny Bay']
orange=['Tung Chung', 'Sunny Bay', 'Tsing Yi', 'Lai King', 'Nam Cheong', 'Olympic', 'Kowloon', 'Hong Kong']
airport=['Expo', 'Airport', 'Tsing Yi', 'Kowloon', 'Hong Kong']
red=['Tsuen Wan', 'Tai Wo Hau', 'Kwai Hing','Kwai Fong', 'Lai King', 'Mei Foo', 'Lai Chi Kok', 'Prince Edward', 'Mong Kok', 'Tsim Sha Tsui','Admiralty','Hong Kong']
brown=['Nam Cheong', 'Yuen Long']
green=['Mong Kok','Prince Edward', 'Kowloon Tong','Diamond Hill', 'Ngau Tau Kok','Kowloon Bay', 'Tiu Keng Leng']
blue=['Hong Kong', 'Admiralty', 'Fortress Hill', 'North Point','Chai Wan']
lightblue=['Lok Ma Chau','University','Sha Tin', 'Kowloon Tong','Mong Kok East']
purple=['Tseung Kwan O', 'Tiu Keng Leng', 'North Point']
wholemap=[pink,orange,airport,red,brown,green,blue, lightblue, purple]
wholemapstations=pink+orange+airport+red+brown+green+blue+lightblue+purple

#some dummy variables
originline=[]
destline=[]
interchange=[]
interchange_info=[]
intersect1=[]
line=[]


#Journey details
origin='Tseung Kwan O'
dest='Disneyland'

#function for identifying which line a station is on
def Findline(name):
    line=[]
    for i in range(0,len(wholemap)):
        for j in range(0,len(wholemap[i])):
            if name==wholemap[i][j]:
                line.append(i)
    return line

#list interchange stations and their line numbers
for i in wholemapstations:
    if wholemapstations.count(i)>1 and i not in interchange:
        interchange.append(i)
for i in interchange:
    info=[i]+ Findline(i)
    interchange_info.append(info)
print(interchange_info)
    
#Intersections you can reach with 1 intersection
def possible(name):
    poss=[]
    for i in range(0,len(interchange_info)):
        for j in range(1,len(interchange_info[i])):
            for k in name:
                if k==interchange_info[i][j]:
                    poss.append(interchange_info[i])
    return poss

def nextstations(lines):
    intersect1=[]
    change=possible([lines])
    for j in range(0,len(change)):
        for k in range(1,len(change[j])):
            intersect1.append(change[j][k])
    new=list(set(intersect1)-{lines})
    return new

def findinterchange(list1):
    for i in range(0,len(interchange_info)):
        if set(list1)&set(interchange_info[i])==set(list1):
            return interchange_info[i][0]
        

#identify which line the origin and dest are on
originline0=Findline(origin)
destline=Findline(dest)
print('Origin is on line '+str(originline0), 'Destination is on line ' + str(destline))
if set(originline0)&set(destline)!=set():
    print('Direct path exists')
    raise SystemExit

done=False
path=[]
originline=originline0
for i in originline:
    new=nextstations(i)
    for m in range(0,len(new)):
        path.append([i]) ######
        path[m].append(new[m])
    for m in range(0,len(path)):
        if set(destline)&set(path[m])!=set():
            print('The lines required to take are '+ str(path[m]))
            finalpath=path[m]
            stations=[]
            for a in range(0,len(finalpath)-1):
                stations.append(findinterchange([finalpath[a],finalpath[a+1]]))
            print('The interchange stations required are '+ str(stations))
            raise SystemExit     
    originline=new
    path=[]
    n=0
    for j in originline:
        new=nextstations(j)
        for m in range(0,len(new)):
            path.append([i,j])  #####
            path[m+n].append(new[m])
        n=len(path)
        for m in range(0,len(path)):
            if set(destline)&set(path[m])!=set():
                    print('The lines required to take are '+ str(path[m]))
                    finalpath=path[m]
                    stations=[]
                    for a in range(0,len(finalpath)-1):
                        stations.append(findinterchange([finalpath[a],finalpath[a+1]]))
                    print('The interchange stations required are '+ str(stations))
                    raise SystemExit
        originline=new
        path=[]
        n=0
        for k in originline:
            new=nextstations(k)
            for m in range(0,len(new)):
                path.append([i,j,k]) ####
                path[m+n].append(new[m])
            n=len(path)
            for m in range(0,len(path)):
                if set(destline)&set(path[m])!=set():
                        print('The lines required to take are '+ str(path[m]))
                        finalpath=path[m]
                        stations=[]
                        for a in range(0,len(finalpath)-1):
                            stations.append(findinterchange([finalpath[a],finalpath[a+1]]))
                        print('The interchange stations required are '+ str(stations))
                        raise SystemExit
print('More than 4 intersections required, I am pretty sure this is impossible on this map.')

