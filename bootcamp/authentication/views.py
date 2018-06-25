from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django import forms
from bootcamp.authentication.forms import SignUpForm
from bootcamp.feeds.models import Feed
from django.core.urlresolvers import reverse_lazy

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if not form.is_valid():
            return render(request, 'authentication/signup.html',
                          {'form': form})

        # else:
        #     username = form.cleaned_data.get('username')
        #     email = form.cleaned_data.get('email')
        #     password = form.cleaned_data.get('password')
        #     User.objects.create_user(username=username, password=password,
        #                              email=email)
        #     user = authenticate(username=username, password=password)
        #     login(request, user)
        #     welcome_post = '{0} has joined the network.'.format(user.username)
        #     # feed = Feed(user=user, post=welcome_post)
        #     # feed.save()
        #     return redirect('/')
        else:
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            User.objects.create_user(username=username, password=password,
                                     email=email)
            user = authenticate(username=username, password=password)
            login(request, user)
            welcome_post = '{0} has joined the network.'.format(user.username)
            subject="Thankyou for signup"
            message='welcome to our channel'
            from_email=settings.EMAIL_HOST_USER
            to_list=[email,settings.EMAIL_HOST_USER]
            send_mail("subject","this it ",'rasiist2018@gmail.com',['mansi.deolalikar@gmail.com'])
            send_mail(subject, message, from_email,to_list, fail_silently=True )


    else:
        return render(request, 'authentication/signup.html',
                      {'form': SignUpForm()})
# SendUserEmails view class
    #success_url = reverse_lazy('admin:users_user_changelist')

# SendUserEmails view class
