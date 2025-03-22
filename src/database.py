import kagglehub
from sqlalchemy import text
from sqlalchemy import create_engine
from sqlalchemy.types import Text, Integer
import pandas as pd
import sys

def download_dataset():
    path = kagglehub.dataset_download("shivamb/netflix-shows")
    print("Path to dataset files:", path)
    return path

def load_database(path):
    df=pd.read_csv(path+"/netflix_titles.csv",header=0)
    DATABASE_URL=f"postgresql://postgres:netflix@localhost:5432/netflix_shows"

    try:
        engine = create_engine(DATABASE_URL)
        with engine.connect() as conn:
            result = conn.execute(text("select 'connected successfully!' as message;"))
            print(result.fetchone()[0])
    except ModuleNotFoundError:
        print("Error: Missing required package. Please run:")
        print("pip install psycopg2-binary")
        sys.exit(1)
    except Exception as e:
        print(f"Database connection error: {e}")
        print("Please ensure PostgreSQL is running and the database exists")
        sys.exit(1)

    print("Uploading data to database...")
    df.to_sql('netflix_shows', engine, if_exists="replace", index=False, dtype={
        "show_id": Text,
        "type": Text,
        "title": Text,
        "director": Text,
        "cast": Text,
        "country": Text,
        "date_added": Text,  
        "release_year": Integer,
        "rating": Text,
        "duration": Text,  
        "listed_in": Text,
        "description": Text
    })
    print("Data upload complete!")

