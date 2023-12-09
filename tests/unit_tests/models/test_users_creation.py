import uuid
from datetime import date, datetime, timedelta

import pytest
from pydantic import ValidationError

from daftar_common.models.users import User, UserClassroom


# Create an instance of UserClassroom
@pytest.fixture
def user_classroom():
    return UserClassroom(id_classroom=uuid.uuid4(), is_teacher="Yes")


@pytest.fixture
def user(user_classroom):
    return User(
        pseudo="user1",
        firstname="John",
        lastname="Doe",
        email="johndoe@example.com",
        is_admin=False,
        birthdate=date(1990, 1, 1),
        classrooms=[user_classroom],
    )


def test_create_user(user):
    """Check the creation of a simple, classic user"""
    assert user.pseudo == "user1", "pseudo should be user1"
    assert user.firstname == "John", "firstname should be John"
    assert user.lastname == "Doe", "lastname should be Doe"
    now = datetime.now()
    assert now - timedelta(seconds=2) < user.created_at < now + timedelta(seconds=2), "created_at should be now"


def test_create_user_types(user):
    """Check the type of variables created from the user"""
    assert isinstance(user.id, uuid.UUID), "id should be a UUID"
    assert isinstance(user.pseudo, str), "pseudo should be a string"
    assert isinstance(user.birthdate, date), "birthdate should be a date"
    assert isinstance(user.classrooms, list), "classrooms should be a list"
    assert isinstance(user.created_at, datetime), "updated_at should be a datetime"


def test_create_user_mand_only():
    """Check the creation of a user with mandatory fields only"""
    user = User(
        pseudo="user1",
        firstname="John",
        lastname="Doe",
        email="johndoe@example.com",
        is_admin=False,
        birthdate=date(1990, 1, 1),
    )

    assert user.pseudo == "user1", "pseudo should be user1"
    assert user.email == "johndoe@example.com", "email should be correct"
    assert user.classrooms == [], "classrooms should be empty"
    assert user.address == "", "address should be empty"


def test_create_user_wrong_email():
    """Check the creation of a user with a wrong email"""
    with pytest.raises(
        ValidationError,
        match="value is not a valid email address",
    ):
        User(
            pseudo="user1",
            firstname="John",
            lastname="Doe",
            email="johndoe",
            is_admin=False,
            birthdate=date(1990, 1, 1),
        )


def test_create_user_with_different_date_format():
    """Check the creation of a user with a different date format"""
    with pytest.raises(
        ValidationError,
        match="Input should be a valid date or datetime",
    ):
        User(
            pseudo="user1",
            firstname="John",
            lastname="Doe",
            email="johndoe@gmail.com",
            is_admin=False,
            birthdate="1990-1-1",
        )


def test_create_user_with_str_date():
    """Check the creation of a user with a string date"""
    user = User(
        pseudo="user1",
        firstname="John",
        lastname="Doe",
        email="johndoe@gmail.com",
        is_admin=False,
        birthdate="1990-01-01",
    )
    assert user.birthdate == date(
        1990, 1, 1
    ), "birthdate should be converted corretly to date"
