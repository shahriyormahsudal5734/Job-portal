from .models import Job
import django_filters



class UserFilter(django_filters.FilterSet):
    class Meta:
        model = Job
        fields = {
            'title': [ 'contains'],
            'viloyat5': ['exact'],
            'category5': ['exact']
        }   