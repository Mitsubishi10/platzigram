from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

#forms
from users.forms import ProfileForm, SignupForm


#funcion de login
def login_view(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user:
            login(request,user)
            return redirect('feed')
        else:
            return render(request,'users/login.html', {'error': 'Invalid username and password'})
        
    return render(request,'users/login.html') 


#funcion de crear una cuenta
def signup(request):
    """ METODO DE INSCRIBIRSE """
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            form = SignupForm()

        return render(
            request=request,
            template_name='users/signup.html',
            context={'form': form}
        )




#funcion de cierre de sesion 
@login_required 
def logout_view(request): 
    logout(request)
    return redirect('login') 


@login_required
def update_profile(request):
    #funcion para actualizar perfil 

    profile = request.user.profile

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data

            profile.website = data['wesite']
            profile.phone_number = data['phone_number']
            profile.biography = data['biography']
            profile.picture = data['picture']
            profile.save()

            return redirect('update_profile')

        else:
            form = ProfileForm()

        return render(
            request=request,
            template_name='users/update_profile.html',
            context={
                'profile': profile,
                'user': request.user,
                'form': form

            }
        )
