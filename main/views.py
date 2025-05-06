from django.contrib import messages
from django.shortcuts import redirect, render , get_object_or_404
from .models import Article, Contacts
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import JsonResponse
from django.core.files.storage import FileSystemStorage

def articles(request):
    query = request.GET.get('q')
    articles = Article.objects.all()

    if query:
        articles = articles.filter (
            title__icontains=query
        ) 
    featured = articles[:1]
    context = {'articles': articles, 'featured': featured}
    return render (request, 'main/articles.html', context)

def main(request):
    latest = Article.objects.all()[:3]
    return render (request, 'main/home.html', {'latest': latest})

# Create your views here.

def article_detail(request,slug):
    article = get_object_or_404(Article, slug=slug)
    return render(request, 'main/article_detail.html', {'article': article})

@login_required
def custom_upload_function(request):
    if request.method == 'POST' and request.FILES.get('upload'):
        file = request.FILES['upload']
        fs = FileSystemStorage()
        filename = fs.save(file.name, file)  # Сохраняем файл в заданном месте
        file_url = fs.url(filename)  # Получаем URL для доступа к файлу
        return JsonResponse({
            'uploaded': 1,
            'fileName': filename,
            'url': file_url
        })
    return JsonResponse({'uploaded': 0})

def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')  # в форме это "subject"
        message = request.POST.get('message')  # в форме это "message"

        if name and email and subject and message:
            contact = Contacts(name=name, email=email, subject=subject, message=message)
            contact.save()

            messages.success(request, 'Спасибо за сообщение!')
            return redirect('contacts')
        else:
            messages.error(request, 'Пожалуйста, заполните все поля.')

    return render(request, 'main/contacts.html')

def page_not_found(request, exception):
    return render(request, '404.html', status=404)

def server_error(request):
    return render(request, '500.html', status=500)

def permission_denied(request, exception):
    return render(request, '403.html', status=403)

