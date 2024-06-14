# Gacha App
A rudimentary version of the gacha system for Honkai: Star Rail without the summon animation and way simpler design. It does carry the soft pity and hard pity of the system for 5 stars, so users can experience the summoning without using currency on the actual game. Main difference is that I did not include the 3 stars and pity for 4 stars, so you would only get 4 stars until hitting a 5 star.

## Technologies used:
* Javascript (front-end code)
* Python (back-end)
* React (handling of the front-end)
* HTML, CSS

## Features:
* Banner:
![Banner](/static/Banner.png)
    * Starts on Seele banner as it was originally the first limited 5 star banner of HSR
    * Has three methods of interacting with the banner; 1x summon, 10x summon, and a drop down menu in the top left corner
![Drop Down Menu](/static/menu.png)
    * Shows names of the various limited 5 stars up to Robin, so user can change the banner to pull for the limited 5 star they desire
![Banner Change](/static/banner-change.png)
    * Changed to banner of 5 star selected from the drop down menu
* 1x Summon:
![1x Summon page](/static/summon.png)
    * You would see one img of a 4 or 5 star for the single summon
    * To return to banner, user just has to click anywhere on the page

* 10x Summons:
![10x Summons page](/static/summons.png)
    * You would see two rows of 5 imgs of 4 or 5 star characters for the 10x summons
    * User would need to click anywhere on the page to return to the banner

## Instructions on how to run a cloned repo
If a user wishes to try this app out on their own device, then there is some requirements needed to run this as I did, or equivalents:
* Programs used (may use equivalents if similar):
    * Visual Studio Code
    * Git

* Steps to install:
    * clone repo: git clone {insert github repo link of project}
    * create a virtual environment with python version 3.12.2 
    * at the root of the directory (where you'd see the public, server, and static folders, and other files), open terminal (I used a Git Bash terminal) and run pip install requirements.txt to install all dependencies needed for Python
    * also run npm install to install all dependencies listed in the package.json

* To Setup and Run App:
    * Setup two terminals as to run this app, you'd need to have one terminal run 'Python backend/server.py' to run the backend, and the other terminal run 'npm start' to run the React frontend
    * Once 'npm start' finishes, a tab on your browser should automatically open allowing you to start using the app