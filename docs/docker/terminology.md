`container`
==

Container – a running instance that encapsulates required software. 
Containers are always created from images. A container can expose ports and volumes to interact with other containers or/and the outer world. 
Containers can be easily killed / removed and re-created again in a very short time. 
Containers don’t keep state.


`image`
==

Image – the basic element for every container. 
When you create an image, every step is cached and can be reused (Copy On Write model). 
Depending on the image, it can take some time to build. Containers, on the other hand, can be started from images right away.

`layers`
==

A layer is a modification applied to a Docker image as represented by an
instruction in a Dockerfile. Typically, a layer is created when a base image
is changed—for example, consider a Dockerfile that looks like this:

```
FROM ubuntu
Run mkdir /tmp/logs
RUN apt-get install vim
RUN apt-get install htop
```

Now in this case, Docker will consider Ubuntu image as the base image
and add three layers:

- One layer for creating /tmp/logs
- One other layer that installs vim
- A third layer that installs htop

When Docker builds the image, each layer is stacked on the next and
merged into a single layer using the union filesystem. Layers are uniquely
identified using sha256 hashes. This makes it easy to reuse and cache
them. When Docker scans a base image, it scans for the IDs of all the layers
that constitute the image and begins to download the layers. If a layer
exists in the local cache, it skips downloading the cached image.


`port`
==

Port – a TCP/UDP port in its original meaning. 
To keep things simple, let’s assume that ports can be exposed to the outer world (accessible from the host OS) or 
connected to other containers – i.e., accessible only from those containers and invisible to the outer world.

`volume`
==

Volume – can be described as a shared folder. 
Volumes are initialized when a container is created. 
Volumes are designed to persist data, independent of the container’s lifecycle.

`registry`
==

Registry – the server that stores Docker images. 
It can be compared to Github – you can pull an image from the registry to deploy it locally, and push locally built images to the registry.

`docker hub`
==

Docker Hub – a registry with web interface provided by Docker Inc. 
It stores a lot of Docker images with different software. 
Docker Hub is a source of the “official” Docker images made by the Docker team or 
in cooperation with the original software manufacturer (it doesn’t necessary mean that these “original” 
images are from official software manufacturers). Official images list their potential vulnerabilities. 
This information is available to any logged-in user. There are both free and paid accounts available. 
You can have one private image per account and an infinite amount of public images for free.

`Dockerfile`
==

A Dockerfile is a set of instructions that tells Docker how to build an image.
A typical Dockerfile is made up of the following:

- A `FROM` instruction that tells Docker what the base
image is
- An `ENV` instruction to pass an environment variable
- A `RUN` instruction to run some shell commands (for
example, install-dependent programs not available in
the base image)
- A `CMD` or an `ENTRYPOINT` instruction that tells Docker
which executable to run when a container is started

`Docker Engine`
==

Docker Engine is the core part of Docker. Docker Engine is a client-server
application that provides the platform, the runtime, and the tooling for
building and managing Docker images, Docker containers, and more.
Docker Engine provides the following:
- Docker daemon
- Docker CLI
- Docker API

`Docker daemon`
=

The Docker daemon is a service that runs in the
background of the host computer and handles the
heavy lifting of most of the Docker commands.
The daemon listens for API requests for creating
and managing Docker objects, such as containers,
networks, and volumes. Docker daemon can also
talk to other daemons for managing and monitoring
Docker containers. Some examples of inter-daemon
communication include communication Datadog for
container metrics monitoring and Aqua for container
security monitoring.

`Docker CLI`
==

Docker CLI is the primary way that you will interact with Docker. Docker
CLI exposes a set of commands that you can provide. The Docker CLI
forwards the request to Docker daemon, which then performs the
necessary work.

Most common commands:

- `docker build`
- `docker pull`
- `docker run`
- `docker exec`

`Docker API`
=

`Docker Compose`
=

Docker Compose is a tool for defining and running multi-container
applications. Much like how Docker allows you to build an image for your
application and run it in your container, Compose use the same images
in combination with a definition file (known as the compose file) to build,
launch, and run multi-container applications, including dependent and
linked containers.
The most common use case for Docker Compose is to run applications
and their dependent services (such as databases and caching providers)
in the same simple, streamlined manner as running a single container
application.

