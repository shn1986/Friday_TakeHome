# Friday_TakeHome
 
Setting up a PySpark environment using virtual environment
This guide will walk you through the process of setting up a PySpark environment using virtual environment. This will allow you to run PySpark code without interfering with other Python environments or packages on your system.

Prerequisites
    Python 3.6 or later
    pip
    virtualenv
Step 1: Install virtualenv
    pip install virtualenv

Step 2: Create a virtual environmentStep 2: Create a virtual environment
    virtualenv spark_env
    This will create a new directory called spark_env that contains the necessary files for the virtual environment.

Step 3: Activate the virtual environment
    Activate the virtual environment by running the following command in your command prompt
    spark_env\Scripts\activate.bat
    You should see the name of the virtual environment in the command prompt, indicating that it is active.

Step 4: Install PySpark
    pip install pyspark
    This will install the latest version of PySpark and its dependencies in the virtual environment.

Step 5: Verify the installation
    To verify the installation, run the following command in the virtual environment:
    python -c "import pyspark; print(pyspark.__version__)"

Step 6: Deactivate the virtual environment
    When you are done working with PySpark, you can deactivate the virtual environment by running the following command:
    deactivate
    You should now see the command prompt change back to the original state.

Note
You will need to activate the virtual environment each time you want to use PySpark by running the command spark_env\Scripts\activate.bat and deactivate it when you are done using it by running the command deactivate.

Tips
You can install other packages in the virtual environment by using pip. For example, you can install pandas by running pip install pandas command.
You can also specify a specific version of PySpark to be installed by running the command pip install pyspark==3.0.1
You can also specify the path of python executable of your virtual environment while creating it, by running the command virtualenv spark_env -p C:\Python38\python.exe
This will give you a clean and isolated environment to work with PySpark, without interfering with other Python environments or packages on your system.