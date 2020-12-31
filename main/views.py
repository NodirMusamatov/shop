from django.http import JsonResponse
from django.shortcuts import render
from main.models import Slider, Review, Menu, Cheff, Partner, Register, Information, Category, Size, Award
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
    menu = Menu.objects.filter(status=0).order_by('-rating')[:6]
    best_menus = Menu.objects.filter(is_best_seller=True)[:3]
    rebate_menus = Menu.objects.filter(is_rebate=True)
    informations = Information.objects.filter(status=0)
    categorys = Category.objects.filter(is_main=True)
    sizes = Size.objects.filter(status=0)

    return render(request, 'product.html', {
        'page': 'product',
        'informations': informations,
        'categorys': categorys,
        'sizes': sizes,
        'best_menus': best_menus,
        'rebate_menus': rebate_menus,
        'menu': menu
    })


