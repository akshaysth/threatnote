def test_login_post(app, init_database):
    response = app.post(
        "/login",
        data=dict(email="admin1@test.io", password="admin"),
        follow_redirects=True,
    )
    assert response.status_code == 200
    assert b"Dashboard" in response.data
    assert b"Requirements" in response.data


def test_login_already_logged_in(app, init_database, login_default_user):
    response = app.post(
        "/login",
        data=dict(email="admin1@test.io", password="admin"),
        follow_redirects=True,
    )
    assert response.status_code == 200
    # assert b"Already logged in!" in response.data
    assert b"Sign Out" in response.data
    assert b"Sign In" not in response.data


def test_invalid_login(app, init_database):
    response = app.post(
        "/login",
        data=dict(email="admin1@test.io", password="notadmin"),
        follow_redirects=True,
    )
    assert response.status_code == 200
    assert b"Error! Incorrect login credentials!" in response.data
    assert b"Sign In" in response.data
