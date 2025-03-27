# Streaming platforms database display

Don't you know what to watch on Netflix, Disney+ or any streaming platform? <br/>
My program will recommend something for you

## Libraries

### Python (backend)
- flask
- pandas
- sqlalchemy
- kagglehub
- scikit-learn

### TypeScript (frontend)
- React


I use OMDB api key, so I am limited to 1000 queries per day
## Commands

```md
source venv/bin/activate
```

To create database using docker
```md
docker run --name shows -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=shows -e POSTGRES_DB=shows_db -p 5432:5432 -d postgres
```

Password: `shows`

To get to the database using psql
```md
psql -h localhost -U postgres -d shows_db
```
