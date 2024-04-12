from django.shortcuts import redirect, reverse
from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.request import Request

from .models import Book, Profile
from .serializers import BookSerializer, ProfileSerializer


def _get_book_info():
    """
    Функция генерирующая сводную информацию по книгам с учетом профилей.

    Args:

    Returns:
        books_info (list[dict[str, str|int|bool]]): сводная инфо по книгам
        profiles (list[Profile]): список объектов Профиль
    """

    profiles = Profile.objects.values('column_name', 'is_visible')
    col_status = {profile['column_name']: profile['is_visible']
                    for profile in profiles}

    books = Book.objects.all()
    books_slz = BookSerializer(books, many=True)

    books_info = [[{'column_value': book[col], 'is_visible': col_status[col]}
                    for col in book] for book in books_slz.data]

    return books_info, profiles


@api_view(['GET', 'POST'])
@renderer_classes([TemplateHTMLRenderer])
def book(request: Request, pk: int = None, action: str = None) -> Response:
    """
    API функция для управления книгами: добавлять, изменять и удалять книги.
    И для управления видимостью параметров книг.

    Args:
        request (Request): параметры входящего запроса
        pk (int): индекс книги (defaul=None)
        action (str): флаг действия для управления книгами (default=None)

    Returns:
        (Response): ответ в виде шаблона html страницы с обработанными данными
    """

    if request.method == 'GET':

        if not pk and not request.data and not action:
            print('GET', end='\n\n')

            books, profiles = _get_book_info()

            return Response({'books': books,
                             'profiles': profiles,},
                            template_name='bookapp/main.html',
                            status=status.HTTP_200_OK)
        
        if action == 'create':
            print('CREATE', end='\n\n')

            return Response(template_name='bookapp/book_form.html')

        
        if action == 'update':
            print('UPDATE_form')

            book = Book.objects.get(pk=pk)
            serializer = BookSerializer(book)
            return Response(serializer.data,
                            template_name='bookapp/book_form.html')
    
        if action == 'del':
            print('DELETE', end='\n\n')

            book = Book.objects.get(pk=pk)
            book.delete()
            books, profiles = _get_book_info()

            return redirect(reverse("bookapp:books"))
            
        
    elif request.method == 'POST':
        
        if action == 'update':
            print('PUT', end='\n\n')
            
            book = Book.objects.get(pk=pk)
            serializer = BookSerializer(book, data=request.data)

        elif action == 'create':
            print('POST', end='\n\n')

            serializer = BookSerializer(data=request.data)

        else:
            print('POST profiles form', end='\n\n')

            profiles = Profile.objects.all()
            for profile in profiles:
                profile.is_visible = True if request.data.get(profile.column_name) == 'True' else False
                profile.save()

            return redirect(reverse("bookapp:books"))
        
        if serializer.is_valid():
            serializer.save()

            return redirect(reverse("bookapp:books"))
        
        faild_data = serializer.errors
        faild_data['flag'] = 'error'

        return Response(faild_data, template_name='bookapp/book_form.html', status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
@renderer_classes([TemplateHTMLRenderer])
def profile(request: Request) -> Response:
    """
    API функция для управления видимостью параметров книг.

    Args:
        request (Request): параметры входящего запроса

    Returns:
        (Response): ответ в виде шаблона html страницы с обработанными данными
    """
    if request.method == 'GET':
        profiles = Profile.objects.all()
    
    elif request.method == 'POST':
        profiles = Profile.objects.all()
        for profile in profiles:
            profile.is_visible = True if request.data.get(profile.column_name) == 'True' else False
            profile.save()

    return Response({'profiles': profiles,},
                    template_name='bookapp/profiles_form.html',
                    status=status.HTTP_200_OK)
