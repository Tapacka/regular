from pprint import pprint
import re
import csv

with open("phonebook_raw.csv") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

contacts_list2 = []
for people in contacts_list:
    b = []
    for data in people:
        pattern = re.compile(r"(\+7|8)\s*\(?(\d+)\)?[\s-]*(\d\d\d)[\s-]*(\d\d)[\s-]*(\d\d)")
        result = pattern.sub(r'+7(\2)\3-\4-\5', data)
        pattern2 = re.compile(r"\D*доб\D*\s*(\w\w\w\w)\)?")
        result2 = pattern2.sub(r'доб.\1', result)
        b.append(result2)
    contacts_list2.append(b)

contacts_list3 = []
for people in contacts_list2:
    p = []
    for i in people[0:2]:
        p.extend(i.split())
    p.extend(people[2:])
    contacts_list3.append(p)

q = []
contacts_list4 = []
for people in contacts_list3:
    if people[0:2] not in q:
        q.append(people[0:2])
        contacts_list4.append(people)
    else:
        q.append(people[0:2])
        n1 = q.index(people[0:2])
        contacts_list4.append((contacts_list3[n1]).extend(people[4:]))
contacts_list4 = list(filter(None, contacts_list4))

pprint(contacts_list4)

with open("phonebook.csv", "w") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(contacts_list4)