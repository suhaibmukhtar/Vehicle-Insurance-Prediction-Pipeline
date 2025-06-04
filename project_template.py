import os
from pathlib import Path
Main_Path = Path(__file__).parent
Main_Package_path = os.path.join(Main_Path,"src")

list_of_files = [
    f"{Main_Package_path}/__init__.py",
    f"{Main_Package_path}/config/__init__.py",
    f"{Main_Package_path}/config/config.py",
    f"{Main_Package_path}/components/__init__.py",
    f"{Main_Package_path}/components/data_ingestion.py",
    f"{Main_Package_path}/components/data_transformation.py",
    f"{Main_Package_path}/components/model_trainer.py",
    f"{Main_Package_path}/components/model_evaluation.py",
    f"{Main_Package_path}/components/model_pusher.py",
    f"{Main_Package_path}/components/data_validation.py",
    f"{Main_Package_path}/configuration/__init__.py",
    f"{Main_Package_path}/configuration/mongo_db_connection.py",
    f"{Main_Package_path}/configuration/aws_connection.py",
    f"{Main_Package_path}/cloud_storage/__init__.py",
    f"{Main_Package_path}/cloud_storage/aws_storage.py",
    f"{Main_Package_path}/data_access/__init__.py",
    f"{Main_Package_path}/data_access/proj1_data.py",
    f"{Main_Package_path}/constants/__init__.py",
    f"{Main_Package_path}/entity/__init__.py",
    f"{Main_Package_path}/entity/config_entity.py",
    f"{Main_Package_path}/entity/artifact_entity.py",
    f"{Main_Package_path}/entity/estimator.py",
    f"{Main_Package_path}/entity/s3_estimator.py",
    f"{Main_Package_path}/exception/__init__.py",
    f"{Main_Package_path}/logger/__init__.py",
    f"{Main_Package_path}/pipeline/__init__.py",
    f"{Main_Package_path}/pipeline/train_pipeline.py",
    f"{Main_Package_path}/pipeline/prediction_pipeline.py",
    f"{Main_Package_path}/utils/__init__.py",
    f"{Main_Package_path}/utils/main_utils.py",
    f"{Main_Package_path}/Dockerfile",
    f"{Main_Package_path}/.dockerignore",
    f"{Main_Package_path}/README.md",
    f"{Main_Package_path}/requirements.txt",
    f"{Main_Package_path}/exception.py",
    f"{Main_Package_path}/logger.py",
    f"{Main_Package_path}/setup.py",
    f"{Main_Package_path}/pyproject.toml",
    "config/model.yaml",
    "config/schema.yaml",
    "README.md",
    "Project_flow.md"
]
for file_path in list_of_files:
    file_path = Path(file_path)
    filedir, filename = os.path.split(file_path)
    if filedir and not os.path.exists(filedir):
        os.makedirs(filedir, exist_ok=True)
    if (not os.path.exists(file_path)) or (os.path.getsize(file_path) == 0):
        with open(file_path, 'w') as f:
            pass
    else:
        print(f"File {file_path} already exists and is not empty.")