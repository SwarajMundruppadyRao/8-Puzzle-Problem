import numpy as np
import queue

global visitednode

#Taking input for initial combination from user
def UserInput():
    print("\nEnter the initial configuration of the puzzle row wise (Enter 0 forblank tile): ")
    initialState=[]
    numbers=9
    for i in range(3):
        print("Enter the numbers in row", i+1)
        for j in range(3):
            print("Enter a number (0-8) without repeating a number. You have",numbers, "more numbers to enter.")
            value=int(input())
            if(value>8)or(value<0):
                print("Please enter a number between 0-8 only")
            else:
                initialState.append(int(value))
            numbers=numbers-1
    userinput=np.reshape(initialState, (3,3))
    initialState=np.transpose(userinput)
    return userinput,initialState


#Defining the goal combination, change this if required...
def goal():
    goalpostion=np.array([[1,2,3], [4,5,6], [7,8,0]])
    return goalpostion


#Function to get the inversion count, Reference: Geeks for Geeks
def getInvCount(arr):
    inv_count = 0
    for i in range(9):
        for j in range(i + 1, 9):
            if arr[j] != 0 and arr[i] != 0 and arr[i] > arr[j]:
                inv_count += 1
    return inv_count


#Function to check if the 8 puzzle problem is solvable or not. Reference: Geeks for Geeks
def isSolvable(puzzle):
    inv_count = getInvCount([j for sub in puzzle for j in sub])
    return (inv_count % 2 == 0)


#Creating a Node
class Node:
    def __init__(self, state, index, parent_index):
        self.state=state
        self.index=index
        self.parent_index=parent_index
    #Function to compare two nodes and determine if they are equal or not
    def __isequal__(self,othernode):
        isequal=np.array_equal(self.state, othernode.state)
        return isequal


#Function to convert the current state to a string
def __str__(self):
    string = f"{' '.join(str(item) for item in self.state.T.flatten())} \n"
    return string
#Defining all the move sequences required to perform the following moves: Up, Down, Left, Right

def ActionMoveUp(current,index):
    i,j=np.where(current.state==0)
    i,j=i[0],j[0]
    copyofcurrentstate=current.state.copy()
    temp=copyofcurrentstate[i,j]
    #Move the block up
    copyofcurrentstate[i,j]=copyofcurrentstate[i-1,j]
    copyofcurrentstate[i-1,j]=temp
    newnode=Node(copyofcurrentstate,index,current.index)
    status=False
    if tuple(map(tuple, newnode.state)) not in visited:
        status=True
    return status,newnode

def ActionMoveDown(current,index):
    i,j=np.where(current.state==0)
    i,j=i[0],j[0]
    copyofcurrentstate=current.state.copy()
    temp=copyofcurrentstate[i,j]
    #Move the block down
    copyofcurrentstate[i,j]=copyofcurrentstate[i+1,j]
    copyofcurrentstate[i+1,j]=temp
    newnode=Node(copyofcurrentstate,index,current.index)
    status=False
    if tuple(map(tuple, newnode.state)) not in visited:
        status=True
    return status,newnode

def ActionMoveLeft(current,index):
    i,j=np.where(current.state==0)
    i,j=i[0],j[0]
    copyofcurrentstate=current.state.copy()
    temp=copyofcurrentstate[i,j]
    #Move the block left
    copyofcurrentstate[i,j]=copyofcurrentstate[i,j-1]
    copyofcurrentstate[i,j-1]=temp
    newnode=Node(copyofcurrentstate,index,current.index)
    status=False
    if tuple(map(tuple, newnode.state)) not in visited:
        status=True
    return status,newnode

def ActionMoveRight(current,index):
    i,j=np.where(current.state==0)
    i,j=i[0],j[0]
    copyofcurrentstate=current.state.copy()
    temp=copyofcurrentstate[i,j]
    #Move the block right
    copyofcurrentstate[i,j]=copyofcurrentstate[i,j+1]
    copyofcurrentstate[i,j+1]=temp
    newnode=Node(copyofcurrentstate,index,current.index)
    status=False
    if tuple(map(tuple, newnode.state)) not in visited:
        status=True
    return status,newnode


