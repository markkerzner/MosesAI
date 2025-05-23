## Setup Local Environment 

1. **Create and activate Virtual Environment**
   - Run the following command to create a virtual environment:
     ```sh
     python -m venv myenv
     source myenv/bin/activate
     python -m pip install --upgrade pip setuptools wheel
     ```
2. **Install IPython Kernel**
    - Install `ipykernel` to attach the Jupyter environment to the same kernel:
      ```sh
      pip install ipykernel && \
      python -m ipykernel install --user --name=myenv --display-name "My env"
      ```

3. **Install Lab Requirements**
   - Install the lab requirements specified in the `requirements.txt` file:
     ```sh
     pip install -r requirements.txt
     ```
4. **Create .env File for all API Keys**
    - We use one .env file at the root of all labs
   
5. **Start Jupyter Lab**
   - Start Jupyter UI with the command:
     ```sh
     jupyter lab
     ```


