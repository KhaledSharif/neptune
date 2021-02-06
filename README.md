# Neptune

### Prerequisites

[Installing Ansible on Ubuntu](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html#installing-ansible-on-ubuntu)

or

[Installing Ansible with pip](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html#installing-ansible-with-pip)


### Usage

```bash
./execute.sh -u USERNAME -n HOSTNAME -p WORKFLOW
```

Example:

```bash
./execute.sh -u jetson -n 192.168.1.118 -p ./draco/provision.yaml
```

### How to run

Provision the Jetson machine by downloading the latest `cmake`, then cloning and building `draco`.

```bash
./execute.sh -u jetson -n 192.168.1.118 -p ./draco/provision.yaml
```

Copy Stanford Bunny mesh file to Jetson.

```bash
./execute.sh -u jetson -n 192.168.1.118 -p ./draco/copy.yaml
```

Run `draco` encoder to compress mesh file.

```bash
./execute.sh -u jetson -n 192.168.1.118 -p ./draco/test.yaml
```

You will be able to find the CSV log file in a auto generated folder:
ip address of jetson followed by unix timestamp of experiment.

```
head ./192.168.1.118/1612552101/logs.csv
```
