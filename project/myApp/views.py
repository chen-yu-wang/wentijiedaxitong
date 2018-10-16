from django.shortcuts import render

# Create your views here.


from .models import Student, Problem, Answer

def registered ( um ,pw ):
    student1 = Student(username = um,password = pw)
    student1.save()

def logIn (um,pw):
    st = Student.objects.all()
    n = len(st)
    i = 0
    while st[i].username != um:
        i += 1
        if i == n:
            return False
    if st[i].password == pw:
        return st[i]
    else:
        return False

def inProblem(pro,stu):
    pro1 = Problem(content = pro, belong = stu)
    pro1.save()
    return pro1

def inAnswer(ans,pro):
    ans1 = Answer(content = ans, belong = pro)
    ans1.save()
    return ans1

def zanProblem(pro):
    pro.zannum += 1

def caiProblem(pro):
    pro.cainum += 1

def zanAnswer(ans):
    ans.zannum += 1

def caiAnswer(ans):
    ans.cainum += 1

def searchProblem(pro):
    return pro.content

def searchAnswer(ans):
    return ans.content

def searchProblemZanNum(pro):
    return pro.zannum

def searchProblemCaiNum(pro):
    return pro.cainum

def searchAnswerZanNum(ans):
    return ans.zannum

def SearchAnswerCaiNum(ans):
    return ans.cainum

def getProblem(stu):
    return stu.problem_set.all()

def getAnswer(pro):
    return pro.answer_set.all()