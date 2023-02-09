
# The test verifies that when the square function is called with the argument 2, it returns the correct result of 4. 
# The assert statement is used to make the comparison, and if the comparison fails the assert statement will raise an exception with an error message indicating what went wrong.

# If the test passes, we can be confident that the square function is working correctly and we can move on to testing other parts of the software. 
# If the test fails, we know that there is an issue with the square function and can fix it before it causes problems elsewhere in the software

def test_square():
    # Test that the square function returns the correct result
    result = square(2)
    assert result == 4, f"Expected 4, but got {result}"

def square(x):
    return x * x


