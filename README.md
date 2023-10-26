# BT_BDD_project

The following are the steps needed to run the Automation on the react site.

#### 🛠 How to Run Locally?
1. Install [Python3](https://www.python.org/downloads/) and [Pipenv](https://pypi.org/project/pipenv/).
   If you had installed python and Pipenv previously, No need to re-install again.

2. Clone this repository and rename the folder as per your requirement.

  Your directory structure should appear as follows;
  ```structure
  BT_BDD_Project
      ├── features
        ├── steps
            ├── add_items_to_cart.py
            ├── filter_validation_sizes.py
        ├──add_items_to_cart.feature
        ├──filter_validation.feature
      ├── behave.ini
      ├── helpers.py
      ├── pipfile
      └── requirements.txt
  ```
3. Installing **Requirements** is important. **(in root)**
   for Mac Users,
  ```requirements1
    python3 -m pip install -r requirements.txt 
  ```
  for Linux Users,
  ```requirements1
    pip install -r requirements.txt 
  ```
4. Navigate to root of **BT_BDD_Project** and run the following commands to test the features;
  
  For checking the filter validation:
  ```
    behave features/Filter_validation.feature
  ```
  For checking cart validation
  ```
    behave features/add_items_to_cart.feature
  ```
5. The output can be seen with the result of how many testcases passed and which scenario's failed.
 

