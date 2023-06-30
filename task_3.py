# -*- coding: windows-1251 -*-
import csv
import re
from logger_1 import logger

phone_pattern = re.compile(r"^(\+7|8)\D*(\d{3})\D*(\d{3})\D*(\d{2})\D*(\d{2})\D*(\d{4})?.*")

@logger
def format_phone(phone):
  nums = phone_pattern.match(phone)
  if nums.groups()[5]:
    phone = phone_pattern.sub(r"+7(\2)\3-\4-\5 доб.\6", phone)
  else:
    phone = phone_pattern.sub(r"+7(\2)\3-\4-\5", phone)

  return phone

with open("phonebook_raw.csv", "r", encoding="utf8") as f:
  contacts_list = list(csv.reader(f, delimiter=","))

contacts_info = {}
for contact in contacts_list[1:]:
  lastname, firstname, surname, organization, position, phone, email = contact[:7]
  name = re.findall(r"([(А-Я][а-я]+)", lastname+firstname+surname)

  if len(name) < 2: continue

  contacts_info.setdefault(name[0]+name[1], {})
  contact_info = contacts_info.get(name[0]+name[1])

  contact_info["lastname"] = name[0]
  contact_info["firstname"] = name[1]

  if len(name) > 2 and not contact_info.get("surname"):
    contact_info["surname"] = name[2]

  if organization and not contact_info.get("organization"):
    contact_info["organization"] = organization

  if position and not contact_info.get("position"):
    contact_info["position"] = position

  if phone and not contact_info.get("phone"):
    contact_info["phone"] = format_phone(phone)

  if email and not contact_info.get("email"):
    contact_info["email"] = email

contacts_list = [contacts_list[0]]
for contact in contacts_info.values():
  contacts_list.append([
    contact.get("lastname"),
    contact.get("firstname"),
    contact.get("surname"),
    contact.get("organization"),
    contact.get("position"),
    contact.get("phone"),
    contact.get("email"),
  ])

with open("phonebook.csv", "w", encoding="utf8") as f:
  csv.writer(f, delimiter=',').writerows(contacts_list)
