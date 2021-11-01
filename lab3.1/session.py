import csv
import random
import json
from faker import Faker

fake = Faker()
Faker.seed(0)
browsers = ['Chrome', "Yandex", "Safari", "Firefox", "Opera", "Edge", "Explorer", "Unknown"]
auth_sessions = []
auth_users = []
auth_status = []

# ====================================================
users_id = []
for num_fac in range(40):
    for stud in range(1, 20001):
        user_id = (num_fac + 1) * 100000 + stud
        users_id.append(user_id)
for teach in range(1, 199001):
    teach_id = 10000000 + teach
    users_id.append(teach_id)
for num_fac in range(40):
    for admin in range(1, 26):
        admin_id = (num_fac + 1) * 100 + admin
        users_id.append(admin_id)

# ====================================================

with open('session.csv', 'w') as csv_file:
    user_writer = csv.writer(csv_file, delimiter=',')
    for i in range(1, 100000001):
        session_id = i
        ip = fake.ipv4()
        browser = random.choice(browsers)
        checker = random.randint(1, 100)
        country = ""
        if checker >= 5:
            country += "Russia"
        else:
            country += "Ukraine"
        year = str(random.randint(2020, 2021))
        month = str(random.randint(1, 12))
        if len(month) == 1:
            month = '0' + month
        day = str(random.randint(1, 30))
        if month == '02':
            day = str(random.randint(1, 28))
        if len(day) == 1:
            day = '0' + day
        date_start = year + '-' + month + '-' + day
        h = str(random.randint(0, 23))
        if len(h) == 1:
            h = '0' + h
        m = str(random.randint(0, 59))
        if len(m) == 1:
            m = '0' + m
        s = str(random.randint(0, 59))
        if len(s) == 1:
            s = '0' + s
        time_start = h + ':' + m + ':' + s
        date_with_time = date_start + ' ' + time_start
        h_1 = str(random.randint(0, 2))
        if len(h_1) == 1:
            h_1 = '0' + h_1
        m_1 = str(random.randint(0, 59))
        if len(m_1) == 1:
            m_1 = '0' + m_1
        s_1 = str(random.randint(0, 59))
        if len(s_1) == 1:
            s_1 = '0' + s_1
        time_end = h_1 + ':' + m_1 + ':' + s_1
        status = 'завершена'
        if date_start == '2021-30-10':
            status = 'активная'
            time_end = None
        id_ = None
        check_id = random.randint(1, 100)
        if check_id <= 20:
            id_ = random.choice(users_id)
            auth_sessions.append(session_id)
            auth_users.append(id_)
            auth_status.append(status)
        json_data = json.dumps({"ip": ip, "browser": browser, "country": country})
        user_writer.writerow([session_id, json_data, date_with_time, status, time_end, id_])

stud_actions = ['просмотр расписания', 'просмотр оценок', 'изменение пароля', 'просмотр МФК', 'просмотр спецкурса',
                'просмотр данных о кафедре', 'просмотр данных о преподавателе', 'запись на МФК', 'запись на спецкурс']
teach_actions = ['просмотр занятий', 'выставление оценок ученику', 'изменение пароля',
                 'просмотр данных об ученике', 'просмотр данных о кафедре']
admin_actions = ['просмотр логов действий ученика', 'просмотр логов действий преподавателя']

with open('session_info.csv', 'w') as csv_file:
    user_writer = csv.writer(csv_file, delimiter=',')
    for i in range(len(auth_sessions)):
        session_id = auth_sessions[i]
        status = auth_status[i]
        us_id = auth_users[i]
        cnt_att = random.randint(1, 10)
        actions = ['вход в аккаунт']
        add_actions = []
        if 1 <= us_id // 100000 <= 40:
            add_actions = random.sample(stud_actions, random.randint(1, len(stud_actions)))
            for j in range(len(add_actions)):
                if add_actions[j] == 'просмотр МФК':
                    add_actions += ' ' + str(random.randint(1, 20000))
                elif add_actions[j] == 'просмотр спецкурса':
                    add_actions += ' ' + str(random.randint(1, 500))
                elif add_actions[j] == 'просмотр данных о кафедре':
                    add_actions += ' ' + str(random.randint(1, 800))
                elif add_actions[j] == 'просмотр данных о преподавателе':
                    add_actions += ' ' + str(random.randint(10000000 + 1, 10000000 + 199000))
                elif add_actions[j] == 'запись на МФК':
                    add_actions += ' ' + str(random.randint(1, 20000))
                elif add_actions[j] == 'запись на спецкурс':
                    add_actions += ' ' + str(random.randint(1, 500))
        elif 1 <= us_id // 100 <= 40:
            add_actions = random.sample(admin_actions, random.randint(1, len(admin_actions)))
            for j in range(len(add_actions)):
                if add_actions[j] == 'просмотр логов действий ученика':
                    add_actions += ' ' + str(random.randint(1, 40) * 100000 + random.randint(1, 20000))
                if add_actions[j] == 'просмотр логов действий преподавателя':
                    add_actions += ' ' + str(random.randint(10000000 + 1, 10000000 + 199000))
        else:
            add_actions = random.sample(teach_actions, random.randint(1, len(teach_actions)))
            for j in range(len(add_actions)):
                if add_actions[j] == 'выставление оценок ученику':
                    add_actions += ' ' + str(random.randint(1, 40) * 100000 + random.randint(15001, 20000))
                if add_actions[j] == 'просмотр данных об ученике':
                    add_actions += ' ' + str(random.randint(1, 40) * 100000 + random.randint(1, 20000))
                if add_actions[j] == 'просмотр данных о кафедре':
                    add_actions += ' ' + str(random.randint(1, 800))
        actions += add_actions
        if status == 'завершена':
            actions.append('выход из аккаунта')
        actions_array = '{'
        for j in range(len(actions) - 1):
            actions_array += '"' + actions[j] + '", '
        actions_array += '"' + actions[len(actions) - 1] + '"}'
        user_writer.writerow([session_id, cnt_att, actions_array])
