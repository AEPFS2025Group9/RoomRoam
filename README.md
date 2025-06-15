# RoomRoam
This repository belongs to Group 9 from Class B for "Anwendungsentwicklung mit Python" in Business Artifical Intelligence. The objectives of this project is the use of newly learned skills in Python on a tool for hotel reservations.

## Contributors
Benjamin Börlin - Classes, Debugging, User Stories, Data Visualization

Alex Suter - Classes, Debugging, Main User Stories

Jiapei Sun - Classes, Debugging, Main User Stories

Damian Martin - Classes, Debugging, DB User Stories, Data Access, User Interface

## 1. Introduction
Our hotel reservation system is made up of several modules that handle everything from managing hotels, rooms and their facilities, to processing bookings, payments, and user data. To keep things organised, the project is divided into different folders each focused on a specific part of the system. These include the user interface, business logic, data access, model classes, and the database. This structure helped us build the system in a clear and modular way.

## 2. System Architecture
RoomRoam is a hotel reservation system we developed in Python. We built it in a way that keeps things organised, clear, and easy to expand later if needed. To do that, we split the system into different modules, each taking care of a specific part of the overall functionality like handling hotel data, managing bookings, or storing guest information. All the data is stored in a local SQL database, and we kept a clean structure in the code to make development and teamwork easier.

### 2.1 What the System Is Made Of
#### Hotels and Rooms
* At the heart of the system is the part that manages hotels and their rooms. Each hotel has things like a name, location, and star rating, while rooms come with details such as type, price, and what facilities are included. We defined all this using Python model classes and linked them up with the database through a custom data access layer.
#### Bookings
* When guests book a room, their reservation goes through our booking module. This part checks whether rooms are available for the selected dates and saves all necessary information about the reservation. It also connects to the part of the system that creates an invoice for the booking so everything is logged and ready for confirmation.
#### Search
* Users can search for hotels based on their needs – like location, number of guests, or date range. The system helps filter the right results using these criteria. There’s also a review function where guests can leave feedback after their stay, which is saved and can be viewed later.
#### Admin
* Admins have access to tools for editing background data, like room types or available facilities. These changes go directly into the database without the need to adjust any code, so managing the system stays flexible.

### 2.2 Tools and Technologies We Used
#### Language and Database
We used Python to build the whole system because it’s straightforward and easy to work with in teams. For storing the data, we chose a simple local SQL database. Instead of using a full ORM like SQLAlchemy, we wrote our own data access classes to keep things more transparent.
#### PyCharm and GitHub
Most of the development was done in PyCharm. It made writing, testing, and navigating the code a lot easier. We also connected everything with GitHub, which we used regularly to keep track of code changes, collaborate through branches and pull requests, and review each other's work.
#### Deepnote for Testing and Validation
To make sure everything worked properly, we also used Deepnote. It allowed us to run parts of the system in notebooks, inspect the output, and test database operations on the fly. This was especially helpful for checking if search filters or booking logic were doing what they should. We also used it to quickly debug and test changes before pushing them to GitHub.

### 2.3 How We Organised the Project
We planned and tracked our work using a Kanban board, where we could easily move tasks through different stages like “to do”, “in progress”, or “done”. This helped us stay organised and see what was left to finish. If priorities shifted or something took longer than expected, it was easy to adapt and keep the team in sync.

### 3. Implementation
 
