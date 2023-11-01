from ecommerceapp.models import Category,Tags,Vendor,Product,ProductImages,CartOrder,CartOrderItems,ProductReview,WishList,Address

def default(request):
    categories=Category.objects.all()
    # print("Context processor is called. Categories:", categories)

    return {
        'categories':categories,
    }