class GardenError(Exception):
    def __init__(self, msg: str = 'Unknown garden error'):
        super().__init__(msg)


class PlantError(GardenError):
    def __init__(self, msg: str = 'Unknown plant error'):
        super().__init__(msg)


class WaterError(GardenError):
    def __init__(self, msg: str = 'Unknown water error'):
        super().__init__(msg)


def test_plant_error() -> None:
    try:
        print('Testing PlantError...')
        raise PlantError('The tomato plant is wilting!')
    except PlantError as e:
        print('Caught PlantError:', e, end='\n\n')


def check_water_tank() -> None:
    raise WaterError('Not enough water in the tank!')


def test_water_error() -> None:
    try:
        print('Testing WaterError...')
        check_water_tank()
    except WaterError as e:
        print('Caught WaterError:', e, end='\n\n')


def test_all_errors() -> None:
    print('Testing catching all garden errors...')
    try:
        raise PlantError('The tomato plant is wilting!')
    except GardenError as e:
        print('Caught GardenError:', e)
    try:
        check_water_tank()
    except GardenError as e:
        print('Caught GardenError:', e, end='\n\n')
    print('All custom error types work correctly!')


if __name__ == '__main__':
    print('=== Custom Garden Errors Demo ===\n')
    test_plant_error()
    test_water_error()
    test_all_errors()
