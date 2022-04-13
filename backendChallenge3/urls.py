from django.contrib import admin
from django.urls import path
from analisar_transacoes.views import (
    upload_file,

)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', upload_file, name='form_transacoes')
]
