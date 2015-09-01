#!/bin/bash
BASE_PATH=$(dirname "${BASH_SOURCE}")
BASE_PATH=$(cd "${BASE_PATH}"; pwd)

source $BASE_PATH/env/bin/activate
python $BASE_PATH/syncer_scripts/update_figure-2-26.py $*
