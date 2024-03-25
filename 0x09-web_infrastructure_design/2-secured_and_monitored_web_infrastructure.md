Task 2 : Secured and monitored web infrastructure

![317160E7-8FA9-4219-97EF-66F321DD12A5](https://github.com/flamonrose23/alx-system_engineering-devops/assets/128868164/3a080530-cba2-43c3-a4e8-25273916c62e)

## Description ##

It is a design of a 3 servers web infrastructure that hosts the website www.foobar.com, it must be secured, serve encrypted traffic, and be monitored.

## Specifics About This Infrastructure ##

* What are firewalls for:
Firewalls serve to protect computer networks from unauthorized access or malicious activity by controlling incoming and outgoing network traffic. They enhance security by controlling and monitoring traffic, safeguarding the infrastructure from potential threats.

* Purpose of SSL Certificate:
SSL Certificate for HTTPS: Enables secure and encrypted communication, protecting sensitive data during transmission.

* Why is the traffic served over HTTPS:
Traffic is served over HTTPS (Hypertext Transfer Protocol Secure) to ensure secure communication between the client (such as a web browser) and the server. 

* What monitoring is used for:
Detecting and responding to security threats, anomalies, or suspicious activities within a system or network to prevent data breaches, unauthorized access, or other security incidents.

* How the monitoring tool is collecting data:
As a tool used of agents collect data for monitoring from servers and tracking the performance of the system and securing operations.

* Explain what to do if you want to monitor your web server QPS:
By following these steps, we can effectively monitor the Query Per Second (QPS) of the web server, enabling proactive management and ensuring optimal performance:
Choose a monitoring tool ; Install a monitoring agent on the server ; Configure QPS metrics and set up alerts and nalyze metrics, optimize performance, and scale resources as needed.

## Issues With This Infrastructure ##

* Terminating SSL at the load balancer level is an issue because it would leave the traffic between the load balancer and the web servers unencrypted.

* Having only one MySQL server capable of accepting writes is an issue because it is not scalable and can act as a single point of failure for the web infrastructure.

* Having servers with all the same components (database, web server and application server) might be a problem:
It can cause resource contention, such as competition for CPU, memory, and I/O. This can result in slow performance and make it hard to pinpoint issues. Additionally, such a setup isn't easily expandable.
