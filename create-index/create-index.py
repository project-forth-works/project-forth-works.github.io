#!/usr/bin/env python3

import os, re, sys
from datetime import datetime
import urllib.parse


def READMEs(dir):
  readmeList=[]
  os.chdir(os.path.join(dir,'..'))

  for root, dirs, files in os.walk(os.path.basename(dir), topdown = True):
    dirs.sort()
    for name in files:
      if name.lower() == "readme.md":
        readmeList.append(os.path.join(root, name))
  return readmeList

def stripLeafs(l): # remove all READMES, where the directory has a prefix
  # collect all dirs
  dirs=[]
  for f in l: # first get all the parentdirectories of all the file
    parentDir=os.path.dirname(os.path.dirname(f))
    if parentDir not in dirs:
      dirs.append(parentDir)
  filtered=[]
  for f in l: # now collect all the files in these parent directories
    if os.path.dirname(f) in dirs:
      filtered.append(f)
  return filtered


class IndexEntry():
  def __init__(self, level, path):
    self.level=level
    self.path=path
    self.title=os.path.basename(path)
    self.name=""
    self.description=""

    self.klass=""
    classes=["toplevel", "category", "idea", "item", "item2", "item3"]
    if 0 <= level < len(classes):
      self.klass=classes[level]

    self.links=[]
  
  def addLink(self, link):
    self.links.append(link)
  
BASEURL="https://github.com/project-forth-works/project-forth-works/tree/main"

HEADING=re.compile(r"#(.*)")
ITEM_WITH_LINK=re.compile(r" *-.*\[(.*)\]\(([^)]*)\)(.*)")
ITEM=re.compile(r" *- ")

def stripFirst(name):
  return os.path.sep.join((name.split(os.path.sep)[1:]))

def scanReadMe(name):
  l=len(name.split(os.path.sep))
  entry=IndexEntry(l-2, stripFirst(os.path.dirname(name)))

  takeDescriptionFromThisLine=False
  for line in open(name).readlines():
    m=ITEM.match(line) 
    if not m and takeDescriptionFromThisLine:
      title, link, description = entry.links[-1]
      entry.links[-1]=(title, link, line.strip())
      # print(line)
      takeDescriptionFromThisLine=False
      continue
    takeDescriptionFromThisLine=False
   
    m=ITEM_WITH_LINK.match(line) 
    if m:
      title=m.group(1)
      link=m.group(2)
      if not link.startswith('http'):
        d=stripFirst(name) # strip top level
        # print(name, '->', name.split(os.path.sep))
        link = os.path.join(BASEURL, os.path.dirname(d), link)
      description=m.group(3)        
      # print(name, 'Title:', title, 'Link:', link, 'Description:', description)
      entry.addLink( (title.strip(), link, description.strip(',;: ')) )
      if description.strip()=="":
        takeDescriptionFromThisLine=True
      continue
    m=HEADING.match(line)
    if m:
      entry.name=m.group(1).strip()
      continue
  return entry

def collectDescriptions(entries):
  for f in entries:
    # print(f.path)
    for e in entries:
      for (title, url, description) in e.links:
        unquotedURL=urllib.parse.unquote(url)
        #if f.path=="System-Software/Assemblers/ARMv8 assembler":
        #  print(unquotedURL)
        if unquotedURL.endswith(f.path):
          f.description=description
          break

def scanReadMeFiles(l):
  readmeList=list(map(scanReadMe, l))
  collectDescriptions(readmeList)
  return readmeList

def writeEntries(f, entries):
  levels=[]
  for e in entries:
    while len(levels)>0 and levels[-1]>=e.level:
      f.write("%s</div>\n" % (' '*3*levels[-1],))
      levels.pop()

    f.write("%s<div class='%s' title='%s'>\n"% (' '*3*e.level, e.klass, e.title))
    f.write("%s<a class='%s' href='%s'>%s</a>\n"% (' '*3*(e.level+1), e.klass, os.path.join(BASEURL,e.path), e.title))
    f.write("%s<span class='%s-description'>%s</span>\n" % (' '*3*(e.level+1), e.klass, e.description))
    levels.append(e.level)
  while len(levels)>0:
    f.write("%s</div>\n" % (' '*3*levels[-1],))
    levels.pop()


def createIndex(f, entries):
  f.write("<!DOCTYPE html>\n")
  f.write("<!-- index generated by create-index on %s -->\n" % (datetime.now(),))
  f.write("<html>\n")
  f.write("<head>\n")
  f.write("<h1><a href='https://github.com/project-forth-works/project-forth-works'>Project Forth Works Index</a></h1>")
  f.write("<link rel='stylesheet' href='idx.css'>\n")
  f.write("</head>\n")
  f.write("<body>\n")
  writeEntries(f, entries)
  f.write("</body>\n")
  f.write("</html>\n")


if __name__=="__main__":
  print("Start")
  readmeList=READMEs("../../project-forth-works")
  for f in readmeList:
    print(f)

  entries=list(scanReadMeFiles(readmeList))

  print(entries[0].path)
  createIndex(open("project-forth-works.github.io/idx.html","w"), entries)

  print("End")