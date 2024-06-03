import os
from pathlib import Path
import logging
import sys
logging.basicConfig(level=logging.INFO,format='[%(asctime)s]:%(message)s',datefmt='%Y-%m-%d %H:%M:%S')
project_name='hand_sign_detection'
list_of_files=[".github/workflows/.gitkeep","data/.gitkeep","f{project_name}/__init__.py","f{project_name}/components/__init__.py","f{project_name}/components/data_ingestion.py","f{project_name}/components/data_validation.py","f{project_name}/components/model_trainer.py","f{project_name}/constant/__init__.py","f{project_name}/constant/training_pipeline/__init__.py","f{project_name}/constant/application.py","f{project_name}/entity/config_entity.py","f{project_name}/entity/artifacts_entity.py","f{project_name}/exception/__init__.py","f{project_name}/logger/__init__.py","f{project_name}/pipeline/__init__.py","f{project_name}/pipeline/training_pipeline.py","f{project_name}/utils/__init__.py","f{project_name}/utils/main_utils.py","templates/index.html","app.py","Dockerfile","requirements.txt","setup.py"]

for file in list_of_files:
    file=Path(file)
    filedir,file_name=os.path.split(file)
    if filedir != '':
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Created directory {filedir}")
    if (not os.path.exists(file)) or (os.path.getsize(file)==0):
        with open(file,'w') as f:
            pass
        logging.info(f"Created empty file: {file}")
    else:
        logging.info(f"File already exists: {file}")
        

