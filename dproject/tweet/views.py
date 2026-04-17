from django.shortcuts import render
from .models import Tweet
from .forms import TweetForm # import the TweetForm from the forms module to use it in the views for creating and editing tweets
from django.shortcuts import get_object_or_404 , redirect # import get_object_or_404 to retrieve an object or return a 404 error if it does not exist, and redirect to redirect users after certain actions (like after creating a tweet)
from django.contrib.auth.decorators import login_required  # Import the login_required decorator
from django.contrib.auth import login  # Import the login function for logging in users
from .forms import UserRegistrationForm  # Import the UserRegistrationForm for user registration

# Create your views here.

def index(request):
    return render(request, 'index.html')


def tweet_list(request):
    tweets = Tweet.objects.all().order_by('-created_at') # retrieve all Tweet objects from the database and order them by the created_at field in descending order (newest first)
    return render(request, 'tweet_list.html', {'tweets': tweets}) # render the 'tweet_list.html' template and pass the retrieved tweets as context to be displayed in the template

@login_required # use the login_required decorator to ensure that only authenticated users can access the tweet_create view, which allows users to create new tweets. If a user is not logged in, they will be redirected to the login page.
def tweet_create(request):
    if request.method == "POST": # check if the request method is POST, which indicates that the form has been submitted
        form = TweetForm(request.POST, request.FILES) # create an instance of the TweetForm with the submitted data (request.POST) and any uploaded files (request.FILES)
        if form.is_valid(): # check if the form data is valid according to the form's validation rules
            tweet = form.save(commit=False)
            tweet.user = request.user # set the user of the tweet to the currently logged-in user (request.user) before saving the tweet to the database
            tweet.save()
            return redirect('tweet_list')  # redirect to tweet list page
    else:
        form = TweetForm()

    return render(request, 'tweet_form.html', {'form': form})

@login_required 
def tweet_edit(request, tweet_id): 
    tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user)

    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES, instance=tweet)
        if form.is_valid():
            tweet =form.save(commit=False)
            tweet.user = request.user
            form.save()
            return redirect('tweet_list')
    else:
        form = TweetForm(instance=tweet)

    return render(request, 'tweet_form.html', {'form': form})


@login_required
def tweet_delete(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user)
    if request.method == 'POST':
        tweet.delete()
        return redirect('tweet_list')
    return render(request, 'tweet_confirm_delete.html', {'tweet': tweet})

# registration view

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)  # Create a user object but don't save it to the database yet
            user.set_password(form.cleaned_data['password1'])  # Set the user's password using the cleaned data from the form
            user.save()
            login(request, user)
            return redirect('tweet_list')  # Redirect to the tweet list page after successful registration and login
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})