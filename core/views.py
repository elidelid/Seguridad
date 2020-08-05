from  django.shortcuts import render,HttpResponse
html_base = """
    <h1>Menu</h1>
    <ul>
        <li>   <a href="/">Portada</a>              </li>
        <li>   <a href="/inventario/">Acerca de</a>   </li>
        <li>   <a href="/contact/">Contacto</a>     </li>
    </ul>
"""
def home(request, plantilla="home.html"):
    return render(request, plantilla);


def home(request):
    html_responsde = "<h1>¿Quiénes somos?</h1>"
    html_responsde = html_base + html_responsde
    return HttpResponse(html_responsde);

def inventario(request, plantilla="inventario.html"):
    return render(request, plantilla);

def inventario(request):
    html_responsde = "<h1>Pagina Acerca De </h1>"
    html_responsde = html_base + html_responsde
    return HttpResponse(html_responsde);

def contact(request, plantilla="contact.html"):
    return render(request, plantilla);

def contact(request):
    html_responsde = "<h1>la pagina de contacto</h1>"
    html_responsde = html_base + html_responsde
    return HttpResponse(html_responsde);

#Template Tag
def home(request, plantilla="home.html"):
    return render(request, plantilla);

def Seinpri(request, plantilla="Seinpri.html"):
    return render(request, plantilla);

def contact(request, plantilla="contact.html"):
    return render(request, plantilla);




