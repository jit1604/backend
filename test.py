





class mylist():

    def __init__(self,name):

        self.name = name
        self.grp = {}

    def add(self,thing,num):

        if thing in self.grp:
            self.grp[thing] += num
            return thing + " has been increased by " + str(num)

        else:
            self.grp[thing] = num
            return thing + " has been added for " + str(num) + "pieces"

    def remove(self,thing,*num):

        if thing not in self.grp:
            return thing + " does not exist in list"

        if thing in self.grp and len(num) == 1:
            if num[0] > self.grp[thing]:
                x = self.grp[thing]
                del self.grp[thing]
                return thing + " only exists in " + str(x) + " quantity"
            else:
                self.grp[thing] -= num[0]
                return thing + " removed in " + str(num[0]) + " quantity"

        del self.grp[thing]
        return thing + " removed completely"


    def find(self,thing):
        if thing in self.grp:
            return thing,self.grp[thing]
        return thing + " is not in list"











    
            

    
        
