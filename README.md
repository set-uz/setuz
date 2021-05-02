<p align="center">
  <img src="https://user-images.githubusercontent.com/44405438/115976379-f20bea80-a586-11eb-9a2b-7100e124e79e.png" />
</p>

<p align="center">
<img alt="Tests" src="https://github.com/awtkns/fastapi-crudrouter/workflows/Python%20application/badge.svg" />
<img alt="Docs" src="https://github.com/awtkns/fastapi-crudrouter/workflows/docs/badge.svg" />
  <img alt="License" src="https://img.shields.io/github/license/awtkns/fastapi-crudrouter?color=%2334D058" />
<img alt="Version" src="https://img.shields.io/pypi/v/setuz" />
</p>

```shell
pip install setuz
```

```python
from setuz import SetUz

setuz = SetUz('token')

# page default = 1
# page_size default = 25
# last_tm default = 0

# get brand
brand = setuz.get_brand(page=1, page_size=25, last_tm=0)
brand_result = "BrandListSchema(count=6, next=None, prev=None, results=[BrandSchema(id=122, name='CocaCola', tm=1)])"
print(brand.results[0].name)  # CocaCola
print(brand.count)  # 6

# get measurement
measurement = setuz.get_measurement()
measurement_result = "MeasurementListSchema(count=4, next=None, prev=None, results=[MeasurementSchema(id=4, name='Штука', short_name='шт', tm=1)])"
print(measurement.results[0].name)  # Штука
print(measurement.count)  # 4

# get order
order = setuz.get_order()
order_result = "OrderListSchema(count=1, next=None, prev=None, results=[OrderSchema(id=1, total_price=700000.0, status='pending', order_products=[OrderProductSchema(id=1, total_price=600000.0, quantity=12, product=Product(provider_product_id=1, name='Test product'))], created_date=datetime.datetime(2021, 4, 26, 4, 28, 55, 656147))])"
print(order.count)  # 1
print(order.results[0].id)  # 1

# get category
setuz.get_category()
category_result = [{
    'id': 3,
    'name': 'Notebook',
    'photo': {
        'id': 173,
        'children': [
            {
                "id": 4,
                "name": "Acer Nitro 5",
                "children": []
            }
        ]
    }}]
print(category_result[0]['name'])  # Notebook

# create product
from setuz.schemes.product import ProductCreateSchema, ProductImagesSchema

file_id = setuz.upload_file('<file_path>')
images = ProductImagesSchema(photo_id=file_id, is_main=True)

product = ProductCreateSchema(
    provider_product_id=1,  # product_id
    category_id=3,  # category set id
    brand_id=122,  # brand set id
    measurement_id=4,  # measurement set id
    name='Iphone XL 10',
    description='Iphone GG  WP',
    price=12.5,
    barcode='123331244',
    cashback=0,
    product_images=[images]
)

result = setuz.create_product(product)
if result is True:
    print('success create')
else:
    print('error', result)

result = setuz.delete_product(1)  # delete product  id = provider product id 
if result is True:
    print('success delete')
else:
    print('error', result)

```