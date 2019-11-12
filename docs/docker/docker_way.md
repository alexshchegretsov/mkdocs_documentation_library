`Docker way`
=

Docker has some restrictions and requirements, depending on the architecture of your system (applications that you pack into containers). 
You can ignore these requirements or find some workarounds, but in this case, you won’t get all the benefits of using Docker. 
My strong advice is to follow these recommendations:

- 1 application = 1 container.
- Run the process in the foreground (don’t use systemd, upstart or any other similar tools).
- Keep data out of containers – use volumes.
- Do not use SSH (if you need to step into container, you can use the docker exec command).
- Avoid manual configurations (or actions) inside container.


