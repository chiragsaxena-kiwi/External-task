import json

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

# from enroll.serializers import EmployeeSerializer
# from enroll.models import Employee



class RegistrationTestcas(APITestCase):
    # def test_registration(self):
    #     data = {'username':'testcase','email': 'test@localhost.app','password1': 'some_strong_psw'}
    #     response = self.client.post('/api/registration/',data)
        # self.assertEqual(response.status_code,status.HTTP_201_CREATED)
    #   def test_abaout_page_status_code(self):
    #       data = {'username':'testcase','email': 'test@localhost.app','password1': 'some_strong_psw'}
    #       response = self.client.post('/api/registration/',data)
    #       self.assertEquals(response.status_code, 200)
      def test_abaout_page_status_code(self):
          response = self.client.get(reverse("profile"))
          self.assertEqual(response.status_code, 200)  

      def test_abaout_page_status_code11(self):
          response = self.client.get(reverse("n4"))
          self.assertEqual(response.status_code, 200)     

      
      def test_abaout_page_status_code12(self):
            url=reverse('list')   
            self.assertEqual(resolve(url),func,project_list)      


      def test_abaout_page_status_code1(self):
          response = self.client.get(reverse("detail"))
          self.assertEqual(response.status_code, 200) 
      def test_abaout_page_status_code2(self):
          response = self.client.get(reverse("signup"))
          self.assertEqual(response.status_code, 200)
      def test_abaout_page_status_code3(self):
          response = self.client.get(reverse("signin"))
          self.assertEqual(response.status_code, 200)   
    #   def test_abaout_page_status_code4(self):
    #       response = self.client.get(reverse("logout"))
    #       self.assertEqual(response.status_code, 200)
    #   def test_abaout_page_status_code5(self):
    #       response = self.client.get(reverse("allusers"))
    #       self.assertEqual(response.status_code, 200)
    
      def test_abaout_page_status_code7(self):
          response = self.client.get(reverse("n4"))
          self.assertEqual(response.status_code, 200)  
      def test_abaout_page_status_code8(self):
          response = self.client.get(reverse("upload"))
          self.assertEqual(response.status_code, 200)  
 #urls
                       
from django.test import SimpleTestCase
from django.urls import reverse,resolve
from apps.web_admin.views.auth import LoginView,Logout,DashboardView,ForgotPasswordView

class TestingUrls(SimpleTestCase):
    """testing the urls"""
    def test_login(self):
        """testing the login url"""
        url = reverse('logout')
        self.assertEqual(resolve(url).func.view_class, LoginView)              
                   



   
   
   

