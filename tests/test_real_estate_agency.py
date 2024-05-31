import pytest
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist


@pytest.fixture()
def create_user(db):
    return User.objects.create_user("Igor")


@pytest.mark.django_db
def test_check_username(create_user):
    print('check-user1')
    assert create_user.username == "Igor"


def test_non_existent_entry():
    with pytest.raises(ObjectDoesNotExist):
        User.objects.get(username="non-existent-user")


@pytest.mark.parametrize("username", ["Igor", "non-existent-user"])
def test_get_user_by_username(username, create_user):
    if username == "Igor":
        assert User.objects.get(username=username) == create_user
    else:
        with pytest.raises(ObjectDoesNotExist):
            User.objects.get(username=username)