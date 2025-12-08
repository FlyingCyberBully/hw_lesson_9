from pages.registration_page import RegistrationPage
from models.user import User


def test_registration_high_level():

    student = User(
        first_name='John',
        last_name='Doe',
        email='john.doe@example.com',
        gender='Male',
        phone='1234567890',
        birth_day='23',
        birth_month='January',
        birth_year='1990',
        subject='Maths',
        hobby='Sports',
        picture='test.jpg',
        address='Some Street 1',
        state='NCR',
        city='Delhi'
    )

    registration_page = RegistrationPage()

    registration_page.open().register(student).should_have_registered(student)
