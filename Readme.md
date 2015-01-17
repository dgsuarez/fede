Fede (Fast & Easy Docker Exec)
======

Easily run commands on your running docker containers.

Usage
-----

###Exec

~~~
fede exec [docker-exec-params] container-name-regex command [params]
~~~

So, for one off commands:

~~~bash
fede exec web ps aux
~~~

For interactive stuff:

~~~bash
fede exec -it db mysql -p
~~~

###Stub

~~~
fede stub stub-name [docker-exec-params] container-name-regex command [params]
~~~

So the same as for exec, but adding a stub name to the beginning. This will
create an executable file in `.fede/stubs` with the given name that'll run
fede exec with the given parameters when called, so for example:

~~~bash
fede stub mysql -it db mysql
~~~

And then...

~~~bash
./fede/stubs/mysql -p
~~~

Finally, if you add .fede/stubs to your `$PATH`...

~~~
mysql -p
~~~

And it'll just run inside your `db` container!


Details
-------

* The provided container name is used as a regexp, so for a container called
  `fig_web_1` you may use `fig_web`, `web` or even `w`
* If multiple commands match, the command will be run on just one of them
