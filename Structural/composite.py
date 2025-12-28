# when the logic can be divided into a treee like structure

# file system can have files and folders
# files individually can exist and folders can have multiple files
# which we can add and remove
# so now folder and file inherit from file system
# functionality to get the size will be different

from abc import ABC, abstractmethod

class FileSystem(ABC):
    @abstractmethod
    def getSize(self):
        pass

class File(FileSystem):
    def __init__(self, name: int, size: str):
        self.name = name
        self.size = size
    
    def getSize(self):
        return self.size

class Folder(FileSystem):
    def __init__(self, name: str):
        self.name = name
        self.children = []
        
    def addChild(self, comp: FileSystem):
        self.children.append(comp)
    
    def removeChild(self, comp: FileSystem):
        self.children.remove(comp)
    
    def getSize(self):
        # print("self.childeren : ",self.children[0].getSize())
        return sum([c.getSize() for c in self.children])
    

f1 = File('f1', 100)
f2 = File('f2', 400)

folder = Folder('ABC')
folder.addChild(f1)
folder.addChild(f2)

print("folder size ------")
print(folder.getSize())

folder.removeChild(f1)
print('new folder size ======')
print(folder.getSize())

print("f1 size : ", f1.getSize())
print("f2 size : ", f2.getSize())
