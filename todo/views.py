from django.shortcuts import render,redirect

# Create your views here.
lst = [
    {'待办事项':'遛狗','已完成':False},
    {'待办事项':'打豆豆','已完成':True}
]
for i,j in lst:
    print('%s,%s'%(i,j))
def home(request):
    global lst
    content = {'content': lst}
    if request.method == 'POST':
        if request.POST['待办事项'] == '':
            content_warning = {'content':lst,'warning':'请输入内容!'}
            return render(request, 'home.html',content_warning)
        else:
            lst.append({'待办事项':request.POST['待办事项'],'已完成':False})
            content_success = {'content':lst,'success':'添加成功!'}
            return render(request,'home.html',content_success)
    else:

        return render(request, 'home.html', content)

def about(request):
    return render(request,'todolistabout.html')

def edit(request,forloop_counter):
    content = {'待修改事项': lst[int(forloop_counter) - 1]['待办事项']}
    if request.method == 'POST':
        if request.POST['已修改事项'] == '':
            return render(request, 'todolisteditt.html', {'warning':'请输入内容!'})
        else:
            lst[int(forloop_counter) - 1]['待办事项'] = request.POST['已修改事项']
            return redirect('待办事项主页')
    else:

        return render(request,'todolisteditt.html',content)

def t_del(request,forloop_counter):
    lst.pop(int(forloop_counter) - 1)

    return redirect('待办事项主页')

def sus(request,forloop_counter):
    if lst[int(forloop_counter) - 1]['已完成'] == False:
        lst[int(forloop_counter) - 1]['已完成'] = True
        return redirect('待办事项主页')
    else:
        lst[int(forloop_counter) - 1]['已完成'] = False
        return redirect('待办事项主页')