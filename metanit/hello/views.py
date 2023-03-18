from django.shortcuts import render
from django.http import HttpResponse
  

def index(request):
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


def about(request, name, age):
    return HttpResponse(f"""
            <h2>О пользователе</h2>
            <p>Имя: {name}</p>
            <p>Возраст: {age}</p>
    """)

def contact(request):
    return HttpResponse("Контакты")
# Create your views here.
