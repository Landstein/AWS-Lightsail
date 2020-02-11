## Hosting Config file in AWS S3

Sticking with the AWS theme I have decided to use S3 to transfer the file.  Though there are many alernatives. 

1.) Select S3 from the AWS console

![](https://github.com/Landstein/AWS-Lightsail/blob/master/images/s31.png)

2.) Create New Bucket
![](https://github.com/Landstein/AWS-Lightsail/blob/master/images/s32.png)

3.) Fill in name and select next

![](https://github.com/Landstein/AWS-Lightsail/blob/master/images/s34.png)

4.) Select the bucket

![](https://github.com/Landstein/AWS-Lightsail/blob/master/images/s35.png)

![](https://github.com/Landstein/AWS-Lightsail/blob/master/images/s36.png)

5.) Permissions > all uncheck block public access 
![](https://github.com/Landstein/AWS-Lightsail/blob/master/images/s37.png)

6.) save
![](https://github.com/Landstein/AWS-Lightsail/blob/master/images/s38.png)

8.) 
![](https://github.com/Landstein/AWS-Lightsail/blob/master/images/s39.png)

9.) Copy Public URL 
![](https://github.com/Landstein/AWS-Lightsail/blob/master/images/s310.png)

### On the Ubuntu instance 

1.) cd to the folder with your python script
2.) wget {the public URL for the config file in your S3 bucket}


I highly recommend you delete the config file from S3 once it has been transfered to your Ubuntu instance.  Additionally you can just close the config file to the public.  
