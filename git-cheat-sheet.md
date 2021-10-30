# Git Cheat Sheet

## Simple Git workflow

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
