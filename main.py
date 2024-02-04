from datetime import datetime, timedelta
import sys
from collections import UserDict

# import traceback
# from types import NoneType

# from xml.etree.ElementPath import find


class Iterrable:
    def __init__(self, some_object, per_page):
        self.some_object = some_object
        self.current = 0
        self.per_page = per_page
        self.keys = list(self.some_object.keys())
        self.acc = []

    def __next__(self):
        if self.current < len(self.some_object):
            while True:
                res = self.some_object[self.keys[self.current]]
                self.acc.append(res)
                self.current += 1

                if self.current % self.per_page == 0 or self.current >= len(
                    self.some_object
                ):
                    res = self.acc
                    self.acc = []
                    return res

        raise StopIteration

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass
    # реалізація класу


class Phone(Field):
    # реалізація класу
    def __init__(self, phone):
        if len(str(phone)) != 10 or not phone.isdigit():
            raise ValueError(f"{phone} not correct format")
        super().__init__(str(phone))


class Birthday(Field):
    def __init__(self, birthday=None):
        super().__init__(birthday)


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    # реалізація класу
    def find_phone(self, phone):
        for phone_el in self.phones:
            if phone_el.value == phone:
                return phone_el
        return None
        # raise ValueError(f"{phone} not found")

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        for_remove = self.find_phone(phone)
        if for_remove:
            self.phones.remove(for_remove)

    def edit_phone(self, phone, new_phone):
        phone_el = self.find_phone(phone)
        if not phone_el:
            raise ValueError(f"{phone} not found")
        phone_el.value = new_phone

    # @property
    # def birthday(self):
    #     return self._birthday

    # @birthday.setter
    def set_birthday(self, birthday):
        if not birthday:
            self.birthday = Birthday(birthday)
            return

        try:
            datetime.strptime(birthday, "%Y-%m-%d").date()
        except ValueError as e:
            print(f"Birthday {birthday} invalid format")
            raise ValueError(e)
        self.birthday = Birthday(birthday)

    def days_to_birthday(self):
        if self.birthday:
            cur_date = datetime.now().date()
            delta_date = (self.birthday.replace(year=cur_date.year) - cur_date).days
            if delta_date < 0:
                delta_date = (
                    self.birthday.replace(year=cur_date.year + 1) - cur_date
                ).days
            return delta_date

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}, birthday: {self.birthday}"


class AddressBook(UserDict):
    # реалізація класу

    # def __init__(self):
    #     self.per_page = 3

    def find(self, string):
        # print(f'self: {self}')
        for el in self.data.values():
            if el.name.value == string:
                print("return el")
                return el
        # print("return {}")
        # raise ValueError(f"Name: {string} there is no such.")
        return None

    def add_record(self, record):
        print(f"add_record: {record}")
        self.data[record.name.value] = record
        # self.data[record.name.value] = '123s'

    def delete(self, name):
        # print(f'self: {self}\t name: {name}\t \nAlex: {self.data.__delitem__('Alex')}')
        for el in self.data.values():
            if el.name.value == name:
                self.data.__delitem__(name)
                break

    def __iter__(self):
        # print("!!!Iterable")
        return Iterrable(self.data, 3)


book = AddressBook()

b1 = Record("Alex")
b1.add_phone("0503220000")
b1.add_phone("0673220000")
# b1.set_birthday("2000-03-15")
# print(f"days_to_birthday: {b1.days_to_birthday()}")
# b1.birthday = "2000-03-15"
print(b1)
book.add_record(b1)
# print(f'find_phone: {b1.find_phone("0503220000")}')
# book.get("Alex").edit_phone("0503220000", "0953220000")
# book.get("Alex").remove_phone("0673220001")
# print(b1)

for i in range(1, 15):
    rec1 = Record(f"Alex{i}")
    rec1.add_phone(f"05032200{i:02}")
    book.add_record(rec1)

print(book)

for e in book:
    print(e)

# b2 = Record("Bob")
# b2.add_phone("111")
# b2.add_phone("222")
# # print(b2)
# book.add_record(b2)
# # print(book)
# # book.delete('Alex')
# # print(book.get('Alex'))
# book.get("Alex").remove_phone("123")
# book.get("Alex").edit_phone("456", "7890")
# print(book.get("Alex"))
# # print(book.get("Alex").find_phone("789"))
# print(book)


def print_boolean(bool):
    if bool:
        print("True")
    else:
        print("False")


# def check_phone_number(phone):
#     return ''


