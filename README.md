# AirBnB_clone

## Description
This is the AirBnB clone project, called The Holberton B&B as part of [Holberton School](https://holbertonschool.com) full stack training. The goal of the project is to deploy on the server a simple copy of the AirBnB website. The project is divided into following parts:
- A Front-end application for user interactions.
- An API for front-end and the backend integration.
- A database that stores the data.
- A command interpreter to manipulate data without a visual interface for development and debugging.

### Part 1: Create a Command Interpreter to manage your AirBnB objects that does following:
- Supports basic help, quit, exit and enter commands.
```
help
ctrl+d
quit
exit
enter
```
- Create a new object (ex: a new User or a new Place).
```
create <classname>
```
- Retrieve an object from a file, a database etc.
```
show <classname>
all
<classname>.count
<classname>.show
```
- Do operations on objects (count, compute stats, etc.).
```
<classname>.count
```
- Update attributes of an object.
```
update <classname> <id> <attribute_to_update> <updating_value>
```
- Destroy an object.
```
destroy <classname> <id>
```
![Alt text](https://github.com/guptaNswati/AirBnB_clone/blob/master/screenshots/cmi.png)
### Styling and Specifications
Programs styling and formatting is based on pep8 style guide and is checked as:
```
pep8 file.py
```

### Compilation
All programs must run with pyton 3.4.3 on Ubuntu 14.04.
To run the command interpreter:
```
./console.py or python3 console.py
```
To run the unittests:
```
python3 -m unittest discover tests
or to run for a specific file:
python3 -m tests.test_file.py
```

### Directories and Files
- console.py is the entry point of command interpreter.
- /models - contains all data(objcet) classes.
- /models/engine - contains all storage classes.
- /tests - contains all unit tests for classes.
- /tests/test_models/test_engine - contains unit tests for all storage classes.
- /screenshots - contains screenshots of sample output.


## Authors
- **Richard Sim**, \<100@holbertonschool.com>
- **Swati Gupta**, \<77@holbertonschool.com>