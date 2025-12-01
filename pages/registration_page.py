from pathlib import Path
from selene import browser, have
from models.user import User


class RegistrationPage:

    def open(self):
        browser.open('/automation-practice-form')
        return self

    def register(self, user: User):
        browser.element('#firstName').type(user.first_name)
        browser.element('#lastName').type(user.last_name)
        browser.element('#userEmail').type(user.email)

        browser.all('[for^=gender-radio]').element_by(have.text(user.gender)).click()
        browser.element('#userNumber').type(user.phone)

        # Date of Birth
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').click()
        browser.element(
            f'.react-datepicker__month-select option[value="{user.birth_month_value}"]'
        ).click()

        browser.element('.react-datepicker__year-select').click()
        browser.element(
            f'.react-datepicker__year-select option[value="{user.birth_year}"]'
        ).click()

        browser.element(f'[aria-label*="{user.birth_day}"]').click()

        # Subject
        browser.element('#subjectsInput').type(user.subject).press_enter()

        # Hobby
        browser.all('[for^="hobbies-checkbox"]').element_by(have.text(user.hobby)).click()

        # Picture
        path = str(
            Path(__file__).parent.parent.joinpath('resources', user.picture).resolve()
        )
        browser.element('#uploadPicture').set_value(path)

        # Address
        browser.element('#currentAddress').type(user.address)

        # State and City
        browser.element('#state').click()
        browser.all('[id^="react-select-3-option"]').element_by(have.text(user.state)).click()

        browser.element('#city').click()
        browser.all('[id^="react-select-4-option"]').element_by(have.text(user.city)).click()

        # Submit
        browser.element('#submit').click()
        return self

    def should_have_registered(self, user: User):
        browser.element('#example-modal-sizes-title-lg').should(
            have.text('Thanks for submitting the form')
        )

        browser.all('.modal-content table tbody tr td:nth-child(2)').should(
            have.exact_texts(
                f'{user.first_name} {user.last_name}',
                user.email,
                user.gender,
                user.phone,
                f'{user.birth_day} January,{user.birth_year}',
                user.subject,
                user.hobby,
                user.picture,
                user.address,
                f'{user.state} {user.city}',
            )
        )
