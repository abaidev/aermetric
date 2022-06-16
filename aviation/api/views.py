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
            "pre_legend": len(list(filter(lambda item: item.type == 'PreLegend', qs))),
            "warning": len(list(filter(lambda item: item.type == 'Warning', qs))),
            "paired_b": len(list(filter(lambda item: item.type == 'Paired B', qs))),
            "legend": len(list(filter(lambda item: item.type == 'Legend', qs))),
            "lower_b": len(list(filter(lambda item: item.type == 'Lower B', qs))),
            "repeat_legend": len(list(filter(lambda item: item.type == 'Repeat Legend', qs))),
            "upper_a": len(list(filter(lambda item: item.type == 'Upper A', qs))),
            "lower_a": len(list(filter(lambda item: item.type == 'Lower A', qs))),
            "paired_a": len(list(filter(lambda item: item.type == 'Paired A', qs))),
        }

    res_data = []
    aircraft_models = Aircraft.objects.values_list('aircraft', flat=True).distinct()

    if aircraft_models:
        for aircraft in aircraft_models:
            qs = Aircraft.objects.filter(aircraft=aircraft)
            res_data.append(data_form(list(qs), aircraft=aircraft))

        for status, _ in CHOICES['status']:
            qs = Aircraft.objects.filter(status=status)
            res_data.append(data_form(list(qs), status=status))

        for ac_type, _ in CHOICES['type']:
            qs = Aircraft.objects.filter(type=ac_type)
            res_data.append(data_form(list(qs), type=ac_type))

    return Response(res_data)
