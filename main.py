# Summary:
# Mass Github repo cloner coded in Python 3.
# (c) 2021 TheRealMysticSavages
from github import Github
import git, os, sys

num = 0 # Identifier number for looking at repo parameter
gitrequests = [] # List for github repo(s)

finished = 0 # Fixed index errors after finishing
local = '\\'.join(__file__.split('\\')[0:-1])

clear = lambda: os.system('cls')
g = Github() # Shortens Github API host

# The biggest pain to code ever
def pygit_clone(name, repository):
    global num, finished # The rest of the program couldn't find these variables
    user = g.get_user(name)
    for repo in user.get_repos(): # adds all repos to list
        clear()
        gitrequests.append(repo.full_name)
    if repository == '*': # The 'all' parameter
        finished += 1
        for repo in user.get_repos():
            git.Git(local).clone('https://github.com/'+repo.full_name)
    while repository not in gitrequests[num]:
        num += 1
        if repository in gitrequests[num]: # Hey look, I found it
            finished += 1
            git.Git(local).clone('https://github.com/'+name+'/'+repository)
    if repository == name: # Solves the confusion of repos named after the user like 'judge0/judge0'
        finished += 1
        git.Git(local).clone('https://github.com/'+name+'/'+name)

if __name__ == '__main__':
    try:
        pygit_clone(sys.argv[1], sys.argv[2])
    except IndexError:
        if finished == 1:
            print('Cloning complete.')
        else:
            print('Error: Missing arguments "name" and "repository".')
    except TypeError:
        print(f'Error: Missing argument "repository".')
