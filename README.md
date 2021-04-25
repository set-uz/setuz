<p align="center">
  <img src="https://user-images.githubusercontent.com/44405438/115976379-f20bea80-a586-11eb-9a2b-7100e124e79e.png" />
</p>

<p align="center">
<img alt="Tests" src="https://github.com/awtkns/fastapi-crudrouter/workflows/Python%20application/badge.svg" />
<img alt="Docs" src="https://github.com/awtkns/fastapi-crudrouter/workflows/docs/badge.svg" />
  <img alt="License" src="https://img.shields.io/github/license/awtkns/fastapi-crudrouter?color=%2334D058" />
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

# get category
setuz.get_category()
# result 
category_result = [{
    'id': 3,
    'name': 'Notebook',
    'photo': {
        'id': 173,
        'path': 'http://devapi.set.uz/media/2021/4/11/47a7d863-f95d-4ba9-9ad0-c13ac7507685.jpg',
        'children': []
    }}]
print(category_result[0]['name'])  # Notebook
```