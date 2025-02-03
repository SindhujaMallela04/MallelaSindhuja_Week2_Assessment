from abc import ABC, abstractmethod

class UserAuthentication(ABC):
    @abstractmethod
    def login(self):
        pass
    def logout(self):
        pass

class GoogleAuth(UserAuthentication):
    def login(self, username, password):
        print(f"Login Successful for {username} using Google Authentication.")

    def logout(self):
        print("Logged out.")

class FacebookAuth(UserAuthentication):
    def login(self, username, password):
        print(f"Login Successful for {username} using Facebook Authentication.")

    def logout(self):
        print("Logged out.")

def main():
    google_auth = GoogleAuth()
    google_auth.login("Ramesh", "Hey@123")
    google_auth.logout()

    facebook_auth = FacebookAuth()
    facebook_auth.login("Ramesh", "123@Hey")
    facebook_auth.logout()
main()