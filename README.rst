PPAR
====

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


