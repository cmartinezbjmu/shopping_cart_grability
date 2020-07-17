# Shopping Cart - Grability



Shopping cart es una aplicación que le permite a los usuarios registrar productos en la aplicación, a los usuarios finales agregar productos a un carrito de compras y efectuar la orden de compra después de registrarse. Esta aplicación está siendo desarrollada con el framework Django y Django REST Framework.

## Requisitos de instalación

```bash
* Python versión = 3.8
* PostgreSQL version >= 11
* Instalar el administrador de entornos virtuales 'pipenv'(https://pypi.org/project/pipenv/) 
```

## Instalación

- Clone el repositorio con el comando "git clone https://github.com/cmartinezbjmu/shopping_cart_grability.git"
- Acceda al directorio del proyecto y ejecute "pipenv install" para instalar todas las dependecias del proyecto.
- Cree un archivo .env en la raíz del proyecto con los siguientes datos

```bash
  - SECRET_KEY=q!ywis$p!m8v1s*+n4qucn7^1lcl=9q_aj9hbd$=hkg2=4=!#t
  - DBNAME=shopping_cart_db
  - DBUSER=postgres
  - DBPASS=admin
  - DBHOST=127.0.0.1
  - DBPORT=5432
```

Nota: Los valores expuestos aquí son de ejemplo y deben cambiarse para evitar fallas de seguridad en la aplicación.

## Ejecute la aplicación

Inicie el entorno virtual

```bash
pipenv shell
```

Ejecute las migraciones en la base de datos

```bash
python manage.py migrate
```

Finalmente, inicie la aplicación

```bash
python manage.py runserver
```



## Endpoints

### Usuarios

- #### Registro

  Este endpoint permite realizar un registro de usuario suministrando los datos de username, password1 y password2. A continuación relaciono un ejemplo para el consumo:

  ```
  curl -X POST \
    http://127.0.0.1:8000/api/v1/users/rest-auth/registration/ \
    -H 'Content-Type: application/json' \
    -H 'cache-control: no-cache' \
    -d '{
            "username": "Grability",
            "password1": "Grability2020*",
            "password2": "Grability2020*"
        }'
  ```

- #### Login

  Este endpoint permite realizar la autenticación de un usuario registrado. A continuación relaciono un ejemplo para el consumo:

  ```
  curl -X POST \
    http://127.0.0.1:8000/api/v1/users/rest-auth/login/ \
    -H 'Content-Type: application/json' \
    -d '{
            "username": "Grability",
            "password": "Grability2020*"
  			}'
  ```

  Posteriormente le retornará un Token de autenticación con el cual podrá ejecutar su orden de compra en el carrito de compras.

- #### Logout

  Este endpoint permite cerrar sesión en la aplicación. A continuación relaciono un ejemplo para el consumo:

  ```
  curl -X POST \
    http://127.0.0.1:8000/api/v1/users/rest-auth/logout/
  ```

###Productos

- #### Agregar un producto

  Este endpoint le permite agregar un producto con los campos de nombre, precio, cantidad disponible y una imagen del producto. A continuación relaciono un ejemplo para el consumo:

  ```
  curl -X POST \
    http://127.0.0.1:8000/api/v1/products/new \
    -H 'Content-Type: application/json' \
    -F 'folder_of_your_image/apple.png' \
    -F name=Manzana \
    -F price=2000 \
    -F amount_avaliable=50
  ```

- #### Lista de productos

  Este endpoint le permite obtener una lista de los productos registrados en la aplicación con la información registrada. A continuación relaciono un ejemplo para el consumo:

  ```
  curl -X GET \
    http://127.0.0.1:8000/api/v1/products
  ```

- #### Detalle de un producto

  Este endpoint permite obtener el detalle de un producto en especifico registrado en la aplicación. A continuación relaciono un ejemplo para el consumo:

  ```
  curl -X GET \
    http://127.0.0.1:8000/api/v1/products/1
  ```

- ### Actualizar un producto

  Este endpoint permite actualizar la información total o parcial de un producto registrado en la aplicación. A continuación relaciono un ejemplo para el consumo:

  ```
  curl -X PATCH \
    http://127.0.0.1:8000/api/v1/products/update/1 \
    -F price=1500 \
    -F amount_avaliable=3
  ```

- #### Borrar un producto

  Este endpoint permite eliminar un producto registrado en la aplicación. A continuación relaciono un ejemplo para el consumo:

  ```
  curl -X DELETE \
    http://127.0.0.1:8000/api/v1/products/delete/1 
  ```

### Cart

El carro de compras se implementó guardando la información que el usuario registra en el carro de compras en la misma sesión del usuario, buscando una mayor agilidad en la aplicación y redunciendo las consultas a base de datos. 

- #### Añadir un producto

  Este endpoint permite agregar un producto disponible en la aplicación al carro de compras.

  ```
  curl -X POST \
    http://127.0.0.1:8000/api/v1/cart/add/1/
  ```

- #### Remover un producto

  Este endpoint permite remover un producto del carro de compras.

  ```
  curl -X POST \
    http://127.0.0.1:8000/api/v1/cart/remove/3/
  ```

- #### Incrementar la cantidad de un producto

  Este endpoint permite incrementar la cantidad de un producto añadido al carro de compras.

  ```
  curl -X POST \
    http://127.0.0.1:8000/api/v1/cart/increment/3/
  ```

- #### Decrementar la cantidad de un producto

  Este endpoint permite disminuir la cantidad de un producto añadido al carro de compras.

  ```
  curl -X POST \
    http://127.0.0.1:8000/api/v1/cart/decrement/1/
  ```

- #### Limpiar el carro de compras

  Este endpoint permite limpiar el carro de compras.

  ```
  curl -X GET \
    http://127.0.0.1:8000/api/v1/cart/clear
  ```

- #### Obtener el detalle de los productos añadidos al carro de compras

  Este endpoint permite obtener el detalle de los productos añadidos al carro de compras.

  ```
  curl -X GET \
    http://127.0.0.1:8000/api/v1/cart/detail
  ```

### Ordenes

- #### Crear orden de compra

  Este endpoint permite al usuario ejecutar la compra que tiene almacenada en el carrito de compras.

  ```
  curl -X GET \
    http://127.0.0.1:8000/api/v1/orders/
  ```
  
### Pruebas
   
- #### Pruebas unitarias
  La aplicación cuenta con pruebas unitarias sobre cada una de las aplicaciones, se pueden ejecutar con este comando
  ```bash
  python manage.py test
  ```

- #### Colección de Postman
  Se creó una colección de Postman que permite ejecutar pruebas directamente desde la aplicación, puede importarlo usando el siguiente [link] (https://www.getpostman.com/collections/bf1a8121f180a8fcb662)
