# grammatical-error-detection

mkdir grammar-checker
cd grammar-checker
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install flask torch transformers nltk

import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')

Get-ExecutionPolicy
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

Start Python Interpreter: After activating the virtual environment, start the Python interpreter by typing:

bash
Copy code
python
Download NLTK Resources: Now you can enter the following commands one at a time within the Python interpreter:

python
Copy code
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
Exit the Python Interpreter: Once you have downloaded the required resources, you can exit the Python interpreter by typing:

python
Copy code
exit()
