EAST=1
WEST=2
NORTH=3
SOUTH=4

dise=[0]*6

def moveDise(myDise,direction):
    tmpDise=dise[:]
    if direction == EAST:
        myDise[0]=tmpDise[3]
        myDise[2]=tmpDise[0]
        myDise[3]=tmpDise[5]
        myDise[5]=tmpDise[2]
    elif direction == WEST:
        myDise[0]=tmpDise[2]
        myDise[2]=tmpDise[5]
        myDise[3]=tmpDise[0]
        myDise[5]=tmpDise[3]        
    elif direction == NORTH:
        myDise[0]=tmpDise[4]
        myDise[1]=tmpDise[0]
        myDise[4]=tmpDise[5]
        myDise[5]=tmpDise[1]
    elif direction == SOUTH:
        myDise[0]=tmpDise[1]
        myDise[1]=tmpDise[5]
        myDise[4]=tmpDise[0]
        myDise[5]=tmpDise[4]
    
N,M,y,x,K = map(int,input().split())
myMap = []

for _ in range(N):
    node=list(map(int,input().split()))
    myMap.append(node)
orderList=map(int,input().split())
for direction in orderList:
    tmpX=x
    tmpY=y

    try:
        if direction == EAST:
            tmpX+=1
        elif direction == WEST:
            tmpX-=1
        elif direction == NORTH:
            tmpY-=1
        elif direction == SOUTH:
            tmpY+=1
        if tmpX<0 or tmpY<0:
            raise Exception()
        floor=myMap[tmpY][tmpX]
        moveDise(dise,direction)
        if floor == 0:
            myMap[tmpY][tmpX]=dise[5]
        else:
            dise[5]=floor
            myMap[tmpY][tmpX]=0
        print(dise[0])        
        x=tmpX
        y=tmpY        
    except: pass