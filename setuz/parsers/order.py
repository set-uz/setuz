from ..schemes.order import OrderSchema, OrderListSchema, OrderProductSchema, Product
from typing import List
from datetime import datetime


def order_parser(response) -> OrderListSchema:
    data = response.json()
    orders: List[OrderSchema] = []

    for result in data['results']:
        order_products: List[OrderProductSchema] = []

        for order_product in result['order_products']:
            order_products.append(OrderProductSchema(
                id=order_product['id'],
                total_price=order_product['total_price'],
                quantity=order_product['quantity'],
                product=Product(
                    provider_product_id=order_product['product']['provider_product_id'],
                    name=order_product['product']['name']
                )
            ))

        orders.append(OrderSchema(
            id=result['id'],
            total_price=result['total_price'],
            status=result['status'],
            created_date=datetime.strptime(result['created_date'], '%Y-%m-%dT%H:%M:%S.%f'),
            order_products=order_products,
            tm=result['tm']
        ))

    return OrderListSchema(
        count=data['count'],
        next=data['next'],
        prev=data['next'],
        results=orders
    )
