
#!/usr/bin/env bash

# setup.sh
# Create the python enviroment to deploy the application as an hosted Interactive Web Service on AWS EC2 instance

#Pass ENVNAME
ENVNAME=${1:-pyenv}

# update local packages 
sudo apt-get update -y
# install dependencies
sudo apt-get install -y python3-pip python3-dev python3-venv
# create the python enviroment
python3 -m venv ${ENVNAME}
# activate a virtual environment¶
source ./${ENVNAME}/bin/activate
#install packages
pip install -r ./src/score_interactive_endpoint/requirements.txt
