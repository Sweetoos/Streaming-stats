# Netflix database display

Don't you know what to watch on Netflix? <br/>
My program will recommend something for you



## Libraries
- pandas
- sqlalchemy
- kagglehub
- sys

in future

- scikit-learn
- frontend (flask or django, probably the first one)

## Commands

```md
source venv/bin/activate
```

To create database using docker
```md
docker run --name netflix_db -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=netflix -e POSTGRES_DB=netflix_shows -p 5432:5432 -d postgres
```

Password: `netflix`

To get to the database using psql
```md
psql -h localhost -U postgres -d netflix_shows
```