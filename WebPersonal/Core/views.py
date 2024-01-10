from django.shortcuts import render, HttpResponse

html_base = """
            <h1>Mi Web Personal</h1>
            <ul>
                <li><a href="/">Portada</a></li>
                <li><a href="/about/">Acerca de</a></li>
            </ul>
            """


#definiendo HOME
def home(request):
    return HttpResponse(html_base + '<h1> Mi web personal </h1>')


#definiendo ABOUT
def about(request):
    return HttpResponse(html_base + '''
                        <h1>Mi Web Personal</h1>
                        <h2>Acerca de</h2>
                        <p>Me llamo Lucas y practico con Django</p>
                        
                        '''
                        )
