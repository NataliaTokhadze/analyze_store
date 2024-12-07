from django.core.management.base import BaseCommand
from django.db.models import Sum, Avg, Count, Min, Max, Q, F
from shop.models import Tag, Category, Item

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
            count_items = Category.objects.aggregate(count=Count('items'))
            print(count_items)

            items = Item.objects.aggregate(min_price=Min('price'), max_price=Max('price'), avg_price=Avg('price'))
            print(items)


            category_Items_count = Category.objects.annotate(count=Count('items'))
            for category in category_Items_count:
                    print(F'{category.name} : {category.count}')

            category_Items_price_sum = Item.objects.annotate(sum=Sum('price'))
            for category in category_Items_price_sum:
                    print(F'{category.name} : {category.sum}')


            for item in Item.objects.select_related('category').all():
                   print(F'{item.name} : {item.category.name}')

            for tags in Tag.objects.prefetch_related('items').all():
                   print(F'{tags.name} : {[item.name for item in tags.items.all()]}')
                   




            