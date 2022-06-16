from django.apps import apps
from django.db.models import Count, Sum, Q
from rest_framework.decorators import api_view
from rest_framework.response import Response
from aviation.models import CHOICES
from aviation.decorators import query_debugger

Aircraft = apps.get_model("aviation", "Aircraft")


@query_debugger
@api_view(http_method_names=['GET'])
def aircraft_stats(request):
    def data_form(qs, aircraft=None, status=None, type=None):
        qd = qs.aggregate(
            pre_legend=Count('type', filter=Q(type='PreLegend')),
            warning=Count('type', filter=Q(type='Warning')),
            paired_b=Count('type', filter=Q(type='Paired B')),
            legend=Count('type', filter=Q(type='Legend')),
            lower_b=Count('type', filter=Q(type='Lower B')),
            repeat_legend=Count('type', filter=Q(type='Repeat Legend')),
            upper_a=Count('type', filter=Q(type='Upper A')),
            lower_a=Count('type', filter=Q(type='Lower A')),
            paired_a=Count('type', filter=Q(type='Paired A')),
            info_count=Sum('info_count'),
            errors_count=Sum('errors_count'),
        )
        qd.update({
            "aircraft": aircraft,
            "status": status,
            "type": type,
        })
        return qd

    res_data = []
    aircraft_models = Aircraft.objects.values_list('aircraft', flat=True).distinct()

    if aircraft_models:
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
