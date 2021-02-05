#!/bin/bash

set -e

if [ "$#" -ne 1 ]; then
    echo "You must enter exactly 1 command line arguments"
    exit 1
fi

NEPTUNE_WORKFLOW=$1 ANSIBLE_STDOUT_CALLBACK=yaml ansible-playbook -i ./hosts -u jetson ./playbook.yaml