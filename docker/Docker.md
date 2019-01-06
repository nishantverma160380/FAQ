----------------------------------------------------------------------------------------------------------------------------------------------------------
Docker Certified Associate Test Review Questions Set 1
-----------------------------------------------------------------------------------------------------------------------------------------
Question 1
Which of the following Dockerfile options creates a mount point with the specified name and marks it as holding externally mounted volumes from native host or other containers?
A	WORKDIR
B	VOLUME ---------------------
C	RUN
D	ONBUILD
Question 2
Dockerfile option EXPOSE publish the port to external systems. True or false?
A	True
B	False -----------------------
Question 3
Which of the Dockerfile options initializes a new build stage and sets the base image for subsequent instructions?
A	CMD
B	ONBUILD
C	FROM --------------------
D	RUN
Question 4
What does docker image rm command do?
A	Display detailed information on one or more images
B	Show the history of an image
C	Remove one or more images -----------------------
D	Remove unused images
Question 5
Which of the following is NOT how to create an efficient image via a Dockerfile?
A	Combine multiple applications into a single container -------------------
B	Use multi-stage builds
C	Avoid installing unnecessary packages
D	Start with an appropriate base image
Question 6
What Dockerfile option LABEL does?
A	Provide defaults for an executing container
B	Tells Docker how to test a container to check that it is still working
C	Label a container that will run as an executable
D	Adds metadata to an image ------------------------------
Question 7
Which of the Dockerfile options executes any commands in a new layer on top of the current image and commit the results?
A	RUN -----------------------
B	ONBUILD
C	FROM
D	CMD
Question 8
Which of the following docker image commands display detailed information on one or more images?
A	docker image history
B	docker image ls
C	docker image inspect ---------------------
D	docker image detail
Question 9
What docker image prune command does?
A	Display detailed information on one or more images
B	Remove one or more images
C	Remove unused images ---------------------
D	Show the history of an image
Question 10
What Dockerfile option EXPOSE does?
A	Label a container that will run as an executable
B	Informs Docker that the container listens on the specified network ports at runtime ------------------------
C	Expose defaults for an executing container
D	Adds metadata to an image


----------------------------------------------------------------------------------------------------------------------------------------------------------
Docker Certified Associate Test Review Questions Set 2
----------------------------------------------------------------------------------------------------------------------------------------------------------
Question 1
Which of the following statements is incorrect?
When a container is deleted, the writable layer is persisted. -------------------------
The column 'size' of docker ps -s output shows the amount of data that is used for the writable layer of each container.
Copy-on-write is a Docker strategy of sharing and copying files for maximum efficiency.
The column 'virtual size' of docker ps -s output shows the amount of data used for the read-only image data used by the container plus the container's writable layer 'size'.
Question 2 WRONG
Each container shares common writeable container layer. True or false?
True
False -------------------------
Question 3 CORRECT
Docker image is built up from a series of layers and each layer represents an instruction in the image's Dockerfile. True or false?
False
True -------------------------
Question 4 CORRECT
Which of the following is NOT a valid way to tag a Docker image?
Tag an image referenced by Name
Tag an image referenced by user ID -------------------------
Tag an image referenced by image ID
Tag an image referenced by Name and Tag
Question 5 WRONG
What is the docker command for displaying layers of a Docker image?
docker layers
docker image layers
docker history -------------------------
docker info
Question 6 CORRECT
Which of the following is the correct command to tag an image?
docker tag image SOURCE_IMAGE[:TAG] TARGET_IMAGE[:TAG]
docker tag TARGET_IMAGE[:TAG] SOURCE_IMAGE[:TAG]
docker tag SOURCE_IMAGE[:TAG] TARGET_IMAGE[:TAG] -------------------------
docker build tag SOURCE_IMAGE[:TAG] TARGET_IMAGE[:TAG]
Question 7 WRONG
Which of the following is the correct command to store an image to a registry?
docker upload [OPTIONS] NAME[:TAG]
docker commit [OPTIONS] NAME[:TAG]
docker store [OPTIONS] NAME[:TAG]
docker push [OPTIONS] NAME[:TAG] -------------------------
Question 8 CORRECT
What is the image storage solution that is part of Docker Enterprise Edition called?
Docker Registry
Universal Control Plane
Docker Trusted Registry -------------------------
Docker Hub
Question 9 CORRECT
What is the docker command to remove one or more images?
docker delete
docker remove
docker image rm -------------------------
docker image delete
Question 10 CORRECT
What is the docker command to pull an image or a repository from a registry?
docker deploy
docker pull -------------------------
docker checkout
docker build


