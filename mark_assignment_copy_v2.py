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
        python_folder = 'python' + str(x)
        exist = os.path.exists(python_folder)  # 判断是否存在文件夹
        if not exist:
            folder = os.getcwd()
            os.mkdir(os.path.join(folder, python_folder))
            # os.mkdir(folder+'/python'+str(x)) #创建存放py作业文件的文件夹
        else:
            pass
    exist = os.path.exists('temp')  # 判断是否存在文件夹
    if not exist:
        temp_folder = 'temp'
        folder = os.getcwd()
        os.mkdir(os.path.join(folder, temp_folder))
        # os.mkdir(folder + '/temp')  # 创建存放py作业文件的文件夹
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
            try:
                position = []
                for y in range(1, 7):
                    questionpos = "A" + str(aNo) + "Q" + str(y) + "\n"
                    position.append(line_list.index(questionpos))
                # 提取每一道题下面的代码片段
                codeslice = []
                for z in range(5):
                    codeslice.append(
                        line_list[position[z] + 1:position[z + 1]])
                codeslice.append(line_list[position[5] + 1:])
                # 分别保存每一道题的代码片段到一个py文件里
                line_start = line_list[0].find('2')  # 有些学生可能对txt文件进行二次修改，产生BOM
                line_list[0] = line_list[0][line_start:]  # 去除BOM
                for w in range(1, 7):
                    student_answer_each_q = line_list[0].rstrip(
                    ) + "_A" + str(aNo) + "Q" + str(w) + ".py"
                    with open(os.path.join('python' + str(w), student_answer_each_q), 'w', encoding='utf-8') as tmp:
                        for line in codeslice[w - 1]:
                            tmp.write(line)
            except:
                with open(os.path.join('temp', txtfilename), 'w', encoding='utf-8') as tmp:
                    for line in line_list:
                        tmp.write(line)


score = [{}, {}, {}, {}, {}, {}]
total_score = {}
scoretosave = []
# 评分函数，三个档次

step = 0.5


def marks_1(x, qNo):
    global var_m
    fenshu = step * 0
    var_m.set(f'给{fenshu}分')
    score[qNo][x] = fenshu
    print(score[qNo][x])


def marks_2(x, qNo):
    global var_m
    fenshu = step * 1
    var_m.set(f'给{fenshu}分')
    score[qNo][x] = fenshu
    print(score[qNo][x])


def marks_3(x, qNo):
    global var_m
    fenshu = step * 2
    var_m.set(f'给{fenshu}分')
    score[qNo][x] = fenshu
    print(score[qNo][x])


