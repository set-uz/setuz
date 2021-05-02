import requests
from .exceptions.auth_error import AuthenticationError, NotFoundError
from .parsers.measurement import measurement_parser, MeasurementListSchema
from .parsers.brand import brand_parser, BrandListSchema
from .parsers.order import order_parser, OrderListSchema
from .settings import SetSettings
from .schemes.product import ProductCreateSchema
import dataclasses


class SetUz(SetSettings):

    def get_order(
            self, page: int = 1, page_size: int = 25, last_id: int = 0, last_tm: int = 0
    ) -> OrderListSchema:
        url = f'{self.main_api}/order/{self.get_default_query_parm(page, page_size, last_id, last_tm)}'
        response = requests.get(url, headers=self.headers)
        self.check_status_code(response.status_code)
        return order_parser(response)

    def get_measurement(
            self, page: int = 1, page_size: int = 25, last_id: int = 0, last_tm: int = 0
    ) -> MeasurementListSchema:

        url = f'{self.main_api}/measurement/{self.get_default_query_parm(page, page_size, last_id, last_tm)}'
        response = requests.get(url, headers=self.headers)
        self.check_status_code(response.status_code)
        return measurement_parser(response)

    def get_brand(
            self, page: int = 1, page_size: int = 25, last_id: int = 0, last_tm: int = 0
    ) -> BrandListSchema:

        url = f'{self.main_api}/brand/{self.get_default_query_parm(page, page_size, last_id, last_tm)}'
        response = requests.get(url, headers=self.headers)
        self.check_status_code(response.status_code)
        return brand_parser(response)

    def create_product(self, product_dto: ProductCreateSchema):
        product_dto = dataclasses.asdict(product_dto)
        url = f'{self.main_api}/product/'
        response = requests.post(url, headers=self.headers, json=product_dto)
        self.check_status_code(response.status_code)
        if response.status_code == 201:
            return True
        return print(response.text)

    def delete_product(self, provider_product_id: int):
        url = f'{self.main_api}/product/{provider_product_id}/'
        response = requests.delete(url, headers=self.headers)
        self.check_status_code(response.status_code)
        return True

    def upload_file(self, file_path: str) -> int:
        file = open(file_path, 'rb')
        url = f'{self.url}/api/v1/file/'
        response = requests.post(url, files={'file': file})
        self.check_status_code(response.status_code)
        return response.json()['id']

    def get_category(self):
        url = f'{self.main_api}/category/'
        response = requests.get(url, headers=self.headers)
        self.check_status_code(response.status_code)
        data = response.json()
        return data

    def check_status_code(self, status_code: int):
        if status_code == 401:
            raise AuthenticationError
        elif status_code == 404:
            raise NotFoundError

    def get_default_query_parm(self, page: int = 0, page_size: int = 25, last_id: int = 0, last_tm: int = 0) -> str:
        return f'?page={page}&page_size={page_size}&last_id={last_id}&last_tm={last_tm}'
