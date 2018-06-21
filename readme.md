# Hacker News Search Engine

Query Hacker News public dataset through BigQuery API.

## Getting Started
* The project is built with Python and Django framework
* Python and Django is required installation to run the code locally. Run the bow code to check Django version
    ```
    python -m django --version
    ```
### Installing
* clone the repository
* In the command line, go into the main folder
* Create an environment
    ```
    conda create --name myenv
    ```
* Activate an environment, and install all dependencies 
    ```
    pip install -r requirements.txt
    ```
* In the main folder, run the development server
    ```
    python manage.py runserver
    ```

### Project Structure
* Django project - news
* Django app in the above project - search engine

### Explore Dataset

* title, datatype is string,  max is 198 characters, min is 0 characters
* text, datatype is string, max is 27405 characters, min is 0 characters
* date, datetype is timestamp (human readable time in UTC), max is 2015-10-13 08:44:34.000 UTC, min is 2006-10-09 18:21:51.000 UTC

### Read the query results from BIgQueryAPI
* Create a project in Google Cloud platform Console and enable BigQuery API
* Create a service account and give the role 
* Install python google cloud client library
* full-text searching:
    Case insensitive regex REGEXP_CONTAINS-3.4s Lower-3.9
