from git import Repo

existing_repo = Repo('C:\ScrappingPython\scraping')

#Prints the Repo
print(existing_repo)

# List all branches
for branch in existing_repo.branches:
    print(branch)

print("development" in existing_repo.branches)

# go into py envirmoent
# .\activate
# cd into folder
# run python file


    
         

        