# 图形界面，用于查看学生写的代码，并且可以运行
# 在自动批改作业的过程中，如果遇到无法通过的程序，可以查看并且手动给分
def pygui(stuNo, pyfilename, qNo):
    root = Tk()
    # 设置标题
    root.title('Python作业代码')
    # 设置窗口大小
    if os.name == 'posix':
        root.geometry('680x680+50+30')
    else:
        root.geometry('680x750+50+30')
    # 设置窗口是否可变长、宽，True：可变，False：不可变
    root.resizable(width=False, height=True)
    ft = tkFont.Font(family="Consolas", size=14)
    # 创建窗口
    code = Label(root, text="作业代码")
    code.grid(row=0, column=0)
    # 自适应滚动条
    init_data_Text = Text(root, wrap=NONE, width=70, height=30, font=ft)
    init_data_Text.grid(row=1, column=0, rowspan=10, columnspan=10)
    sy1 = Scrollbar(root, command=init_data_Text.yview)
    sx1 = Scrollbar(root, orient="horizontal", command=init_data_Text.xview)
    init_data_Text['yscrollcommand'] = sy1.set
    sy1.grid(row=1, column=11, rowspan=10, sticky=N + S + E + W)
    init_data_Text['xscrollcommand'] = sx1.set
    sx1.grid(row=11, column=0, columnspan=10, sticky=N + S + E + W)
    # 读取文件内容并展示出来
    file = open(os.path.join("python" + str(qNo + 1),
                             pyfilename), 'r', encoding='utf-8')
    filecontent = file.read()
    file.close()
    init_data_Text.insert("insert", filecontent)
    # 可以修改学生的代码，并生成临时文件，保存在temp文件夹
    # 也可以直接运行，以查看是否正确

    def testcode(filename):
        contents = init_data_Text.get('1.0', END)
        root.clipboard_clear()
        with open(os.path.join('temp', filename), 'w', encoding='utf-8') as tmp:
            for line in contents:
                tmp.write(line)
                root.clipboard_append(line)
    # 提醒批阅者，这题还没有评分
    global var_m
    var_m = StringVar()

    def marks_4(x, qNo):
        global var_m
        if x not in score[qNo]:
            var_m.set("还没有评分，请评分后再点下一个!")
            # print("还没有评分，请评分后再点下一个")
        else:
            var_m.set("")
            root.destroy()
    # 调用testcode函数，用于运行学生作业题的程序
    b1 = Button(root, text='复制到剪切板', command=lambda: testcode(
        pyfilename), width=10, height=2)
    b1.grid(row=20, column=0, padx=5, pady=5)
    # 调用给分函数，用于给学生评分
    b2 = Button(root, text=f'{step*0}', command=lambda: marks_1(
        stuNo, qNo), width=8, height=2)
    b2.grid(row=20, column=1, padx=5, pady=5)
    b3 = Button(root, text=f'{step*1}', command=lambda: marks_2(
        stuNo, qNo), width=8, height=2)
    b3.grid(row=20, column=2, padx=5, pady=5)
    b4 = Button(root, text=f'{step*2}', command=lambda: marks_3(
        stuNo, qNo), width=8, height=2)
    b4.grid(row=20, column=3, padx=5, pady=5)
    # 退出图形界面
    b5 = Button(root, text='下一个', command=lambda: marks_4(
        stuNo, qNo), width=8, height=2)
    b5.grid(row=20, column=4, padx=5, pady=5)
    # 进入消息循环
    var_text_0 = Label(root, textvariable=var_m, font=('Arial', 14), justify='left',
                       padx=5).grid(row=22, columnspan=5)
    root.mainloop()


# 专门针对case study
step_c = 0.5


def marks_c1(x, qNo):
    global var_m
    fenshu = step_c * 0
    var_m.set(f'给{fenshu}分')
    score[qNo][x] = fenshu
    print(score[qNo][x])


def marks_c2(x, qNo):
    global var_m
    fenshu = step_c * 1
    var_m.set(f'给{fenshu}分')
    score[qNo][x] = fenshu
    print(score[qNo][x])


def marks_c3(x, qNo):
    global var_m
    fenshu = step_c * 2
    var_m.set(f'给{fenshu}分')
    score[qNo][x] = fenshu
    print(score[qNo][x])


def marks_c4(x, qNo):
    global var_m
    fenshu = step_c * 3
    var_m.set(f'给{fenshu}分')
    score[qNo][x] = fenshu
    print(score[qNo][x])


def marks_c5(x, qNo):
    global var_m
    fenshu = step_c * 4
    var_m.set(f'给{fenshu}分')
    score[qNo][x] = fenshu
    print(score[qNo][x])

# 有第六个档次的时候解除注释
# def marks_c6(x, qNo):
#     global var_m
#     fenshu = step_c * 5
#     var_m.set(f'给{fenshu}分')
#     score[qNo][x] = fenshu
#     print(score[qNo][x])


