import csv
from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage
from .models import Aircraft

fs = FileSystemStorage(location='tmp/')


@admin.register(Aircraft)
class AircraftAdmin(admin.ModelAdmin):
    list_display = ('aircraft', 'status', 'priority', 'type', 'errors_count', 'info_count',)
    search_fields = ('aircraft',)

    def get_urls(self):
        urls = super().get_urls()
        new_urls = [path('upload-csv/', self.upload_csv), ]
        return new_urls + urls

    def upload_csv(self, request):
        if request.method == "POST":
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

            url = reverse('admin:index')
            return HttpResponseRedirect(url)
        
        return render(request, "admin/csv_upload.html", {})
