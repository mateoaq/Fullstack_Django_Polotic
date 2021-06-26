from .models import Categoria

def blog_menu(request):

    link_menu = Categoria.objects.all()
    return {
        'link_menu': link_menu
    }