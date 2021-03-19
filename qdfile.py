
#!/usr/bin/python
# -*- coding: utf-8 -*-
# --------------------------------------------------
# @Time : 2020/12/20 18:40
# @Author : skywin886
# @File : ls_and_cat.py
# @Version : 1.0
# --------------------------------------------------

# --------------------------------------------------
import os,shutil
import subprocess
from rich.console import Console
from rich.table import Table


dir = '/Users/zbsilent/Downloads/'

console = Console()
repoTable = Table(title="fileloads")
repoTable.add_column("#")
repoTable.add_column("root")
repoTable.add_column("dirs")
repoTable.add_column("files")


oDelete = console.input("\nfileRoot: ")
ddir = dir +oDelete
console.print("\n即将删除的路径是"+ddir,style="green")
response = console.input("\n(Y/N): ")
console.clear(True)

def deleteFile(dirPath):
    #console.print("\n开始执行删除文件操作",style="blue")
    i = 0
    row=''
    next=''
    end =''
    for root,dirs,files in os.walk(dirPath):
        # console.print(dirPath)
        i+=1
        row = root
        # print(type(row))
        # print('父目录是{}'.format(row))
        # if i == 1 :
        #     maxfileSize = len(files)
        #     print(maxfileSize)
        #
        if not os.listdir(root):
            shutil.rmtree(root)
            console.print("空目录为{}".format(root),style="green")
        # if root.endswith('METADATA'):
        #     #os.removedirs(root)
        #     shutil.rmtree(root)
        #     console.print("清空目录为{}".format(root),style="blue")
        # for line in dirs:
        #
        #
        #     # print(type(next))
        #     print('上级目录是{}'.format(next))
        for fi in files:
            if fi.endswith('_src.jar') == False and fi.endswith('.jar') == True:
                #repoTable.add_row(str(i), row, 'next', fi)
                #console.print(repoTable)
                # 执行字符串拼接
                filePath = row +'/'+fi
                print(filePath)
                try:
                    os.remove(filePath)
                    print('已删除文件{}'.format(filePath))
                except Exception as e:
                    console.print(e)
                #print(filePath)
            elif fi.endswith('.qso'):
                filePath = row +'/'+fi
                try:
                    os.remove(filePath)
                    print('已删除文件{}'.format(filePath))
                except Exception as e:
                    console.print(e)
            elif fi.endswith('.bmf'):
                filePath = row +'/'+fi
                try:
                    os.remove(filePath)
                    print('已删除文件{}'.format(filePath))
                except Exception as e:
                    console.print(e)
            elif fi.endswith('.class'):
                filePath = row +'/'+fi
                try:
                    os.remove(filePath)
                    print('已删除文件{}'.format(filePath))
                except Exception as e:
                    console.print(e)
                # print('文件路基是{}'.format(fi))
    console.print("\n删除文件操作结束",style="blue")

        # console.print(file)
        # repoTable.add_row(str(i), row, next, end)
        # console.print(repoTable)

if response.lower =='n' or response.lower=='' :
    print()
else:
    deleteFile(ddir)



#
# list = os.listdir(dir) #列出文件夹下所有的目录与文件
# file = open('./allConfd.conf','a') #结果增量写入文件
# rule=".conf" #设置过滤后的文件类型,可以设置多个类型,为空则不过滤
#
# #判断是否以xxx结尾，结果存入列表
# ruleAll = []
# for i in range(0,len(list)):
#     path = os.path.join(dir,list[i])
#     if path.endswith(rule):
#         ruleAll.append(path)
#
# print(ruleAll)
#
# #将列表中所有文件内容合并至一个文件
# for x in ruleAll:
#  	#换行分隔符
#     file.write("####################""\n")
#     #文件名写入文件
#     file.write("#"+ os.path.basename(x))
#     #文件内容写入文件
#     osFile = subprocess.check_output('cat %s%s' % (dir,os.path.basename(x)), shell=True, cwd="./")
#     file.write(osFile)
#
# #文件写入关闭
# file.close()
