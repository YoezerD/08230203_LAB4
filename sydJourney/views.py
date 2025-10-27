from django.shortcuts import render

def index(request):
    # Renders the learning journey page
    return render(request, 'sydJourney/index.html')

def aboutMe(request):
    # Renders About Me page
    return render(request, 'sydJourney/aboutMe.html')

