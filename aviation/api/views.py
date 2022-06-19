from django.apps import apps
from django.db.models import (
    ExpressionWrapper,
    Q, F, CharField,
    Count, Sum, Value, NullBooleanField
)
from rest_framework.decorators import api_view
from rest_framework.response import Response
from aviation.decorators import query_debugger

Aircraft = apps.get_model("aviation", "Aircraft")


@query_debugger
@api_view(http_method_names=['GET'])
def aircraft_stats(request):
    res_data = []

    # AIRCRAFTS
    a = Aircraft.objects.values('aircraft').distinct().annotate(
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
        status=Value(None, output_field=NullBooleanField()),
        type=Value(None, output_field=NullBooleanField()),
    )

    res_data.append(a)

    # STATUSES
    s = Aircraft.objects.values('status').annotate(
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
        aircraft=Value(None, output_field=NullBooleanField()),
        type=Value(None, output_field=NullBooleanField()),
    )

    res_data.append(s)

    # TYPES
    t = Aircraft.objects.values('type').annotate(
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
        aircraft=Value(None, output_field=NullBooleanField()),
        status=Value(None, output_field=NullBooleanField()),
    )

    res_data.append(t)

    return Response(res_data)
