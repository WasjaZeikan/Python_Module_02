def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature() -> None:
    temp: str = "30"
    print('\nInput data is', temp)
    print(f'Temperature is now {input_temperature(temp)}°C', end='\n\n')
    temp = 'abc'
    print('\nInput value is', temp)
    try:
        print(f'Temperature is now {input_temperature(temp)}°C', end='\n\n')
    except Exception as ex:
        print('Caught input_temperature error:', ex)
    print("\nAll tests completed - program didn't crash!")


if __name__ == '__main__':
    print('=== Garden Temperature ===')
    test_temperature()
