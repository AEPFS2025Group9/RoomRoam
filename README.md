# RoomRoam
This repository belongs to Group 9 from Class B for "Anwendungsentwicklung mit Python" in Business Artifical Intelligence. The objectives of this project is the use of newly learned skills in Python on a tool for hotel reservations.

## Contributors
Benjamin Börlin - Project Board, Classes, Debugging, Data Visualization

Alex Suter - Classes, Debugging, User Stories

Jiapei Sun - Classes, Debugging, User Stories

Damian Martin - Classes, Debugging, Data Access


## Project
Link to Kanban Board: https://github.com/orgs/AEPFS2025Group9/projects/2


## How to get started with RoomRoam on a Deepnote Notebook

1. Import standard libraries

     **import shutil
   
     import os**


3. Import pandas

     **import pandas as pd**


5. Import py files from our directory

     **import model

     import data_access

     import business_logic

     import ui.input_helper as input_helper**


7. Copy original database for a fresh start

     **source = "database/hotel_reservation_sample.db"

     db_file = "database/using_db.db"

     shutil.copyfile(source, db_file)**

 
9. Set environment variabe

     **os.environ["DB_FILE"] = db_file**


11. Configure display sattings for Data Frames

     **pd.set_option("display.max_rows", None)

     pd.set_option("display.max_columns", None)

     pd.set_option("display.width", None)

     pd.set_option("display.max_colwidth", None)**


13. Import Managers

     **from business_logic.admin_manager import AdminManager

     from business_logic.booking_manager import BookingManager

     from business_logic.master_data_manager import MasterDataManager

     from business_logic.search_manager import SearchManager**



## Deliverables
* Source Code und Artefakte
  * Link zum Deepnote-Projekt mit allen ausführbaren Notebooks, Dateien und der 
endgültigen Datenbank,  
  * Link zum GitHub-Repository, 
  * Link zu einer Projekt Board 
* Dokumentation/Bericht (Link zu GitHub Markdown-Datei(en)) 
* Link zum Präsentationsvideo (das auf Microsoft Stream, SWITCHtube oder YouTube 
gehostet wird; eingeschränkter/ungelisteter Zugang möglich und empfohlen)


## Help
*Link to instructions for formatting this README file: https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax*
