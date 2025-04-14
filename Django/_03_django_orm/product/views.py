from django.shortcuts import render
from django.http import HttpResponse
from product.models import Product, Category, Discount, Review
from django.db.models import Avg, Count
from datetime import datetime, timedelta

def test_n_1(request):

    # 1:N = Product:Review
    result = ''

    # 1. 특정 제품의 모든 리뷰 select
    # (1) 5
    # reviews = Review.objects.filter(product_id=1)

    # (2) 6
    # product = Product.objects.get(id=1)
    # reviews = Review.objects.filter(product=product)

    # (3) 2
    product = Product.objects.get(id=1)
    reviews = product.review.all()

    for review in reviews:
        result += str(review.id) \
                    + '/' + review.product.name \
                    + '/' + str(review.user_id) \
                    + '/' + str(review.rating) \
                    + '/' + review.comment + '<br>'

    # 2. 특정 제품의 평균 평점과 리뷰 개수 select
    product = Product.objects.get(id=1)
    avg_rating = product.review.aggregate(avg_rating=Avg('rating'))['avg_rating']
    review_cnt = product.review.count()
     
    result = f'{product.name}의 리뷰 평점: {avg_rating}({review_cnt}개 리뷰)'

    # 3. 평점이 높은 리뷰(4점 이상)만 select
    high_rating_reviews = product.review.filter(rating__gte=4)
    for review in high_rating_reviews:
        result += f'[High Rating] {review.user_id}의 {review.comment}({review.rating})'

    # 4. 모든 제품의 평균 평점과 리뷰 개수 select
    products_with_review = Product.objects.annotate(
        avg_rating=Avg('review__rating'),
        review_count=Count('review')
    )
    result = ''
    for product in products_with_review:
        result += f'Product {product.name} | Avg Rating {product.avg_rating} | Review Cnt {product.review_count}<br>'

    # 5. 특정 기간동안 작성된 리뷰 select 
    start_date = datetime.now() - timedelta(weeks=4)
    end_date = datetime.now()
    reviews_by_date = \
        Review.objects.filter(created_at__range=(start_date, end_date))
    for review in reviews_by_date:
        result += str(review.id) \
                    + '/' + review.product.name \
                    + '/' + str(review.user_id) \
                    + '/' + str(review.rating) \
                    + '/' + review.comment + '<br>'
    
    return HttpResponse(result)


def test_1_1(request):

    # 1:1 = Product:Discount
    result = ''

    # 1. 특정 제품의 할인 정보 select
    product_id = 1

    try:
        discount = Discount.objects.get(product_id=product_id)
        result = f'Product {discount.product.name} | Discount {discount.discount_percentage}%'
    except Discount.DoesNotExist:
        result = f'Product {product_id}는 할인 안함'

    # 2. 할인 중인 모든 제품 select
    current_date = datetime.now()
    current_discount = Discount.objects.filter(start_date__lte=current_date, end_date__gte=current_date)
    for discount in current_discount:
        result += f'<br>[할인중!!!] {discount.product.name} ({discount.discount_percentage}%)'

    # 3. 특정 할인율 이상인 제품 select
    high_discount = Discount.objects.filter(discount_percentage__gte=20)
    for discount in high_discount:
        result += f'<br>[파격세일!!!] {discount.product.name} ({discount.discount_percentage}%)'

    # 4. 할인 정보와 함께 모든 제품 정보 select
    products = Product.objects.all()
    for product in products:
        if hasattr(product, 'discount'):
            result += f'<br>[ALL] {product.name} ({product.discount.discount_percentage}% 세일)'
        else:
            result += f'<br>[ALL] 할인 안 하는 {product.name}'

    # 5. 할인 기간이 지난 제품 select
    expired_discount = Discount.objects.filter(end_date__lt=current_date)
    for discount in expired_discount:
        result += f'<br>[할인종료!!!] {discount.product.name} ({discount.discount_percentage}%)'

    return HttpResponse(result)

def test_prefetch(request):

    result = ''

    products = Product.objects.prefetch_related('discount')
    for product in products:
        if hasattr(product, 'discount'):
            result += f'<br>[ALL] {product.name} ({product.discount.discount_percentage}% 세일)'
        else:
            result += f'<br>[ALL] 할인 안 하는 {product.name}'

    return HttpResponse(result)


def test_n_m(request):

    # N:M = Product:Category
    result = ''

    # 1. 특정 제품이 속한 모든 카테고리 select
    product_id = 9
    product = Product.objects.get(id=product_id)
    categories = product.categories.all()
    result = f'Product {product.name}의 category<br>'
    for category in categories:
        result += f'{category.name}/'

    # 2. 특정 카테고리에 속한 모든 제품(이름, 가격, 재고량) select
    category_name = '패션/의류'

    category = Category.objects.get(name=category_name)
    products = category.products.all()

    result = f'Category {category.name}의 제품<br>'
    for product in products:
        result += f'{product.name} | {product.price}원 | 수량: {product.stock}개<br>'

    # 3. 카테고리가 없는 제품 select
    products_no_cat = Product.objects.filter(categories__isnull=True)

    result = '카테고리 미포함 제품<br>'
    for product in products_no_cat:
        result += f'{product.name} | {product.price}원 | 수량: {product.stock}개<br>'

    # 4. 특정 제품에 새 카테고리 추가
    new_category_name = "Seasonal"
    product = Product.objects.get(id=product_id)
    new_category, created = Category.objects.get_or_create(name=new_category_name)

    product.categories.add(new_category)

    # result = Product.objects.get(id=product_id).categories.all()

    # 5. 모든 카테고리와 각 카테고리의 제품 수 select
    cateogories_with_count = Category.objects.annotate(
        product_count=Count('products')
    )
    for category in cateogories_with_count:
        result += f'Category {category.name}에는 {category.product_count}개의 제품이!<br>'

    # 6. 여러 카테고리에 속한 제품 select
    multi_cat_products = Product.objects.annotate(
                                category_count=Count('categories')
                            ).filter(category_count__gt=1)
    result = '여러 카테고리에 속한 제품 목록<br>'
    for product in multi_cat_products:
        result += f'{product.name} (Category Count:{product.category_count})<br>'

    return HttpResponse(result)
