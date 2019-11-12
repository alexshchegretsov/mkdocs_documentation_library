`web server vs app server`
=

- Web Server is designed to serve HTTP Content. App Server can also serve HTTP Content but is not limited to just HTTP. 
It can be provided other protocol support such as RMI/RPC
- Web Server is mostly designed to serve static content, though most Web Servers have plugins to support 
scripting languages like Perl, PHP, ASP, JSP etc. through which these servers can generate dynamic HTTP content.
- Most of the application servers have Web Server as integral part of them, that means App Server can do whatever Web Server is capable of. Additionally App Server have components and features to support Application level services such as Connection Pooling, 
Object Pooling, Transaction Support, Messaging services etc.
- As web servers are well suited for static content and app servers for dynamic content, 
most of the production environments have web server acting as reverse proxy to app server. 
That means while servicing a page request, static contents (such as images/Static HTML) are served by web server that interprets the request. 
Using some kind of filtering technique (mostly extension of requested resource) web server identifies dynamic content request and 
transparently forwards to app server.

Application Server is a term that sometimes is mixed with a web server. While a web server handles mainly HTTP protocols, 
the application server deals with several different protocols, including, but not limited, to HTTP.

The Web server's main job is to display the site content and the application server is in charge of the logic, 
the interaction between the user and the displayed content. 
The application server is working in conjunction with the web server, where one displays and the other one interacts.




`Web server`
=

Run python -m 'SimpleHTTPServer' and go to http://localhost:8080. What you see is a web server at its workings. The server simply serves files over HTTP stored on your computer. The key point is that all this is done on top of the HTTP protocol. There also exist FTP servers for example which do exactly the same thing (serving stored files) but on top of a different protocol.

`Application server`
=

Say we have a tiny application like below (snippet from Flask).

```
@app.route('/')
def homepage():
    return '<html>My homepage</html>'

@app.route('/about')
def about():
    return '<html>My name is John</html>'
```

The small example program maps the URL / to the function homepage() and the /about to the function about().

To run this code we need an application server (e.g. Gunicorn) - a program or module that can listen for requests from a client and using our code, return something dynamically. In the example we simply return some very bad HTML.

What's the business logic all the other people talk about? Well, since a URL maps to somewhere specifically in our codebase, we are hypothetically showing some logic about how our program works.

Recapping

web server - serves files stored somewhere (most commonly .css, .html, .js). Common web servers are Apache, Nginx or even Python's SimpleHTTPServer.

application server - serves files generated on the fly. Essentially most web servers have some sort of plugins or even come with built-in functionality to do that. There exist also strict application servers like Gunicorn (Python), Unicorn (Ruby), uWSGI (Python), etc.

Notice that you can actually build a web server with the code of the application server. This is done in some cases during development where you do not want to have a gazillion of different servers running on your computer.

