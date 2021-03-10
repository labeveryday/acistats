# ACI Stats

This is an app that monitor's aci for changes and health stats. Then alerts a webex room.

Use this script to learn the basics of python.

> NOTE: This code will run on Linux, MAC and Windows

## Download the Code

To get started: Download the code and cd to the `acistats` directory

```bash
git clone https://github.com/labeveryday/acistats.git
cd acistats
```

## Python Virtual Environment

When executing python code or installing python packages you should get into the practice of creating and managing python virtual environments.
This will allow you to run different versions of a python library while avoiding software version conflicts. My preferred tool for python virtual environments is [venv](https://docs.python.org/3/library/venv.html)
There are many other tools available. Remember to explore and find the one that works best for you.

**On Linux or Mac**

```python
python3 -m venv venv
source venv/bin/activate
```

**On Windows**

```cmd
python3 -m venv venv
.\venv\Scripts\activate.bat
```

## Install project requirements

Once you have your virtual environment setup and activated you will need to install your python packages. One way to do this is by doing `pip install <python package>`. For this project use the example listed below. It will installed the required libraries and dependencies for this specific project.

```bash
pip install -r requirements.txt
```

## Results

When `main.py` is executed the script with query the always on apic for health and tenant information. Then it will send an update to a webex room. 

![No new tenant](https://github.com/labeveryday/Notes/blob/main/images/nonewtenant.png)

![new tenant](https://github.com/labeveryday/Notes/blob/main/images/newtenant.png)
