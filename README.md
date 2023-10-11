# AirBnB Clone Project

## Project Description

This project aims to create a simplified AirBnB-like system with a command-line interface (CLI) for managing objects. The project is designed to help users create, retrieve, update, and destroy objects while providing storage capabilities and serialization to JSON.

## Features

- Object creation (e.g., User, State, City, Place)
- Object retrieval from storage
- Object updates
- Object deletion
- Data storage using JSON

## How to Run the Command Interpreter

### Interactive Mode

To run the command interpreter in interactive mode, follow these steps:

1. Clone this repository to your local machine.
git clone https://github.com/yourusername/airbnb-clone.git

## Navigate to the project directory
cd airbnb-clone

# Start the command interpreter in interactive mode
./console.py

# You will be presented with the (hbnb) prompt, and you can enter commands interactively
(hbnb) help

# Non-Interactive Mode
# Execute a single command through the command interpreter
echo "help" | ./console.py

# You will receive the output directly
(hbnb) help

# You can also provide input from a file
cat test_help | ./console.py

# The command interpreter will process the input from the file
(hbnb) help

# Running Unit Tests
# To run the unit tests for the project
python3 -m unittest discover tests

# Contributors
# 
Tshegofatso Seane (@tshegofatsoseane98)
Omphile Gopane (@Timothy Grey 1005)


