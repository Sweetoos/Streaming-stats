from database.netflix_db import download_netflix_dataset,load_netflix_database
#from database.imdb_db import download_imdb_database,load_imdb_database ,fetch_video_data
from apikey import my_api_key
import sys
from flask import Flask
from flask_cors import CORS

netflix_dataset_path=download_netflix_dataset()
load_netflix_database(netflix_dataset_path)

# imdb_dataset_path=download_imdb_database()
# load_imdb_database(imdb_dataset_path)

app=Flask(__name__)
CORS(app)

@app.route('/')
def run_site():
    return running_site()

if __name__ == '__main__':
    app.run(debug=True)

# print("Do you want to use this app for now?")
# choice=input('yes/no')
# match(choice):
#     case "yes":
#         # my_api_key=input('Give me your api key')
#         pass
#     case "no":
#         print("Thank you for using this app")
#         sys.exit(1)
#     case _:
#         print("Invalid choice")
#         sys.exit(1)

