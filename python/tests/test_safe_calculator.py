import pytest
from safe_calculator import SafeCalculator

def test_divide_should_not_raise_any_error_when_authorized():
    class MockAuthorizer():
        def authorize(self):
            return True
            
    authorizer = MockAuthorizer()
    calculator = SafeCalculator(authorizer)
    try:
        result = calculator.add(1, 2)
        assert result == 3
    except Exception as e:
        pytest.fail(str(e))
