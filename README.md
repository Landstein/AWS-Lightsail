# AWS-Lightsail
AWS Lightsail Python Automation 

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
