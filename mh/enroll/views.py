from django.shortcuts import render,HttpResponse
from django.contrib import messages

# Create your views here.
from .forms import stuform,teaform

def stu(request):
    if request.method=='POST':
        
        st=stuform(request.POST)
        if st.is_valid():
            st.save()
            st=stuform()
        else:
            HttpResponse("invalid")    
    else:
        st=stuform()
    return render(request,'enroll/stuinfo.html',{'st':st})  


def tea(request):
    if request.method=='POST':
        
        tf=teaform(request.POST)
        if tf.is_valid():
            tf.save()
            tf=stuform()
            
            messages.debug(request,'your registration is done')
            messages.info(request,'your registration is done')
            messages.error(request,'your registration is done')
        else:
            HttpResponse("invalid") 
               
    else:
        tf=stuform()
    return render(request,'enroll/teainfo.html',{'tf':tf})            
        