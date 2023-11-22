import pytest
from unittest.mock import Mock
from discount_applier import DiscountApplier

class MockNotifier():
    def __init__(self):
        self.users_notified = []
    
    def notify(self, user, message):
        self.users_notified.append(user)

def test_apply_v1():
    users = ["0","1","2","3"]
    notifier = MockNotifier()
    discApp = DiscountApplier(notifier)
    discApp.apply_v1(10, users)
    assert len(users) == len(notifier.users_notified)


def test_apply_v2():
    users = ["0","1","2","3"]
    notifier = MockNotifier()
    discApp = DiscountApplier(notifier)
    discApp.apply_v2(10, users)
    for i in range(len(users)):
        assert users[i] == notifier.users_notified[i]
        
def test_mock_apply_v1():
    users = ["0","1","2","3"]
    mock_notifier = Mock()
    mock_notifier.notify = Mock()
    discApp = DiscountApplier(mock_notifier)
    discApp.apply_v1(10, users)
    assert len(users) == mock_notifier.notify.call_count


def test_mock_apply_v2():
    users = ["0","1","2","3"]
    users_notified = []
    
    mock_notifier = Mock()
    mock_notifier.notify = Mock(side_effect=lambda user, _:users_notified.append(user))
    discApp = DiscountApplier(mock_notifier)
    discApp.apply_v2(10, users)
    for i in range(len(users)):
        assert users[i] == users_notified[i]
