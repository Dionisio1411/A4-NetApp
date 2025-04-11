from django.shortcuts import render
from .models import Profile
from .forms import ProfileForm
from django.http import JsonResponse

# Create your views here.
def my_profile_view(requst):
    obj = Profile.objects.get(user=requst.user)
    form = ProfileForm(request.POST or None, request.FILES or None, instance=obj)
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        if form,is_valid():
            instance = form.save()
            return JsonResponse({
                'bio': instance.bio,
                'avatar': instance.avatar.url,
                'user': instance.user.username,
            })
    context = {
        'form': form,
        'obj': obj,
    }
    return render(request, 'profiles/main.html', context)

