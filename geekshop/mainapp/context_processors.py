from basket.models import Basket
from mainapp.models import ProductCategory


def basket(request):
    baskets_list = []
    if request.user.is_authenticated:
        baskets_list = Basket.objects.filter(user=request.user)
    return {'baskets': baskets_list}

def category(request):
    category_list = ProductCategory.objects.all()
    return {'categories': category_list}
