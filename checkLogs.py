#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
    author jiangyan
    since 2014-03-19
    version 1.0
    """
import os,sys,re

class ConstError(Exception):
    pass


class Const(object):
    def __setattr__(self, k, v):
        self.__dict__[k] = v




config = Const();

imageNameArray=[]
imageNameArrayFor=[]
def forEachFiles(path,callback,callbackParam1):
    for filename in os.listdir(path):
        childPath=path+"/"+filename
        if os.path.isfile(childPath):
            callback(childPath,callbackParam1)
        else:
            forEachFiles(childPath,callback,callbackParam1)

def parseImageIsUsed(filepath,callbackParam1):
    fname=callbackParam1
    if filepath.find('.log')!=-1:
        desfile=open(filepath,'r+')
        f = desfile.read()
        prog = re.compile(r'大家好(\d+)\n', re.M)
        match = prog.search(f)
        if match:
            start =  match.start()
            end   =   match.end()
            f = match.groups()[0]
            imageNameArray.append(int(f))
            # print f
        desfile.close()
def checkImageIsUsed():
    #print len(imageNameArray)
    
    for imageName in imageNameArrayFor:
        #print imageName
        for codePath in config.codePath:
            forEachFiles(codePath,parseImageIsUsed,imageName)

imageDict={}
def parseAllImageName(imagePath,filename):
    if imagePath.find(".png")!=-1:
        pathArr=imagePath.split('/')
        imageName=pathArr[len(pathArr)-1]
        imageNameArray.append(imageName)
        imageDict[imageName]=imagePath
        imageNameArrayFor.append(imageName)

def getAllImageName():
    forEachFiles(config.imagePath,parseAllImageName,"")

# /Users/a58/58_ios_libs/WBJob
if __name__ == '__main__':
    forEachFiles('/Users/a58/Library/Developer/CoreSimulator/Devices/D47D288D-9F75-42FC-9F9F-A926C5978558/data/Containers/Data/Application/182B1949-49DD-4166-B4B5-01A5A0D83D6A/Library/Caches/logs',parseImageIsUsed,"")
    # print imageNameArray
    sorts=sorted(imageNameArray) 
    for i in range(0,len(imageNameArray)):
        if i!=sorts[i]:
            print "the i is wrong"+str(i)
# for  foldpath in folders:
# 	print  foldpath
# 	forEachFiles('/Users/a58/58_ios_libs/'+foldpath,parseImageIsUsed,"")





