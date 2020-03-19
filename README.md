# StudentList
List of students implementation in python, django

# First
1. git clone ` https://github.com/DenisOstr/StudentList `
2. Install PostgreSQL with pgAdmin

# Run application
1. Run the following commands (in cmd):
   - ` python manage.py makemigrations `
   - ` python manage.py migrate `
2. Open pgAdmin and find the database named ` students `
3. Go to: 
   - ` students -> Schemas -> public -> Tables `
4. Import the all data from file ` studentList.csv ` into ` Students_students ` table:
   - Click right mouse button on ` Students_students ` and select ` Import/Export... `
   - Then import the ` studentList.csv ` file.
5. Open the ` Students_students ` table with the right mouse button and select ` View/Edit Data > All Rows `.
6. Finally, run local server the following command:
   - ` python manage.py runserver `
7. Open in browser: ` localhost:8000 `

# Demo
> Demo application on Heroku: ` [Student List Application](http://studentslists.herokuapp.com) `

# Author
Denis Ostrovsky
 
# License
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://github.com/DenisOstr/StudentList/blob/master/LICENSE)
> © Denis Ostrovsky
