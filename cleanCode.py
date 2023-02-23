# Just a reminder to import things or you will run into an error
# Example (repo must be imported)
from git import Repo
import os
import argparse



# C:\ScrappingPython\scraping
class GitOperation:
    #constructer in python
    def __init__(self,repo_url):
        self.repo_url = repo_url
        self.repo_dir = repo_url.split("/")[-1].split(".")[0]
        self.repo = self.clone()
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
   
    def gitLogCommits(self,branchname):
        print('git log commits for branch: ',branchname)
        commits = self.repo.iter_commits(branchname)

        for commit in commits:
            print('*'*50)
            print("Commit id: ",commit,'\nCommit stats: ', commit.stats.files,"\nCommit Author: ", commit.author,"\nCommmit Commiter: ", commit.committer,"\nCommit Message: ", commit.message, "\nCommit Date:", commit.committed_datetime,) # will print the date and time in which the commit made.
            print('*'*50)

    def list_files(self):
        print([item.path for item in self.repo.tree().traverse() if item.type == "blob"])


    def read_file(self, file_path):
        file_path = os.path.join(self.repo_dir, file_path)
        print('*'*50)
        print('Printing File Content: ')
        print('*'*50)
        with open(file_path, "r") as file:
            print(file.read())
            print('*'*50)

    def clone(self):
        if not os.path.exists(self.repo_dir):
            print('Cloning the Repository')
            try:
                Repo.clone_from(self.repo_url, self.repo_dir)
            except: 
                print('Repo Not found')
                return None
        print('Connected with the repository')  
        return(Repo(self.repo_dir))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("repo_url", type=str, help="URL of the repository to scrape")
    args = parser.parse_args() 
    gitObject = GitOperation(args.repo_url)
    #print(gitObject.repo == None) 
    #object of a class or an instance of a class
    #gitObject = GitOperation(repo_url = 'C:\ScrappingPython\scraping') 
    #gitObject = GitOperation(repo_url = 'https://github.com/oleend/actions.git') 
    if gitObject.repo:
        gitObject.listBranch()
        gitObject.createOrSwitchBranch('main')
        #gitObject.commitFile('cleanCode.py')
        gitObject.list_files()
        gitObject.read_file('README.md')
    #existing_repo = Repo('C:\ScrappingPython\scraping')
    #gitObject.gitLogCommits('test')
    #gitObject.gitLogCommits('development')


    