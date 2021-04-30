from taggit.models import Tag


def sidebar_data(request):
    return {
        'categories': Tag.objects.all().order_by('-id')[:5]
    }
