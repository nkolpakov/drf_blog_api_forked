from django.urls import reverse, resolve
from django.test import SimpleTestCase

from account.api import views

# Create your tests here.


class UrlsTest(SimpleTestCase):
    
    def test_app_name(self):
        self.assertEqual(resolve("/account/api/").app_name, "account:api")

    def test_users_list(self):
        path = reverse("account:api:users-list")
        self.assertEqual(resolve(path).func.view_class, views.UsersList)
        self.assertNotEqual(
            resolve(path).func.view_class, views.UsersDetailUpdateDelete
        )

    def test_user_profile(self):
        path = reverse("account:api:profile")
        self.assertEqual(resolve(path).func.view_class, views.UserProfile)
        self.assertNotEqual(resolve(path).func.view_class, views.UsersList)

    def test_login(self):
        path = reverse("account:api:login")
        self.assertEqual(resolve(path).func.view_class, views.Login)
        self.assertNotEqual(resolve(path).func.view_class, views.Register)

    def test_register(self):
        path = reverse("account:api:register")
        self.assertEqual(resolve(path).func.view_class, views.Register)
        self.assertNotEqual(resolve(path).func.view_class, views.Login)

    def test_verify_otp(self):
        path = reverse("account:api:verify-otp")
        self.assertEqual(resolve(path).func.view_class, views.VerifyOtp)
        self.assertNotEqual(resolve(path).func.view_class, views.Login)

    def test_change_two_step_password(self):
        path = reverse("account:api:change-two-step-password")
        self.assertEqual(resolve(path).func.view_class, views.ChangeTwoStepPassword)
        self.assertNotEqual(resolve(path).func.view_class, views.CreateTwoStepPassword)

    def test_create_two_step_password(self):
        path = reverse("account:api:create-two-step-password")
        self.assertEqual(resolve(path).func.view_class, views.CreateTwoStepPassword)
        self.assertNotEqual(resolve(path).func.view_class, views.ChangeTwoStepPassword)

    def test_delete_account(self):
        path = reverse("account:api:delete-account")
        self.assertEqual(resolve(path).func.view_class, views.DeleteAccount)
        self.assertNotEqual(resolve(path).func.view_class, views.Register)

    def test_users_detail_update_delete(self):
        path = reverse("account:api:users-detail", args=[1])
        self.assertEqual(resolve(path).func.view_class, views.UsersDetailUpdateDelete)
        self.assertNotEqual(resolve(path).func.view_class, views.UsersList)
