import django_filters
from djstore import models


class ProductFilter(django_filters.FilterSet):
    ORDER_CHOICE = (
        ('ascending', 'Ascending'),
        ('descending', 'Descending')
    )

    ordering = django_filters.ChoiceFilter(label='ordering',
                                         choices=ORDER_CHOICE,
                                         method='filter_by_order')

    price__gt = django_filters.NumberFilter(field_name='price', lookup_expr='gt')
    price__lt = django_filters.NumberFilter(field_name='price', lookup_expr='lt')

    class Meta:
        model = models.Product
        fields = ['ordering', 'price__gt', 'price__lt']

    def filter_by_order(self, queryset, name, value):
        expression = 'price' if value == 'descending' else '-price'
        return queryset.order_by(expression)