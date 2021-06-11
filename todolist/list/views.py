from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import List


# Create your views here.
# 直接访问,设置一个链接，返回一个固定界面
def list_view(request):
    return HttpResponseRedirect('/list/tolist')

# 增加事项
def add_list(request):
    if request.method=='POST':
        # 获取表单内容
        toList = request.POST['todolist']
        deadLine = request.POST['date']
        # 创建数据
        result = List.objects.create(todo_List=toList, dead_Line=deadLine)
        #测试，如果创建未成功，提示出错
        if result:
            #return HttpResponse('成功')  #用来调试单个功能
            return HttpResponseRedirect('/list/tolist')
        else:
            return HttpResponse('-----add error-----')


# 显示待办事项
def to_list(request):
    id = request.GET.get('id')
    #todo_list = List.objects.all()  #显示全部
    #按照没完成的和截止日期先后，按顺序输出
    todo_list = List.objects.filter(isDone=False).order_by('dead_Line')
    return render(request, 'list/list.html', locals())


# 更新事项
def update_list(request):
    id = request.GET.get('id')
    #获取响应的id值
    # 尝试能否获得数据，若不能抛出错误
    try:
        list = List.objects.get(id=id, isDone=False)
    except Exception as e:
        print('---error')
        return HttpResponse('---The list id is error')
    list.isDone = True
    list.save()
    return HttpResponseRedirect('/list/tolist')


# 显示已办事项
def done_list(request):
    #done_list = List.objects.all()
    #换个界面，显示已完成的to do list
    done_list = List.objects.filter(isDone=True)
    return render(request, 'list/done.html', locals())


# 删除事项
def delete_list(request):
    #1.获取id
    # 2.并根据id获取到数据库中的指定数据
    # 3.删除
    id = request.GET.get('id')
    list = List.objects.get(id=id)
    result = list.delete()
    #成功则刷新一下界面，不成功输出错误
    if result:
        return HttpResponseRedirect('/list/tolist')
    else:
        return HttpResponse('-----delete error-----')
