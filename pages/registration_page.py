from pathlib import Path
from selene import browser, have


class RegistrationPage:

    def open(self):
        browser.open('/automation-practice-form')
        return self

    def fill_first_name(self, value: str):
        browser.element('#firstName').type(value)
        return self

    def fill_last_name(self, value: str):
        browser.element('#lastName').type(value)
        return self

    def fill_email(self, value: str):
        browser.element('#userEmail').type(value)
        return self

    def choose_gender(self, gender: str):
        browser.all('[for^=gender-radio]').element_by(have.text(gender)).click()
        return self

    def fill_phone(self, value: str):
        browser.element('#userNumber').type(value)
        return self

    def set_birth_date(self, day: str, month_value: str, year_value: str):
        browser.element('#dateOfBirthInput').click()

        browser.element('.react-datepicker__month-select').click()
        browser.element(f'.react-datepicker__month-select option[value="{month_value}"]').click()

        browser.element('.react-datepicker__year-select').click()
        browser.element(f'.react-datepicker__year-select option[value="{year_value}"]').click()

        browser.element(f'[aria-label*="{day}"]').click()

        return self

    def fill_subject(self, subject: str):
        browser.element('#subjectsInput').type(subject).press_enter()
        return self

    def choose_hobby(self, hobby: str):
        browser.all('[for^="hobbies-checkbox"]').element_by(have.text(hobby)).click()
        return self

    def upload_picture(self, filename: str):
        path = str(Path(__file__).parent.parent.joinpath('resources', filename).resolve())
        browser.element('#uploadPicture').set_value(path)
        return self

    def fill_address(self, value: str):
        browser.element('#currentAddress').type(value)
        return self

    def select_state(self, state: str):
        browser.element('#state').click()
        browser.all('[id^="react-select-3-option"]').element_by(have.text(state)).click()
        return self

    def select_city(self, city: str):
        browser.element('#city').click()
        browser.all('[id^="react-select-4-option"]').element_by(have.text(city)).click()
        return self

    def submit(self):
        browser.element('#submit').click()
        return self

    def should_have_registered(self, *expected_values):
        browser.element('#example-modal-sizes-title-lg').should(
            have.text('Thanks for submitting the form')
        )

        browser.all('.modal-content table tbody tr td:nth-child(2)').should(
            have.exact_texts(*expected_values)
        )
