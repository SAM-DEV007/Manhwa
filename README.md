# Manhwa
The 9 Best Fantasy Manhwa website hosted on AWS

## Website links
**NOTE: Load balancer and Auto Scaling group is removed for cost saving and is replaced with Nginx. The Route53 and AWS Certificate manager is replaced with Cloudflare DNS.\**

### Domain
**The domain is removed to prevent incurring costs.**

## Tasks
- <ins>**Deploy a web application**</ins>\
  The web application, inspired by "[The 50 Best Fantasy Manhwa You Must Read Now](https://animemangatoon.com/best-fantasy-manhwa-webtoons/)" is deployed using Django with Python 3.11.5.
  - <ins>**Display a list of manhwa titles, their genres, and brief descriptions using mock data**</ins>\
    The website is dynamically loaded using the JavaScript file which fetches JSON of mock data from the RDS. It uses basic HTML, CSS and JS.
  - <ins>**Hosted on a cloud platform</ins>**
    - The website is hosted on AWS and has EC2 instance with autoscaling, target groups, load balancer and launch template.
    - The static files and the images are stored in S3 bucket with public view access.
    - A RDS database is used to save and load the JSON data for dynamic loading which is passed to JavaScript.
- <ins>**Auto-scaling enabled**</ins>\
  Auto-scaling is enabled supported by launch template, target group and load balancer. More [info](#auto-scaling) is included here.
- <ins>**Security measures**</ins>
  - <ins>**Enabling HTTPS**</ins>\
    Domain name is added to hosted zones with Route 53 and SSL certificate generated from AWS Certificate Manager.
  - <ins>**Configure firewall**</ins>\
    Security groups are set-up with APN which allows access to only 80 (HTTP) and 443 (HTTPS), and are forwarded to 8000 (Deployment) port. The rest of the traffic from different ports are refused connection.

## Auto-scaling
The auto-scaling group uses Instance based auto-scaling, i.e., it auto-scales based on the CPU utilization of the instances. The minimum is set to 1 instance and maximum is set to 2 instances. The CPU utilization must reach more than 70% usage in order to trigger auto-scaling. It can also trigger in arbitrary shutdown/restart/crash of the instances.

The support for auto-scaling is extended by launch template, trigger group and load balancer.\
The launch template provides the overview of the instance and the operations to perform on launch. The User Data, which is executed on launch of an instance, is as follows:

*NOTE: The below script is for older version of the repository. All the contents are now shifted to ASG folder.*
```bash
#!/bin/bash
set -e

GIT_REPO_URL="https://github.com/SAM-DEV007/Manhwa.git"

PROJECT_MAIN_DIR_NAME="Manhwa"

git clone "$GIT_REPO_URL" "/home/ubuntu/$PROJECT_MAIN_DIR_NAME"

cd "/home/ubuntu/$PROJECT_MAIN_DIR_NAME"

cat <<EOF > .env
SECRET_KEY=secret key

DATABASE_NAME=database name
DBUSER=user
DBPASSWORD=pwd
DBHOST=host name
DBPORT=port

AWS_ACCESS_KEY_ID=access key
AWS_SECRET_ACCESS_KEY=secret access key
AWS_STORAGE_BUCKET_NAME=s3 bucket
EOF

chmod +x scripts/*.sh

./scripts/instance_os_dependencies.sh
./scripts/python_dependencies.sh
./scripts/gunicorn.sh
./scripts/start_app.sh
```
The trigger group and load balancer makes sure that the user is forwarded to the correct port from the request coming from HTTP or HTTPS.\
The load balancer is application-based and the public DNS is used to access the active instance of the application. It checks requests from port 80 (HTTP) and 443 (HTTPS), also defined in security group, and forwards the user to the target group.\
The target group, then, forwards the user to the registered active and healthy instance with port 8000 (Deployment port).

## EC2 Instance - Cost Cutting Measures
AutoScaling group, Target group, Load balancer and Launch templates are removed.\
A single EC2 instance is currently being maintained with its IPv4 address and DNS hosting.

User Data script:
```bash
#!/bin/bash
set -e

GIT_REPO_URL="https://github.com/SAM-DEV007/Manhwa.git"

PROJECT_MAIN_DIR_NAME="Manhwa"

git clone "$GIT_REPO_URL" "/home/ubuntu/$PROJECT_MAIN_DIR_NAME"

cd "/home/ubuntu/$PROJECT_MAIN_DIR_NAME"

cat <<EOF > .env
SECRET_KEY=secret key

DATABASE_NAME=database name
DBUSER=user
DBPASSWORD=pwd
DBHOST=host name
DBPORT=port

AWS_ACCESS_KEY_ID=access key
AWS_SECRET_ACCESS_KEY=secret access key
AWS_STORAGE_BUCKET_NAME=s3 bucket
EOF

chmod +x scripts/*.sh

./scripts/instance_os_dependencies.sh
./scripts/python_dependencies.sh
./scripts/gunicorn.sh
./scripts/nginx.sh
./scripts/start_app.sh
```
