from django.shortcuts import render


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Product
import json

@csrf_exempt
def product_list(request):
    if request.method == 'GET':
        products = list(Product.objects.values())
        return JsonResponse(products, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        product = Product.objects.create(
            name=data['name'],
            description=data['description'],
            price=data['price'],
            quantity=data['quantity']
        )
        return JsonResponse({'id': product.id}, status=201)

@csrf_exempt
def product_detail(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return JsonResponse({'error': 'Product not found'}, status=404)

    if request.method == 'GET':
        return JsonResponse({
            'name': product.name,
            'description': product.description,
            'price': str(product.price),
            'quantity': product.quantity,
            'created_at': product.created_at,
            'updated_at': product.updated_at
        })
    elif request.method == 'PUT':
        data = json.loads(request.body)
        product.name = data.get('name', product.name)
        product.description = data.get('description', product.description)
        product.price = data.get('price', product.price)
        product.quantity = data.get('quantity', product.quantity)
        product.save()
        return JsonResponse({'id': product.id}, status=200)
    elif request.method == 'DELETE':
        product.delete()
        return JsonResponse({'message': 'Product deleted'}, status=204)
