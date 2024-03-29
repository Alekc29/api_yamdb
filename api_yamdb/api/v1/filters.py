import django_filters as filter
from reviews.models import Title


class TitleFilter(filter.FilterSet):
    name = filter.CharFilter(
        field_name='name', lookup_expr='icontains'
    )
    category = filter.CharFilter(
        field_name='category__slug', lookup_expr='icontains'
    )
    genre = filter.CharFilter(
        field_name='genre__slug', lookup_expr='icontains'
    )

    class Meta:
        model = Title
        fields = ['name', 'year', 'category', 'genre']
