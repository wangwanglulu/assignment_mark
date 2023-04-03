#!/usr/bin/env Python
# coding=utf-8

import os
import re
import csv
from tkinter import *  # 图形界面
import tkinter.font as tkFont
# import pytest #单元测试，需要pip安装


# 提取txt作业文件，并且将每一题生成py文件，并保存到python文件夹
def create_pyfile(aNo):
    os.chdir("A" + str(aNo))  # 到当前文件夹
    for x in range(1, 7):
        exist = os.path.exists('python' + str(x))  # 判断是否存在文件夹
        if not exist:
            folder = os.getcwd()
            os.mkdir(folder + '\\python' + str(x))  # 创建存放py作业文件的文件夹
        else:
            pass
    exist = os.path.exists('temp')  # 判断是否存在文件夹
    if not exist:
        folder = os.getcwd()
        os.mkdir(folder + '\\temp')  # 创建存放py作业文件的文件夹
    else:
        pass
    for txtfilename in os.listdir("."):  # 提取文件夹里文件的名字
        if txtfilename.lower().endswith(".txt"):
            file = open(txtfilename, 'r', encoding='utf-8-sig')
            filecontent = file.readlines()  # 读取文件内容
            line_list = []
            for line in filecontent:
                line_list.append(line)  # 将所有内容保存在一个列表里
            file.close()
            # print(line_list) #查看列表
            # 查找每一个作业题的位置，1-6题
            position = []
            for y in range(1, 7):
                questionpos = "A" + str(aNo) + "Q" + str(y) + "\n"
                position.append(line_list.index(questionpos))
            # 提取每一道题下面的代码片段
            codeslice = []
            for z in range(5):
                codeslice.append(line_list[position[z] + 1:position[z + 1]])
            codeslice.append(line_list[position[5] + 1:])
            # 分别保存每一道题的代码片段到一个py文件里
            line_start = line_list[0].find('2')  # 有些学生可能对txt文件进行二次修改，产生BOM
            line_list[0] = line_list[0][line_start:]  # 去除BOM
            for w in range(1, 7):
                with open('python' + str(w) + '/' + line_list[0].rstrip() + "_A" + str(aNo) + "Q" + str(w) + ".py", 'w', encoding='utf-8') as tmp:
                    for line in codeslice[w - 1]:
                        tmp.write(line)


score = [{}, {}, {}, {}, {}, {}]
total_score = {}
scoretosave = []
# 评分函数，三个档次


def marks_1(x, qNo):
    score[qNo][x] = 0
    print(score[qNo][x])


def marks_2(x, qNo):
    score[qNo][x] = 0.5
    print(score[qNo][x])


def marks_3(x, qNo):
    score[qNo][x] = 1
    print(score[qNo][x])


# 图形界面，用于查看学生写的代码，并且可以运行
# 在自动批改作业的过程中，如果遇到无法通过的程序，可以查看并且手动给分
def pygui(stuNo, pyfilename, qNo):
    root = Tk()
    # 设置标题
    root.title('Python GUI')
    # 设置窗口大小
    root.geometry('580x680+50+25')
    # 设置窗口是否可变长、宽，True：可变，False：不可变
    root.resizable(width=False, height=True)
    ft = tkFont.Font(family="Consolas", size=12)
    # 创建窗口
    code = Label(root, text="作业代码")
    code.grid(row=0, column=0)
    # 自适应滚动条
    init_data_Text = Text(root, wrap=NONE, width=60, height=30, font=ft)
    init_data_Text.grid(row=1, column=0, rowspan=10, columnspan=10)
    sy1 = Scrollbar(root, command=init_data_Text.yview)
    sx1 = Scrollbar(root, orient="horizontal", command=init_data_Text.xview)
    init_data_Text['yscrollcommand'] = sy1.set
    sy1.grid(row=1, column=11, rowspan=10, sticky=N + S + E + W)
    init_data_Text['xscrollcommand'] = sx1.set
    sx1.grid(row=11, column=0, columnspan=10, sticky=N + S + E + W)
    # 读取文件内容并展示出来
    file = open("python" + str(qNo + 1) + "/" +
                pyfilename, 'r', encoding='utf-8')
    filecontent = file.read()
    file.close()
    init_data_Text.insert("insert", filecontent)
    # 可以修改学生的代码，并生成临时文件，保存在temp文件夹
    # 也可以直接运行，以查看是否正确

    def testcode(filename):
        contents = init_data_Text.get('1.0', END)
        root.clipboard_clear()
        with open('temp/' + filename, 'w', encoding='utf-8') as tmp:
            for line in contents:
                tmp.write(line)
                root.clipboard_append(line)
    # 提醒批阅者，这题还没有评分

    def marks_4(x, qNo):
        if x not in score[qNo]:
            print("还没有评分，请评分后再点下一个")
        else:
            root.destroy()
    # 调用testcode函数，用于运行学生作业题的程序
    b1 = Button(root, text='复制到剪切板', command=lambda: testcode(
        pyfilename), width=10, height=2)
    b1.grid(row=20, column=0, padx=5, pady=5)
    # 调用给分函数，用于给学生评分
    b2 = Button(root, text='0分', command=lambda: marks_1(
        stuNo, qNo), width=8, height=2)
    b2.grid(row=20, column=1, padx=5, pady=5)
    b3 = Button(root, text='0.5分', command=lambda: marks_2(
        stuNo, qNo), width=8, height=2)
    b3.grid(row=20, column=2, padx=5, pady=5)
    b4 = Button(root, text='1分', command=lambda: marks_3(
        stuNo, qNo), width=8, height=2)
    b4.grid(row=20, column=3, padx=5, pady=5)
    # 退出图形界面
    b5 = Button(root, text='下一个', command=lambda: marks_4(
        stuNo, qNo), width=8, height=2)
    b5.grid(row=20, column=4, padx=5, pady=5)
    # 进入消息循环
    root.mainloop()

