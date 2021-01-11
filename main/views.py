from django.http import JsonResponse
from django.shortcuts import render
from main.models import Slider, Review, Menu, Cheff, Partner, Register, Information, Category, Size, Award, Galery,Rebate, Filial, Blog
import math
# Create your views here.


def indexHandler(request):
    if request.method == 'GET':
        sliders = Slider.objects.filter(status=0)
        reviews = Review.objects.filter(status=0).order_by('-rating')
        menu = Menu.objects.filter(status=0).order_by('-rating')
        best_menus = Menu.objects.filter(is_best_seller=True)
        rebate_menus = Menu.objects.filter(is_rebate=True)
        cheffs = Cheff.objects.filter(status=0).order_by('-rating')[:2]
        partners = Partner.objects.filter(status=0).order_by('-rating')
        informations = Information.objects.filter(status=0)
        categorys = Category.objects.filter(is_main=True)
        sizes = Size.objects.filter(status=0)
        awards = Award.objects.all()
        category_id = int(request.GET.get('category_id', 0))


        return render(request, 'index.html', {
            'page': 'main',
            'sliders': sliders,
            'reviews': reviews,
            'menus': menu,
            'cheffs': cheffs,
            'partners': partners,
            'informations': informations,
            'categorys': categorys,
            'sizes': sizes,
            'best_menus': best_menus,
            'awards': awards,
            'rebate_menus': rebate_menus
        })


    else:
        r = Register()
        name = request.POST.get('name', '')
        phone = request.POST.get('phone', '')
        email = request.POST.get('email', '')
        message = request.POST.get('message', '')


        r.name = name
        r.phone = phone
        r.email = email
        r.message = message
        r.save()

        return JsonResponse({'success': True, 'errorMsg': '', '_success': True})



def aboutItemHandler(request, cheff_id):
    blog = None
    awards = []
    if cheff_id == 0:
        blogmains = Cheff.objects.filter(status=0).order_by('-rating')[:1]
        if blogmains:
            blog = blogmains[0]
            awards = Award.objects.filter(cheff__id=blog.id)
    else:
        blog = Cheff.objects.get(id=int(cheff_id))
        awards = Award.objects.filter(cheff__id=cheff_id)

    cheffs = Cheff.objects.filter(status=0).order_by('-rating')[:3]
    partners = Partner.objects.filter(status=0)
    informations = Information.objects.filter(status=0)


    return render(request, 'about-item.html', {
        'cheffs': cheffs,
        'partners': partners,
        'awards': awards,
        'informations': informations,
        'page': 'about',
        'blog': blog
    })

def productHandler(request):
    q = request.GET.get('q', '')
    category_id = int(request.GET.get('category_id', 0))

    limit = int(request.GET.get('limit', 6))
    p = int(request.GET.get('p', 1))
    stop = p * limit
    start = (p - 1) * limit

    if q:
        menu = Menu.objects.filter(status=0).filter(title__contains=q).order_by('-rating')[start:stop]
        item_count = Menu.objects.filter(status=0).filter(title__contains=q).count()
    else:
        if category_id:
            menu = Menu.objects.filter(status=0).filter(category__id=category_id).order_by('-rating')[start:stop]
            item_count = Menu.objects.filter(status=0).filter(category__id=category_id).count()
        else:
            menu = Menu.objects.filter(status=0).order_by('-rating')[start:stop]
            item_count = Menu.objects.filter(status=0).count()



    page_count = math.ceil(item_count / limit)
    page_range = range(1, page_count + 1)
    prev_p = p - 1
    next_p = p + 1

    menu_count = Menu.objects.filter(status=0).count()




    best_menus = Menu.objects.filter(is_best_seller=True)[:3]
    rebate_menus = Menu.objects.filter(is_rebate=True)
    is_new = Menu.objects.filter(is_new=True)
    informations = Information.objects.filter(status=0)
    categorys = Category.objects.filter()
    sizes = Size.objects.filter(status=0)

    return render(request, 'product.html', {
        'page': 'product',
        'informations': informations,
        'categorys': categorys,
        'sizes': sizes,
        'best_menus': best_menus,
        'rebate_menus': rebate_menus,
        'menu': menu,
        'menu_count': menu_count,
        'is_new': is_new,

        'limit': limit,
        'p': p,
        'stop': stop,
        'start': start,
        'item_count': item_count,
        'page_count': page_count,
        'page_range': page_range,
        'prev_p': prev_p,
        'next_p': next_p,

        'category_id': category_id,
        'q': q
    })

