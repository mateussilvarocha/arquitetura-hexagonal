# securit.py
from cryptography.fernet import Fernet

class LoginSQL:
    def __init__(self, key):
        self.__cipher_suite = Fernet(key)
        self.__host_name = "localhost"
        self.__user_name = "root"
        self.__user_password = self.__cipher_suite.encrypt(b'1234')
    
    @property
    def host_name(self):
        return self.__host_name
    
    @host_name.setter
    def host_name(self, value):
        self.__host_name = value
    
    @property
    def user_name(self):
        return self.__user_name
    
    @user_name.setter
    def user_name(self, value):
        self.__user_name = value
    
    @property
    def user_password(self):
        return self.__cipher_suite.decrypt(self.__user_password).decode()

    @user_password.setter
    def user_password(self, value):
        self.__user_password = self.__cipher_suite.encrypt(value.encode())

#um exemplo a ser considerado:

'''from cryptography.fernet import Fernet

class LoginSQL:
    def __init__(self, key):
        self.__cipher_suite = Fernet(key)
        self.__host_name = "localhost"
        self.__user_name = "root"
        self.__user_password = self.__cipher_suite.encrypt(b'1234')
    
    @property
    def host_name(self):
        return self.__host_name
    
    @host_name.setter
    def host_name(self, value):
        self.__host_name = value
    
    @property
    def user_name(self):
        return self.__user_name
    
    @user_name.setter
    def user_name(self, value):
        self.__user_name = value
    
    @property
    def user_password(self):
        return self.__cipher_suite.decrypt(self.__user_password).decode()

    @user_password.setter
    def user_password(self, value):
        self.__user_password = self.__cipher_suite.encrypt(value.encode())
'''