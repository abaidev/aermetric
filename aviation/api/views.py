from django.apps import apps
from django.db.models import Sum
from rest_framework.decorators import api_view
from rest_framework.response import Response
from aviation.models import CHOICES

Aircraft = apps.get_model("aviation", "Aircraft")


@api_view(http_method_names=['GET'])
def aircraft_stats(request):
    def data_form(qs, aircraft=None, status=None, type=None):
        return {
            "aircraft": aircraft,
            "status": status,
            "type": type,
            "info_count": qs.aggregate(Sum("info_count"))["info_count__sum"],
            "errors_count": qs.aggregate(Sum("errors_count"))["errors_count__sum"],
            "pre_legend": qs.filter(type="PreLegend").count(),
            "warning": qs.filter(type="Warning").count(),
            "paired_b": qs.filter(type="Paired B").count(),
            "legend": qs.filter(type="Legend").count(),
            "lower_b": qs.filter(type="Lower B").count(),
            "repeat_legend": qs.filter(type="Repeat Legend").count(),
            "upper_a": qs.filter(type="Upper A").count(),
            "lower_a": qs.filter(type="Lower A").count(),
            "paired_a": qs.filter(type="Paired A").count(),
        }

    res_data = []
    aircraft_models = Aircraft.objects.values_list('aircraft', flat=True).distinct()

    for aircraft in aircraft_models:
        qs = Aircraft.objects.filter(aircraft=aircraft)
        res_data.append(data_form(qs, aircraft=aircraft))

    for status, _ in CHOICES['status']:
        qs = Aircraft.objects.filter(status=status)
        res_data.append(data_form(qs, status=status))

    for ac_type, _ in CHOICES['type']:
        qs = Aircraft.objects.filter(type=ac_type)
        res_data.append(data_form(qs, type=ac_type))

    return Response(res_data)
