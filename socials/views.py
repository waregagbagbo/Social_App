from django.shortcuts import render,redirect,HttpResponseRedirect
from .models import Profile,SocialTweet
from .forms import SocialTweetForm
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.


@login_required(login_url='login')
def dashboard(request):
    form = SocialTweetForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            socials = form.save(commit=False)
            socials.user = request.user
            socials.save()
            return redirect("socials:dashboard")

    followed_socials = SocialTweet.objects.filter(
        user__profile__in = request.user.profile.follows.all()
    ).order_by("-created_at")
    context = {
        'form':form
    }
    return render(request,"social_pages/dashboard.html",context)

@login_required(login_url='login')
def profile_list(request):
    # fetch all the user profiles except self
    profiles = Profile.objects.exclude(user=request.user)
    context = {
        'profiles': profiles
    }
    return render(request, 'social_pages/profile_list.html',context)

@login_required(login_url='login')
def profile(request, pk):
    profile = Profile.objects.get(pk=pk)
    if request.method == 'POST':
        current_user_profile = request.user.profile
        data = request.POST
        action = data.get('follow')
        if action == 'follow':
            current_user_profile.follows.add(profile)
        elif action == 'unfollow':
            current_user_profile.follows.remove(profile)
        current_user_profile.save()        
    context ={
        'profile':profile
    }
    return render(request,'social_pages/profile.html',context)



def registerPage(request):
    if request.method == "POST":
        #then creat an instance object by
       form = CustomUserCreationForm(request.POST)
       # theafter check if valid
       if form.is_valid():
           form.save()
           username = form.cleaned_data.get('username')
           password = form.cleaned_data.get('password1')
           user = authenticate(request,username=username,password=password)
           messages.SUCCESS(request,'Succcessful registration')
           login(request,user)                
           return redirect('socials:dashboard')
       else:
           messages.ERROR(request,'Invalid')
           messages.ERROR(request,form.erros)
    else:
        form = CustomUserCreationForm()
    context={
        'form':form
        }
    return render(request,'social_pages/register.html',context)


# login page
def loginPage(request):
    username = request.POST['username']
    password = request.POST['password1']
    user = authenticate(request,username=username, password=password1)
    if profile is not None:
        login(request,user)
        messages.success(request,"Successful, and enjoy")
        return redirect('socials:dashboard')
    else:
        return render(request,'socials:register')

def mainPage(request):
    return render(request,'social_pages/main.html')


#logout view
def logoutPage(request):
    redirect(request)
    return HttpResponseRedirect(reverse('main'))