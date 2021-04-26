from ..schemes.brand import BrandListSchema, BrandSchema


def brand_parser(response) -> BrandListSchema:
    data = response.json()
    brands: list = []

    for result in data['results']:
        brands.append(BrandSchema(
            id=result['id'],
            name=result['name'],
            tm=result['tm']
        ))

    instance: BrandListSchema = BrandListSchema(
        count=data['count'],
        next=data['next'],
        prev=data['prev'],
        results=brands
    )
    return instance
