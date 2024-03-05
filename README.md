# Odoo dockerized build

## Description

This is a Dockerized build for Odoo ERP system project

## Pre-requirements

This project built with Docker. To build and run it on your machine you
will need to install [Docker
Engine](https://docs.docker.com/engine/install/) and [Docker
Compose](https://docs.docker.com/compose/install/).

## Settings

### Local

Find your local envs file in `.envs/.local/` folder

Also you can find local Odoo config file in `compose/local/odoo/` folder
named `odoo.conf`

This project is ready to run locally

## Basic Commands

Local Build, Migrate and Run

To build the application go to project root and run:

    $ docker-compose build

To init Odoo Database go to project root and run:

    $ docker-compose run --rm odoo /init

To run built application go to project root and run:

    $ docker-compose up

To open running application just open [localhost](http://localhost:8069)

Use username **admin** and password **admin**