def page404Handler(request):
    return render(request, '404.html', {})


def ProductDetailHandler(request, product_id):
    product = Menu.objects.get(id=int(product_id))


    reviews = Review.objects.filter(status=0).order_by('-rating')
    menu = Menu.objects.filter(status=0).order_by('-rating')
    cheffs = Cheff.objects.filter(status=0).order_by('-rating')[:2]
    informations = Information.objects.filter(status=0)
    categorys = Category.objects.filter()
    sizes = Size.objects.filter(status=0)
    best_menus = Menu.objects.filter(is_best_seller=True)



    return render(request, 'product-detail.html', {
        'product': product,
        'page': 'product',
        'reviews': reviews,
        'menus': menu,
        'cheffs': cheffs,
        'informations': informations,
        'categorys': categorys,
        'sizes': sizes,
        'best_menus': best_menus
    })

def GaleryHandler(request):
    galerys = Galery.objects.filter(status=0)
    informations = Information.objects.filter(status=0)

    return render(request, 'galery.html', {
        'page':'galery',
        'galerys': galerys,
        'informations': informations

    })

def RebateHandler(request):
    informations = Information.objects.filter(status=0)
    rebate_menus = Menu.objects.filter(is_rebate=True)
    categorys = Category.objects.filter().order_by('-rating')



    return render(request, 'rebate.html', {
        'page': 'rebate',
        'informations': informations,
        'rebate_menus': rebate_menus,
        'categorys': categorys


    })

def ContactHandler(request):
    informations = Information.objects.filter(status=0)
    filials = Filial.objects.all()


    return render(request, 'contact.html', {
        'page': 'contact',
        'informations': informations,
        'filials': filials


    })


def BlogHandler(request):
    informations = Information.objects.filter(status=0)
    p = int(request.GET.get('p', 1))
    limit = int(request.GET.get('limit', 3))
    stop = p * limit
    start = (p - 1) * limit
    prev_p = p - 1
    next_p = p + 1
    item_count = Blog.objects.filter(status=0).count()
    page_count = math.ceil(item_count / limit)
    page_range = range(1, page_count + 1)
    blogs = Blog.objects.filter(status=0)[start:stop]
    best_menus = Menu.objects.filter(is_best_seller=True)[:3]
    menu = Menu.objects.filter(status=0).order_by('-rating')

    return render(request, 'blog.html', {
        'page': 'blog',
        'informations': informations,
        'stop': stop,
        'start': start,
        'prev_p': prev_p,
        'next_p': next_p,
        'page_count': page_count,
        'page_range': page_range,
        'blogs': blogs,
        'best_menus': best_menus,
        'menu': menu,
        'limit': limit,
        'p': p

    })

def BlogDetailHandler(request, blog_id):
    blog_1 = Blog.objects.get(id=int(blog_id))
    informations = Information.objects.filter(status=0)
    blogs = Blog.objects.filter(status=0)
    best_menus = Menu.objects.filter(is_best_seller=True)[:3]
    menu = Menu.objects.filter(status=0).order_by('-rating')

    return render(request, 'blog-detail.html', {
        'page': 'blog',
        'informations': informations,
        'blogs': blogs,
        'best_menus': best_menus,
        'menu': menu,
        'blog_1': blog_1

    })