import json
import xml.etree.ElementTree as ElemTree


class FileConverter:
    def open_and_convert_to_object(self, path_to_file):
        raise NotImplementedError


class FileWriter:
    def write(self, rooms_list):
        raise NotImplementedError


class JSONConverter(FileConverter):
    def open_and_convert_to_object(self, path_to_file):
        try:
            with open(path_to_file, 'r', encoding='utf-8') as json_file:
                obj = json.load(json_file)
                return obj
        except FileNotFoundError:
            raise FileNotFoundError(f"Unfortunately, file with path '{path_to_file}' doesn't exist. "
                                    f"Please, check the path to each required file.")
        except IsADirectoryError:
            raise IsADirectoryError("Unfortunately, you didn't point the name of file. "
                                    "The program needs it to continue.")
        except PermissionError:
            raise PermissionError(f"Unfortunately, access to file with path {path_to_file} denied.")


class JSONWriter(FileWriter):
    def write(self, rooms_list):
        with open('output_files/updated_rooms.json', 'w') as json_file:
            json.dump(rooms_list, json_file)
        print(f'Updated list of rooms was added to output_files/updated_rooms.json successfully!')


class XMLWriter(FileWriter):
    def _parse_rooms_to_xml(self, rooms_list):
        root = ElemTree.Element('rooms')
        for room_dictionary in rooms_list:
            room = ElemTree.Element('room')
            root.append(room)
            room_id = ElemTree.SubElement(room, 'id')
            room_id.text = str(room_dictionary.get('id'))
            room_name = ElemTree.SubElement(room, 'name')
            room_name.text = room_dictionary.get('name')
            students_of_room = ElemTree.SubElement(room, 'students')
            for student in room_dictionary.get('students'):
                student_info = ElemTree.SubElement(students_of_room, 'student')
                student_id = ElemTree.SubElement(student_info, 'id')
                student_id.text = str(student.get('id'))
                student_name = ElemTree.SubElement(student_info, 'name')
                student_name.text = student.get('name')

        tree = ElemTree.ElementTree(root)
        return tree

    def write(self, rooms_list):
        xml_tree = self._parse_rooms_to_xml(rooms_list)
        with open('output_files/updated_rooms.xml', 'w') as xml_file:
            xml_tree.write(xml_file, encoding='unicode')
            print('Updated list of rooms was added to output_files/updated_rooms.xml successfully!')
