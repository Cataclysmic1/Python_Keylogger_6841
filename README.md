# General Guide

## Installation

First, clone the repository to a suitable place on your machine:

```https://github.com/Cataclysmic1/Python_Keylogger.git```

Next, when you are in the root directory of the cloned repository, setup your virtual python environment:
```
python3 -m venv venv

source venv/bin/activate
```

Now install the required dependencies for the requirements.txt file:

```pip install -r requirements.txt```

## Utilisation

To use the python keylogger you have **2** options. You can either use:

- **Script1.py**
  
  or

- **Script2.py**

Both of these scripts generally do the same thing, however there are a few key differences that you should keep in mind when choosing which one you want to use and compile with.

**Script1.py** has more features than Script2.py such as the capability to copy the clipboard and not display a command prompt screen while running the keylogger. This script when compiled, is placed into a folder, alongside its dependencies as files. The allows Sript1 to be harder to detect by Windows Defender, at the cost of being a little more suspicious to the victim. However, through social engineering, the victim could be led to believe that the folder that contains the script alongside its dependencies exist to perform tasks sch as disk cleanup, etc..

**Script2.py** has similar features to Script1.py except the ones mentioned above. What sets Script2 apart from Script1, is that it is able to be compiled into a standalone .exe file with no other files needed for it to run. However, this comes at the cost of Windows defender being able to flag the keylogger easier, thus Script2 having less features to avoid being detected while being a standalone .exe.

## Compiling

To compile either one of these scripts, we will be using a tool called **Nuitka**, which was automatically installed when the **requirements.txt** installed all the dependencies needed for the project. This tool is similar to pyintaller but it also is able to convert the python code to native C/C++, naturally obfuscating the code, making it harder to flag and reverse engineer.

**Script1.py**:

```nuitka --standalone --windows-console-mode=disable --msvc=latest Script1.py```

Placeholder

**Script2.py**:

```nuitka --standalone --onefile --msvc=latest Script2.py```

Placeholder
