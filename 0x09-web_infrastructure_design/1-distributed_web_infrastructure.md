Task 1 : Distributed web infrastructure

![622A9A17-8881-4A08-A360-F43C543FEB60_1_105_c](https://github.com/flamonrose23/alx-system_engineering-devops/assets/128868164/33eab26c-a7d1-489a-bbd8-91eabdb187b4)

## Description ##

It is a design about adding 3 servers of web infrastructure hosting www.footer.com including two servers, a load balancer (HAProxy), an Nginx web server, an application server, a set of application files, and a MySQL database. This infrastructure atttempts to reduce the traffic to the primary server by distributing some of the load to a replica server with the help of a server that balances the load between the primary server and the replica server.
And the load balancer helps optimize performance and maintain high availability.

## Specifics About This Infrastructure ##

* For every additional element, why you are adding it:
Introducing an additional server allows us to incorporate a load balancer, effectively managing high volumes of incoming traffic. This helps handle lots of people visiting our site at once. Plus, it keeps us safe from problems if one server breaks down.

* What distribution algorithm your load balancer is configured with and how it works:
The distribution algorithm used by the load balancer is typically configured as part of its settings or configuration. One common algorithm is Round Robin, where the load balancer distributes incoming requests equally among the available servers in a circular order.
This algorithm works by using each server behind the load balancer that selects the next available server in the sequence to handle the request. After, the selected server processes the request and sends back the response to the user through the load balancer.For the next incoming request, the load balancer moves to the next server in the sequence, distributing the workload evenly across all servers.
And, the processus is continued in cycle routing each new request to the next available server in a rotating sequence.

* Is your load-balancer enabling an Active-Active or Active-Passive setup, explain the difference between both:
The HAProxy load-balancer is enabling an Active-Passive setup rather than an Active-Active setup. The difference between them is that in an Active-Active setup, both servers are actively serving traffic simultaneously, provinding load distribution ; otherwise , in an Active-Passive setup designates one server as the active server, while the other remains passive and takes over only if the active server fails, offering better failover capabilities.

* How a database Primary-Replica (Master-Slave) cluster works:
A Primary-Replica cluster in a MySQL database involves one Primary (Master) node and one or more Replica (Slave) nodes.However, the Primary server is capable of performing read/write requests while Replica nodes replicate data from the Primary and serve read operations.

* What is the difference between the Primary node and the Replica node in regard to the application:
The Primary node is responsible for write operations while the Replica node is capable of processing read operations.

## Issues With This Infrastructure ##

* Where are SPOF:
If the main MySQL database server goes down, the whole site can't be updated (like adding or deleting users). The server with the load balancer and the application server connecting to the main database are also single points of failure.

* Security issues (no firewall, no HTTPS):
Without a firewall or HTTPS encryption, the infrastructure may be vulnerable to security breaches, data interception, and unauthorized access. 

* No monitoring:
The absence of monitoring tools leaves the infrastructure blind to performance issues, security threats, and downtime causes.
