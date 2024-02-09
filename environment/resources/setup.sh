#!/bin/bash 
# sudo pip install boto3

# bucket=`aws s3api list-buckets --query "Buckets[].Name" | grep s3bucket | tr -d ',' | sed -e 's/"//g' | xargs`
# echo export bucket=`aws s3api list-buckets --query "Buckets[].Name" | grep s3bucket | tr -d ',' | sed -e 's/"//g' | xargs` >> /home/ec2-user/.bashrc
# echo export bucket_url="https://${bucket}.s3-us-west-2.amazonaws.com/index.html" >> /home/ec2-user/.bashrc
# FILE_PATH="/home/ec2-user/environment/resources/website_security_policy.json"
# FILE_PATH_2="/home/ec2-user/environment/resources/permissions.py"

# aws s3 cp ./resources/website s3://$bucket/ --recursive --cache-control "max-age=0"

# sed -i "s/<FMI_1>/$bucket/g" $FILE_PATH_2

# sed -i "s/<FMI_1>/$bucket/g" $FILE_PATH
# sed -i "s/<FMI_2>/$bucket/g" $FILE_PATH
# sed -i "s/<FMI_3>/$ip_address/g" $FILE_PATH
# sed -i "s/<FMI_4>/$bucket/g" $FILE_PATH

# python3 /home/ec2-user/environment/resources/permissions.py



# Launch Commands
# Firstly, install boto3
sudo pip install boto3

# Secondly, Move the website files to the S3 bucket
aws s3 cp ./resources/website s3://assignmentfoodsharehubbucket/ --recursive --cache-control "max-age=0"

# Thirdly, Set the website security policy file
python3 /home/ec2-user/environment/resources/permissions.py

# Update single file aws s3 cp ./resources/website/addDonation.html s3://assignmentfoodsharehubbucket/addDonation.html --cache-control "max-age=0"