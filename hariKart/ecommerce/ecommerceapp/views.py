from django.shortcuts import render
from ecommerceapp.models import Category,Tags,Vendor,Product,ProductImages,CartOrder,CartOrderItems,ProductReview,WishList,Address
from django.db.models import Count,Avg
from ecommerceapp.forms import ProductReviewForm
from django.http import JsonResponse


# Create your views here.
def index(request):
    products = Product.objects.all().order_by("-pid")
    Categories =  Category.objects.all()
    context= {
        "products":products,
        "categories":Categories
    }
    return render(request, "index.html", context)



def product_list_view(request):
    products = Product.objects.all()
    # products = Product.objects.filter(featured="True")
    context= {
        "products":products
    }

    return render(request, "shop-top-filter.html", context)
 

def category_list_view(request):
    Categories =  Category.objects.all()
    products = Product.objects.all().order_by("-pid")
    context = {
        "categories":Categories,
        "products":products
    }
    return render(request, 'shop-category.html', context)

def category_product_list_view(request, cid):
    category = Category.objects.get(cid=cid)
    product = Product.objects.filter(category=category)

    context = {
        "category" : category,
        "products" : product,
    }
    return render(request, "shop-top-filter.html", context)

def vendor_list_view(request):
    vendor = Vendor.objects.all()
    context = {
        "vendor" : vendor
    }    
    return render(request, "vendor/vendor-list.html", context)

def vendor_detail_view(request, vid):
    vendor = Vendor.objects.get(vid=vid)
    products = Product.objects.filter(vendor=vendor)
    context = {
        "v" : vendor,
        "products" : products,
    }    
    return render(request, "vendor/vendor-detail.html", context)

# def product_detail_view(request, pid):
#     product = Product.objects.get(pid=pid)
#     # products = Product.objects.filter(category=category)
#     products = Product.objects.all()
#     vendor = Vendor.objects.get(vendor=product.vid)
#     p_images = product.p_images.all()
#     context = {

#         "product" : product,
#         "products" : products,
#         "p_images" : p_images,
#     }    
#     return render(request, "product-detail.html", context)

def product_detail_view(request, pid):
    product = Product.objects.get(pid=pid)
    vendor_name = product.vendor
    vendor = Vendor.objects.get(title=vendor_name)
    products = Product.objects.all()
    p_images = product.p_images.all()
    reviews = ProductReview.objects.filter(product=product).order_by("date")
    avg_rating = ProductReview.objects.filter(product=product).aggregate(rating=Avg('rating'))
    review_form = ProductReviewForm()
    

    make_review = True
    if request.user.is_authenticated:
        user_rev_count = ProductReview.objects.filter(user=request.user, product=product).count()
        if user_rev_count > 0:
                make_review = False


    context = {
        "product": product,
        "vendor": vendor,
        "products": products,
        "p_images": p_images,
        "reviews" : reviews,
        "make_review" : make_review,
        "avg_rating": avg_rating,
        "review_form": review_form,
        
    }    
    return render(request, "product-detail.html", context)


def ajax_add_review(request, pid):
    r_product = Product.objects.get(pk=pid)
    user = request.user

    review = ProductReview.objects.create(
        user=user,
        review = request.POST['review'],
        rating = request.POST['rating'],
        product=r_product,
    )

    context = {
        'user': user.username,
        'review': request.POST['review'],
        'rating' : request.POST['rating'],    
    }
    
    avg_rating = ProductReview.objects.filter(product=r_product).aggregate(rating=Avg('rating'))

    return JsonResponse(
        {   
        'bool':True,
        'context' : context,
        'avg_rating' : avg_rating
        } 
    )
    

def search_view(request):
    query = request.Get.get("q")

    products = Product.objects.filter(title__icontains = query, description__icontains = query).order_by("-date")

    context = {
        "products": products,
        "query" : query,
    } 
    return render(request, "search.html", context)