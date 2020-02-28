from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
import datetime

# Create your views here.
from eshopadmin.models import itemCategory, product


@login_required
def index(request):
    return render(request, 'eshopadmin/dashboard.html')


def manageItemCategory(request):
    cotext = dict()

    if request.method == "POST":
        categoryName = request.POST.get('categoryName')
        description = request.POST.get('description')
        item = itemCategory(categoryName=categoryName, description=description)
        item.save()

        # return render(request, 'eshopadmin/manageCategory.html',cotext)
    cotext['items'] = itemCategory.objects.filter(is_active=1).order_by('-created_date')

    return render(request, 'eshopadmin/manageCategory.html', cotext)


def itemCategoryDelete(request, id):
    cotext = dict()
    instance = itemCategory.objects.get(id=id)
    instance.delete()
    cotext['del_msg'] = "successfully delete"
    cotext['items'] = itemCategory.objects.filter(is_active=1).order_by('-created_date')
    return redirect('eshopadmin:manageItemCategory')


# def ItemCategoryEdit(request):
#     cotext = dict()
#     id = request.POST.get('id')
#     cotext['edit_item'] =  obj = get_object_or_404(itemCategory, pk=id)
#     return render(request, 'eshopadmin/manageCategory.html', cotext)

def editItemCategory(request):
    cotext = dict()

    if request.method == "POST":
        categoryName = request.POST.get('categoryName')
        description = request.POST.get('description')
        id = request.POST.get('id')
        itemCategory.objects.filter(id=id).update(categoryName=categoryName, description=description,
                                                  modified_date=datetime.datetime.now())

    return redirect('eshopadmin:manageItemCategory')


def productManage(request):
    cotext = dict()
    product_company = request.user.username
    cotext['itemcat'] = itemCategory.objects.filter(is_active=1)

    if request.method == "POST":
        itemCategory_id = request.POST.get('itemCategory_id')
        item = itemCategory.objects.get(pk=itemCategory_id)
        product_name = request.POST.get('product_name')
        product_code = request.POST.get('product_code')
        product_total = request.POST.get('product_total')
        product_price = request.POST.get('product_price')
        product_image = request.FILES.get('product_image')
        product_discount = request.POST.get('product_discount')
        product_detail = request.POST.get('product_detail')

        pot = product(product_code=product_code, product_name=product_name,
                      product_discount=product_discount,
                      product_price=product_price, product_detail=product_detail, product_total=product_total,
                      product_company=product_company, product_image=product_image, itemCategory_id=item
                      )
        pot.save()

    cotext['products'] = product.objects.all()

    return render(request, 'eshopadmin/manageProduct.html', cotext)


def productEdit(request):
    cotext = dict()
    product_company = request.user.username
    cotext['itemcat'] = itemCategory.objects.filter(is_active=1)

    if request.method == "POST":
        id = request.POST.get('id')
        itemCategory_id = request.POST.get('itemCategory_id')
        item = itemCategory.objects.get(pk=itemCategory_id)
        product_name = request.POST.get('product_name')
        product_code = request.POST.get('product_code')
        product_total = request.POST.get('product_total')
        product_price = request.POST.get('product_price')
        product_image = request.FILES.get('product_image')
        product_discount = request.POST.get('product_discount')
        product_detail = request.POST.get('product_detail')

        test = product.objects.get(id=id)
        test.product_code = product_code
        test.product_name = product_name
        test.product_total = product_total
        test.product_price = product_price
        if product_image is None:
            test.product_image = test.product_image
        else:
            test.product_image = product_image
        test.product_discount = product_discount
        test.product_detail = product_detail
        test.itemCategory_id = item
        test.modified_date = datetime.datetime.now()
        test.save()

        # product.objects.filter(id=id).update(product_code=product_code, product_name=product_name,
        #               product_discount=product_discount,
        #               product_price=product_price, product_detail=product_detail, product_total=product_total,
        #               product_company=product_company, product_image=product_image, itemCategory_id=item,
        #                                           modified_date=datetime.datetime.now())

        cotext['products'] = product.objects.all()

        return redirect('eshopadmin:productManage')


def productDelete(request, id):
    cotext = dict()
    instance = product.objects.get(id=id)
    instance.delete()
    cotext['del_msg'] = "successfully delete"
    cotext['items'] = itemCategory.objects.filter(is_active=1).order_by('-created_date')
    return redirect('eshopadmin:productManage')
