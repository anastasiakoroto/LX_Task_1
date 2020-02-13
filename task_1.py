import argparse
import os

from list_handler import ListsHandler


class ArgParser:

    def create_parser(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('path_to_students_file', help='Path to students file')
        parser.add_argument('path_to_rooms_file', help='Path to rooms file')
        parser.add_argument('format', help='Format of output file')
        return parser

    def is_valid_file(self, filepath):
        if not os.path.exists(filepath):
            return False
        return True

    def run_command_line(self):
        parser = self.create_parser()
        args = parser.parse_args()
        students_file_path = args.path_to_students_file
        rooms_file_path = args.path_to_rooms_file
        output_format = args.format
        if self.is_valid_file(students_file_path) and self.is_valid_file(rooms_file_path):
            list_handler = ListsHandler(students_file_path, rooms_file_path, output_format)
            list_handler.write_updated_rooms_to_file()


if __name__ == '__main__':
    # students = '/Users/Anastasia/PycharmProjects/LeverX Course/task_1/input_files/students.json'
    # rooms = '/Users/Anastasia/PycharmProjects/LeverX Course/task_1/input_files/rooms.json'

    # obj = ListsHandler(students, rooms, 'json')
    # obj.write_updated_rooms_to_file()
    # obj_2 = ListsHandler(students, rooms, 'xml')
    # obj_2.write_updated_rooms_to_file()

    arg_parser = ArgParser()
    arg_parser.run_command_line()
