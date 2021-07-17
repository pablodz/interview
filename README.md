# Interview Vozy

Pablo Díaz

## Requirements

- Docker
- Docker-compose

## Tasks already done

- [x] Código fuente
- [x] Archivos docker
- [x] docker compose
- [x] README.md
- [x] Estructuración de proyecto
- [x] Patrones de diseño
- [x] Pruebas de API
- [ ] Cobertura

## To replicate Microservice app

Python REST/API based with mongoDB that stores cats information, like the line bellow:

```json
{
    "catid": "1",
    "catname": "michifuz"
}
```

![](https://imgur.com/c821a4A.png)


1. Clone the repository

```bash
git clone https://github.com/pablodz/interview
cd interview
```

2. Install basic dependencies
```bash
sudo apt-get install build-essential
# To run makefiles
make help
```

3. Build and wake-up the services

```bash
make run
```

You'll see a similar shell

![](https://imgur.com/ryrUhPN.png)

> ENDPOINTS EXAMPLE: <br>
> `http://0.0.0.0:5000/v1/api` # Returns all cats in JSON <br>
> `http://0.0.0.0:5000/v1/api/1` # Returns cat with ID=1 <br>
> `http://0.0.0.0:5000/v1/api/catname/michifuz` # Returns cat called 'michifuz'


1. Open another shell and run tests, 4 in total (GET,POST,PUT,DELETE)

```bash
# install if necesary
# pip3 install pytest
make test # This script runs locally not dockerized
```

![](https://imgur.com/gt39l8d.png)
