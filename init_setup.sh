echo [$(date)]: "Start"
echo [$(date)]: "Creating conda environment"
conda create --prefix ./env python=3.8 -y
echo [$(date)]: "activating env with python version 3.8"
source activate ./env
echo [$(date)]: "installing requirements"
pip install -r requirements_dev.txt
echo [$(date)]: "End"