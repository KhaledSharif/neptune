#!/bin/bash

set -e

while getopts u:n:p: flag
do
    case "${flag}" in
        u) username=${OPTARG};;
        n) hostname=${OPTARG};;
        p) playbook=${OPTARG};;
    esac
done

echo $hostname > /tmp/ansible_hosts

NEPTUNE_WORKFLOW=$playbook ANSIBLE_STDOUT_CALLBACK=yaml ansible-playbook -i /tmp/ansible_hosts -u $username ./playbook.yaml