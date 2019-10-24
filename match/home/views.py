from django.shortcuts import render
from django.shortcuts import HttpResponse
from . import models


# 新闻中心
def news(req):
    contents = models.News.objects.all()
    return render(req, "home/news.html", {"contents": contents})


# 主页
def index(req):
    return render(req, "base.html")


# 通知公告
def notice(req):
    return render(req, "home/notice.html")


# 大赛方案
def plan(req):
    return render(req, "home/plan.html")


# 走进大赛
def walk(req):
    return render(req, "home/walk.html")


# 领导关怀
def leader(req):
    return render(req, "home/leader.html")


# 我要参赛
def mode(req):
    return render(req, "home/mode.html")


# 联系我们
def contact(req):
    return render(req, "home/contact.html")
