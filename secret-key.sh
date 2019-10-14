#!/bin/bash

# This script creates a random 50-character string 
# and saves it into a .env file.
# This script should be executed by calling 
# source /path/to/script/secret-key.sh

echo Generating secret key

echo SECRET_KEY=$(\
python -c"import random; print(''.join(random.SystemRandom().\
choices('abcdefghijklmnopqrstuvwxyz0123456789', k=50)))"\
) >> .env

echo Saved to environment variable file