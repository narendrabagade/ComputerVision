# ComputerVision
Install OpenCV with other required libraries to start. 
We have used Miniconda to create the Python environment, and this installation is tested on a macOS-m1 chip,Let’s start the installation!
**Step 1**: Install Miniconda
**Step 2**: Understanding the Base Environment
        After successful installation, by opening the terminal, one should be able to see `base` in the command line. This indicates that you are in the base environment of      miniconda. Now, the best part about miniconda is you can create virtual environments with specific Python versions. Now, you can create multiple venvs with a specific Python version within it.
**Step 3**: Create a New Conda Environment with Python 3.11
        Create a new environment:
            conda create --name opencv-env python=3.11
        Activate the environment:
            conda activate opencv-env
        Verify the Python version in the environment:
            python --version
**Step 4**: Check and Upgrade pip
        Check pip version:
          pip --version
        Upgrade pip:
          pip install --upgrade pip

**Install OpenCV and Other Required Libraries**
  Now, whether you are using any Python environment (local virtual environment or Conda environment), you can install OpenCV and all the required libraries using pip.
  We will use the pip package manager to install all packages. You can install any package by simply typing "pip install" followed by the package name. You can install multiple packages simultaneously by typing on the same line.

The key package to install is:
    pip install opencv-contrib-python streamlit moviepy jupyter matplotlib ipykernel 
    
    pip install pyautogui mediapipe mime
    
And we are done with the installation!
