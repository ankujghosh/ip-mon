# ip-mon
OpenSource IP monitoring and RPM(Real-Time Performance Monitoring) project written in python with many features

About:

This project provides the feature to monitor remote IP host and logs to filenamed rpm.log

It is currently created for linux machine and require superuser permission to run.

Current Version 

23122018 : ipmon.v1.0.py

Requirement:

* pyhton3 installed
* Require sudo rights as the file is written in /var/log/ folder, but code can be editted to wtite to local home folder to avoid super user access

Current Features:

23122018:
* Only log when the connection fails/passes to avoid un-necessary storage issue.
* Accept user input as  IPv4 to probe, delay between ping(sec), threshold value to pass/fail a connection.
* Logging can be enabled to a specific timestamp(accordance to local time), can be left blank for infinite monitoring
  -Watch the Youtube demo how to use, Check the "External Resources:" section
* Logs ping and mtr report to rpm.log when the connection fails

Upcoming Features:

23122018:
* Route failover in case of Multiple ISP deployment
* Multiple host monitoring
* IPv6 Capability
* Continous logging
* File size limitation when continuous logging enabled
* Email Notification on connection status change
* Collection of Local Interface, IP Stack, CPU, Memory Stats under troubleshooting logs
* Create different file while collecting troubleshooting logs
* Collect predictable logs when the network degrades

Pending Task:

23122018:
* Rigorous tesing on all param to evaluate exceptions
* Need to log if the program is stopped due to kernel sigterm messages
* Adding help menu to the program

External Resources:

Youtube Demo Link : https://youtu.be/gKOd4sx8dCc

Notes:

I have started learning python recently and believe in learning with realtime problem solving. I created this project to use it on my home Rasberry-Pi

  Please suggest

* Any other feature which can be included, taken that I will improve the core project i.e. IP monitoring and RPM(Real-Time Performance Monitoring)
* Please suggest any kind of testing which I can perform
* 

Credits:

goos3bumps

Contacts:

networkingbaseline@gmail.com

Other thoughts:

None for now
