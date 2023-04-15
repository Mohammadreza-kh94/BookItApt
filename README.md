# Book It Apartment

A `Django` web-based application that allows users to book and manage apartment reservations.

![](./static/Screen%20Recording%202023-04-15%20at%2014.05.28.gif)

## Requirements:

| Requirement | Specification          |
| ----------- | ---------------------- |
| OS          | Ubuntu 18.04 or higher |
| Language    | Python                 |
| Interpreter | Python 3.8+            |

## Local Development QuickStart:

### - Using docker-compose:

Dependencies:

- `docker` and `docker-compose`

  ```bash
  # install
  $ git clone https://github.com/Mohammadreza-kh94/BookItApt.git
  $ cd BookItApt

  # configure (the defaults are fine for development)
  $ edit `.env.sample` and save as `.env`

  # run it
  $ docker-compose up --build
  ```

  Once it's done building and everything has booted up:

  - Access the app at: [http://localhost:8000](http://localhost:8000)

### - Running locally

- Dependencies:

  - Linux system
  - Python 3.8+
  - virtualenv
  - PostgreSQL

- Installation

  ```bash
  # install
  $ git clone https://github.com/Mohammadreza-kh94/BookItApt.git
  $ cd BookItApt
  $ virtualenv -p /path/to/python3 venv
  $ source venv/bin/activate
  $ pip install -r requirements.txt

  # configure
  $ edit `.env.sample` and save as `.env`

  # run db migrations
  $ python manage.py migrate

  # backend dev server:
  $ python manage.py runserver
  ```

## TODO:
- Implement a user management system to allow for user authentication, authorization, and user profile management
- Fix the bug that allows users to reserve an estate for conflicting dates
- Add a filtering feature on the attributes of each estate