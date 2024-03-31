from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import *
from django.db.models import Count, Q
from django.contrib.auth.decorators import login_required
# importing messages
from django.contrib import messages

# Model Forms.
from .forms import UserPostForm, AcceptJobform
# String module
from django.template.loader import render_to_string

# Create your views here.

def home(request):
    user_posts = UserPost.objects.all()
    
    # Display latest posts.
    latest_blogs = BlogPost.objects.order_by('-timestamp')[0:3]

    latest_topics = UserPost.objects.order_by('-date_created')[0:3]
    
    context = {
        'user_posts':user_posts,
        'latest_blogs':latest_blogs,
        'latest_topics':latest_topics
    }
    return render(request, 'forum-main.html', context)

@login_required(login_url='login')
def userPost(request):
    # User Post form.
    form = UserPostForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            title = request.POST.get('title')
            description = request.POST.get('description')
            topic = UserPost.objects.create(title=title, author=request.user.author, description=description)
            topic.save()
            return redirect('home')
    else:
        form = UserPostForm()

    context = {'form':form}
    return render(request, 'user-post.html', context)

@login_required(login_url='login')
@login_required(login_url='login')
def postTopic(request, pk):
    post_topic = get_object_or_404(UserPost, pk=pk)

    context = {
        'topic': post_topic,
    }
    return render(request, 'topic-detail.html', context)

@login_required(login_url='login')
def acceptJobPosting(request, pk):
    post = get_object_or_404(UserPost, id=pk)
    if request.method == 'POST':
        # Process the form submission
        comment = request.POST.get('comment')  # Assuming the comment is submitted via a form

        # Save the job acceptance
        job_acceptance = JobAcceptance.objects.create(user_post=post, accepted_by=request.user, comment=comment)
        job_acceptance.save()

        # Mark the job posting as accepted
        post.accepted = True
        post.save()

        # Redirect to the job posting detail page
        return redirect('topic-detail', pk=pk)

    # If the request method is not POST (e.g., GET request), render a form to accept the job
    return render(request, 'accept_job_posting.html', {'post': post})

@login_required(login_url='login')
def userDashboard(request):
    topic_posted = request.user.author.userpost_set.all()
    ans_posted = request.user.answer_set.all()
    topic_count = topic_posted.count()
    ans_count = ans_posted.count()
    
    context = {
        'topic_posted':topic_posted,
        'ans_posted':ans_posted,
        'topic_count':topic_count,
        'ans_count':ans_count
    }
    return render(request, 'user-dashboard.html', context)

def searchView(request):
    queryset = UserPost.objects.all()
    search_query = request.GET.get('q')

    if search_query:
        queryset = queryset.filter(
            Q(title__icontains=search_query) | Q(description__icontains=search_query) 
        ).distinct()
        
        q_count = queryset.count()
    else:
        messages.error(request, f"Oops! Looks like you didn't put any keyword. Please try again.")
        return redirect('home')

    
    context = {
        'queryset':queryset,
        'search_query':search_query,
        'q_count':q_count
    }

    return render(request, 'search-result.html', context)


# Blog listing page view.
def blogListView(request):
    
    # Display all blog posts.
    all_posts = BlogPost.objects.all()
    
    context = {
        'all_posts':all_posts
    }
    return render(request, 'blog-listing.html', context)

    
# Blog single post detail view.
def blogDetailView(request, slug):
    # Get specific post by slug.
    post_detail = get_object_or_404(BlogPost, slug=slug)

    context = {
        'post_detail':post_detail,
    }

    return render(request, 'blog-detail.html', context)  



