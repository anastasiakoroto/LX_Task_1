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
        with open('updated_rooms.json', 'w') as json_file:
            json.dump(obj, json_file)

    def write_to_xml(self, obj):
        with open('updated_rooms.xml', 'w') as xml_file:
            xml_file.write('<?xml version="1.0" encoding="UTF-8"?>')
            xml_file.write('<rooms>')
            for dct in obj:
                xml_file.write('<room>')
                xml_file.write('<id>' + str(dct['id']) + '</id>')
                xml_file.write('<name>' + dct['name'] + '</name>')
                xml_file.write('<students>')
                for student in dct['students']:
                    xml_file.write('<student>')
                    xml_file.write('<id>' + str(student['id']) + '</id>')
                    xml_file.write('<name>' + student['name'] + '</name>')
                    xml_file.write('</student>')
                xml_file.write('</students>')
                xml_file.write('</room>')
            xml_file.write('</rooms>')


class ListsHandler:

    def __init__(self, st_path, room_path, format_type):
        self.st_path = st_path
        self.room_path = room_path
        self.format = format_type

        st_file_handler = FileHandler(self.st_path)
        self.students_list = st_file_handler.decode_json()

        rooms_file_handler = FileHandler(self.room_path)
        self.rooms_list = rooms_file_handler.decode_json()

        self.file_writer = FileWriter()

    def _add_student_to_room(self, room, student):
        student = student.copy()
        student.pop('room')
        if room.get('students') is None:
            room['students'] = [student]
        else:
            room['students'].append(student)
        return room

    def get_rooms_and_students_list(self):
        room_list = copy.deepcopy(self.rooms_list)
        for student in self.students_list:
            for room in room_list:
                if student['room'] == room['id']:
                    self._add_student_to_room(room, student)
        return room_list

    def write_updated_rooms_to_file(self):
        updated_room_list = self.get_rooms_and_students_list()
        if self.format == 'json':
            self.file_writer.write_to_json(updated_room_list)
        elif self.format == 'xml':
            self.file_writer.write_to_xml(updated_room_list)
        else:
            print(f'There are no functionality for {self.format} format. Sorry :c\nBut you can choose json/xml c:')


if __name__ == '__main__':
    students = '/Users/Anastasia/PycharmProjects/LeverX Course/task_1/students.json'
    rooms = '/Users/Anastasia/PycharmProjects/LeverX Course/task_1/rooms.json'

    obj = ListsHandler(students, rooms, 'json')
    obj.write_updated_rooms_to_file()
    obj_2 = ListsHandler(students, rooms, 'xml')
    obj_2.write_updated_rooms_to_file()
