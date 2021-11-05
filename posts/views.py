"""Las Vistas de la aplicscion posts"""
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render 

#Utilities
from posts.forms import PostForm

# from django.http import HttpResponse
from  datetime  import datetime


posts= [
    {
        'title': 'Mont Blac',
        'user': { 
            'name': 'Yesica Cortes',
            'picture':'https://picsum.photos/60/60?image=1027'
        },
        'timestamp':datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'http://picsum.photos/800/600/?image=1036',
        
    },
   {
        'title': 'Via Lactea',
        'user': { 
            'name': 'Christian  Van der  Henst',
            'picture':'https://picsum.photos/60/60?image=1005'
        },
        'timestamp':datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'http://picsum.photos/800/800/?image=903',
        
    },
    {
        'title': 'Nuevo auditorio',
        'user': { 
            'name': 'Uriel (thespianartist)',
            'picture':'https://picsum.photos/60/60?image=883'
        },
        'timestamp':datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'http://picsum.photos/500/700/?image=1076',
        
    },
]

@login_required
def list_posts(request):

  return render (request,'posts/feed.html',{'posts':posts}) 

@login_required
def create_post(request):
#crear un nuevo post
         
        if request.method == 'POST':
            form = PostForm(request.POST,request.FILES)
            if form.isvalid():
                form.save()
                return redirect('feed') 

        else: 
            form = PostForm
            
        return render ( 
            request=request,
            template_name='posts/new.html',
            context={
                'form':form,
                'user': request.user,
                'profile':request.user.profile
            }

        )    



