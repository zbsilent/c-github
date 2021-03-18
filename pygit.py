#! /usr/bin/env python
# -*- coding: utf-8 -*-
import json
from github import Github
from rich.console import Console
from rich.table import Table

console = Console()

# Set your Github access token
#console.print("Enter a Github access token that has the `delete_repo` permission", style="blue")
print("开始清楚GITHUB仓库")
console.print ("(https://docs.github.com/en/free-pro-team/github/authenticating-to-github/creating-a-personal-access-token)")
#token = console.input("\nAccess token: ")
token ='b86c03cd54396f93133b0d477f87eb371b4df27a'
g = Github(token)


def printRepos():
  allRepos = []
  repoTable = Table(title="Repos")
  repoTable.add_column("#")
  repoTable.add_column("Name")
  repoTable.add_column("URL")
  repoTable.add_column("Privacy")
  repoTable.add_column("Forked?")
  i = 0
  g.get_user().update()
  for repo in g.get_user().get_repos():
    allRepos.append(repo)
    i+=1

    repoTable.add_row(str(i), repo.name, repo.html_url, ("Private" if repo.private else "Public"), ("Yes" if repo.fork else "No"))
    console.print(repoTable)
  return allRepos

def repoDelete(allRepos):
  console.print("\n\nEnter a repo number to delete", style="blue")
  #toDelete = console.input("\n#: ")

  repo = allRepos[(int(toDelete) - 1)]

  console.print("Delete ", repo.name, "?", style="blue")
  response = console.input("\n(Y/N): ")

  console.clear(True)
  if (response.lower() == "y"):
    try:
      repo.delete()
    except:
      console.print("\nAn error occurred while deleting the repository.", style="bold red")
      console.print("\n")
    else:
      console.print("\nREPO DELETED", style="bold red")
  else:
    console.print("\nDelete skipped", style="blue")
# Repository(full_name="yonyou-sc-dev/justbon-dev-js")
# <class 'github.Repository.Repository'>
def classTodic(classTo):
    return {
        'full_name':classTo.full_name
    }
with open('/Users/Repostory/c-github/repos.txt', 'r', encoding='utf-8') as f:
    data = f.readlines()

# while 1:
allRepos = printRepos()

#print(json.dumps(allRepos[1], default=classTodic))
for classVaule in allRepos:
    dicts = classTodic(classVaule);
    dict = dicts['full_name']
    # tt = json.dumps(dict, default=classTodic)
    # print(type(tttt))
    if dict.find('yonyou-sc-dev')==-1 and dict.find('eshop')==-1 and dict.find('book')==-1 and dict.find('imag')==-1 and dict.find('react'):
        try:
          classVaule.delete()
        except:
          print("An error occurred while deleting the repository.", style="bold red")
          print("")
        else:
          console.print("REPO DELETED", style="bold red")
    else:
         console.print('check name {} is undifin'.format(dict),style="blue")

# print(json.dumps(allRepos[1], default=lambda obj: obj.__dict__, sort_keys=True, indent=4a, default=lambda obj: obj.__dict__, sort_keys=True, indent=4)
# print(type(allRepos[1]))
  # for i in allRepos:
  #     print(i)
  # print(type(allRepos))
  #repoDelete(allRepos)
