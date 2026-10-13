def input_temperature(temp_str: str) -> int:
    temp: int = int(temp_str)
    if temp < 0:
        raise Exception(f'{temp}°C is too cold for plants (min 0°C)')
    if temp > 40:
        raise Exception(f"{temp}°C is too hot for plants (max 40°C)")
    return int(temp_str)


def test(temp_str: str) -> None:
    try:
        print('Input value is', temp_str)
        temp: int = input_temperature(temp_str)
        print(f'Temperature is now {temp}°C', end='\n\n')
    except Exception as ex:
        print('Caught input_temperature error:', ex, end='\n\n')


def test_temperature() -> None:
    test('30')
    test('abc')
    test('100')
    test('-50')
    print("All tests completed - program didn't crash!")


if __name__ == '__main__':
    print('=== Garden Temperature Checker ===')
    test_temperature()
