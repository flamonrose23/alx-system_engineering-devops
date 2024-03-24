Task 0 : simple web stack

/Users/fatimari/Downloads/Web\ infrastructure\ design\ \#1\ -\ Imgur.jpg </br>

## Description ##
It is a design explaining a simple web infrastructure hosting the website that is reachable via www.foobar.com.
This design of one server explaining the process of user or client wants to access the website or the network in general.

## Requirements of infrastructure with explication ##

* What is a server:
A server is a device, a virtual device or computer program or providing functionality for other programs or devices, called “clients”.

* What is the role of the domain name:
It is a human-readable address that users use to access the website. It's configured with a DNS "A" record pointing to the server's IP address (8.8.8.8).
The IP address and domain name alias is mapped in the Domain Name System (DNS).

* What type of DNS record www is in www.foobar.com:
This site uses a record and it can be checked by running dig www.foobar.com.

* What is the role of the web server:
A web server is a software that serves web pages to clients upon their request, it does this over the protocol HTTP.

* What is the role of the application server:
The application server executes dynamic code and communicates with the database.
The application server hosts your web application code. It processes dynamic requests, executes business logic, and interacts with the database when necessary. In this scenario, it’s responsible for running your code base.

* What is the role of the database:
It Is a collection of information that is stored and organized so that it can be easily accessed, updated and managed.

* What is the server using to communicate with the computer of the user requesting the website:
Communication between the client and the server occurs over the internet network through the TCP/IP protocol suite.

## Issues with infrastructure ##

* SPOF:
It means Single Point of Failure explained that this infrastructure has a single server and if it fails, the website becomes unavailable.
And to resolve this situation, load balancing shoulb be consideration a solution for this issue.

* Downtime when maintenance needed (like deploying new code web server needs to be restarted):
When deploying new code for example, users won’t be able to access the site during this period and a load balancer can be the solution also when website goes down.

* Cannot scale if too much incoming traffic:
The infrastructure cannot handle a lot of traffic especially with one server. So, by adding more servers, load balancing and optimization the database, considering as solutions to keep the server working efficienly and preserving good experience for user surfing on the website. 
