#!/bin/bash

sudo apt-get update
curl https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -o ~/miniconda.sh
bash ~/miniconda.sh -b -p $HOME/miniconda
source $HOME/miniconda/etc/profile.d/conda.sh
export PATH="$HOME/miniconda/bin:$PATH"
conda env create --file=environment.yml
conda activate jnbformat
