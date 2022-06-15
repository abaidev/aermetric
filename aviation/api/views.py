from django.apps import apps
from django.db.models import Sum
from rest_framework.decorators import api_view
from rest_framework.response import Response

Aircraft = apps.get_model("aviation", "Aircraft")


@api_view(http_method_names=['GET'])
def aircraft_stats(request, craft_model):
    qs = Aircraft.objects.filter(aircraft=craft_model)
    response_data = {
        "aircraft": craft_model,
        "status": None,
        "type": None,
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
    return Response(response_data)


@api_view(http_method_names=['GET'])
def status_stats(request, status):
    qs = Aircraft.objects.filter(status=status)
    response_data = {
        "aircraft": None,
        "status": status,
        "type": None,
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
    return Response(response_data)