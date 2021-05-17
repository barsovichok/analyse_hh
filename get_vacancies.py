import requests
import collections

api_url = 'https://api.hh.ru/vacancies/'
payload = {'st': 'searchVacancy', 'text': 'QA Engineer', 'search_field': 'name', 'salary': '180000',
           'currency_code': 'RUR', 'only_with_salary': 'true', 'experience': 'between3And6',
           'employment': 'full'}

text = input('Привет! Это анализатор вакансий, расскажет, '
             'какие навыки нужны, чтобы получать 300000 в секунду.'
             'Итак, вакансии кого будем искать? \n')

salary = input('Какую зарплату хотите? \n')
experience = int(input('Cколько у вас лет опыта? \n'))

if 0 <= experience < 1:
    payload.update(experience='noExperience')
elif 1 <= experience <= 3:
    payload.update(experience='between1And3')
elif 3 < experience <= 6:
    payload.update(experience='between3And6')
elif experience > 6:
    payload.update(experience='moreThan6')

payload.update(text=text)
payload.update(salary=salary)

response_vacancies = requests.get(api_url, params=payload).json()

key_skills_in_vacancy = []
key_skills = []
for x in range(len(response_vacancies['items'])):
    response_vacancy = requests.get(response_vacancies['items'][x]['url']).json()
    key_skills_in_vacancy = response_vacancy['key_skills']
    x = x + 1
    for i in range(len(key_skills_in_vacancy)):
        key_skills.append(key_skills_in_vacancy[i]['name'])

c = collections.Counter()
for word in key_skills:
    c[word] += 1

for word in c.most_common():
    print(word)