def pygui_case(stuNo, pyfilename, qNo):
    root = Tk()
    # 设置标题
    root.title('Python作业代码')
    # 设置窗口大小
    root.geometry('680x750+50+30')
    # 设置窗口是否可变长、宽，True：可变，False：不可变
    root.resizable(width=False, height=True)
    ft = tkFont.Font(family="Consolas", size=12)
    # 创建窗口
    code = Label(root, text="作业代码")
    code.grid(row=0, column=0)
    # 自适应滚动条
    init_data_Text = Text(root, wrap=NONE, width=70, height=30, font=ft)
    init_data_Text.grid(row=1, column=0, rowspan=10, columnspan=10)
    sy1 = Scrollbar(root, command=init_data_Text.yview)
    sx1 = Scrollbar(root, orient="horizontal", command=init_data_Text.xview)
    init_data_Text['yscrollcommand'] = sy1.set
    sy1.grid(row=1, column=11, rowspan=10, sticky=N + S + E + W)
    init_data_Text['xscrollcommand'] = sx1.set
    sx1.grid(row=11, column=0, columnspan=10, sticky=N + S + E + W)
    # 读取文件内容并展示出来
    file = open(os.path.join("python" + str(qNo + 1),
                             pyfilename), 'r', encoding='utf-8')
    filecontent = file.read()
    file.close()
    init_data_Text.insert("insert", filecontent)
    # 可以修改学生的代码，并生成临时文件，保存在temp文件夹
    # 也可以直接运行，以查看是否正确

    def testcode(filename):
        contents = init_data_Text.get('1.0', END)
        root.clipboard_clear()
        with open(os.path.join('temp', filename), 'w', encoding='utf-8') as tmp:
            for line in contents:
                tmp.write(line)
                root.clipboard_append(line)
    # 提醒批阅者，这题还没有评分
    global var_m
    var_m = StringVar()

    def marks_44(x, qNo):
        global var_m
        if x not in score[qNo]:
            var_m.set("还没有评分，请评分后再点下一个!")
            # print("还没有评分，请评分后再点下一个")
        else:
            var_m.set("")
            root.destroy()

    # 调用testcode函数，用于运行学生作业题的程序
    c0 = Button(root, text='复制到剪切板', command=lambda: testcode(
        pyfilename), width=10, height=2)
    c0.grid(row=20, column=0, padx=5, pady=5)
    # 调用给分函数，用于给学生评分
    c1 = Button(root, text=f'{step_c*0}分', command=lambda: marks_c1(
        stuNo, qNo), width=8, height=2)
    c1.grid(row=20, column=1, padx=5, pady=5)
    c2 = Button(root, text=f'{step_c*1}分', command=lambda: marks_c2(
        stuNo, qNo), width=8, height=2)
    c2.grid(row=20, column=2, padx=5, pady=5)
    c3 = Button(root, text=f'{step_c*2}分', command=lambda: marks_c3(
        stuNo, qNo), width=8, height=2)
    c3.grid(row=20, column=3, padx=5, pady=5)
    c4 = Button(root, text=f'{step_c*3}分', command=lambda: marks_c4(
        stuNo, qNo), width=8, height=2)
    c4.grid(row=22, column=1, padx=5, pady=5)
    c5 = Button(root, text=f'{step_c*4}分', command=lambda: marks_c5(
        stuNo, qNo), width=8, height=2)
    c5.grid(row=22, column=2, padx=5, pady=5)
    # 有第六个档次的时候解除注释
    # c6 = Button(root, text=f'{step_c*5}分', command=lambda: marks_c6(
    #     stuNo, qNo), width=8, height=2)
    # c6.grid(row=22, column=3, padx=5, pady=5)

    # 退出图形界面
    b5 = Button(root, text='下一个', command=lambda: marks_44(
        stuNo, qNo), width=8, height=2)
    b5.grid(row=20, column=5, padx=5, pady=5)
    # 进入消息循环
    var_text_0 = Label(root, textvariable=var_m, font=('Arial', 14), justify='left',
                       padx=5).grid(row=24, columnspan=5)
    root.mainloop()

# 批改每次作业的所有程序，需要每个题目都查看


def mark_assignment():
    for x in range(1, 7):
        for pyfilename in os.listdir("python" + str(x)):
            stuNo = pyfilename[:10]
            pygui(stuNo, pyfilename, x - 1)
# 批改每次作业的单个题目的程序


def mark_assignment_single_question(x):
    for pyfilename in os.listdir("python" + str(x)):
        stuNo = pyfilename[:10]
        pygui(stuNo, pyfilename, x - 1)


def mark_assignment_single_question_case(x):
    for pyfilename in os.listdir("python" + str(x)):
        stuNo = pyfilename[:10]
        pygui_case(stuNo, pyfilename, x - 1)


# 用于快速批改需要设计函数的作业题
def test_func(aNo, qNo, stuNo, func_name):
    name_of_code = str(stuNo) + '_A' + str(aNo) + 'Q' + str(qNo)
    import name_of_code
    return name_of_code.func_name


# 选择批改哪一次作业，并且将最终的分数保存到可以上传的csv文件
# 可以选择一次批改所有的作业， 也可以一次只批改一题
# 如果只批改一题，则只会保存该题的分数，用于最后汇总

