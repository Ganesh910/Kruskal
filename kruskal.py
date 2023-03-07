"""This program would calculate a Minimum spanning tree from a graph. It will take input as matrix where each value shows the 
weight of the edge between two nodes. If there is no edge between two vertices then the value would be 0"""


class MST:
    
    #Kruskal Method is being used here to find A Minimum spanning tree
    def __init__(self, table, nodes) -> None:
        self.table = table
        self.nodes = nodes
        self.flag = [False for i in range(nodes)]
        self.subgraphs = []

    def check_cycle(self, cord):
        #Return Boolean value for cycle formation
        
        if self.flag[cord[0]]==False and self.flag[cord[1]] == False:
            self.subgraphs.append(set(cord))
            return False

        elif self.flag[cord[0]] == True and self.flag[cord[1]] == True:
            #check cycle
            for i in range(len(self.subgraphs)):
                if cord[0] in self.subgraphs[i]:
                    index1 = i
                
                if cord[1] in self.subgraphs[i]:
                    index2 = i

            if index1==index2:
                return True

            else:
                self.subgraphs[index1] |= self.subgraphs[index2]
                self.subgraphs[index2] |= self.subgraphs[index1]
                return False

        elif self.flag[cord[0]] == True or self.flag[cord[1]] == True:
            #only one node is visited

            for i in self.subgraphs:
                if cord[0] in i or cord[1] in i:
                   i |= set(cord)
            return False

        else:
            print("Something is wrong Daya!")

    def update_flag(self, cord):
        self.flag[cord[0]] = True
        self.flag[cord[1]] = True
        pass

    def create_mst(self):
        ans_table = []

        #Checking all the nodes in ascending order
        for i in range(len(self.table)):

            #If no cycle is formed by joining these points then add them to the list
            if self.check_cycle(self.table[i][1])==False:
                ans_table.append(self.table[i])

                #update the visited nodes
                self.update_flag(self.table[i][1])
        return ans_table
    
nodes = int(input("How many nodes are there: \n"))
edge = int(input("How many edges are there: \n"))
values=[]
cord=[]
for i in range(edge):
    cordinates = tuple(map(int, input("enter nodes name (Nodes name should be 0-n)\n").split()))
    cord.append(cordinates)
    values.append(int(input("Value : \n")))

lis=list(zip(values, cord))
lis.sort()

mst = MST(lis, nodes)
new_graph = mst.create_mst()
print(new_graph)