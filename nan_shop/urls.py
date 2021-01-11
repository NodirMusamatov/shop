"""nan_shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
"""ges_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.views.static import serve
from nan_shop import settings
from main.views import indexHandler, aboutItemHandler, productHandler, page404Handler, ProductDetailHandler , GaleryHandler, RebateHandler, ContactHandler, BlogHandler, BlogDetailHandler

urlpatterns = [
    path('admin/', admin.site.urls),



    url(r'^media/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT
    }),

    path('', indexHandler),
    path('about-item/<int:cheff_id>/', aboutItemHandler),
    path('product/', productHandler),
    path('galery/', GaleryHandler),
    path('rebate/', RebateHandler),
    path('contact/', ContactHandler),
    path('blog/', BlogHandler),
    path('product/<int:product_id>/', ProductDetailHandler),
    path('blog/<int:blog_id>/', BlogDetailHandler),

    #path('*', page404Handler),
]

