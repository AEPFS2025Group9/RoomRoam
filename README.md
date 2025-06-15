# RoomRoam
This repository belongs to Group 9 from Class B for "Anwendungsentwicklung mit Python" in Business Artifical Intelligence. The objectives of this project is the use of newly learned skills in Python on a tool for hotel reservations.

## Contributors
Benjamin Börlin - Classes, Debugging, User Stories, Data Visualization

Alex Suter - Classes, Debugging, Main User Stories

Jiapei Sun - Classes, Debugging, Main User Stories

Damian Martin - Classes, Debugging, DB User Stories, Data Access

## 1. Introduction
Our hotel reservation system is made up of several modules that handle everything from managing hotels, rooms and their facilities, to processing bookings, payments, and user data. To keep things organised, the project is divided into different folders each focused on a specific part of the system. These include the user interface, business logic, data access, model classes, and the database. This structure helped us build the system in a clear and modular way.

## 2. System Architecture

RoomRoam is a hotel reservation system we developed in Python. We built it in a way that keeps things organised, clear, and easy to expand later if needed. To do that, we split the system into different modules, each taking care of a specific part of the overall functionality like handling hotel data, managing bookings, or storing guest information. All the data is stored in a local SQL database, and we kept a clean structure in the code to make development and teamwork easier.

2.1 What the System Is Made Of

Hotels and Rooms
At the heart of the system is the part that manages hotels and their rooms. Each hotel has things like a name, location, and star rating, while rooms come with details such as type, price, and what facilities are included. We defined all this using Python model classes and linked them up with the database through a custom data access layer.

Bookings
When guests book a room, their reservation goes through our booking module. This part checks whether rooms are available for the selected dates and saves all necessary information about the reservation. It also connects to the part of the system that creates an invoice for the booking so everything is logged and ready for confirmation.

Search
Users can search for hotels based on their needs – like location, number of guests, or date range. The system helps filter the right results using these criteria. There’s also a review function where guests can leave feedback after their stay, which is saved and can be viewed later.

Admin
Admins have access to tools for editing background data, like room types or available facilities. These changes go directly into the database without the need to adjust any code, so managing the system stays flexible.

2.2 Tools and Technologies We Used

Language and Database
We used Python to build the whole system because it’s straightforward and easy to work with in teams. For storing the data, we chose a simple local SQL database. Instead of using a full ORM like SQLAlchemy, we wrote our own data access classes to keep things more transparent.

PyCharm and GitHub
Most of the development was done in PyCharm. It made writing, testing, and navigating the code a lot easier. We also connected everything with GitHub, which we used regularly to keep track of code changes, collaborate through branches and pull requests, and review each other's work.

Deepnote for Testing and Validation
To make sure everything worked properly, we also used Deepnote. It allowed us to run parts of the system in notebooks, inspect the output, and test database operations on the fly. This was especially helpful for checking if search filters or booking logic were doing what they should. We also used it to quickly debug and test changes before pushing them to GitHub.

2.3 How We Organised the Project
We planned and tracked our work using a Kanban board, where we could easily move tasks through different stages like “to do”, “in progress”, or “done”. This helped us stay organised and see what was left to finish. If priorities shifted or something took longer than expected, it was easy to adapt and keep the team in sync.

## Project
Link to Kanban Board: https://github.com/orgs/AEPFS2025Group9/projects/2


## How to get started with RoomRoam on a Deepnote Notebook

1. Configure Working Directory
```
/Hotelreservierungssystem (RoomRoam)
```

2. Import standard libraries
```
import shutil
import os
```

3. Import pandas
```
import pandas as pd
```

4. Import py files from our directory
```
import model
import data_access
import business_logic
import ui.input_helper as input_helper
```

5. Copy original database for a fresh start
```
source = "database/hotel_reservation_sample.db"
db_file = "database/using_db.db"
shutil.copyfile(source, db_file)
```
 
6. Set environment variable
```
os.environ["DB_FILE"] = db_file
```

7. Configure display sattings for Data Frames
```
pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)
pd.set_option("display.max_colwidth", None)
```

8. Import Managers
```
from business_logic.admin_manager import AdminManager
from business_logic.booking_manager import BookingManager
from business_logic.master_data_manager import MasterDataManager
from business_logic.search_manager import SearchManager
```


## Reflection
Towards the finalizing stage of our project we have noticed, that our code was not totally aligned. Since we have assigned tasks individually some concepts have been used differently and we had to synchronize our classes and functions. For some of the debugging we have used LLMs to help us generate debugging code in our Notebook. This gave us the possibility to find mistakes or inconsistencies throughout our code.

## Deliverables
* Source Code and artifacts
  * Link to the Deepnote-Projekt
  * Link to the GitHub-Repository, 
  * Link to the Project Board 
* Link to presentation video


## Help
*Link to instructions for formatting this README file: https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax*
