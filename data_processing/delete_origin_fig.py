import os
import re
# this program work for new image whose name is not ended with digit
filePath = 'E:\\test_with_mask'  # change path of folder test_with_mask
folderNameList = os.listdir(filePath)
for folder in folderNameList:
    curPath = filePath + '\\' + folder
    figNameList = os.listdir(curPath)
    for fig in figNameList:
        pattern = r'origin.jpg'
        match = re.search(pattern, fig, re.M|re.I)
        if match:
            curFig = curPath + '\\' + fig
            if os.path.exists(curFig):
                os.remove(curFig)
            else:
                print('{} not exist.'.format(fig))
        else:
            continue

