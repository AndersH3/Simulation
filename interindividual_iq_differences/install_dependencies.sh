#!/bin/bash

# Check if pip3.11 is available
if ! command -v pip3.11 &> /dev/null
then
    echo "pip3.11 could not be found. Please ensure Python 3.11 and its pip are installed."
    exit 1
fi

# Upgrade pip to the latest version
echo "Upgrading pip..."
pip3.11 install --upgrade pip

# Install the necessary packages
echo "Installing numpy, matplotlib, pandas, and scipy..."
pip3.11 install numpy matplotlib pandas scipy

echo "All necessary packages have been installed successfully!"

