class GardenError(Exception):
    def __init__(self, msg: str = 'Unknown garden error'):
        super().__init__(msg)


class PlantError(GardenError):
    def __init__(self, msg: str = 'Unknown plant error'):
        super().__init__(msg)


class WaterError(GardenError):
    def __init__(self, msg: str = 'Unknown water error'):
        super().__init__(msg)


def water_plant(plant_name: str) -> None:
    if not plant_name.istitle():
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")
    print(f"Watering {plant_name}: [OK]")


def test_watering_system() -> None:
    print('\nTesting valid plants...')
    print('Opening watering system')
    try:
        water_plant('Tomato')
        water_plant('Potato')
        water_plant('Carrot')
    except PlantError as e:
        print('Caught PlantError:', e)
        print('.. ending tests and returning to main')
        return
    finally:
        print('Closing watering system')
    print('\nTesting invalid plants...')
    print('Opening watering system')
    try:
        water_plant('Tomato')
        water_plant('potato')
        water_plant('Carrot')
    except PlantError as e:
        print('Caught PlantError:', e)
        print('.. ending tests and returning to main')
        return
    finally:
        print('Closing watering system')


if __name__ == '__main__':
    print('=== Garden Watering System ===')
    test_watering_system()
    print('Cleanup always happens, even with errors!')
