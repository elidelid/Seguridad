from  django.shortcuts import render,HttpResponse
html_base = """
    <h1>Mi Primer Menu</h1>
    <ul>
        <li>   <a href="/">Portada</a>              </li>
        <li>   <a href="/inventario/">Acerca de</a>   </li>
        <li>   <a href="/contact/">Contacto</a>     </li>
    </ul>
"""

# relaciona la parte vista con el template home.html
def home(request, plantilla="home.html"):
    return render(request, plantilla);

def home(request):
    html_responsde = "<h1>la pagina de portada</h1>"
    html_responsde = html_base + html_responsde
    return HttpResponse(html_responsde);

def inventario(request, plantilla="inventario.html"):
    return render(request, plantilla);

def about(request):
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

def about(request, plantilla="about.html"):
    return render(request, plantilla);

def contact(request, plantilla="contact.html"):
    return render(request, plantilla);



