import os
from random import sample
import shutil
from PIL import Image

MINLEN = 5

def delFigs(filePath):
    folderNameList = os.listdir(filePath)
    for folder in folderNameList:
        curPath = filePath + '\\' + folder
        figNameList = os.listdir(curPath)
        if len(figNameList) > MINLEN:
            figDelList = sample(figNameList, len(figNameList) - MINLEN)
            for fig in figDelList:
                curFig = curPath + '\\' + fig
                if os.path.exists(curFig):
                    os.remove(curFig)
                else:
                    print('{} not exist.'.format(fig))
            # print('{} figs deleted from {}.'.format(len(figDelList), folder))
        elif len(figNameList) < MINLEN:
            for fig in figNameList:
                curFig = curPath + '\\' + fig
                if os.path.exists(curFig):
                    os.remove(curFig)
                else:
                    print('{} not exist.'.format(fig))
            os.rmdir(curPath)
            # print('folder {} is deleted.'.format(curPath))
        else:
            print('folder {} is valid.'.format(curPath))


def resizeImg(filePath):
    x_s, y_s = 250, 250
    folderNameList = os.listdir(filePath)
    for folder in folderNameList:
        curPath = filePath + '\\' + folder
        figNameList = os.listdir(curPath)
        for fig in figNameList:
            infile = curPath + '\\' + fig
            outfile = curPath + '\\' + 'adjust_' + fig
            im = Image.open(infile)
            out = im.resize((x_s, y_s), Image.ANTIALIAS)
            out.save(outfile)
            os.remove(infile)


def renameImg(filePath):
    folderNameList = os.listdir(filePath)
    for folder in folderNameList:
        curPath = filePath + '\\' + folder
        figNameList = os.listdir(curPath)
        count = 1
        for fig in figNameList:
            curFig = curPath + '\\' + fig
            os.rename(curFig, curPath + '\\' + folder + str(count) + '_origin' + '.jpg')
            count += 1


def copyFile(filePath, dest, start, end):
    folderNameList = os.listdir(filePath)
    for folder in folderNameList:
        curPath = filePath + '\\' + folder
        figNameList = os.listdir(curPath)
        copyPath = dest + '\\' + folder
        folder = os.path.exists(copyPath)
        if not folder:
            os.makedirs(copyPath)
        else:
            print('{} has existed.'.format(copyPath))
        for i in range(start, end):
            fig = figNameList[i]
            shutil.copy(curPath + '\\' + fig, copyPath + '\\' + fig)


if __name__ == '__main__':
    # filePath = 'E:\\2020FA\\EECS504\\project\\data_processing\\origin_data\\lfw'
    # delFigs(filePath)
    # renameImg(filePath)
    # resizeImg(filePath)
    # dest = 'E:\\2020FA\\EECS504\\project\\data_processing\\origin_data\\lfw_mixed_dataset\\train_without_mask'
    # start, end = 0, 2
    # copyFile(filePath, dest, start, end)
    # dest = 'E:\\2020FA\\EECS504\\project\\data_processing\\origin_data\\lfw_mixed_dataset\\train_with_mask'
    # start, end = 2, 4
    # copyFile(filePath, dest, start, end)
    #
    # dest = 'E:\\2020FA\\EECS504\\project\\data_processing\\origin_data\\lfw_mixed_dataset\\test_with_mask'
    # start, end = 4, 5
    # copyFile(filePath, dest, start, end)
    filePath = 'E:\\2020FA\\EECS504\\project\\data_processing\\origin_data\\AFDB_pure_dataset\\train_without_mask'
    dest = 'E:\\2020FA\\EECS504\\project\\data_processing\\origin_data\\AFDB_mixed_dataset\\train_without_mask'
    start, end = 7, 14
    copyFile(filePath, dest, start, end)

