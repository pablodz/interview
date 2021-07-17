# Interview Vozy

First commit



## Run Microservice app

1. Clone the repository

```bash
git clone https://github.com/pablodz/interview
cd interview
```

2. Build the dockerfiles

```bash
sudo docker-compose build
```
> To use port 80 (production) under ubuntu, we need to use sudo

3. Wakeup web and database services

```bash
sudo docker-compose up
# Then check localhost:8501
```

