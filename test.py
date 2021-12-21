import unittest
import requests

class ApiTest(unittest.TestCase):
    API_URL = "http://127.0.0.1:5000/"
    USER_REGISTER_URL = "{}register".format(API_URL)
    CREATE_NOTE_URL = "{}note".format(API_URL)
    GET_USERS_URL = "{}/users".format(API_URL)
    GET_NOTE_URL = "{}note/1".format(API_URL)
    DELETE_NOTE_URL = "{}note/1".format(API_URL)


    USER_CREDINTIALS = {
        "username": "testap1itest",
        "password": "testestest123"
    }

    def test_1_post_users(self):
        r = requests.post(ApiTest.USER_REGISTER_URL, json=ApiTest.USER_CREDINTIALS)
        self.assertEqual(r.status_code, 201)



if __name__ == '__main__':
    unittest.main(verbosity=2)







