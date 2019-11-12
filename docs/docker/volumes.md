`volumes`
=

Volumes are the preferred mechanism for persisting data
generating by and used by docker containers.

use of volumes:

- decoupling container from storage
- share volume(storage/data) among different containers
- attach volume to container
- on deleting container - volume does not delete

```
docker volume --help

Usage:	docker volume COMMAND

Manage volumes

Commands:
  create      Create a volume
  inspect     Display detailed information on one or more volumes
  ls          List volumes
  prune       Remove all unused local volumes
  rm          Remove one or more volumes

```
