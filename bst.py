#file system on a computer
# goole dirve
# a tree a nonlinear data structure with heirarchical relationship b/w its element without having any 
#cycle ,it is basically reversed from real life tree
 #Quicker  and Easier acess to the data
# store hierarchical data like folder structure organization sturcture, XML/HTML data  
# there are many different type of data structure which perform 
# root : top node without parent 
# edge:a link b/w parent and breakpoint
# leaf : a node which does not have 
# sibling childern of same parent
# ancestor parent ,gradparent,great grand parent of node
class Tree:
    def __init__(self,data):
        self.data=data
        self.children=[]

    def addchild(self,node):
        self.children.append(node)

    def __str__(self,level=0):
        ret=" "*level+str(self.data)+"\n"
        for child in self.children:
            ret += child.__str__(level+1)
        return ret

      
# rootobj=Tree("Drinks")
# hot=Tree("Hot") 
# cold=Tree('Cold')
# rootobj.addchild(hot)
# rootobj.addchild(cold)

# tea=Tree("tea")
# coffee=Tree("Coffee")
# hot.addchild(tea)
# hot.addchild(coffee)

# nonalcholic=Tree("Non-alcholic")
# alcholic=Tree('alcholic')
# cold.addchild(nonalcholic)
# cold.addchild(alcholic)



rootobj=Tree("N1")
N2=Tree("N2")
N3=Tree("N3")
rootobj.addchild(N2)
rootobj.addchild(N3)

N4=Tree("N4")
N5=Tree("N5")
N2.addchild(N4)
N2.addchild(N5)

N6=Tree("N6")
N7=Tree("N7")
N3.addchild(N6)
N3.addchild(N7)

N9=Tree("N9")
N10=Tree("N10")
N4.addchild(N9)
N4.addchild(N10)
print(rootobj)


