import pytest
from safe_calculator import SafeCalculator

def test_divide_should_not_raise_any_error_when_authorized():
    # TODO: write a test that fails due to the bug in
    class MockAuthorizer():
        def authorize(self):
            return True
            
    authorizer = MockAuthorizer()
    calculator = SafeCalculator(authorizer)
    try:
        calculator.add(1, 2)
    except Exception as e:
        pytest.fail(str(e))
