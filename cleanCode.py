# Just a reminder to import things or you will run into an error
# Example (repo must be imported)
from git import Repo



class GitOperation:
    #constructer in python
    def __init__(self,repo):
        self.repo = Repo(repo)
    
    #List Branches, need to refer to self repo as it is part of the constructure of class object
    def listBranch(self):
        for branch in self.repo.branches:
            print(branch)

    def createOrSwitchBranch(self, branchName):
        if (branchName in self.repo.branches):
            # To checkout to a branch:
            self.repo.git.checkout(branchName)
        else:
            # Create a new branch
            self.repo.git.branch(branchName)
            self.repo.git.checkout(branchName)
    def commitFile(self,filename):
       self.repo.index.add(filename)
       self.repo.index.commit(f'Updated {filename}')
       self.repo.remotes.origin.push()

    

if __name__ == "__main__":
    #object of a class or an instance of a class
    gitObject = GitOperation(repo = 'C:\ScrappingPython\scraping') 
    gitObject.listBranch()
    #gitObject.createOrSwitchBranch('TestBranch')
    gitObject.commitFile('cleanCode.py')
