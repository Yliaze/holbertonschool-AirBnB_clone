# HBNB AirBnB Clone

HBNB is a command line interface for managing your AirBnB objects.

## Description

This project is a clone of AirBnB on a command line interface that allows the user to manage various AirBnB objects, including places, users, cities, and more. This project is written in Python 3, making use of the cmd module to manage the command line interface.

## Requirements

- Python 3.5+
- PEP 8 - Style Python Code

## Installation

Ensure you have Python 3 installed. Then, simply clone the repository.

```bash
git clone https://github.com/Yliaze/holbertonschool-AirBnB_clone.git
```

## How to start

To start the program, navigate to the directory containing `console.py` and run the file with Python 3.

```bash
python3 console.py
```

## Usage

The command interpreter allows you to manage the objects of your project.

### Commands

- `quit` or `EOF` to exit the program.
- `create <class name>` to create a new instance of the class.
- `show <class name> <id>` to display the specific instance based on the class name and id.
- `destroy <class name> <id>` to destroy a specific instance based on the class name and id.
- `all <class name>` or just `all` to display all instances of a class or all instances of every class.
- `update <class name> <id> <attribute name> <attribute value>` to update an instance based on the class name and id by adding or updating attribute.

## Examples

To create a new object:

```bash
create BaseModel
```

To display a specific instance:

```bash
show BaseModel 1234-1234-1234
```

## Testing

Tests for this project are contained in the `tests` directory, and can be run using the Python unittest module. For example, to run all tests for the BaseModel class, use:

```bash
python3 -m unittest tests/test_models/test_base_model.py
```

## Structure

```
.
├── AUTHORS
├── README.md
├── console.py
├── file.json
├── models
│   ├── __init__.py
│   ├── amenity.py
│   ├── base_model.py
│   ├── city.py
│   ├── engine
│   │   ├── __init__.py
│   │   └── file_storage.py
│   ├── place.py
│   ├── review.py
│   ├── state.py
│   └── user.py
└── tests
    ├── __init__.py
    └── test_models
        ├── __init__.py
        ├── test_amenity.py
        ├── test_base_model.py
        ├── test_city.py
        ├── test_engine
        │   ├── __init__.py
        │   └── test_file_storage.py
        ├── test_place.py
        ├── test_review.py
        ├── test_state.py
        └── test_user.py
```

## Credits

This project was created by :
Descombes Simon : https://github.com/SimonDesc
Ralliard Valentin : https://github.com/Pizzayolow
Alazet Benjamin : https://github.com/Yliaze
