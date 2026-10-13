def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int('abc')
    elif operation_number == 1:
        0 / 0
    elif operation_number == 2:
        open('file/not/exist')
    elif operation_number == 3:
        20 + 'sd'


def test(num: int) -> None:
    try:
        print(f'Testing operation {num}...')
        garden_operations(num)
        print('Operation completed successfully!')
    except ValueError as e:
        print('Caught ValueError:', e)
    except ZeroDivisionError as e:
        print('Caught ZeroDivisionError:', e)
    except FileNotFoundError as e:
        print('Caught FileNotFoundError:', e)
    except TypeError as e:
        print('Caught TypeError:', e)


def test_error_types() -> None:
    test(0)
    test(1)
    test(2)
    test(3)
    test(4)
    print('\nAll error types tested successfully!')


if __name__ == '__main__':
    print('=== Garden Error Types Demo ===\n')
    test_error_types()
