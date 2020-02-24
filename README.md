# AWS-Lightsail
AWS Lightsail Python Automation 

Link to full write up on [Medium][2]

[![Installing Python3, PIP3 and automating your python script](https://youtu.be/_qXkwHamnyM)](https://youtu.be/_qXkwHamnyM)  - Follow this video once the ubuntu instance is created. 

[2]:https://towardsdatascience.com/automate-python-scripts-with-aws-lightsail-b8dfdd5b0a2f

![](https://github.com/Landstein/AWS-Lightsail/blob/master/images/awslightsail.png)


## Project Goals

The goal of this project is to completely automate the process of collecting data.  I will achieve this by hosting my python script in the cloud using an AWS Lightsail Ubuntu Instance.  


## AWS Lightsail Ubuntu Instance 

To begin you will need to sign up at [Amazon LightSail][1].  The first month is free which will give you plenty of time to decide if this solution is what you need. 

[1]:https://aws.amazon.com/lightsail/

![](https://github.com/Landstein/AWS-Lightsail/blob/master/images/instance_1.png)

###Create an Ubuntu Instance 

1. Click on the Create instance button (circled above). 
2. Under pick your instance image, select Linux/Unix 
3. Select OS only 
4. Select Ubuntu 18.04

![](https://github.com/Landstein/AWS-Lightsail/blob/master/images/instance_2.png)

5. Choose your instance Plan: For this project I will be using the cheapest option ($3.50) as it is more than sufficient to run most python scripts.  Additionally, the first month is free! 

![](https://github.com/Landstein/AWS-Lightsail/blob/master/images/instance_3.png)

6. Name your instance:  For this project I named the instance “Ubuntu-Automation”
7. Create your instance

![](https://github.com/Landstein/AWS-Lightsail/blob/master/images/instance_4.png)

After selecting Create Instance you will be returned to the AWS LightSail dashboard.  It will take the Ubuntu instance a few minutes to be created.  While the instance is being created, its status will be “Pending” like in the screenshot below:

![](https://github.com/Landstein/AWS-Lightsail/blob/master/images/pending.png)

The status will change to “Running” once the instance has been created.  You will also see the IP address assigned to the instance is 3.227.241.208.  This IP address is dynamic and will change every time you reboot the instance.  Depending on the project you plan on hosting it may be necessary to set a Static IP address.  

![](https://github.com/Landstein/AWS-Lightsail/blob/master/images/running.png)

### Create a Static IP Address 

Creating a static IP is optional and only necessary if your project requires it.  I will be creating the static IP address because I open my SQL server only to this IP address for security reasons.  Additionally, I prefer to SSH into the Ubuntu instance from my local machine and having a static IP makes this process easier.   

1. Select the Networking tab in your Lightsail dashboard 
2. Click on “Create static IP” 

![](https://github.com/Landstein/AWS-Lightsail/blob/master/images/ip_1.png)

3. Select your Ubuntu Instance server under “Attach to an instance”
4. Give the Static IP a name
5. Click “Create”

![](https://github.com/Landstein/AWS-Lightsail/blob/master/images/ip_2.png)

You will then see your new static IP Address.  This IP address will not change. 

![](https://github.com/Landstein/AWS-Lightsail/blob/master/images/ip_4.png)


In this example my Static IP address is 18.213.119.58.  








