from collections import deque
def solution(maps):
    cnt =0
    root_node = [0,0,cnt+1] # x y value
    height = len(maps)
    width = len(maps[0])
    target = [len(maps),len(maps[0])]
    queue = []

    queue=deque(queue)

    queue.append(root_node)
    maps[0][0]=0

    while queue :
        item = queue.popleft()
        x= item[0]+1
        y = item[1]
        value = item[2]
        if(x<height) :
            if (maps[x][y]==1):
            
                if(x==(height-1)) & (y==width-1):
                    return value+1
            
                maps[x][y] =0
                queue.append([x,y,value+1])
        x= item[0]-1
        y = item[1]    
        if(x>=0) :
            if (maps[x][y]==1):
            
                if(x==(height-1)) & (y==width-1):
                    return value+1
                maps[x][y] =0
                queue.append( [x,y,value+1])
        
        x= item[0]
        y = item[1]+1    
        if(y<width) :
            if (maps[x][y]==1):
            
                if(x==(height-1)) & (y==width-1):
                    return value +1
                maps[x][y] =0
                queue.append([x,y,value+1])
        
        x= item[0]
        y = item[1] -1    
        if(y>=0) :
            if (maps[x][y]==1):
                if(x==(height-1)) & (y==(width-1)):
                    return value+1
                maps[x][y] =0
                queue.append([x,y,value+1])
    return -1
    
    
    
    


    

    

    