----------------------------------------------------------------------------------------------------------------------------------------------------------Docker Certified Associate Test Review Questions Set 3a - Orchestration
----------------------------------------------------------------------------------------------------------------------------------------------------------
Question 1
What is the default format of docker inspect output?
A	json -------------------------------------------
B	html
C	xml
D	yaml
Question 2
Which of the following is the docker command to enable autolock on an existing swarm cluster?
A	docker swarm update --autolock-swarm=true
B	docker swarm update --autolock=true ---------------------------------
C	docker swarm autolock
D	docker swarm --autolock=true
Question 3
What is the function of docker inspect command?
A	To manage Docker configs
B	To display system-wide information
C	To inspect changes to files or directories on a container's filesystem
D	To return low-level information on Docker objects --------------------------------
Question 4
What is the difference between a replicated and a global service?
A	Replicated service runs one task on every node. Global service runs multiple task on every node.
B	Good candidates for replicated service are monitoring agents that you want to run on every node in the swarm. Good candidates for global service are http servers.
C	Number of identical tasks can be specified for a replicated service. There is no pre-specified number of tasks for global service. ------------------
D	Replicated service can only be deployed on manager node. Global service can be deployed on both manager and worker node.
Question 5
What are the two types of docker swarm services?
A	local and global services
B	replicated and global services -------------------------------------------
C	distributed and replicated services
D	replicated and local services


----------------------------------------------------------------------------------------------------------------------------------------------------------
Pivotal Cloud Foundry (PCF) Certification Exam Review Questions and Answers Set 3 – Cloud Foundry Architecture
----------------------------------------------------------------------------------------------------------------------------------------------------------
Question 1
Which of the following is the function of Doppler?
A	Gathers logs from Metron
B	Exposes app logs
C	Handles client requests for logs
D	Persists app packages and droplets to the Blobstore
Question 2
Which of the following is a component of Loggregator?
A	Brain
B	Doppler
C	Metron
D	Blobstore
Question 3
Which of the following is NOT a component in PCF Elastic Runtime?
A	Diego
B	Virtual switch
C	Loggregator
D	Cloud Controller API
Question 4
Containers are run within ...
A	A blobstore
B	A Doppler
C	A Metron
D	A cell
Question 5
What is a droplet?
A	A websocket endpoint that exposes app logs, container metrics and ER component metrics
B	A component that CF uses to create and manage isolated environments called containers
C	A staged app packaged with everything needed to run in a container
D	An open framework for managing the full development and deployment life cycle of large-scale distributed software applications.
Question 6
Which of the following is a component of Diego?
A	Brain
B	Loggregator
C	Doppler
D	Cloud Controller
Question 7
Which of the following are components of Brain?
A	Metron and Executor
B	Auctioneer and Converger
C	Doppler and Converger
D	Auctioneer and Executor
Question 8
Which of the following is a component of Cloud Controller?
A	Metron
B	Brain
C	Doppler
D	Stager
Question 9
What are the two data stores used by the Cloud Controller?
A	Blobstore and buildpacks
B	Blobstore and CC_DB
C	Droplets and buildpacks
D	Droplets and CC_DB
Question 10
What is Cloud Foundry's API endpoint for?
A	Provides access to the system and to manage spaces and orgs
B	Represents a Cell in the BBS/Auctions
C	Handles client requests for logs
D	Schedules tasks and Long-Running Processes (LRPs)




----------------------------------------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------------------------------------------


