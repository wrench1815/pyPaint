# pyPaint

A Paint program using Python 3 and Tkinter

# Libraries used

This Project uses Python 3.8 along with an inbuilt module called Tkinter. Although This project is build in Python version 3.8.3, but it will work with any Python 3 version. Unless there any changes to the Tkinter Module.

# How to Run on your Machine

Download the Windows Executable from [releases Page](https://github.com/wrench1815/pyPaint/releases)

Or if you wish to build it on your own or try editing code etc, follow below steps.

## Steps to Setup Working Dev Environment

1. Clone the Repo by either forking or downloading Zip.
2. Extract the File if Downloaded using Zip method.
3. Open a Terminal in the Folder and setup a _Python Virtual Environment_ using **venv**.

   - ### Windows

     ```powershell
     py -3.8 -m venv <virtual_environment_name>
     ```

   - ### Linux/MacOS

     ```shell
     python3.8 -m venv <virtual_environment_name>
     ```

     where &lt;virtual_environment_name&gt; is your preferred name for Virtual Environment

4. Activate the Environment by executing `activate` file stored in the Virtual Environment.

   ```shell
   # for Linux or Mac
   source ./<virtual_environment_name>/bin/activate

   # for Windows
   ./<virtual_environment_name>/scripts/activate
   ```

5. Check for any updates available using `pip` if required
6. Install the Dependencies from `requirements.txt`

   ```shell
   # works same on Windows, linux and MacOs
   pip install -r requirements.txt
   ```

7. Now run by simply using these Commands

   ```shell
   # for Windows use py
   py -3.8 main.py

   #for MacOS or Linux use python
   python3.8 main.py
   ```

# License

This Project is Licensed Unlicensed. It means You are free to do whatever you want with the code and use wherever you want to.
