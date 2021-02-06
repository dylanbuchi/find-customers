# Customers REST API
### An API to list customers and get them by id

## Demo:
<img src=https://user-images.githubusercontent.com/52018183/107127881-ef5afc80-6897-11eb-8ff6-0bc4377c2bd5.gif with=400 height=400/>

-------

This project uses the MapBox API, to get the customers's city latitude and longitude and the map images:
- https://docs.mapbox.com/api/overview/ 

The project has already everything set up so there is no need to create an API key, you can skip step **5** and **6**

## Running the Project Locally

**1**. Clone the repository to your local machine:

```bash
git clone https://github.com/dylanbuchi/customers-rest-api.git
```
**2**. Go to the root directory of the project:

```bash
cd customers-rest-api/
```
**3**. Create a python virtual environment and activate it:

```bash
python -m venv venv
source venv/bin/activate
```
**4**. Install the requirements file:
  
```bash
pip install -r requirements.txt
```

**5**. Create the database:
```bash
python manage.py makemigrations
python manage.py migrate
```

**6**. Load the customers file into the database:
```bash
python manage.py load_customers --path ./data/customers.csv
``` 



**7**. Run the development server:

```bash
python manage.py runserver
```

The project will be available at http://127.0.0.1:8000/

```bash
You can access a customer by id with the user interface on the home page or like this: http://127.0.0.1:8000/api/v1/customers/{id_number}/
```
