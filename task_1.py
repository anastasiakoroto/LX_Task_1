import copy
import json


class FileHandler:

    def __init__(self, path_to_file):
        self.file_path = path_to_file

    def load_file(self):
        with open(self.file_path, 'r', encoding='utf-8') as current_file:
            current_file = current_file.read()
        return current_file

    def decode_json(self):
        content = self.load_file()
        data = json.loads(content)
        return data


class FileWriter:

    def write_to_json(self, obj):
        with open('format.json', 'w') as json_file:
            json.dump(obj, json_file)

    def write_to_xml(self):
        pass


class Union:

    def add_student_to_room(self, room, student):
        student = student.copy()
        student.pop('room')
        if room.get('students') is None:
            room['students'] = [student]
        else:
            room['students'].append(student)
        return room

    def get_rooms_and_students_list(self, stud_list, room_list):
        room_list = copy.deepcopy(room_list)
        for student in stud_list:
            for room in room_list:
                if student['room'] == room['id']:
                    self.add_student_to_room(room, student)
        return room_list


if __name__ == '__main__':
    students = '/Users/Anastasia/PycharmProjects/LeverX Course/task_1/students.json'
    rooms = '/Users/Anastasia/PycharmProjects/LeverX Course/task_1/rooms.json'

    students_file = FileHandler(students)
    students_list = students_file.decode_json()
    print('Students list: ', students_list)
    rooms_file = FileHandler(rooms)
    rooms_list = rooms_file.decode_json()
    print('Rooms list: ', rooms_list)

    union_obj = Union()
    result = union_obj.get_rooms_and_students_list(students_list, rooms_list)
    print('-' * 50)
    print('Result:', result, sep='\n')

    fw = FileWriter()
    fw.write_to_json(result)
