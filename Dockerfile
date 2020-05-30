FROM python:3.7.4
# Metadata
LABEL container.base.image="SimpleML"
LABEL software.name="SimpleML"
LABEL software.description="CLI tool for no code ML"
LABEL tags="ML"

RUN apt-get update
RUN apt-get install -y locales python3-pip python3-dev python3-virtualenv fabric \
      libpq-dev libjpeg-dev libxml2-dev libxslt-dev libfreetype6-dev libffi-dev \
      git curl wget
RUN apt-get install build-essential swig

RUN pip install --upgrade pip 
# Without LC_ALL setting httpretty installation fails
# Set the locale
RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8
# Needed for pytest when run tests with docker exec -it
ENV TERM xterm
WORKDIR /home/simpleML/

COPY requirements.txt /home/simpleML/requirements.txt
RUN pip3 install -r requirements.txt
#RUN pip3 install scikit-learn auto-sklearn pandas matplotlib numpy
# Copy MIDI Files
COPY simpleML/ /home/simpleML/

# Set Python3 as default python version
# RUN update-alternatives --install /usr/bin/python python /usr/bin/python3 1
CMD ["/bin/bash"]