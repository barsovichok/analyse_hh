import requests
import collections


def get_dictonaries():
    dictionaries = requests.get('https://api.hh.ru/dictionaries').json()
    return dictionaries


def get_schedule(dictionaries):
    schedule = dictionaries['schedule']
    return schedule


def get_employment(dictionaries):
    employment = dictionaries['employment']
    return employment


dictionaries = get_dictonaries()
schedule = get_schedule(dictionaries)
employment = get_employment(dictionaries)
