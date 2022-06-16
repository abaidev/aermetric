from django.apps import apps
from rest_framework.decorators import api_view
from rest_framework.response import Response
from aviation.models import CHOICES
from aviation.decorators import query_debugger

Aircraft = apps.get_model("aviation", "Aircraft")

@query_debugger
@api_view(http_method_names=['GET'])
def aircraft_stats(request):
    def data_form(qs, aircraft=None, status=None, type=None):
        return {
            "aircraft": aircraft,
            "status": status,
            "type": type,
            "info_count": sum([item.info_count for item in qs]),
            "errors_count": sum([item.errors_count for item in qs]),
            "pre_legend": sum(list(filter(lambda item: item.type == 'pre_legend', qs))),
            "warning": sum(list(filter(lambda item: item.type == 'warning', qs))),
            "paired_b": sum(list(filter(lambda item: item.type == 'paired_b', qs))),
            "legend": sum(list(filter(lambda item: item.type == 'legend', qs))),
            "lower_b": sum(list(filter(lambda item: item.type == 'lower_b', qs))),
            "repeat_legend": sum(list(filter(lambda item: item.type == 'repeat_legend', qs))),
            "upper_a": sum(list(filter(lambda item: item.type == 'upper_a', qs))),
            "lower_a": sum(list(filter(lambda item: item.type == 'lower_a', qs))),
            "paired_a": sum(list(filter(lambda item: item.type == 'paired_a', qs))),
        }

    res_data = []
    aircraft_models = Aircraft.objects.values_list('aircraft', flat=True).distinct()

    if aircraft_models:
        for aircraft in aircraft_models:
            qs = Aircraft.objects.filter(aircraft=aircraft)
            res_data.append(data_form(qs.iterator(), aircraft=aircraft))  # or list(qs)
        for status, _ in CHOICES['status']:
            qs = Aircraft.objects.filter(status=status)
            res_data.append(data_form(qs.iterator(), status=status))

        for ac_type, _ in CHOICES['type']:
            qs = Aircraft.objects.filter(type=ac_type)
            res_data.append(data_form(qs.iterator(), type=ac_type))

    return Response(res_data)
