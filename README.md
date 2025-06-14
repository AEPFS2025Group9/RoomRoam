# RoomRoam
This repository belongs to Group 9 from Class B for "Anwendungsentwicklung mit Python" in Business Artifical Intelligence. The objectives of this project is the use of newly learned skills in Python on a tool for hotel reservations.

## Contributors
Benjamin Börlin - Classes, Debugging, User Stories, Data Visualization

Alex Suter - Classes, Debugging, Main User Stories

Jiapei Sun - Classes, Debugging, Main User Stories

Damian Martin - Classes, Debugging, DB User Stories, Data Access


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
