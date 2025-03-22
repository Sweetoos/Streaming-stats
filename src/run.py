from database import download_dataset,load_database

dataset_path=download_dataset()
load_database(dataset_path)