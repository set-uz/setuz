import requests
from exceptions.auth_error import AuthenticationError, NotFoundError

from schemes.measurement import MeasurementListSchema, MeasurementSchema
from schemes.brand import BrandListSchema, BrandSchema


class SetUz:
    def __init__(self, token: str, version: int = 1):
        self.token: str = token
        self.version: int = version
        self.headers: dict = dict(Authorization=self.token)
        self.main_api: str = f'http://devapi.set.uz/api/v{self.version}/integration'

    def get_measurement(
            self, page: int = 1, page_size: int = 25, last_id: int = 0, last_tm: int = 0
    ) -> MeasurementListSchema:

        url = f'{self.main_api}/measurement/{self.get_default_query_parm(page, page_size, last_id, last_tm)}'
        response = requests.get(url, headers=self.headers)
        self.check_status_code(response.status_code)
        data = response.json()
        measurements: list = []

        for result in data['results']:
            measurements.append(MeasurementSchema(
                id=result['id'],
                name=result['name'],
                short_name=result['short_name']
            ))

        instance: MeasurementListSchema = MeasurementListSchema(
            count=data['count'],
            next=data['next'],
            prev=data['prev'],
            results=measurements
        )
        return instance

    def get_brand(
            self, page: int = 1, page_size: int = 25, last_id: int = 0, last_tm: int = 0
    ) -> BrandListSchema:

        url = f'{self.main_api}/brand/{self.get_default_query_parm(page, page_size, last_id, last_tm)}'
        response = requests.get(url, headers=self.headers)
        self.check_status_code(response.status_code)
        data = response.json()
        brands: list = []

        for result in data['results']:
            brands.append(BrandSchema(
                id=result['id'],
                name=result['name']
            ))

        instance: BrandListSchema = BrandListSchema(
            count=data['count'],
            next=data['next'],
            prev=data['prev'],
            results=brands
        )
        return instance


    def get_category(self):
        url = f'{self.main_api}/category/'
        response = requests.get(url, headers=self.headers)
        self.check_status_code(response.status_code)
        data = response.json()
        print(data)

    def check_status_code(self, status_code: int):
        if status_code == 401:
            raise AuthenticationError
        elif status_code == 404:
            raise NotFoundError

    def get_default_query_parm(self, page: int = 0, page_size: int = 25, last_id: int = 0, last_tm: int = 0) -> str:
        return f'?page={page}&page_size={page_size}&last_id={last_id}&last_tm={last_tm}'


setuz = SetUz('dppjstbn04cg7z55ulvoey2x6gm0zz45')
setuz.get_category()

