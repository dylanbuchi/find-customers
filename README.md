# Customers REST API
### An API to list customers and get them by id
-------
This project uses the MapBoxAPI, to get the customers's city latitude and longitude:
- https://docs.mapbox.com/api/overview/ 

The project already has the database so there is no need to create an API key, so you can skip part **5** and **6**
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