Figxec
======

Easily run commands on your running docker containers.

Usage
-----

~~~
figxec [docker-exec-params] container-name-regex command [params]
~~~

So, for one off commands:

~~~bash
figxec web ps aux
~~~

For interactive stuff:

~~~bash
figxec -it db mysql -p
~~~

Details
-------

* The provided container name is used as a regexp, so for a container called
  `fig_web_1` you may use `fig_web`, `web` or even `w`
* If multiple commands match, the command will be run on just one of them
