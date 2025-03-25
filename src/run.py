from database.netflix_db import download_netflix_dataset,load_netflix_database
from database.imdb_db import download_imdb_database,load_imdb_database,fetch_video_data
from apikey import my_api_key
import sys

netflix_dataset_path=download_netflix_dataset()
load_netflix_database(netflix_dataset_path)

imdb_dataset_path=download_imdb_database()
load_imdb_database(imdb_dataset_path)

print("Do you want to use this app for now?")
choice=input('yes/no')
match(choice):
    case "yes":
        my_api_key=input('Give me your api key')
    case "no":
        print("Thank you for using this app")
        sys.exit(1)
    case _:
        print("Invalid choice")
        sys.exit(1)

fetch_video_data("Breaking Bad",my_api_key)