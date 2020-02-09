import copy
import json
import xml.etree.ElementTree as ElemTree


class FileHandler:

    def __init__(self, path_to_file):
        self.file_path = path_to_file

    def json_to_obj(self):
        with open(self.file_path, 'r', encoding='utf-8') as current_file:
            obj = json.load(current_file)
            return obj


class FileWriter:

    def write_to_json(self, obj):
        with open('updated_rooms.json', 'w') as json_file:
            json.dump(obj, json_file)

    def write_to_xml(self, obj):
        root = ElemTree.Element('rooms')
        for dct in obj:
            room = ElemTree.Element('room')
            root.append(room)
            room_id = ElemTree.SubElement(room, 'id')
            room_id.text = str(dct['id'])
            room_name = ElemTree.SubElement(room, 'name')
            room_name.text = dct['name']
            room_st = ElemTree.SubElement(room, 'students')
            for student in dct['students']:
                stud = ElemTree.SubElement(room_st, 'student')
                st_id = ElemTree.SubElement(stud, 'id')
                st_id.text = str(student['id'])
                st_name = ElemTree.SubElement(stud, 'name')
                st_name.text = student['name']

        tree = ElemTree.ElementTree(root)
        with open('updated_rooms.xml', 'w') as exp_file:
            tree.write(exp_file, encoding='unicode')


class ListsHandler:

    def __init__(self, st_path, room_path, format_type):
        self.st_path = st_path
        self.room_path = room_path
        self.format = format_type

        st_file_handler = FileHandler(self.st_path)
        self.students_list = st_file_handler.json_to_obj()

        rooms_file_handler = FileHandler(self.room_path)
        self.rooms_list = rooms_file_handler.json_to_obj()

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
