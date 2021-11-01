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

## Simple Git workflow for desktop:
Github can be used with a command-line interface. But there is a more beginner-friendly alternative: the GitHub Desktop. This is a free open-source product developed by GitHub, which is fully integrated with GitHub.  

### Start using the GitHub Desktop as follows:

  1. Download GitHub Desktop from http://desktop.github.com  
	There are versions for Windows and OSX (both Intel and Apple-silicon.
  2. Install the desktop on your computer.
  3. Start it.
  4. Follow the instructions.
	
![MainWindowGitHubDesktop](https://user-images.githubusercontent.com/11397265/139668403-62408fe4-84aa-441f-b3f5-9a190d01ecf2.jpg)

When using GitHub desktop there are a **few principles** which help you understand how it principally functions:  

  1. The desktop functions as a jumping-board. For instance from it you can jump to GitHub, or to the cloned files on your computer, or to the editors you use to edit files. 
  2. Adding a clone of a repository on GitHub is easiest done by going to GitHub, selecting the relevant project, clicking on the code button which causes a little menu to open. In that menu select "open in GitHub Desktop". This clones the repository to your computer by copying the repository and it's contents to a directory on your computer, where you can edit it.
  3. If you open GitHub Desktop, it will check for changes in the central repository and for any local changes. Changes in the global repository can be pulled in to your copy by pressing the "Fetch Origin"-button in the centre of the top of your GitHub Desktop window.
  4. Publishing your local changes to the central repository is done by adding a summary in the left bottom describing the changes and pushing the "Commit" button in the left lower corner.
  5. Editing the copy on your computer can be done with your usual editing-tools. Go to the directory containing the clones from the GitHub desktop directly by pushing the button" Show in Finder" in the centre on the right side.  


That is basically all there is to start using GitHub via the GitHub Desktop. The Desktop contains several help functions to help you get along. Have fun!
