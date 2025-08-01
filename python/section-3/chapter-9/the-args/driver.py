from number_utils import sum_all_numbers

# Comprehensive test case handler
test_case = input()

if test_case == "basic_test":
    # Test basic functionality with integers
    print(sum_all_numbers(1, 2, 3))
    print(sum_all_numbers())  # Should return 0
    print(sum_all_numbers(10, 20, 30))
    print(sum_all_numbers(1, 2, "three"))  # Error

elif test_case == "float_test":
    # Test with floating point numbers
    print(sum_all_numbers(1.1, 2.2, 3.3))
    print(sum_all_numbers(5.5, 5.0))

elif test_case == "mixed_numbers_test":
    # Test with a mix of integers and floats
    print(sum_all_numbers(5, 5.5))
    print(sum_all_numbers(10, 20.5, 30))

elif test_case == "zero_values_test":
    # Test with zero values
    print(sum_all_numbers(0, 0, 0))
    print(sum_all_numbers(0))           # Should return 0
    print(sum_all_numbers())            # Should return 0

elif test_case == "negative_values_test":
    # Test with negative values
    print(sum_all_numbers(-1, -2, -3))
    print(sum_all_numbers(-5, -5))
    print(sum_all_numbers(-5, 5))       # Should return 0

elif test_case == "large_values_test":
    # Test with very large values
    print(sum_all_numbers(1000000000, 2000000000))
    print(sum_all_numbers(1000000000000000, 2000000000000000))

elif test_case == "single_value_test":
    # Test with a single value
    print(sum_all_numbers(5))           # Should return 5
    print(sum_all_numbers(-10))         # Should return -10
    print(sum_all_numbers(3.5))         # Should return 3.5

elif test_case == "error_handling_test":
    # Test with various non-numeric inputs
    print(sum_all_numbers("string"))    # Error
    print(sum_all_numbers([1, 2, 3]))   # Error
    print(sum_all_numbers({"key": "value"}))  # Error
    print(sum_all_numbers(True))        # Error or 1 (depending on your design)
    print(sum_all_numbers(None))        # Error

elif test_case == "mixed_valid_invalid_test":
    # Test with a mix of valid and invalid types
    print(sum_all_numbers(1, 2, "three"))      # Error
    print(sum_all_numbers(1, [2, 3], 4))       # Error
    print(sum_all_numbers(1.5, "two", 3))      # Error

elif test_case == "empty_args_test":
    # Test with no arguments
    print(sum_all_numbers())  # Should return 0