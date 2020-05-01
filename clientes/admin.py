from django.contrib import admin
from .models import Empregado,Departamento,  Telefone, CPF
# Register your models here.


class EmpregadoAdmin(admin.ModelAdmin):
    #fields = ('nome', 'endereco')
    list_display = ('id','nome', 'endereco', 'email')
    list_filter = ('departamentos',)
    search_fields = ('id','nome','departamentos__nome',)



admin.site.register(Departamento)
admin.site.register(Empregado, EmpregadoAdmin)
admin.site.register(Telefone)
admin.site.register(CPF)