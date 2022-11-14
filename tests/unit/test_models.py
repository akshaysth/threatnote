from threatnote.models import Organization, User


def test_new_org():
    org = Organization("threatnote.io", "temp_key_12345", org_id=1)
    assert org.name == "threatnote.io"
    assert org.org_key == "temp_key_12345"
    assert org.id == 1


def test_new_user():
    user = User(name="test", email="test@test.com", password_plaintext="Password!")
    assert user.email == "test@test.com"
    assert user.password != "Password!"
    assert user.role == "user"


def test_new_admin_user(init_database):
    user = User(
        name="admin",
        email="admin@test.com",
        password_plaintext="admin",
        role="admin",
        org_id=2,
    )
    assert user.email == "admin@test.com"
    assert user.password != "admin"
    assert user.role == "admin"
    assert user.organization == 2


def test_new_admin_user_with_fixture(new_admin_user):
    assert new_admin_user.email == "admin@note.io"
    assert new_admin_user.password != "admin"
    assert new_admin_user.role == "admin"
    assert new_admin_user.organization == 2


def test_new_user_with_fixture(new_user):
    assert new_user.email == "user@note.io"
    assert new_user.password != "user"
    assert new_user.role == "user"
    assert new_user.organization == 2


def test_user_id(new_user):
    new_user.id = 24
    assert isinstance(new_user.get_id(), str)
    assert not isinstance(new_user.get_id(), int)
    assert new_user.get_id() == "24"