def assignment(aNo, which):
    if aNo == 1:
        zh_score = "作业一"
    elif aNo == 2:
        zh_score = "作业二"
    elif aNo == 3:
        zh_score = "作业三"
    elif aNo == 4:
        zh_score = "作业四"
    create_pyfile(aNo)
    if which == 0:
        mark_assignment()
    elif which != 0 and aNo != 4:
        mark_assignment_single_question(which)
    elif which != 0 and aNo == 4:
        mark_assignment_single_question_case(which)
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
        with open('A' + str(aNo) + '_marks_to_upload.csv', "w", encoding='utf-8-sig', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["用户名", zh_score])
            writer.writerows(scoretosave)
            f.close()
    else:
        with open('A' + str(aNo) + 'Q' + str(which) + '_marks.csv', "w", encoding='utf-8-sig', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["用户名", zh_score])
            writer.writerows(scoretosave)
            f.close()



# 在每次只批改一题的情况下，批改完后运行该函数可以汇总分数，生成可以上传的计分表
collect = [{}, {}, {}, {}, {}, {}]
sum_up_total_score = {}
sum_up_scoretosave = []


def sum_up_score(aNo):
    if aNo == 1:
        zh_score = "作业一"
    elif aNo == 2:
        zh_score = "作业二"
    elif aNo == 3:
        zh_score = "作业三"
    elif aNo == 4:
        zh_score = "作业四"
    # os.chdir("A"+str(aNo))
    for x in range(1, 7):
        with open('A' + str(aNo) + 'Q' + str(x) + '_marks.csv', encoding='utf-8-sig') as f:
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
    with open('A' + str(aNo) + '_marks_to_upload.csv', "w", encoding='utf-8-sig', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["用户名", zh_score])
        writer.writerows(sum_up_scoretosave)
        f.close()


# 主菜单


def make_selection_func(aNo, qNo):
    def selection():
        global your_choice, var
        your_choice = (aNo, qNo)
        var.set(f'要批改A{aNo}Q{qNo}吗？请点击“确定”')
    return selection


def make_selection_func_sum(aNo):
    def selection_sum():
        global your_choice, var
        your_choice = (aNo,)
        var.set(f'要汇总A{aNo}的分数吗？请点击“确定”')
    return selection_sum


def assignmentgui():
    global your_choice, var
    your_choice = ''
    window = Tk()
    # 设置标题
    window.title('作业批改程序')
    # 设置窗口大小
    if os.name == 'posix':
        window.geometry('560x560+50+30')
    else:
        window.geometry('480x560+50+30')
    # 设置窗口是否可变长、宽，True：可变，False：不可变
    window.resizable(width=False, height=True)
    ft = tkFont.Font(family="Consolas", size=14)
    # 创建窗口
    var = StringVar()
    var.set('请选择？')
    text = "请注意！每个题目必须一次性批完，否则无法保存。\n"\
        "先批完一次作业所有题，再运行该次作业的分数汇总。\n "
    lab_text = Label(window, text=text, justify='left',
                     padx=5).grid(row=1, columnspan=5)
    for assNo in range(1, 5):
        for questionNo in range(1, 7):
            text = f'A{assNo}Q{questionNo}'
            sum_up_text = f'A{assNo} 分数汇总'
            locals()[f'selection{assNo}{questionNo}'] = make_selection_func(
                assNo, questionNo)
            Button(window, text=text, command=locals()[f'selection{assNo}{questionNo}'], width=10, height=2).grid(
                row=questionNo * 2 + 2, column=assNo, padx=5, pady=5)
            lab_text_0 = Label(window, textvariable=var, bg='yellow', font=('Arial', 14), justify='left',
                               padx=5).grid(row=18, columnspan=5)
        locals()[f'selection_sum{assNo}'] = make_selection_func_sum(
            assNo)
        Button(window, text=sum_up_text, command=locals()[f'selection_sum{assNo}'], width=10,
               height=2).grid(row=16, column=assNo, padx=5, pady=5)
    Button(window, text='确定', command=window.destroy, width=10,
           height=2).grid(row=20, column=assNo, padx=5, pady=5)
    window .mainloop()
    if your_choice:
        if len(your_choice) == 1:
            sum_up_score(your_choice[0])
        else:
            assignment(your_choice[0], your_choice[1])


assignmentgui()