# DECORATOR input_error
def input_error(func):
    # two params - name, phone
    # You didn't provide a phone number
    # You did not enter your name and phone number

    one_params = ["handler_phone"]

    def wraper(*args):
        # print(f'func name: {func.__name__}') #print

        # print (args[0])
        result = None
        try:
            is_need_one_params = func.__name__ in one_params
            len_args = len(args[0])

            if is_need_one_params and len_args < 1:
                raise ValueError("Give me name please")
            elif not is_need_one_params and len_args < 2:
                raise ValueError("Give me name and phone please")

            result = func(*args)

        except ValueError as e:
            print(f"------- ValueError: {e}")

        except KeyError as e:
            print(f"------- keyerror: {e}")

        except IndexError as e:
            print(f"------- IndexError: {e}")

        except Exception as e:
            print("------ EXCEPTION - Exception {e}")
            # tb = sys.exc_info()

        return result

    return wraper


def find_name(name):
    # for i in range(len(phonebook)):
    # if phonebook[i]["name"] == name:
    # return i
    # return -1
    pass


def handler_hello(*args):
    print("How can I help you?")
    return


@input_error
def handler_add(*args):
    # print(f"*** add_handler")
    name, phone = args[0]
    # print(f"name: {name}\t phone: {phone}")
    # idx = find_name(name)
    new_contact = Record(name)  # .add_phone(phone)
    new_contact.add_phone(phone)
    find_contact = book.find(name)
    if len(find_contact) > 0:
        raise ValueError(f"Name: {name} already exists.")

    # print(f'new_contact: {new_contact}\t type new_contact: {type(new_contact)}')
    # print(f'find_contact: {find_contact}\t type find_contact: {type(find_contact.keys())}')
    # print(f'find_contact len: {len(find_contact)}')
    # contact = {'name': name, 'phone': phone}
    # if idx >= 0:

    # if len(find_contact) > 0:
    #     raise ValueError(f"name {name} already exists")

    # phonebook.append(contact)
    # print(f"Success added, name: {name}, phone: {phone}")
    # print(f"____phonebook: {phonebook}")
    # return f'{name} {phone}'
    book.add_record(new_contact)
    return new_contact


@input_error
def handler_change(*args):
    name, phone, new_phone = args[0]

    find_name = book.find(name)
    if find_name == "":
        raise ValueError(f"Name: {name} there is no such.")

    # idx = find_name(name)
    # if len(find_name) == 0:
    #     raise ValueError(f"{name} there is no such.")
    find_phone = find_name.find_phone(phone)
    if len(find_phone) == 0:
        raise ValueError(f"Phone: {phone} there is no such.")
    # book.edit_phone()
    find_name.edit_phone(phone, new_phone)
    # phonebook[idx]["phone"] = phone

    # print(f"Success change, name: {name}, phone: {phone}")
    # print(phonebook)
    return f"{name} {phone}"


@input_error
def handler_phone(*args):
    name, *phone = args[0]
    idx = find_name(name)
    if idx < 0:
        raise ValueError(f"{name} there is no such.")
    # print(phonebook[idx]["phone"])
    # return phonebook[idx]["phone"]


# @input_error
def handler_show_all(*args):
    res = ""
    for el in book.values():
        # res += f'{el['name']}: {el['phone']}\n'
        res += f"{el.name}: {'; '.join(p.value for p in el.phones)}\n"
    # print()
    # print(phonebook)
    return res


# @input_error
def handler_end_program(*args):
    print("Good bye!")
    sys.exit()


command_list = {
    "hello": handler_hello,
    "add": handler_add,
    "change": handler_change,
    "phone": handler_phone,
    "show all": handler_show_all,
    "good bye": handler_end_program,
    "close": handler_end_program,
    "exit": handler_end_program,
    "quit": handler_end_program,
}


def command_parse(string):
    # print(f"current command_parse {string}")
    string_lower = string.lower().strip()
    command_find = list(
        filter(lambda key: string_lower.startswith(key), command_list.keys())
    )
    # if find
    if len(command_find) == 0:
        print("command not found")
        return
    command_current = command_list[command_find[0]]
    command_parameters = string.replace(command_find[0], "").strip().split()
    res = command_current(command_parameters)
    return res

    # handler_end_program()


while False:
    command_input = input("Input command: ")
    # command_input = "hello sasha 124"
    # command_input = "add sasha +124"
    # command_input = "add Aleksandr1 +124"
    # command_input = "add Aleksandr +124"
    # command_input = "add "
    # command_input = "add sasha"
    # command_input = "add 124"
    # command_input = "change Aleksandr1 +124"
    # command_input = "change Aleksandr +124"
    # command_input = "change "
    # command_input = "change Aleksandr "
    # command_input = "phone Aleksandr"
    # command_input = "phone Aleksandr12"
    # command_input = "phone"
    # command_input = "show all"
    if command_input == "":
        continue
    res = command_parse(command_input)
    print(res)
    # end_program()
    # break
