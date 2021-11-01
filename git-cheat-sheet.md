# Git Cheat Sheet

## Simple Git workflow for command window:

First [download and install GIT](https://git-scm.com/downloads) for your OS.  
Then open a terminal/command window, now select the work drive and directory for Git.  
``` 
```
| What                                 | How                                                              |
|--------------------------------------|------------------------------------------------------------------|
| import new repository in current DIR | `git clone https://github.com/embeddingForth/embeddingForth.git` |
| check for local repository changes   | `git status`                                                     |
| update your local repository         | `git pull`                                                       |
| add new file for next commit         | `git add "filename.ext"`                                         |
| commit changes and add explanation   | `git commit -m "Comments about update"`                          |
| correct typo in last commit          | `git commit --amend`                                             |
| publish local commits to remote repo | `git push`                                                       |


## Create new directories

Empty directories are not stored in Git. Create a dummy file or `readme` to have them:

    mkdir new-directory
	echo "# Overview of random generators user the XORshift methods #" >new-directory/readme.md
	git add new-directory/readme.md
	git commit -m "Add new-directory folder"
	git push

## Simple Git workflow for desktop
![MainWindowGitHubDesktop](https://user-images.githubusercontent.com/11397265/139654141-a1bf33c5-b5c8-4d8b-8f97-7ac1ec9ce2ae.png)
