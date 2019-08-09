# 本程序所使用的语言版本为:Python3.7
# -*-encoding: utf-8 -*-
# @Author    : Luo Guifeng
# @Email     : luoguifeng14@126.com
# @IDE       : PyCharm
# @Project   : Python-project-case
# @File      : studentsystem.py
# @Date      : 2019/8/8
# @Time      : 14:01

import re, os

def main():
    ctrl = True
    while (ctrl):
        menu()
        option = input("请选择：")
        option_str = re.sub("\D", "", option)
        if option_str in ['0', '1', '2', '3', '4', '5', '6', '7']:
            option_int = int(option_str)
            if option_int == 0 :
                print("您已经退出学生信息管理系统！")
                ctrl = False
            elif option_int == 1:
                insert()
            elif option_int ==2:
                search()
            elif option_int ==3:
                delete()
            elif option_int ==4:
                modify()
            elif option_int == 5:
                sort()
            elif option_int == 6:
                total()
            elif option_int == 7:
                show()


# 录入学生成绩信息函数
def insert():
    studentList=[]
    mark = True
    while mark:
        id = input("请输入ID（如1001）：")
        if not id:
            break
        name = input('请输入姓名：')
        if not name:
            break
        try:
            english = int(input('请输入英语成绩：'))
            python = int(input('请输入python成绩：'))
            c = int(input('请输入C语言成绩：'))
        except:
            print('输入无效，不是整型数值...重新录入信息')
            continue

        student = {'id': id, 'name': name, 'english': english, 'python': python, 'c': c}
        studentList.append(student)
        inputMark = input('是否继续添加？（y/n）:')
        if inputMark == 'y':
            mark = True
        else:
            mark = False
    save(student)
    print('学生信息录入完毕！')


# 查找学生成绩信息
def search():
    pass


# 删除学生信息
def delete():
    mark = True
    while mark:
        studentId = input('请输入要删除的学生ID：')
        if studentId is not '':
            if os.path.exists(filename):
                with open(filename, 'r') as rfile:
                    student_old = rfile.readlines()
            else:
                student_old = []
            ifdel = False
            if student_old:
                with open(filename, 'w') as wfile:
                    d = {}
                    for list in student_old:
                        d = dict(eval(list))
                        if d['id'] !=studentId:
                            wfile.write(str(d) + '\n')
                        else:
                            ifdel = True
                    if ifdel:
                        print('ID为{}的学生信息已经被删除...'.format(studentId))
                    else:
                        print('没有找到ID为{}的学生信息...'.format(studentId))
            else:
                print('无学生信息...')
                break
            show()
            inputMark = input('是否继续删除？（y/n）:')
            if inputMark == 'y':
                mark = True
            else:
                mark = False


# 修改学生成绩信息
def modify():
    pass


# 学生成绩排名
def sort():
    pass


# 统计学生总人数
def total():
    pass


# 显示所有学生信息
def show():
    pass


#将学生信息保存到文件
def save(student):
    try:
        student_txt = open(filename, 'a')
    except Exception as e:
        student_txt = open(filename, 'w')
    for info in student:
        student_txt.write(str(info) + '\n')
    student_txt.close()


def menu():
    print("""    
    |————————————学生信息管理系统————————————|
    |                                      |
    |   ============功能菜单============    |
    |                                       |
    |   1.录入学生成绩信息                   |
    |   2.查找学生成绩信息                   |
    |   3.删除学生信息                       |
    |   4.修改学生成绩信息                   |
    |   5.学生成绩排名                       |
    |   6.统计学生总人数                     |
    |   7.显示所有学生信息                   |
    |   0.退出系统                          |
    |  ==================================  |
    |  说明：通过数字或↑↓方向键选择菜单       |
    |———————————————————————————————————————|
        """)


if __name__ == '__main__':
    main()


