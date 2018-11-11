import sys
import factory


class DataFactory(factory.Factory):
    id = factory.Faker('ean13')
    year = factory.Faker('year')
    title = factory.Faker('sentence')
    description = factory.Faker('text')

sys.stdout.write([factory.build(dict, FACTORY_CLASS=DataFactory) for _ in range(1000)].__str__())
