from django.shortcuts import render
from django.views.generic import CreateView
from .models import Comment
from .forms import CommentForm


# Create your views here.
def comment(request):
    if request.method == 'POST':
        cmntform = CommentForm(request.POST)
        if cmntform.is_valid():
            cmntform.save()
    else:
        cmntform = CommentForm()
    return render(request, 'details.html', {'form': cmntform})
    
