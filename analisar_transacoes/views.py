from django.shortcuts import render
from analisar_transacoes.forms import UploadFileForm

def upload_file(request,*args,**kwargs):
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        file_size = uploaded_file.size / (1024*1024)
        print(uploaded_file.name)
        print(round(file_size,2), "MB")
    return render(request, "analisar_transacoes/form_transacoes.html", locals())

