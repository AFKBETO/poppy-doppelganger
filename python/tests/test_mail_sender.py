from mail_sender import MailSender, Request
from dataclasses import dataclass
from unittest.mock import Mock


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
    http_client = MockHttp()
    sender = MailSender(http_client)
    user = User("Name", "Email")
    response = sender.send_v1(user, "Message")
    req = response.request
    
    assert user.name == req.name and user.email == req.email


def test_send_v2():
    http_client = MockHttp(MockResponse(503))
    sender = MailSender(http_client)
    user = User("Name", "Email")
    response = sender.send_v2(user, "Message")
    req = response.request

    assert isinstance(req, Request)
    
def test_mock_send_v1():
    http_client = Mock()
    http_client.post = Mock()
    sender = MailSender(http_client)
    user = User("Name", "Email")
    response = sender.send_v1(user, "Message")
    req = response.request
    
    assert user.name == req.name and user.email == req.email


def test_mock_send_v2():
    http_client = Mock()
    response = Mock()
    response.code = 503

    
    http_client.post = Mock(return_value=response)
    sender = MailSender(http_client)
    user = User("Name", "Email")
    response = sender.send_v2(user, "Message")

    assert http_client.post.call_count == 2
