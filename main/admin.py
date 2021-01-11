from django.contrib import admin
from main.models import *

# Register your models here.

class SliderAdmin(admin.ModelAdmin):
    pass
admin.site.register(Slider, SliderAdmin)


class ReviewAdmin(admin.ModelAdmin):
    pass
admin.site.register(Review, ReviewAdmin)



class MenuAdmin(admin.ModelAdmin):
    pass
admin.site.register(Menu, MenuAdmin)



class CheffAdmin(admin.ModelAdmin):
    pass
admin.site.register(Cheff, CheffAdmin)




class PartnerAdmin(admin.ModelAdmin):
    pass
admin.site.register(Partner, PartnerAdmin)



class RegisterAdmin(admin.ModelAdmin):
    pass
admin.site.register(Register, RegisterAdmin)



class InformationAdmin(admin.ModelAdmin):
    pass

admin.site.register(Information, InformationAdmin)



class СategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Category, СategoryAdmin)



class SizeAdmin(admin.ModelAdmin):
    pass

admin.site.register(Size, SizeAdmin)


class AwardAdmin(admin.ModelAdmin):
    pass

admin.site.register(Award, AwardAdmin)


class GaleryAdmin(admin.ModelAdmin):
    pass
admin.site.register(Galery, GaleryAdmin)


class RebateAdmin(admin.ModelAdmin):
    pass
admin.site.register(Rebate, RebateAdmin)



class FilialAdmin(admin.ModelAdmin):
    pass
admin.site.register(Filial, FilialAdmin)


class BlogAdmin(admin.ModelAdmin):
    pass
admin.site.register(Blog, BlogAdmin)


