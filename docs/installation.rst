Getting Started
===============

Docker
------

Development
***********

::

  docker build -t footyhints:latest .
  docker run -d -p 5000:5000 footyhints:latest

Production
**********

::

  docker build -t footyhints:latest --build-arg FOOTYHINTS_TYPE=production --build-arg FOOTYHINTS_API_TOKEN=<INSERT API TOKEN HERE> --no-cache .
  docker run -d -p 5000:5000 footyhints:latest