# 批改每次作业的所有程序，需要每个题目都查看


def mark_assignment():
    for x in range(1, 7):
        for pyfilename in os.listdir("python" + str(x) + "/"):
            stuNo = pyfilename[:10]
            pygui(stuNo, pyfilename, x - 1)
# 批改每次作业的单个题目的程序


def mark_assignment_single_question(x):
    for pyfilename in os.listdir("python" + str(x) + "/"):
        stuNo = pyfilename[:10]
        pygui(stuNo, pyfilename, x - 1)


# 用于快速批改需要设计函数的作业题
def test_func(aNo, qNo, stuNo, func_name):
    name_of_code = str(stuNo) + '_A' + str(aNo) + 'Q' + str(qNo)
    import name_of_code
    return name_of_code.func_name


# 选择批改哪一次作业，并且将最终的分数保存到可以上传的csv文件
# 可以选择一次批改所有的作业， 也可以一次只批改一题
# 如果只批改一题，则只会保存该题的分数，用于最后汇总
def assignment(aNo, which):
    create_pyfile(aNo)
    if which == 0:
        mark_assignment()
    else:
        mark_assignment_single_question(which)
    for x in score:
        if x:
            for y in x.keys():
                if y not in total_score:
                    total_score[y] = x[y]
                elif y in total_score:
                    total_score[y] += x[y]
    print(total_score)
    for studentNo, studentScore in total_score.items():
        scoretosave.append([studentNo, studentScore])
    os.chdir('..')
    if which == 0:
        with open('A' + str(aNo) + '_marks_to_upload.csv', "w", newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["number", "score"])
            writer.writerows(scoretosave)
            f.close()
    else:
        with open('A' + str(aNo) + 'Q' + str(which) + '_marks.csv', "w", newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["number", "score"])
            writer.writerows(scoretosave)
            f.close()


# 在每次只批改一题的情况下，批改完后运行该函数可以汇总分数，生成可以上传的计分表
collect = [{}, {}, {}, {}, {}, {}]
sum_up_total_score = {}
sum_up_scoretosave = []


def sum_up_score(aNo):
    # os.chdir("A"+str(aNo))
    for x in range(1, 7):
        with open('A' + str(aNo) + 'Q' + str(x) + '_marks.csv') as f:
            reader = csv.reader(f)
            header_row = next(reader)
            for row in reader:
                if int(row[0]) not in collect[x - 1]:
                    collect[x - 1][int(row[0])] = float(row[1])
    print(collect)
    for x in collect:
        if x:
            for y in x.keys():
                if y not in sum_up_total_score:
                    sum_up_total_score[y] = x[y]
                elif y in sum_up_total_score:
                    sum_up_total_score[y] += x[y]
    for studentNo, studentScore in sum_up_total_score.items():
        sum_up_scoretosave.append([studentNo, studentScore])
    with open('A' + str(aNo) + '_marks_to_upload.csv', "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["number", "score"])
        writer.writerows(sum_up_scoretosave)
        f.close()


# 批改第一次作业所有题，必须一次性批完，无需运行汇总分数的函数,自动汇总
# assignment(1,0)
# 批改第一次作业单个题目，每个题目必须一次性批完，否则无法保存，改完后保存该题的所有分数
assignment(1, 1)  # 批改第一次作业第一题
# assignment(1,2) #批改第一次作业第二题
# assignment(1,3) #批改第一次作业第三题
# assignment(1,4) #批改第一次作业第四题
# assignment(1,5) #批改第一次作业第五题
# assignment(1,6) #批改第一次作业第六题
# 如果是按一题一题来批改的，运行该函数来汇总所有分数，请先批完所有题再运行
# sum_up_score(1)

# assignment(2,0) #批改第二次作业所有题
# assignment(2,1) #批改第二次作业第一题
# assignment(2,2) #批改第二次作业第二题
# assignment(2,3) #批改第二次作业第三题
# assignment(2,4) #批改第二次作业第四题
# assignment(2,5) #批改第二次作业第五题
# assignment(2,6) #批改第二次作业第六题
# sum_up_score(2) #汇总分数

# assignment(3,0) #批改第三次作业所有题
# assignment(3,1) #批改第三次作业第一题
# assignment(3,2) #批改第三次作业第二题
# assignment(3,3) #批改第三次作业第三题
# assignment(3,4) #批改第三次作业第四题
# assignment(3,5) #批改第三次作业第五题
# assignment(3,6) #批改第三次作业第六题
# sum_up_score(3) #汇总分数

# assignment(4,0)
# assignment(4,1)
# assignment(4,2)
# assignment(4,3)
# assignment(4,4)
# assignment(4,5)
# assignment(4,6)
# sum_up_score(4)
