# Manhwa
The 9 Best Fantasy Manhwa website hosted on AWS

# Website links
### Load balancer DNS
- http://manhwa-loadbalancer-1444081216.ap-south-1.elb.amazonaws.com
### Domain
<ins>Expiry on 15 October 2025</ins>
- http://bestmanhwa.tech/
- https://bestmanhwa.tech/

# Tasks
- <ins>**Deploy a web application**</ins>\
  The web application, inspired by "[The 50 Best Fantasy Manhwa You Must Read Now](https://animemangatoon.com/best-fantasy-manhwa-webtoons/)" is deployed using Django with Python 3.11.5.
  - <ins>**Display a list of manhwa titles, their genres, and brief descriptions using mock data**</ins>\
    The website is dynamically loaded using the JavaScript file which fetches JSON of mock data from the RDS. It uses basic HTML, CSS and JS.
  - <ins>**Hosted on a cloud platform</ins>**
    - The website is hosted on AWS and has EC2 instance with autoscaling, target groups, load balancer and launch template.
    - The static files and the images are stored in S3 bucket with public view access.
    - A RDS database is used to save and load the JSON data for dynamic loading which is passed to JavaScript.
- <ins>**Auto-scaling enabled**</ins>\
  Auto-scaling is enabled supported by launch template, target group and load balancer. More [info]() is included here.
- <ins>**Security measures**</ins>
  - <ins>**Enabling HTTPS**</ins>\
    Domain name is added to hosted zones with Route 53 and SSL certificate generated from AWS Certificate Manager.
  - <ins>**Configure firewall**</ins>\
    Security groups are set-up with APN which allows access to only 80 (HTTP) and 443 (HTTPS), and are forwarded to 8000 (Deployment) port. The rest of the traffic from different ports are refused connection.
