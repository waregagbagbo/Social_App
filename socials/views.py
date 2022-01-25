from django.shortcuts import render
from .models import Profile,SocialTweet
from .forms import SocialTweetForm
from .forms import CustomUserCreationForm

# Create your views here.

'''def dashboard(request):
    if request.method == 'POST':
        form  = SocialForm(request.POST)
        if form.is_valid():
            socia = form.save(commit= False)
            socia.user = request.user
            socia.save()
            return redirect("social:dashboard")
    form = SocialForm()
    context ={
        'form'
    }

    return render(request,'social_pages/dashboard.html')'''



def dashboard(request):
    form = SocialTweetForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            socials = form.save(commit=False)
            socials.user = request.user
            socials.save()
            return redirect("socials:dashboard")


    followed_socials = SocialTweet.objects.filter(
        user__profile__in=request.user.profile.follows.all()
    ).order_by("-created_at")
    context = {
        'form':form
    }
    return render(request, "social_pages/dashboard.html",context)




def profile_list(request):
    # fetch all the user profiles except self
    profiles = Profile.objects.exclude(user=request.user)
    context = {
        'profiles': profiles
    }
    return render(request, 'social_pages/profile_list.html',context)



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


def userAccount(request):
    return render(request,'users/home.html')



def register(request):
    if request.method == "GET":
        return render(
            request, "users/register.html",
            {"form": CustomUserCreationForm}
        )
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.backend = "django.contrib.auth.backends.ModelBackend"
            login(request, user)
            return redirect(reverse("dashboard"))