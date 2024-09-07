# N a m e   :裴鲲鹏
# Student ID:202100172014
# Date&Time :2022/10/28 18:52


def showGraph(linkList):
    for vert in linkList:
        for n in vert.getNeighbor():
            print("%s --> %s  lenth：%s"%(vert.getValue(),n,vert.getWightTo(n)))
class vertix:
    def __init__(self,v):
        self.value=v
        self.neighbor={}
        self.D=float("inf")
    def getValue(self):
        return  self.value
    def getNeighbor(self):
        return self.neighbor.keys()
    def addNeighbor(self,v,w):
        self.neighbor[v]=w
    def getWightTo(self,v):
        return self.neighbor[v]
    def getD(self):
        return self.D
    def setD(self,newD):
        self.D=newD

import heapq
class dijkstra:
    def __init__(self,gragh):
        self.gragh=gragh
    def getMinPath(self,start):
        for i,node in enumerate(self.gragh): # enumerate将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列
            node.setD(i)
        self.gragh[start].setD(0)
        #创建二叉堆
        mydata=[[node.getD(),node.getValue()] for node in self.gragh]
        heapq.heapify(mydata)
        #优先队列中以D为键建立优先级
        while mydata:
            key,thisIndex=heapq.heappop(mydata)
            thisNode=self.gragh[thisIndex]
            for neibor in self.gragh[thisIndex].getNeighbor():
                self.gragh[neibor].setD(min(self.gragh[neibor].getD(),thisNode.getD()+thisNode.getWightTo(neibor)))
            tempData=[]
            for node in mydata:
                tempVer=self.gragh[node[1]]
                heapq.heappush(tempData,[tempVer.getD(),tempVer.getValue()])
            mydata=tempData
        res=[]
        for ver in self.gragh:
            res.append(ver.getD())
        return res


if __name__ == '__main__':
    G = {'0': {1: 12, 5: 16, 6: 14},
         '1': {0: 12, 2: 10, 5: 17},
         '2': {1: 10, 3: 3, 4: 5, 5: 6},
         '3': {2: 3, 4: 4},
         '4': {2: 5, 3: 4, 5: 2, 6: 8},
         '5': {0: 16, 1: 17, 2: 6, 4: 2, 6: 1 },
         '6': {0: 14, 4: 8, 5: 1}}
    l, inputData= [], []
    for i in G:
        l.append(G[i])
    for i in range(len(l)):
        inputData.append(list(l[i].items()))
    #构造邻接表
    linkList=[]
    for i in range(len(inputData)):
        thisVerix=vertix(i)
        for v,w in inputData[i]:
            thisVerix.addNeighbor(v,w)
        linkList.append(thisVerix)
    showGraph(linkList)
    myDijstrs=dijkstra(linkList)
    print("result of the smallest path starting from node 'zero':")
    print(myDijstrs.getMinPath(0))