#### 3.1 Class Modell
To structure the data layer of our system, we used a class diagram from the very beginning as a blueprint for building our Python model classes. This diagram outlines all the core entities in the hotel reservation domain and their relationships, such as how hotels are linked to rooms, how guests make bookings, and how invoices are generated.
![image](https://github.com/user-attachments/assets/89df59ef-a535-40a5-9c4e-a662f7dae8e0)

While the class diagram provided a solid starting point, we made some adjustments during development to match technical requirements and simplify certain workflows. These changes included modifying relationships, refining method logic, and adapting class responsibilities so the system could run smoothly and meet all functional requirements.
Overall, using this visual model helped us plan the system more effectively and keep our codebase structured and consistent.

#### We used the given class structure in the folder model as it was mostly complete for the user storys.
 
Addtionally, we created the class *`review`* which is used by the guest to search for reviews of a hotel and to write a review as well.
The class contains the following attributes:
* review_id
* guest_id
* hotel_id
* rating
* comment
* review_date
 
#### 3.2 Business Logic
We created a dedicated folder for our business logic containing the different manager roles. These include:
 
* `admin_manager´: Provides methods to get information about bookings and create, udpate and remove hotels
* `booking_manager` : Provides methods to perform booking processes such as canceling bookings
* `invoice_manager` : Provdides methods to handle invoices like seeing the details of a specific invoice
* `master_data_manager` : Provides methods to create, update and delete roomtypes and facilities
* `review_manager` : Provides use hotel reviews such as creating a customer review
* `search_manager` : Provides methods to do searching activities such as sesarching for hotels in a city

### 4. Database Design
The hotel reservation system is backed by a relational database, structured according to a normalized schema that was provided by the instructors. This schema includes key entities such as Hotels, Guests, Rooms, Bookings, Invoices, and Facilities. While minor practical extensions (like seasonal pricing and review tracking) were introduced, we stayed true to the original model to maintain clarity and consistency.

#### 4.1 Database Initialization
The database is initialized at runtime through class-based data access layers. Each table (e.g., hotels, rooms, bookings, invoices, reviews) is created if it doesn't already exist, ensuring idempotent startup behavior. Review table creation, for instance, is explicitly triggered via:

ReviewDAL().create_table()

This ensures all necessary structures are in place before any guest or admin operations.

#### 4.2 User Stories and Database Operations

Each user story from the specification was implemented using clean database queries encapsulated in dedicated manager and DAL (Data Access Layer) classes.

Example User Stories and Corresponding Database Features:

* As a guest, I want to search for hotels in a specific city.
  → SQL joins on the hotels and addresses tables, exposed through SearchManager.

* As a guest, I want to leave a review after my stay.
  → A review entry is inserted into the reviews table using ReviewDAL.

* As an admin, I want to see occupancy rates by room type in my hotel.
  → A grouped SQL aggregation fetches booking counts per room type, optionally filtered by hotel. The result is visualized using matplotlib via:

AdminManager.get_room_type_summary_as_df(hotel_id)

* Optional Extensions:
  Dynamic pricing was implemented based on check-in month, affecting invoice generation logic.

#### 4.3 Extensibility and Data Visualization

To support analytical insights, we introduced functions that export booking data as pandas DataFrames. This enabled a visual dashboard (bar chart) showing room popularity per hotel or across all hotels, supporting admins in optimizing their room allocation strategy.

## 6. Reflection

Towards the final stage of our project, we noticed that our codebase was not fully aligned. Since tasks had been assigned individually, different interpretations of certain concepts had emerged. This resulted in discrepancies across classes and functions, which required a concerted effort to synchronize and standardize the codebase.

Another challenge we encountered was the frequent change of contributors working on the code. As different team members modified the project at various times, this sometimes led to misunderstandings or inconsistent implementations. This dynamic made it difficult to maintain a unified structure and caused occasional setbacks in the development process.

To tackle these issues, we also used large language models (LLMs) to assist with debugging. The LLMs helped us generate debugging code within our Deepnote notebook, which proved useful in identifying logical errors and inconsistencies that we had overlooked during our own code reviews.

Despite the initial struggles, we managed to harmonize our implementation. Through clear communication, continuous testing, and the strategic use of debugging tools, we were able to resolve all major issues. Now, the system functions as intended and reflects a well-integrated result of our combined efforts.

## 7. Deliverables
* Source Code and artifacts
  * Link to the Deepnote-Projekt, https://deepnote.com/workspace/Hotelreservierung-bb01673e-6ecf-43ff-a846-c2f58343e63b/project/Code-harmonization-4110b8bf-941b-4151-bec6-7a024162a31b/notebook/Alex-Neu-b22a3f42ed5b426499ee1c60d1a8674d
  * Link to the GitHub-Repository, 
  * Link to the Project Board, Link to Kanban Board: https://github.com/orgs/AEPFS2025Group9/projects/2
* Link to presentation video, https://fhnw365-my.sharepoint.com/:v:/g/personal/benjamin_boerlin_students_fhnw_ch/ERXoAqbLbtpGsc7m_F9onroBml1e6k0jo7-y9LTyHjqdfQ?e=CVNTQp


## Help
*Link to instructions for formatting this README file: https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax*

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
