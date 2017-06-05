from datetime import date, timedelta
import re

from django.db.models import Q

from .models import Person


search_regex = re.compile(
    "(((?(3)$|([^\W\d_]+(\.?)(\s+[^\W\d_]+(\.?))*))|(?(7)$|(\d{1,3}))|(?(8)$|([\d+\-()]{6,})))(\s+|$))+$")


def pretty_display(people):
    if people is None:
        return
    today = date.today()
    for person in people:
        age = int((today - person.birthday).days / 365.2425)
        if today.month == person.birthday.month and today.day == person.birthday.day:
            round_age = round((today - person.birthday).days / 365.2425)
            if age < round_age:
                age = round_age
        person.age = age
        if len(person.phone) > 7:
            index = 4
        else:
            index = 3
        person.phone = person.phone[:index] + "-" + person.phone[index:]
    return people


def search(search_query):
    name, age_dates, phone = query_params(search_query)
    query = Q()
    if name:
        for word in name:
            query = query & (Q(name__title__startswith=word) | Q(name__first_name__startswith=word) |
                             Q(name__last_name__startswith=word))
    if age_dates:
        query = query & Q(birthday__gte=age_dates[0]) & Q(birthday__lte=age_dates[1])
    if phone:
        query = query & Q(phone=phone)
    return pretty_display(Person.objects.filter(query))


def is_valid_age(age):
    if age is None:
        return True
    i_age = int(age)
    return 0 <= i_age <= 120


def subtract_years(dt, years):
    try:
        dt = dt.replace(year=dt.year-years)
    except ValueError:
        dt = dt.replace(year=dt.year-years, day=dt.day-1)
    return dt


def age_to_dates(age):
    if age is None:
        return None
    i_age = int(age)
    today = date.today()
    start_date = subtract_years(today + timedelta(days=1), i_age + 1)
    end_date = subtract_years(today, i_age)
    return start_date, end_date


def query_params(search_query):
    match = search_regex.match(search_query)
    if match is None:
        raise InvalidInputError("Improperly formatted input.")
    m_name, m_age, m_phone = match.group(3, 7, 8)
    if not is_valid_age(m_age):
        raise InvalidInputError("Age out of range.")
    name = m_name.split() if m_name else None
    age = age_to_dates(m_age)
    phone = re.sub(r"[()\-+]", "", m_phone) if m_phone else None
    return name, age, phone


class Error(Exception):
    """Base class for exceptions in this module."""
    def __init__(self, message):
        self.message = message


class InvalidInputError(Error):
    def __init__(self, message=""):
        self.message = "Input is invalid" + (": " + message if message else ".")
