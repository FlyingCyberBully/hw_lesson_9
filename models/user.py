from dataclasses import dataclass


@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    phone: str
    birth_day: str
    birth_month: str
    birth_year: str
    subject: str
    hobby: str
    picture: str
    address: str
    state: str
    city: str
