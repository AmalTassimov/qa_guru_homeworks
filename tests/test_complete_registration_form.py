import os

from selene import browser, have


def test_submit_registration_form():
    browser.open('/automation-practice-form')

    browser.element('#firstName').type('John')
    browser.element('#lastName').type('Smith')
    browser.element('#userEmail').type('Smith@mail.ru')
    browser.element('[for=gender-radio-1]').click()
    browser.element('#userNumber').type('9772846999')

    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click()
    browser.all('.react-datepicker__month-select option') \
        .should(have.size_greater_than(0)) \
        .filtered_by(have.exact_text('September')).first.click()
    browser.element('.react-datepicker__year-select').click()
    browser.all('.react-datepicker__year-select option') \
        .should(have.size_greater_than(0)) \
        .filtered_by(have.exact_text('1985')).first.click()
    browser.element('.react-datepicker__day--004') \
        .should(have.no.css_class('.react-datepicker__day--outside-month')).click()

    browser.element('#subjectsInput').type('Math').press_enter()
    browser.element('#subjectsInput').type('Physics').press_enter()

    browser.element('[for="hobbies-checkbox-1"]').click()

    browser.element('#uploadPicture').set_value(os.path.join(os.path.abspath('..\\resources'), 'test_img.jpg'))

    browser.element('#currentAddress').type('Moscow')
    browser.element('#state').click()
    browser.element('#react-select-3-option-2').should(have.exact_text('Haryana')).click()
    browser.element('#city').click()
    browser.element('#react-select-4-option-1').should(have.exact_text('Panipat')).click()
    browser.element('#submit').click()

    browser.element('.modal-title').should(have.exact_text('Thanks for submitting the form'))
    browser.all('tbody tr').should(have.exact_texts(
        'Student Name John Smith',
        'Student Email Smith@mail.ru',
        'Gender Male',
        'Mobile 9772846999',
        'Date of Birth 04 September,1985',
        'Subjects Maths, Physics',
        'Hobbies Sports',
        'Picture test_img.jpg',
        'Address Moscow',
        'State and City Haryana Panipat'
    ))
