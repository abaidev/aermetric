import csv
from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage
from .models import Aircraft

fs = FileSystemStorage(location='tmp/')


def index(request):
    if request.method == 'POST':
        file = request.FILES.get('dataFile')
        content = file.read()
        file_content = ContentFile(content)
        file_name = fs.save(
            "_tmp.csv", file_content
        )
        tmp_file = fs.path(file_name)

        csv_file = open(tmp_file)
        reader = csv.reader(csv_file)
        next(reader)

        product_list = []
        for id_, row in enumerate(reader):
            (
                priority,
                type,
                aircraft,
                status,
                errors_count,
                info_count,
            ) = row
            product_list.append(
                Aircraft(
                    priority=priority,
                    type=type,
                    aircraft=aircraft,
                    status=status,
                    errors_count=errors_count,
                    info_count=info_count,
                )
            )

        Aircraft.objects.bulk_create(product_list)
        fs.delete(tmp_file)
        return HttpResponse("<h5>data is uploaded</h5>")

    return render(request, 'index.html', {})
