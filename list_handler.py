from file_handlers import JSONConverter, JSONWriter, XMLWriter
from task_1 import ArgParser


class ListsHandler:

    def __init__(self):
        self.arg_parser = ArgParser()
        students_path, room_path, self.format = self.arg_parser.get_arguments()

        self.xml_writer = XMLWriter()
        self.json_converter = JSONConverter()
        self.json_writer = JSONWriter()
        self.students_list = self.json_converter.open_and_convert_to_object(students_path)
        self.rooms_list = self.json_converter.open_and_convert_to_object(room_path)

    def _add_students_to_rooms(self, rooms_dict, students_list):
        for student in students_list:
            student_id_name = student.copy()
            student_id_name.pop('room')
            rooms_dict[student.get('room')]['students'].append(student_id_name)
        return rooms_dict

    def get_rooms_and_students_list(self):
        rooms_dict = {}  # key - room_id, value - list of room info
        for room in self.rooms_list:
            rooms_dict[room.get('id')] = {'id': room.get('id'), 'name': room.get('name')}
            rooms_dict[room.get('id')].setdefault('students', [])
        rooms_dict = self._add_students_to_rooms(rooms_dict, self.students_list)
        room_list = list(rooms_dict.values())
        return room_list

    def write_updated_rooms_to_file(self):
        updated_room_list = self.get_rooms_and_students_list()
        if self.format == 'json':
            self.json_writer.write(updated_room_list)
        elif self.format == 'xml':
            self.xml_writer.write(updated_room_list)
        else:
            print(f'There are no functionality for {self.format} format. Sorry :c\nBut you can choose json/xml c:')


if __name__ == '__main__':
    list_handler = ListsHandler()
    list_handler.write_updated_rooms_to_file()
