from django.shortcuts import render
from analisar_transacoes.models import Transacao
from analisar_transacoes.forms import UploadFileForm
import csv
import codecs


def upload_file(request,*args,**kwargs):
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        file_size = uploaded_file.size / (1024*1024)

        data = codecs.iterdecode(uploaded_file, 'utf8')

        csv_reader = csv.reader(data, delimiter=',')
        for row in csv_reader:
            print(row)



    return render(request, "analisar_transacoes/form_transacoes.html", locals())

