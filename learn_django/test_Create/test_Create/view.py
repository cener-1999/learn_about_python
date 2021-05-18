from  django.shortcuts import render

def run(request):
    context={}
    context['key']="values"
    return render(request,'index.html',context)