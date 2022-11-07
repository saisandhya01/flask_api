# flask_api

API server using Flask to fetch bank list and their branches. Site hosted in [https://flask-bank-list-app.herokuapp.com/](https://flask-bank-list-app.herokuapp.com/)

Data used from here: [https://github.com/Amanskywalker/indian_banks](https://github.com/Amanskywalker/indian_banks)

## API endpoints

- ```/``` : Fetch the list of all banks.
- ```/{ifsc}``` : Fetch details of the bank with IFSC code as parameter passed in the route.
- ```/bank/{id}```: Fetch the list of all branches of a bank with the particular id passed in the route

## Usage

- Install Python3
- Install pip 
- Go to terminal 
- ```python app.py```

