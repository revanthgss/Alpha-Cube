# Brahmastra

## Problem
During disaster the communication between the relief forces and victims become a major problem due to low network connectivity. 
Also many lives are lost due to lack of proper evacuation and placement of the relief camp.
Our idea is to solve this problem by creating a USSD based messaging service which aims to bring faster connectivity between victim and relief forces. We want to focus on usability in low connection situations. We will also work on giving the best location for the Emergency response team and also compute evacuation paths effectively during various natural tragedies.

## Idea
1. As USSD based services are session based, they are fast when compared to SMS based systems. So this system will work even in areas with lower network connectivity.It allows survivors to ask for help through a quick and efficient process. Also Genetic Algorithm can be used to get the best location for Emergency response team. 
2. We are also building an algorithm which dynamically generates the evacuation routes(only if road connectivity is there) during emergency situations. The location data of the persons are taken from the USSD service. The region where most persons are there is computed and it is given most priority for support by relief teams. If road connectivity is possible, we also find efficient routes to the relief camp.

## Features
1. The victim can ask for help or support by selecting through various options.
2. The relief forces are able to show recent updates/location of relief camps to the victim.
3. This will find the most efficient location in which it can serve all the locations within the city once emergency happens. 
4. Generating the Evacuation Routes during Disaster occurence.
