# SQEEDER
SQEEDEL is Python3 simple command line app to convert SQL insert statement to the Laravel Seeder. This project was built because sometime I am very tired to manually create seeder and add the insert statement of pre-use data in laravel seeder. 

## Usage
To use the app simple clone the repository into local or just donwload the zip file extract it and run with. Make sure you already installed python 3 on your machine.
```python
python3 main.py -f <sqlfile.sql> -o <theseederfile.php>
```
If youre in windows machine and already installed python 3 just use `python` instead of `python3`.
### Available Command
Currently, there is only two command :) 
1. `python3 main.py -h` for help.
2. `python3 main.py -f <sqlfile.sql> -o <theseederfile.php>` for convert the sql.

## How it works
The app work by parsing the sql file line by line and the get the table structure and the data to insert and covert it to array. The acceptence sqli statement of the sql file is : 
```sql
INSERT INTO users (id, name, email) VALUES (1, 'John Doe', 'john@example.com'),
(2, 'Doe John', 'doe@example.com'),
(3, 'Marie Doe', 'marie@example.com'),
(4, 'Marie John', 'mriejohn@example.com');
```
Because the app read the sql file make sure there is no empty line before or after the insert statement.

## Depedencies
The app using two builtin library of python : 
1. sys
2. getopt
That means, we don;t need to install any library to use the app.

## Contributing
Any contributing is allowed to the project to make it better.

## Licence
This project is under GNU General Public Licence.