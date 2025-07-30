## Specific Steps

### Environment Setup

1. Open PyCharm and launch the software.
2. Configure the conda environment.

```sh
conda create -n <your_env_name>
conda activate <your_env_name>
```

3. Install Backend Dependencies.

```sh
pip3 install Django==4.1
pip3 install -ihttps://mirrors.aliyun.com/pypi/simple/ django-cors-headers
pip3 install pymysql
pip3 install ruamel.yaml
pip3 install PyYAML
pip3 install torch torchvision torchaudio
pip3 install torch_geometric
pip3 install torch_sparse
pip3 install torch_scatter
pip3 install torch_cluster
pip3 install matplotlib
pip3 install networkx
pip3 install transformers
pip3 install scikit-learn
pip3 install pandas
pip3 install django-redis
pip3 install celery
```

4. Install MySQL.

```sh
sudo apt-get update
sudo apt-get install mysql-server mysql-common
sudo mysql -u root
```

5. Create a New Database and Add Data

```mysql
create database sf_web_001;
use sf_web_001;
source <path>/sf_web_001_with_data.sql
```



### Software Usage

1. Run the software.

```sh
cd backend
python manage.py runserver 127.0.0.1:9528
```

2. Software Operation

Simply click according to the prompts on the panel.

The operation may take some time. You can check the backend to see which step it is on. Avoid frequent operations, and wait for the backend functions to complete before proceeding to the next step.

3. Data Download

Click on "Data download" Data export will take some time. You can monitor the backend and wait for a while.



### Note

During secondary development, if you modify the frontend, you also need to:

```sh
cd frontend
npm run build:prod
```

This will generate a `dist` folder in the `frontend` directory. Then, replace the `dist` folder in both `frontend` and `backend` with the new one.



Login Account: editor, Password: FdpDg@2024
