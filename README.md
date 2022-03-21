# Boilerplate backend flask

This is a basic boilerplate which provides a backend starter pack.

It use Python and the following technologies:

* Flask
* Pytest
* Flasgger

## How to install the boilerplate

At first, download the bundle after that and create a virtual environment and activate it (UNIX systems):
```{bash}
$ python3 -m venv venv
$ source venv/bin/activate
```

If you are using windows you should use the following commands:
```{windows}
$ python -m venv venv
$ venv\Scripts\activate
```

After that, install the needed packages with:
```{bash}
pip install -r requirements.txt 
```

### Run server
To run the server you need to use:
```{bash}
python app.py
```

### Run tests
To run the tests you have to use the following command:
```{bash}
python -m pytest -vvv
```

# WSGI

To run the WSGI server run:
```{bash}
uwsgi --ini uwsgi.ini
```

### Config WSGI

[Follow this tutorial](https://www.digitalocean.com/community/tutorials/como-hacer-funcionar-aplicaciones-de-flask-con-uwsgi-y-nginx-en-ubuntu-18-04-es)

[Read this](https://stackoverflow.com/questions/15878176/uwsgi-invalid-request-block-size)

[And this](https://learntutorials.net/es/flask/topic/4637/implementando-la-aplicacion-flask-usando-el-servidor-web-uwsgi-con-nginx)


### Run in Google Cloud

[![Run on Google Cloud](https://storage.googleapis.com/cloudrun/button.svg)](https://console.cloud.google.com/cloudshell/editor?shellonly=true&cloudshell_image=gcr.io/cloudrun/button&cloudshell_git_repo=https://github.com/mrverde/tfm_backend.git)