import requests
from sqlalchemy import create_engine, Column, Integer, Float, String, ForeignKey, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

DATABASE_URL=f"postgresql://postgres:shows@localhost:5432/shows_db"
engine=create_engine(DATABASE_URL)
SessionLocal=sessionmaker(bind=engine)
session=SessionLocal()

Base=declarative_base()

class Video(Base):
    __tablename__="videos"
    id=Column(Integer, primary_key=True, autoincrement=True)
    title=Column(String, nullable=False)
    year=Column(Integer,nullable=True)
    imdb_rating=Column(Float,nullable=False)
    type=Column(String,nullable=False)

    episodes=relationship("Episode", back_populates="series")

class Episode(Base):
    __tablename__="episodes"
    id=Column(Integer, primary_key=True, autoincrement=True)
    title=Column(String, nullable=False)
    season=Column(Integer, nullable=False)
    episode=Column(Integer, nullable=False)
    imdb_rating=Column(Float, nullable=True)
    series_id=Column(Integer, ForeignKey=('videos.id'), nullable=False)

    series=relationship('Video',back_populates='episodes')

Base.metadata.create_all(engine)

def fetch_video_data(title, api_key, content_type='movie'):
    url=f"http://www.omdbapi.com/?t={title}&apikey={api_key}"
    response=requests.get(url)
    if response.status_code==200:
        data=response.json()
        if "Title" in data and "imdbRating" in data:
            return{
                "title": data["Title"],
                "year": data["Year",""],
                "imdbRating": float(data["imdbRating"]),
                "type": content_type,
            }
    return None

def fetch_episodes(series_title, api_key, seasons):
    series=session.query(Video).filter_by(Video.title==series_title).first()
    if not series:
        print("Series not found")
        return

    for season in range(1, seasons+1):
        url=f"http://www.omdbapi.com/?t={series_title}&Season={season}&apikey={api_key}"
        response=requests.get(url)
        if response.status_code==200:
            data=response.json()
            if "Title" not in data or "imdbRating" not in data:
                break

            episode_data=Episode(
                    title=data["Title"],
                    season=season,
                    episode=episode,
                    imdb_rating=float(data["imdbRating"]),
                    series_id=series.id
            )
    session.commit()
