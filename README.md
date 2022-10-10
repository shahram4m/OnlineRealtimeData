# Elements assignment
<p align="center">
  <img src="https://assets.website-files.com/5cd40c117f1ff810bf42803b/6113f5151e62af8a73e8c924_logo-motion-black.svg">
</p>
elements is a simple rest api application written by Python3.x & Django 4.x This project is for present.

##  Demo
[Final project preview.](in progress)

## Guidance on implementation strategy:
I designed a table to store file data and a table to store file addresses.
In the first stage:
I validate the file address, then, in the first run of the app, I get the data in a partitioned form by the Panda library and save it in the table.
I have created a schedule in the program, the settings of which I get the data every 24 hours,
The mechanism is to delete previous information and insert new information.

The user can get the data through the following API,
The information received by the user is cached for one hour for better speed and efficiency, this time can be adjusted.

Paginated to send a conditional parameter on the title and description fields
Getting paged information:
```sh
  http://127.0.0.1:801/information/getAllItems/?limit=5&offset=5
```

Getting paginated information with sending the condition:
```sh
http://127.0.0.1:801/information/getByPredicate/?limit=5&offset=0&description=Description 1&title=1
```

At any time, the user can create a new address to receive the file, and the program will receive the information from the last entered address at the next schedule.
It is possible with this address:
```sh
http://127.0.0.1:801/fileInformation/create/
http://127.0.0.1:801/fileInformation/getAllItems/
```

In this program, I have created the following tests:
1. Test the method of receiving paginated information
2. Test receiving paged information by sending a condition
3. Test to validate the address of the file that is available and has the content of the CSV file
4. Test for the content of the file to be full
5. Test to register the address of the new file
6. Test to get the list of file addresses
You can run the tests by running the following command
```sh
Python manage.py test
```


## Technologies used in this course

This project and video series are best practices for Backend Engineering with Python and Django and the most common technologies every backend engineer should know. Technologies used in this course are listed below.
-   [Python 3.x](https://www.python.org/) - Programming Language
-   [Django 4.1.x](https://www.djangoproject.com/) - Powerful Web Framework
-   [Django Rest Framework](https://www.django-rest-framework.org/) - Web API's
-   [Jinja2](https://jinja.palletsprojects.com/en/2.11.x/) - Template Engine
-   [Gunicorn](https://gunicorn.org/) - WSGI HTTP Server
-   [PostgreSQL](https://www.postgresql.org/) - PostgreSQL Database
-   [NginX](https://www.nginx.com/) - High performance web server
-   [Docker](https://www.docker.com/) - Container Platform
-   [GitHub](https://github.com/) - Version Control
-   [TravisCI](https://travis-ci.org/) - Continues Integration and Deployment
-   [Postman](https://www.postman.com/) - API Testing
-   [Pandas](https://www.Pandas.pydata.org/) - Get csv file 


##  Installation
First **clone** or **download** this project.
```sh
$ git clone https://github.com/shahram4m/elements.git
```
Then create **docker network** and **volumes** as below.

```sh
$ docker volume create elements_postgresql
$ docker volume create elements_static_volume
$ docker volume create elements_files_volume
```
```sh
$ docker network create nginx_network
$ docker network create elements_network
```
You need to create .env file in the project root file with default values.
```sh
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=postgres
```
Now run django and postgresql and nginx container with **docker-compose**.
```sh
$ docker-compose up -d
```
You can see elements web page on http://localhost:801, Template and API's are accessable by  docker containers which you can see with below command.
```sh
$ docker ps -a
```
**Output** should be like this.
```sh
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                    NAMES
b4f0baec6839        elements-nginx      "/docker-entrypoint.…"   18 hours ago        Up 2 hours          0.0.0.0:801->80/tcp      elements-nginx-1
a01ccd01ee37        elements-elements   "sh -c 'python manag…"   2 hours ago         Up 2 hours          0/tcp   elements         elements-elements-1
3f5cd0bf7057        postgres:12         "docker-entrypoint.s…"   2 hours ago         Up 2 hours          0.0.0.0:5432->5432/tcp   elements_postgresql
```
**nginx** container as common web server, **elements** container as django application and **elements_postgresql** as postgreSQL database container.

## Contributing
Contributions are  **welcome**  and will be fully  **credited**. I'd be happy to accept PRs for template extending.

## License
This project is licensed under the MIT License - see the [LICENSE](https://github.com/shahram4m/elements/main/LICENSE) file for details

