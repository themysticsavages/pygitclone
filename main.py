from github import Github
import git, os, sys

num = 0
gitrequests = []

finished = 0
local = '\\'.join(__file__.split('\\')[0:-1])

clear = lambda: os.system('cls')
g = Github()

def pygit_clone(name, repository):
    global num, finished
    user = g.get_user(name)
    for repo in user.get_repos():
        clear()
        gitrequests.append(repo.full_name)
    if repository == '*':
        finished += 1
        for repo in user.get_repos():
            git.Git(local).clone('https://github.com/'+repo.full_name)
    while repository not in gitrequests[num]:
        num += 1
        if repository in gitrequests[num]:
            finished += 1
            git.Git(local).clone('https://github.com/'+name+'/'+repository)
    if repository == name:
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