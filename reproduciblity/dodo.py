def task_conda_env():
    return {
        'actions': [
            'conda env create -f environment.yml'
        ],
    }    

def task_run_nb():
    return {
        'actions': [
            'conda activate jreproduce && papermill run_notebook.ipynb run_notebook_executed.ipynb'
        ]
    }