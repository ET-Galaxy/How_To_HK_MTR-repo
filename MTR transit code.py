def RequiredPath(origin, dest):
    pink=['Disneyland','Sunny Bay']
    orange=['Tung Chung', 'Sunny Bay', 'Tsing Yi', 'Lai King', 'Nam Cheong', 'Olympic', 'Kowloon', 'Hong Kong']
    airport=['Expo', 'Airport', 'Tsing Yi', 'Kowloon', 'Hong Kong']
    red=['Tsuen Wan', 'Tai Wo Hau', 'Kwai Hing','Kwai Fong', 'Lai King', 'Mei Foo', 'Lai Chi Kok', 'Prince Edward', 'Mong Kok', 'Tsim Sha Tsui','Admiralty','Hong Kong']
    brown=['Nam Cheong', 'Yuen Long']
    green=['Mong Kok','Prince Edward', 'Kowloon Tong','Diamond Hill', "Choi Hung",'Ngau Tau Kok','Kowloon Bay', 'Tiu Keng Leng']
    blue=['HKU','Hong Kong', 'Admiralty', "Tin Hau",'Fortress Hill', 'North Point','Chai Wan']
    lightblue=['Lok Ma Chau','University','Sha Tin', 'Kowloon Tong','Mong Kok East', 'Exhibition Centre', 'Admiralty']
    purple=['Tseung Kwan O', 'Tiu Keng Leng', 'North Point']
    wholemap=[pink,orange,airport,red,brown,green,blue, lightblue, purple]
    wholemapstations=pink+orange+airport+red+brown+green+blue+lightblue+purple
    colors={0: 'pink', 1: 'orange', 2: 'airport', 3: 'red', 4: 'brown', 5: 'green', 6: 'blue', 7: 'lightblue', 8: 'purple'}

    #some dummy variables
    originline=[]
    destline=[]
    interchange=[]
    interchange_info=[]
    intersect1=[]
    line=[]

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
        return('Direct path exists')
    else:
        # First iteration without list of lists
            path=[]
            for i in originline0:
                new=nextstations(i)
                for m in new:
                    path.append([i, m])
            for i in path:
                if set(destline)&set(i)!=set():
                    return("Take the following lines "+str([colors[no] for no in i]))
            originline0=path.copy()
        #Second iteration onwards with lists of lists
            while True:
                path=[]
                for i in originline0:
                    new=nextstations(i[-1])
                    for m in new:
                        path.append(i+[m])
                for i in path:
                    if set(destline)&set(i)!=set():
                        return("Take the following lines "+str([colors[no] for no in i]))
                originline0=path.copy()
print(RequiredPath("Disneyland", "Tseung Kwan O"))
