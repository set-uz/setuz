from ..schemes.measurement import MeasurementListSchema, MeasurementSchema


def measurement_parser(response) -> MeasurementListSchema:
    data = response.json()
    measurements: list = []

    for result in data['results']:
        measurements.append(MeasurementSchema(
            id=result['id'],
            name=result['name'],
            short_name=result['short_name'],
            tm=result['tm']
        ))

    instance: MeasurementListSchema = MeasurementListSchema(
        count=data['count'],
        next=data['next'],
        prev=data['prev'],
        results=measurements
    )
    return instance
