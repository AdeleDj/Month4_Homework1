from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Book

# Create your views here.
def twain(request):
    return HttpResponse('Через 20 лет вы будете больше разочарованы теми вещами, которые вы не делали, чем теми, которые вы сделали. Так отчальте от тихой пристани. Почувствуйте попутный ветер в вашем парусе. Двигайтесь вперед, действуйте, открывайте! (Марк Твен)')

def remarque(request):
    return HttpResponse('Чем меньше знаешь, тем проще жить. Знание делает человека свободным, но несчастным. Выпьем лучше за наивность, за глупость и за все, что с нею связано, — за любовь, за веру в будущее, за мечты о счастье; выпьем за дивную глупость, за утраченный рай! (Эрих Мария Ремарк)')

def tolstoi(request):
    return HttpResponse('Все приходит вовремя для того, кто умеет ждать. (Лев Толстой)')


def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})

def book_detail(request, id):
    book = get_object_or_404(Book, id=id)
    return render(request, 'books/book_detail.html', {'book': book})