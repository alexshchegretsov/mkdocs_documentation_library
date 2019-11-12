`FROM`
=

The
`FROM` instruction tells the Docker Engine which base image to use for
subsequent instructions. Every valid Dockerfile must start with a FROM
instruction. The syntax is as follows:
```
FROM <image> [AS <name>]
OR
FROM <image>[:<tag>] [AS <name>]
OR
FROM <image>[@<digest>] [AS <name>]
```
Where <image> is the name of a valid Docker image from any public/
private repository. If the tag is skipped, 
Docker will fetch the image tagged
as the latest. This is verified by this simple step.


`WORKDIR`
=

`WORKDIR` instruction sets the current working directory for `RUN`, `CMD`,
`ENTRYPOINT`, `COPY`, and `ADD` instructions. The syntax is as follows:
`WORKDIR /path/to/directory`
`WORKDIR` can be set multiple times in a Dockerfile and, if a relative
directory succeeds a previous WORKDIR instruction, 
it will be relative to the
previously set working directory.

Now we’ll modify the Dockerfile to add couple of WORKDIR instructions.
```
FROM ubuntu:latest
WORKDIR /usr
WORKDIR src
WORKDIR app
CMD pwd

docker run this_image
/usr/src/app
```


