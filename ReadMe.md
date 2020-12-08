# Library of Ruina Fanpage Website
This is the project dedicated to storing information on Library of Ruina. All the requirements should be available in requirements.txt

- Do note that you will need to make your own database. 
  - Currently the database used in the settings.py is postgres. As a demo, you could delete that part out and replace it with sqlite3
- Type in command:
  - pip install requirements.txt
  - python3 manage.py makemigrations
  - python3 manage.py migrate
- To run server:
  - python3 manage.py runserver


This is the code for the website: [aeonmoon.h](http://aeonmoon.herokuapp.com/).

Queries used:
- Get a list of Cards grouped in coressponding Guest Groups. Each Guest groups grouped in their coressponding Rank group. 
- Get a count of Cards in each Guest Groups
- Get a list of Decks
- Get a list of Guests grouped in Guest
- Get a list of Characters
- Get a list of Pages grouped in their own Guest groups
- Get a list of guides
- Get all the available information in Cards with corresponding Office
- Get all the available information in Decks with corresponding Cards inside
- Get all the available information in a Page with corresponding Guests/Office
- Get all the available information in Guides
- Get all the available information on Characters with corresponding Page
- Allow users to make their own decks through choosing their own cards.


Users are allowed to:
- Make their own decks
- Make their own Guides with the available decks
- Browse through Cards
- Browse through Decks
- Browse through Guests
- Browse through Characters 
- Browse trhough Guides
