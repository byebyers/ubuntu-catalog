Quick start

To run this file, you'll need Vagrant and VirtualBox installed.

VirtualBox can be downloaded here: https://www.virtualbox.org/wiki/Downloads Vagrant can be found here: https://www.vagrantup.com/downloads.html

Once you have Vagrant and VirtualBox up and running, open a command prompt and navigate to vagrant/ inside this directory, and run the following commands:

vagrant up vagrant ssh cd /vagrant/catalog python lotsofbabies.py (to populate database) python project.py Go to http://localhost:5000 to see app running
