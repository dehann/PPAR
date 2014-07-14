PPAR
====

Basically an LCM wrapper for querying values from a json file. The initial purpose of this little project is to standardize parameter distribution amount multiple projects.

Write your parameters in human readible json file format, point the pparService.py at this file and querying the json file will be available over LCM. This prevents me from hardcoding parameters over and over in several scirps or projects -- especially in different languages.

At present there is little error checking and robustness built into this code -- will be added as dependcy on ppar grows in the future.

Dependencies
------------

::

    sudo apt-get install cmake python
    
MIT LCM must also be installed:

::

    cd ~/Downloads
    wget http://lcm.googlecode.com/files/lcm-1.0.0.tar.gz
    tar xzf lcm-1.0.0.tar.gz
    cd lcm-1.0.0
    ./configure
    make -j
    sudo make install
    sudo ldconfig
    
    
Installing
----------

To get the code:

::

     cd ~
     git clone https://github.com/dehann/PPAR.git
     cd PPAR
     mkdir build
     cd build
     cmake ..
     make

Python path variable must include

::
     
     ??/PPAR/build/include/lcmtypes/ppar
     and the lcm functions, please see LCM documentation
     
Running the service
-------------------

At present the python program runs directly from in src directory, which isn't great, but this has been a quick turnaround little project -- more later...

::
     
     cd PPAR/src
     python pparService.py ??/some_param_file.json

The json file
-------------

At minimum, the json file should include the LCM channel names with which requests and replies will be sent. For example, you'll see data/example.json has at least:

::
    
    {
      "ppar" : {
        "lcm" : {
          "reply-channel" : "PPAR_REPLY_EXAMPLE",
          "request-channel" : "PPAR_REQUEST_EXAMPLE"
        }
      }
    }

