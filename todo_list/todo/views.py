from django.shortcuts import render



def home_view(request):
    return render(request, 'html/home.html')


def todo_list_view(request):
    return render(request, 'html/todo_list.html')