#Back Tracking
def generate_path(explored,current):
    backtracking=[]
    node_info=[]
    path_str=[]
    #Initialising node to current
    node=current
    backtracking.append(node)
    path_str.append(node.__str__())
    exploredn=np.array(explored)
    Parent_Node_Index_i=node.parent_index
    index = np.where([node.index == Parent_Node_Index_i for node in exploredn])[0]
    
    while not node.index==0:
        index = np.where([node.index == Parent_Node_Index_i for node in exploredn])[0]
        node=exploredn[index[0]]
        Parent_Node_Index_i=node.parent_index
        backtracking.append(node)
        path_str.append(node.__str__())
        node_info_str = "{}\t {}\t {}\n".format(node.index,node.parent_index,node.__str__())
        node_info.append(node_info_str)
    
    #Output the backtracked node information into the no
    with open("nodePath.txt", "w") as f:
            path_str.reverse()
            f.writelines(path_str)
            
    # Write info about nodes to a text file
    node_info_str = "{}\t {}\t {}\n".format("Index", "Parent Index","State")
    node_info.append(node_info_str)
    with open("NodesInfo.txt", "w") as f:
            node_info.reverse()
            f.writelines(node_info)
    return backtracking


# Solve the given 8 puzzle problem for the given start and goal positions
def bfs(start,goal):
    import queue
    queue=queue.Queue()
    global visited
    visited=set()
    current=Node(start,0,0)
    goal=Node(goal,None,None)
    index=0
    explored=[]
    explored_str=[]
    if current.__isequal__(goal):
        pass
    else:
        queue.put(current)
        while not current.__isequal__(goal):
            if not queue.empty():
                current=queue.get()
                explored.append(current)
                explored_str.append(current.__str__())
                #Finding the Blank Tile Location
                i,j=np.where(current.state==0)
                i=i[0]
                j=j[0]
            #Check if there is space to move the blank tile up, down, left or right
            if i+1<3:
                index+=1
            #If there is space downwards, move the blank tile down and explore the new node if not visited
                status,node=ActionMoveDown(current,index)
                if status:
                    visited.add(tuple(map(tuple, node.state)))
                    queue.put(node)
            if j+1<3:
                index+=1
                #If there is space towards the right, move the blank tile right and explore the new node if not visited
                status,node=ActionMoveRight(current,index)
                if status:
                    visited.add(tuple(map(tuple, node.state)))
                    queue.put(node)
            
            if i-1>=0:
                index+=1
                #If there is space upwards, move the blank tile up and explore the new node if not visited
                status,node=ActionMoveUp(current,index)
                if status:
                    visited.add(tuple(map(tuple, node.state)))
                    queue.put(node)
            
            if j-1>=0:
                index+=1
                #If there is space towards the left, move the blank tile left and explore the new node if not visited
                status,node=ActionMoveLeft(current,index)
                if status:
                    visited.add(tuple(map(tuple, node.state)))
                    queue.put(node)
    # Write the Explored Nodes into a text file
    with open("Nodes.txt", "w") as f:
        f.writelines(explored_str)
    return generate_path(explored,current)

def main():
    print("Starting the Code")
    inputreceived, initialState=UserInput()
    goalconfiguration=goal()
    print("Entered puzzle configuration : \n",inputreceived)
    print("Goal Configuration:\n",goalconfiguration)
    # Check if the initial state is solvable, else exit program
    if isSolvable(inputreceived):
        print("The puzzle is solvable.\n"+"Solving the puzzle using BFS\n")
        bfs(inputreceived, goalconfiguration)
        print("Created all the files required to run the Animate.py file")
        print("Run Animate.py file using: python3 Animate.py command in the terminal to watch how the puzzle was solved")
    else:
        print("The puzzle is not solvable for the entered combination, Enter another configuration after running the code again.")

if __name__=='__main__':
    main()