from mail_sender import MailSender, Request
from dataclasses import dataclass

@dataclass
class MockResponse:
    code: int
    request: any = None

@dataclass
class User:
    name: str
    email: str

class MockHttp():
    def __init__(self, response = MockResponse(200)):
        self.response = response
    def post(self, url, request):
        self.response.request = request
        return self.response

def test_send_v1():
    # TODO: write a test that fails due to the bug in MailSender.send_v1
    http_client = MockHttp()
    sender = MailSender(http_client)
    user = User("Name", "Email")
    response = sender.send_v1(user, "Message")
    req = response.request
    
    assert user.name == req.name
    assert user.email == req.email


def test_send_v2():
    # TODO: write a test that fails due to the bug in MailSender.send_v2
    http_client = MockHttp(MockResponse(503))
    sender = MailSender(http_client)
    user = User("Name", "Email")
    response = sender.send_v2(user, "Message")
    req = response.request

    assert isinstance(req, Request)
