

def test_ping(test_app):
    # Given - test_app
    # When - request to /ping
    # Then - assert response is ...
    expected_json = {'environment': 'dev', 'ping': 'pong', 'testing': True}
    response = test_app.get('/ping')

    assert response.status_code == 200
    assert response.json() == expected_json


# Tests structure:
# State	|                           Explanation                                                     |	Code
# Given	| the state of the application before the test runs	setup code, fixtures, database state    |
# When	| the behavior/logic being tested	                                                        | code under test
# Then	| the expected changes based on the behavior	                                            | asserts
