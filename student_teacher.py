#!/usr/bin/env python3

import sys
from collections import Counter

class Person(object):
    """
    返回具有给定名称的 Person 对象
    """

    def __init__(self, name):
        self.name = name

    def get_details(self):
        """
        返回包含人名的字符串
        """
        return self.name

    def get_grade(self,scores):
        return ''



class Student(Person):
    """
    返回 Student 对象，采用 name, branch, year 3 个参数
    """

    def __init__(self, name, branch, year):
        Person.__init__(self, name)
        self.branch = branch
        self.year = year

    def get_details(self):
        """
        返回包含学生具体信息的字符串
        """
        return "{} studies {} and is in {} year.".format(self.name, self.branch, self.year)

    def get_grade(self,scores):
        c = Counter(scores)
        pc = c['A']+c['B']+c['C']
        return "Pass: {}, Fail: {}".format(pc,c['D'])


class Teacher(Person):
    """
    返回 Teacher 对象，采用字符串列表作为参数
    """
    def __init__(self, name, papers):
        Person.__init__(self, name)
        self.papers = papers

    def get_details(self):
        return "{} teaches {}".format(self.name, ','.join(self.papers))

    def get_grade(self,scores):
        c = Counter(scores).most_common()
        seq = []
        for k,v in c:
            seq.append("{}: {}".format(k,v))
        return ",".join(seq)


if len(sys.argv)!=3:
    print("arguments  count is not 2!")
    sys.exit(-1)
student1 = Student('Kushal', 'CSE', 2005)
teacher1 = Teacher('Prashad', ['C', 'C++'])
type = sys.argv[1]
scores = sys.argv[2]
scorelist = list(scores)
for s in scorelist:
    if "ABCD".find(s)<=-1:
        raise ValueError("The second arguments must be in ABCD!")
if type=='student':
    print(student1.get_grade(scores))
    sys.exit(0)
if type=='teacher':
    print(teacher1.get_grade(scores))
    sys.exit(0)
print("The first arguments is error!")
