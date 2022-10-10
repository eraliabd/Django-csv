from django.shortcuts import render
from .models import About, RecentWork, Contact, Skill, Comment


def home(request):
    about = About.objects.get()
    recent_work = RecentWork.objects.all()
    skills = Skill.objects.all()

    if request.method == 'POST':
        model = Contact()
        model.name = request.POST.get('name', '')
        model.email = request.POST.get('email', '')
        model.message = request.POST.get('message', '')

        model.save()

    context = {
        'about': about,
        'works': recent_work,
        'skills': skills,
    }
    return render(request, 'index.html', context)


def detail(request, work_id, work_name):
    about = About.objects.get()
    work = RecentWork.objects.get(id=work_id)

    if request.method == 'POST':
        model = Comment()
        model.name = request.POST.get('name', '')
        model.email = request.POST.get('email', '')
        model.comment = request.POST.get('comment', '')
        model.work = work

        model.save()

    comments = work.works.filter()

    context = {
        'work': work,
        'about': about,
        'comments': comments,
    }
    return render(request, 'detail.html', context)


# def reply_detail(request, comment_id):
#     reply = Comment.objects.get(id=comment_id)
#
#     if request.method == 'POST':
#         model = ReplyComment()
#         model.name = request.POST.get('name', '')
#         model.email = request.POST.get('email', '')
#         model.reply_comment = request.POST.get('comment', '')
#         model.comment = reply
#
#         model.save()
#
#     reply_comments = reply.reply_comments.filter()
#
#     context = {
#         'replies': reply_comments,
#     }
#
#     return render(request, 'detail.html', context)
