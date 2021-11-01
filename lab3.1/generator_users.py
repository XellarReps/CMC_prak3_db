import csv
import random
from faker import Faker

fake = Faker('ru_RU')
Faker.seed(0)


types_user = ['студент - выпускник', 'преподаватель', 'администратор']
faculties = ['Механико–математический факультет',
             'Факультет вычислительной математики и кибернетики',
             'Физический факультет',
             'Химический факультет',
             'Факультет наук о материалах',
             'Биологический факультет',
             'Факультет биоинженерии и биоинформатики',
             'Факультет почвоведения',
             'Геологический факультет',
             'Географический факультет',
             'Факультет фундаментальной медицины',
             'Факультет фундаментальной физико-химической инженерии',
             'Биотехнологический факультет',
             'Факультет космических исследований',
             'Исторический факультет',
             'Филологический факультет',
             'Философский факультет',
             'Экономический факультет',
             'Юридический факультет',
             'Факультет журналистики',
             'Факультет психологии',
             'Институт стран Азии и Африки',
             'Социологический факультет',
             'Факультет иностранных языков и регионоведения',
             'Факультет государственного управления',
             'Факультет мировой политики',
             'Факультет искусств',
             'Факультет глобальных процессов',
             'Факультет педагогического образования',
             'Факультет политологии',
             'Высшая школа бизнеса (факультет)',
             'Московская школа экономики (факультет)',
             'Высшая школа перевода (факультет)',
             'Высшая школа государственного администрирования (факультет)',
             'Высшая школа государственного аудита (факультет)',
             'Высшая школа управления и инноваций (факультет)',
             'Высшая школа инновационного бизнеса (факультет)',
             'Высшая школа современных социальных наук (факультет)',
             'Высшая школа телевидения (факультет)',
             'Высшая школа культурной политики и управления в гуманитарной сфере (факультет)']


with open('user_info.csv', 'w') as csv_file:
    user_writer = csv.writer(csv_file, delimiter=',')
    for type_user in types_user:
        if type_user == 'студент - выпускник':
            for num_fac in range(40):
                year = 2006
                for stud in range(1, 20001):
                    user_id = (num_fac + 1) * 100000 + stud
                    full_name = fake.name()
                    date = str(year) + '-' + '09' + '-' + '01'
                    email = 's' + str(user_id) + '@gse.msu.ru'
                    if stud % 1250 == 0:
                        year += 1
                    if stud > 15000:
                        user_writer.writerow([user_id, 'студент', full_name, faculties[num_fac], date, email])
                    else:
                        user_writer.writerow([user_id, 'выпускник', full_name, faculties[num_fac], date, email])
        if type_user == 'преподаватель':
            for teach in range(1, 199001):
                teach_id = 10000000 + teach
                full_name = fake.name()
                day = str(random.randint(1, 28))
                if len(day) == 1:
                    day = '0' + day
                m = str(random.randint(1, 12))
                if len(m) == 1:
                    m = '0' + m
                date = str(random.randint(2008, 2021)) + '-' + m + '-' + day
                email = 'teacher-' + str(teach_id) + '@gse.msu.ru'
                user_writer.writerow([teach_id, type_user, full_name, None, date, email])
        if type_user == 'администратор':
            for num_fac in range(40):
                for admin in range(1, 26):
                    admin_id = (num_fac + 1) * 100 + admin
                    full_name = fake.name()
                    day = str(random.randint(1, 28))
                    if len(day) == 1:
                        day = '0' + day
                    m = str(random.randint(1, 12))
                    if len(m) == 1:
                        m = '0' + m
                    date = str(random.randint(2008, 2021)) + '-' + m + '-' + day
                    email = 'admin-' + str(admin_id) + '@gse.msu.ru'
                    user_writer.writerow([admin_id, type_user, full_name, faculties[num_fac], date, email])

