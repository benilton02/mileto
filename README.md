# mileto

# Run Container 

On Liunx
```sh
docker-compose up --build
```

# Create Django-admin user
access container
```sh
docker exec -it mileto_container /bin/bash
```
inside the mileto_container define: user, password and email 
```sh
python manage.py createsuperuser
```

# Access Django-admin
###### Django-admin: [http://0.0.0.0:8000/admin/](http://0.0.0.0:8000/admin/)

# Mileto Docs
###### Swagger: [http://0.0.0.0:8000/swagger/](http://0.0.0.0:8000/swagger/)
###### Redoc: [http://0.0.0.0:8000/redoc/](http://0.0.0.0:8000/redoc/)