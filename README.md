# Cluster and Cloud Computing Project-2

Group Members:
- Team 22
- Zizhao Li (1267416) zizhaol2@student.unimelb.edu.au (Suzhou, China)
- Fu Zhu (1166186) fuzhu@student.unimelb.edu.au (Melbourne, Australia)
- Chuting Wang (1074511) chutingw@student.unimelb.edu.au (Xi’an, China)
- Xuezhu Wu (938808) xuezhuw@student.unimelb.edu.au (Hangzhou, China)
- Yuepeng Sheng (1048382) yuepengs@student.unimelb.edu.au (Shanghai, China)

# Description
Here is the tutorial of running the cloud-based twitter analysis system.
Before you start, please install the Ansible first.
https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html

Once the Ansible is installed, navigate to /mrc and do the following steps 
1. Create instances on MRC
    Download the openrc file from MRC and make sure it is in the directory

    run ./run-nectar.sh


    Once the instances are created, modify the Ansible inventory with the hosts ip. 

2. Deploy docker
    Make sure you have the ssh private key for the instances
    
    run ./run-docker.sh

3. Deploy CouchDB cluster

    run ./run_couchdb_cluster.sh
    
4.  Deploy the data harvester
    
    run ./run_harvest.sh

5.  Deploy the MapReduce program

    run ./run-map-reduce.sh
    
 6. Deploy the web server

    run ./run-web-server.sh

# YouTube Link
https://www.youtube.com/watch?v=aDL3_g_Wqx8
