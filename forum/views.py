from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import *
from django.db.models import Count, Q, F
from django.contrib.auth.decorators import login_required
# importing messages
from django.contrib import messages

# Model Forms.
from .forms import UserPostForm, AnswerForm #, answer
# String module
from django.template.loader import render_to_string

from .models import UserPost

# Create your views here.

def home(request):

    sort_by = request.GET.get('sort', 'postdate')  # Default sort by date created
    
    ordering_options = {
        'category': 'category',
        'views': '-topicview_count', 
        'replies': '-answer_count',
        'postdate': '-date_created',
        'gatorpoints': '-gatorpnts',
    }

    # Validate sorting option
    if sort_by not in ordering_options:
        sort_by = 'date_created'

    user_posts = UserPost.objects.all().order_by(ordering_options[sort_by])

    #user_posts = UserPost.objects.all()
    
    # Display latest posts.
    latest_blogs = BlogPost.objects.order_by('-timestamp')[0:3]

    latest_topics = UserPost.objects.order_by('-date_created')[0:3]
    
    context = {
        'user_posts':user_posts,
        'latest_blogs':latest_blogs,
        'latest_topics':latest_topics,
        'sort_by': sort_by,
        'ordering_options': ordering_options,
    }
    return render(request, 'forum-main.html', context)

@login_required(login_url='login')
def userPost(request):
    # User Post form.
    form = UserPostForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            title = request.POST.get('title')
            category = request.POST.get('category')
            description = request.POST.get('description')
            gatorpnts = request.POST.get('gatorpnts')
            topic = UserPost.objects.create(category=category, title=title, author=request.user.author, description=description, gatorpnts=gatorpnts)
            topic.save()
            return redirect('home')
    else:
        form = UserPostForm()

    context = {'form':form}
    return render(request, 'user-post.html', context)

@login_required(login_url='login')
def postTopic(request, pk):
    # Get specific user post by id.
    post_topic = get_object_or_404(UserPost, pk=pk)

    # Count Post View only for authenticated users
    if request.user.is_authenticated:
        TopicView.objects.get_or_create(user=request.user, user_post=post_topic)

    # Get all answers of a specific post.
    answers = Answer.objects.filter(user_post = post_topic)
    
    # Get points assigned to the post to align with the answers
    gatorpnts = UserPost.objects.get(title=post_topic).gatorpnts

    # Answer form.
    answer_form = AnswerForm(request.POST or None)
    if request.method == "POST":
        if answer_form.is_valid():
            content = request.POST.get('content')
            # passing User Id & User Post Id to DB
            ans = Answer.objects.create(user_post=post_topic, user=request.user, content=content, gatorpnts=gatorpnts)
            ans.save()
            return HttpResponseRedirect(post_topic.get_absolute_url())
    else:
        answer_form = AnswerForm()

    context = {
        'topic':post_topic,
        'answers':answers,
        'answer_form':answer_form,
        'is_moderator': request.user.author.is_moderator,  # Pass moderator status
        'post_is_open': post_topic.is_open,  # Pass post status
        'gatorpnts':gatorpnts,
    }

    # Add accept_answer_url to the context for each answer
    for answer in answers:
        answer.accept_answer_url = reverse('accept_answer', kwargs={'pk': answer.pk})
        context['answers'] = answers  # Update the context with modified answers

    return render(request, 'topic-detail.html', context)

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


@login_required(login_url='login')
def accept_answer(request, pk):
    answer = get_object_or_404(Answer, pk=pk)
    user_post = answer.user_post
    user_name = answer.user.username
 
    if request.user == user_post.author.user:
        # Unaccept all other answers for this post
        user_post.answer_set.exclude(pk=pk).update(accepted=False)

        # Toggle the accepted status of the selected answer
        answer.accepted = not answer.accepted
        answer.save()
    
    if answer.accepted == True and Leaderboard.objects.filter(lead_names=user_name).exists() == False:
        leaders = Leaderboard.objects.create(user=answer.user, lead_names=user_name)
        leaders.save()
        Leaderboard.objects.filter(user = answer.user).update(tot_gatorpnts=F('tot_gatorpnts')+answer.gatorpnts)
    elif answer.accepted == True and Leaderboard.objects.filter(lead_names=user_name).exists() == True:
        Leaderboard.objects.filter(user = answer.user).update(tot_gatorpnts=F('tot_gatorpnts')+answer.gatorpnts)
    elif answer.accepted == False:
        pass
    else:
        pass

    return HttpResponseRedirect(user_post.get_absolute_url())

@login_required(login_url='login')
def close_post(request, pk):
    if request.user.author.is_moderator:
        post = get_object_or_404(UserPost, pk=pk)
        post.is_open = False
        post.save()
    return redirect('topic-detail', pk=pk)

@login_required(login_url='login')
def open_post(request, pk):
    if request.user.author.is_moderator:
        post = get_object_or_404(UserPost, pk=pk)
        post.is_open = True
        post.save()
    return redirect('topic-detail', pk=pk)


