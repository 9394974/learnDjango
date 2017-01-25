from django.test import TestCase

# Create your tests here.


def generate_string(length):
    s = ''
    for i in range(length):
        s += 'a'

    return s

# field error: name length overflow
not_valid_data1 = {
    'courses_id': 1,
    'name': generate_string(51),
    'intro': generate_string(201)
}


# business logic: courses_id not exist
not_valid_data2 = {
    'courses_id': 2,
    'name': 'less than 50 characters',
    'intro': 'less than 200 characters'
}

