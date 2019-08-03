from django.shortcuts import render

# Create your views here.
lst = [
    {'待办事项':'遛狗','已完成':False},
    {'待办事项':'遛狗','已完成':True}
]
for i,j in lst:
    print('%s,%s'%(i,j))
def home(request):
    global lst
    content = {'content': lst}
    if request.method == 'POST':
        if request.POST['待办事项'] == '':
            return render(request, 'home.html', {'warning':'请输入'},content)
        else:
            lst.append({'待办事项':request.POST['待办事项'],'已完成':False})

            return render(request,'home.html',content)
    else:

        return render(request, 'home.html', content)

def about(request):
    return render(request,'todolistabout.html')

def edit(request):
    return render(request,'todolisteditt.html')