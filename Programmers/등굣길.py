def dynamics(x, y,maps,paths):
    
    
    paths[0][0]=maps[0][0]
    for i in range(1,x,1) :
        
        if(maps[i][0]==0):
            paths[i][0]=0
        else :
            
            paths[i][0]=paths[i-1][0]
    for j in range(1,y,1) :
        if(maps[0][j]==0):
            paths[0][j]=0
        else :
            paths[0][j]=paths[0][j-1]
    
    for i in range(1,x,1):
        for j in range(1,y,1):
            if(maps[i][j]==0):
                paths[i][j]=0
            else :
                paths[i][j] = (paths[i-1][j] + paths[i][j-1])% 1000000007
    
    
def solution(m, n, puddles):
    

    x = n
    y = m
    z= puddles
    maps = []
    paths =[]
    for i in range(x):
        col = [1]*y
        path=[0]*y
        
        maps.append(col)
        paths.append(path)
    for i in puddles :
        maps[i[1]-1][i[0]-1]=0
    

    dynamics(x,y,maps,paths)
    return paths[x-1][y-1]


    
