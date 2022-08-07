# Flask-Weather-App
**This is a Flask-based weather application that makes use of the Open Weather API and is deployed using Vagrant, Docker, Docker-Swarm and Ansible.**

Vagrant is used to create the Virtual Machines(VM), Docker is used for containerization, and Docker-Swarm is used for orchestration. Ansible is being used to automate all of the processes rather than manually installing them on the VM.

Certain things must be installed on your system before you can work on this project.

1. Vagrant - https://www.vagrantup.com/docs/installation
2. Git - https://git-scm.com/downloads
3. Virtual Box - https://www.virtualbox.org/wiki/Downloads

## Application
The flask application, requires the following things to be installed:
- Python - `version 3.7 or higher`
- Flask - `pip install Flask`
- Requests - `pip install requests`
- Configparser - `pip install configparser`

Create an account in openweathermap and generate an API key to access the data and save it in another file called `config.ini` for security and proper code structure.

In terms of the project, there is a `app.py` file for all of the **python** code, and the **HTML** code is in the `templates` directory.
There is also a `static` folder that contains some **CSS** and the necessary images. The `requirements.txt` file contains a list of all required modules. Then there is a `Dockerfile` to create a docker-image.

To make a docker-image, follow these steps:
1. Make a docker hub repository.
2. To terminate any of the previous session run this command in your terminal 
  ```
  docker logout
  ```
 3. To create the image, execute
  ```
  docker build -t flaskapp  .
  ```
 4. Give it a tag.
  ```
  docker tag flaskapp harshita09sao/flaskapp:v1
  ```
 5. Login
   ```
   docker login
   ```
 6. Push the Docker image to the Docker Hub repository.
  ```
  docker push  harshita09sao/flaskapp:v1
  ```
 Our Docker image has been created. Let us proceed to the next section.
 
## Deployment
 
There is a `Vagrantfile` here that contains all of the information about the servers, such as the number of servers, the memory and CPU requirements, and so on. Then there is a `hosts` file, also known as an inventory file, which contains all of the information about the servers' IP addresses.

1. To start the virtual machines run this command in your terminal
  ```
  vagrant up
  ```
2. ssh into control
  ```
  vagrant ssh control
  ```
3. As we can see, there is no information about the host in the `etc` file, so let's add it so that ip connectivity is available.
  ```
  sudo cp /vagrant/hosts /etc/hosts
  ```
4. As of now, whenever I tried to ssh into the nodes, I had to provide a password, so to log directly in, let's generate the ssh-key.
  ```
  ssh-keygen
  ```
5. Copy the ssh-id in each node
  ```
  ssh-copy-id node1 && ssh-copy-id node2 && ssh-copy-id node3
  ```
6. Setup ansible
  ```
  sudo apt-get install ansible -y
  ```
7. Go to the Ansible directory and look for myhosts, which is the inventory file that contains all of the configuration. Let's see if ansible is working properly. (Run this command inside the Ansible folder)
  ```
  ansible nodes -i myhosts -m command -a hostname
  ```
8. Installing Python in Ansible to increase functionality.
  ```
  ansible nodes -i myhosts -m command -a 'sudo apt-get -y install python-simplejson'
  ```
9. Ansible includes a playbook1.yml file with the myhosts file, which contains all of the tasks that ansible must complete, so let's run the playbook.
  ```
  ansible-playbook -i myhosts -K playbook1.yml
  ```
10. ssh to node1 and run docker to see if it is installed.
  ```
  docker run hello-world
  ```
11. Docker has been installed, and in the `docker` folder is a `docker-compse.yml` file that contains image and port information. Let's pull the image.
  ```
  docker-compose up
  ```
12. To view the images
  ```
  docker images
  ```
13. To view docker container
  ```
  docker ps -a
  ```
14. Now, for Swarm, move to the Docker-Swarm folder in the control server, where we also have myhosts and a playbook file containing all of the configuration and tasks to be completed. To complete the setup run
  ```
  ansible-playbook -i myhosts -K playbook2.yml
  ```
15. Lets go to node1 and verify
  ```
  docker node ls
  ```
16. Let us remove the present container.
  ```
  docker-compose down
  ```
17. To create container in docker swarm
  ```
  docker stack deploy --compose-file docker-compose.yml flaskApp
  ```
 18. To check, run
   ```
   docker stack ls
   ```
 19. To see the services
   ```
   docker stack services flaskApp
   ```
 20. To scale the app upto 3 replicas
   ```
   docker service scale flaskApp_web=3
   ```
 21. Check 
   ```
   docker service ls
   ```
 22. To get more specific information, run
   ```
   docker service ps flaskApp_web
   ```
 
If you want, you can view the application running in the browser by going to the port, i.e. node IP address:7000. For example, if node1 is used, the port will be `172.16.1.51:7000`. You can do the same for any node.
 
Finally, bring the container down by running `docker-compose down` to stop everything. Then exit out of node1 and control and run `vagrant halt` to stop all the VMs, or `vagrant destroy` to delete the VMs.
