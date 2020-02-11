# TASK 1
## About project
The program:
* merges `students_list` and `rooms_list` into list, which contains info about rooms and students in each room;
* serializes this list to JSON or XML format.

## How to run
To run the program from PyCharm you should open script `task_1.py` and create an object of `ListHandler` type and not to 
forget about parameters: _path_to_students_json_, _path_to_rooms_json_, _output_format_. Then call method 
`write_updated_rooms_to_file`.

_Example:_
```
new_object = ListHandler(path_to_students, path_to_rooms, 'json')
new_object.write_updated_rooms_to_file()
```
