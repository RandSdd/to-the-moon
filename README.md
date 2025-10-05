A simple Titanic survival prediction model using Logistic Regression and 
Scikit-learn. scheduled to be updated with more models and techniques.

1. Environment
Python version: 3.10+
Git version: 2.51.0+

Recommended dependencies:
pip install -r requirements.txt
Example requirements.txt is in the storage folder.

Virtual environment setup
# Windows (PowerShell recommended)
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt

# macOS/Linux
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

For Windows user, PS is recommended
if any errors of rights
please run in PowerShell as administrator
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser

2. Run

Before you run, download train.csv test.csv from Kaggle and
place them in your index

Option 1 – Run directly

python Titanic.py

Option 2 – Jupyter Notebook

jupyter notebook LR_Titanic.ipynb

3. Results(to be filled)
| Model               | Accuracy | Precision | Recall | F1-score |
| ------------------- | -------- | --------- | ------ | -------- |
| Logistic Regression | 0.763    |     \     |    \   |     \    |

Note: The code uses random_state=42 for data splitting and model 
initialization to ensure reproducible results.
train : val : test = 0.6 : 0.2 : 0.2

4. Dataset Source

Titanic dataset: Kaggle – Titanic: Machine Learning from Disaster

5. Acknowledgment
SecFFL Laboratory, Nanjing University of Posts and Telecommunications
Open-source contributors from Scikit-learn, Matplotlib, and Kaggle community
Any specific mentors or collaborators who provided feedback



