import pytest
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
    # TODO: write a test that fails due to the bug in
    # DiscountApplier.apply_v2
    pass
