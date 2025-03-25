import kagglehub
from sqlalchemy import text, Index
from sqlalchemy import create_engine, MetaData, Table, Column
from sqlalchemy.types import Text, Integer
import pandas as pd
import sys

def download_netflix_dataset():
    path = kagglehub.dataset_download("shivamb/netflix-shows")
    print("Path to dataset files:", path)
    return path

def load_netflix_database(path):
    df = pd.read_csv(path+"/netflix_titles.csv", header=0)
    df['show_id'] = df['show_id'].str.replace('s', '').astype(int)
    DATABASE_URL=f"postgresql://postgres:shows@localhost:5432/shows_db"

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

    # Create the table with primary key
    metadata = MetaData()
    netflix_shows = Table(
        'netflix_shows', metadata,
        Column('show_id', Integer, primary_key=True),
    )

    print("Uploading data to database...")
    df.to_sql('netflix_shows', engine, if_exists="replace", index=False, dtype={
        "show_id": Integer,
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
    
    # Create unique index
    with engine.connect() as conn:
        conn.execute(text("""
            CREATE UNIQUE INDEX IF NOT EXISTS idx_show_id 
            ON netflix_shows (show_id);
        """))
        conn.commit()
    
    print("Data upload complete!")

