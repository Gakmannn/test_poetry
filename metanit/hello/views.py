from django.shortcuts import render
from django.template.response import TemplateResponse
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect, HttpResponseNotFound, HttpResponseForbidden, HttpResponseBadRequest, JsonResponse
  

def index(request):
    # langs = []
    colors = {"red": "красный", "green": "зеленый", "blue":"синий"}
    langs = ["Python", "JavaScript", "Java", "C#", "C++"]
    data = {"header": "Hello Django",
            "message": "Welcome to Python", "person": Person("Bob", 41), "body": "<h1>Hello World!</h1>", "n": 0, "langs": langs, "data": colors, "users": ["Tom", "Sam", "Bob", "Mike"]}
    return render(request, "index.html", context=data)

def complex(request):
    header = "Данные пользователя"              # обычная переменная
    langs = ["Python", "Java", "C#"]            # список
    user = {"name": "Tom", "age": 23}          # словарь
    address = ("Абрикосовая", 23, 45)           # кортеж

    data = {"header": header, "langs": langs, "user": user, "address": address}
    return render(request, "complex.html", context=data)

def meta(request):
    return HttpResponse(f'''
      {request.META}
      <br>  
      {request.META['QUERY_STRING']}
      <br>  
      {request.scheme}
      <br>  
      {request.body}
      <br>  
      {request.path}
      <br>  
      {request.method}
      <br>  
      {request.encoding}
      <br>  
      {request.content_type}
      <br>  
      {request.GET}
      <br>  
      {request.POST}
      <br>  
      {request.COOKIES}
      <br>  
      {request.FILES}
      <br>  
      {request.headers}
      <br>  
      {request.get_full_path()}
      <br>  
      {request.get_host()}
      <br>  
      {request.get_port()}
    
    ''')


def getUser(request):
    age = request.GET.get("age", 0)
    name = request.GET.get("name", "unindent")
    return HttpResponse(f"<h2>Имя: {name}  Возраст: {age}</h2>")

def user(request, name='undefined', age=0):
    return HttpResponse(f"""
            <h2>О пользователе</h2>
            <p>Имя: {name}</p>
            <p>Возраст: {age}</p>
    """)

def about(request):
    return HttpResponse("About")

# Create your views here.


def products(request, id=-1):
    if id==-1:
        return HttpResponse(f"Список товаров")
    else:
        return HttpResponse(f"Товар {id}")


def comments(request, id):
    return HttpResponse(f"Комментарии о товаре {id}")


def questions(request, id):
    return HttpResponse(f"Вопросы о товаре {id}")

def new(request):
    return HttpResponse("Новые товары")


def top(request):
    return HttpResponse("Наиболее популярные товары")


def contact(request):
    return HttpResponseRedirect("/about")


def details(request):
    return HttpResponsePermanentRedirect("/")


def notFound(request):
    return HttpResponseNotFound("404. Not Found")


def people(request, id):
    people = ["Tom", "Bob", "Sam"]
    # если пользователь найден, возвращаем его
    if id in range(0, len(people)):
        return HttpResponse(people[id])
    # если нет, то возвращаем ошибку 404
    else:
        return HttpResponseNotFound("Not Found")


def access(request, age):
    # если возраст НЕ входит в диапазон 1-110, посылаем ошибку 400
    if age not in range(1, 111):
        return HttpResponseBadRequest("Некорректные данные")
    # если возраст больше 17, то доступ разрешен
    if (age > 17):
        return HttpResponse("Доступ разрешен")
    # если нет, то возвращаем ошибку 403
    else:
        return HttpResponseForbidden("Доступ заблокирован: недостаточно лет")


def json(request):
    return JsonResponse({"name": "Tom", "age": 38})


def person(request):
    bob = Person("Bob", 41)
    return JsonResponse(bob, safe=False, encoder=PersonEncoder)

def notaperson(request):
    bob = [1,2,4]
    return JsonResponse(bob, safe=False, encoder=PersonEncoder)

class Person:
    def __init__(self, name, age):
        self.name = name    # имя человека
        self.age = age      # возраст человека

class PersonEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, Person):
            return obj.__dict__
            return {"name": obj.name, "age": obj.age}
        return super().default(obj)

# установка куки
def set(request):
    # получаем из строки запроса имя пользователя
    username = request.GET.get("username", "Undefined")
    # создаем объект ответа
    response = HttpResponse(f"Hello {username}")
    # передаем его в куки
    response.set_cookie("username", username)
    return response

# получение куки
def get(request):
    # получаем куки с ключом username
    username = request.COOKIES["username"]
    return HttpResponse(f"Hello {username}")
