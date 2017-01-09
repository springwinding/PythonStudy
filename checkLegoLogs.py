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
    if filepath.find('.txt')!=-1:
        desfile=open(filepath,'r+')
        f = desfile.read()
        prog = re.compile(r'\"param\":\"(\d+)\"', re.M)
        maths = prog.findall(f)
        for str in maths:
            imageNameArray.append(int(str))
        desfile.close()
def checkImageIsUsed():
    #print len(imageNameArray)
    
    for imageName in imageNameArrayFor:
        #print imageName
        for codePath in config.codePath:
            forEachFiles(codePath,parseImageIsUsed,imageName)

# /Users/a58/58_ios_libs/WBJob
if __name__ == '__main__':
    forEachFiles('/Users/a58/Library/Developer/CoreSimulator/Devices/AC36393F-EAFD-4251-BC31-C19BC72BAA0F/data/Containers/Data/Application/3BCB74B8-AF14-4D21-9DBF-04C3CF66B271/Documents/WBLegoLogFolder_Comm',parseImageIsUsed,"")
    sorts=sorted(imageNameArray) 
    print
    for i in range(0,len(imageNameArray)):
        if i!=sorts[i]:
            print "the i is wrong"+str(i)
# for  foldpath in folders:
# 	print  foldpath
# 	forEachFiles('/Users/a58/58_ios_libs/'+foldpath,parseImageIsUsed,"")





