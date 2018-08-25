# SDN-Telemetry Introduction
The goal of this LCCN project is to provide a platform to collect telemetry data from an SDN network and run analytics on the data.

This readme file is a guide which will help you get started, run the different components of the project, collect metrics and write analytics.

Students: Idan Yadgar & Omri Huller  
Supervisor: Jalil Morany


# Overview
## SDN simulation & Collect metrics
We used mininet to simulate the SDN, and created a default topology that includes 3 hosts, 4 switches and 1 controller.  
The controller is a ryu controller. We used python, and ryu seemed like a good choice for working with OpenFlow.

Our controller is not a standard controller. Basically, it doesn't communicate with our switches but just listens and waits for commands.  
We created a CLI that communicates with our controller. This CLI allows to install and uninstall different applications.  
Each application collects a different metric (such as byte count, packet count, etc) and one can start and stop collecting the metrics dynamically by installing and uninstalling those applications.

The output directory is watched by a different python script which gets notified when a file is created or modified in this directory.  
When a change is detected, this application pushes the new changes to PNDA and truncates changed file.

## Writing and running analytics
PNDA is a scalable platform to perform big data analytics, which combines different software components together to create a scalable system which can run as distributed cluster on many servers.

PNDA uses Apache Kafka as its entrance gate. Kafka provides a distributed publisher-consumer platform, which can be divided to different topics.  
Each producer can choose a topic and send data into it, and all the consumers of this topic will get this data. Of course, producers and consumers can be each on a different machine.

The same script that pushes the metrics to PNDA is actually a Kafka producer that sends the metrics to PNDA using this mechnism.

PNDA also allows using Apache Spark for data analysis. Apache Spark is a scalable distributed system that allows analysing big data.  
We used spark with python in order to run some analytics on the collected metrics.

The analytics are written and ran inside Jupyter notebooks.  
Jupyter is also included in PNDA. It provides a web interface for writing and running python scripts.  
We created a notebook for each analytic script we wrote and used Spark inside the notebook to manipulate and collect the data.  
Also, in a Jupyter notebook, we can use different python libraries in order to, for example, plot out results.


# Installing dependencies
In order to simulate the network and collect the metrics, we recommend using Ubuntu - but any other distribution should be good.  
In this section we will use the Ubuntu commands in each step.

## Download the project source
Start by cloning this repository to your machine.

Install git: `sudo apt install git`

Clone the repository `git clone https://gitlab.cs.technion.ac.il/lccn/S2018-MEF-SDN-Telemetry.git`

Navigate to the repository directory: `cd S2018-MEF-SDN-Telemetry`


## Install mininet
Start by installing mininet: `sudo apt install mininet`

Deactivate openvswitch-controller by running:  
`sudo service openvswitch-controller stop`  
`sudo update-rc.d openvswitch-controller disable`

Now try to run a mininet test: `sudo mn --test pingall`

If there is an error, try installing mininet via this guide: http://mininet.org/download/  
Try **Option 3: Installation from Packages**.


## Install ryu
Start by installing pip: `sudo apt install python-pip`

Now install ryu: `pip install ryu`


## Install Watchdog
Watchdog is a python library for watching files for modifications, run th following:  
`pip install watchdog`

## Install Kafka for python
Install kafka python: `pip install kafka-python`


# Install Red PNDA
Red PNDA is a smaller version of PNDA. It has less capabilities but contains Kafka, Spark and Jupyter.  
Red PDA is easier to install, as it comes as an image that can be run on a VM.

If you did the last section on a VM, red PNDA can be installed on a different VM, it doesn't have to be a VM inside the machine used for the last section.  
However, the two machine must be able to reach each other and establish a connection.

Download the image [from here](http://d5zjefk3wzew6.cloudfront.net/Red-PNDA_0.2.8.ova).

Install it on VMWare or VirtualBox, with at least 4GB of RAM, 2 CPUs and 8GB of storage. 

After installing and running the machine, use the username *pnda* and password *pnda* to log in.  
Now, run the following: `sudo bash assign-ip.sh eth0`.  
Get the IP of the machine by running `ifconfig`.  
And open your web browser and navigate to this IP, you should see PNDA console (a web interface).

If you have any problem with this section, read [this guide](https://github.com/pndaproject/red-pnda/blob/develop/README.md).
