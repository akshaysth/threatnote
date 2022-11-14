def test_index(app):
    response = app.get("/")
    assert b"redirect" in response.data


def test_index_redirect(app):
    response = app.get("/", follow_redirects=True)
    assert b"Sign In" in response.data


def test_signup(app):
    response = app.get("/signup")
    assert b"Create Account" in response.data


def test_login_get(app):
    response = app.get("/login")
    assert b"Sign In" in response.data


def test_logged_in_dashboard(app, init_database, login_default_user):
    response = app.get("/", follow_redirects=True)
    assert b"Sign Out" in response.data
    assert b"Sign In" not in response.data
    assert b"Dashboard" in response.data
    assert b"Requirements" in response.data
    assert b"Reports" in response.data
    assert b"Indicators" in response.data
    assert b"Consumers" in response.data
    assert b"Settings" in response.data
