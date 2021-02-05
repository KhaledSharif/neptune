# Neptune

### Prerequisites

[Installing Ansible on Ubuntu](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html#installing-ansible-on-ubuntu)

or

[Installing Ansible with pip](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html#installing-ansible-with-pip)


### How to run

Modify the `hosts` file to contain the IP address of your Jetson machine. You should be able to ssh into a user on this machine (Jetson) without a password (ie: ssh key)

```bash
echo "192.168.1.118" > ./hosts
```

Provision the Jetson machine by downloading the latest `cmake`, then cloning and building `draco`.

```bash
./execute.sh ./draco/provision.yaml
```

Copy Stanford Bunny mesh file to Jetson.

```bash
./execute.sh ./draco/copy.yaml
```

Run `draco` encoder to compress mesh file.

```bash
./execute.sh ./draco/test.yaml
```

You will be able to find the CSV log file in a auto generated folder:
ip address of jetson followed by unix timestamp of experiment.

```
head ./192.168.1.118/1612552101/logs.csv
```
