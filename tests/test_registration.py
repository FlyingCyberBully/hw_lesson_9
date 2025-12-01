from pages.registration_page import RegistrationPage


def test_registration_mid_level():
    registration_page = RegistrationPage()

    (
        registration_page
        .open()
        .fill_first_name('John')
        .fill_last_name('Doe')
        .fill_email('john.doe@example.com')
        .choose_gender('Male')
        .fill_phone('1234567890')
        .set_birth_date(day='23', month_value='0', year_value='1990')
        .fill_subject('Maths')
        .choose_hobby('Sports')
        .upload_picture('test.jpg')
        .fill_address('Some Street 1')
        .select_state('NCR')
        .select_city('Delhi')
        .submit()
    )

    registration_page.should_have_registered(
        'John Doe',
        'john.doe@example.com',
        'Male',
        '1234567890',
        '23 January,1990',
        'Maths',
        'Sports',
        'test.jpg',
        'Some Street 1',
        'NCR Delhi'
    )
