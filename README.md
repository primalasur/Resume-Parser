# Resume Parser
This repository contains a Python code implementation of a basic resume parser using NLTK (Natural Language Toolkit) in Jupyter Notebook. The resume parser analyzes the content of multiple resume files in DOCX format and identifies the most suitable candidate for a job based on keyword matching.

# Features
Loads resume data from DOCX files.
Preprocesses the resume text by tokenizing and removing stopwords.
Calculates the word frequency distribution of the cleaned tokens.
Compares the keyword frequency in the resume with a list of predefined keywords.
Ranks the resumes based on the keyword matching score and identifies the most suitable candidate.

# Installation
1. Clone the repository:
git clone https://github.com/your-username/resume-parser.git

2. nstall the required libraries:
pip install nltk python-docx

# Usage
Place the resume files (in DOCX format) in the same directory as the Jupyter Notebook file.

Open the Jupyter Notebook (resume_parser.ipynb) and run the code cells.

Modify the keywords list in the code to match your desired keywords for candidate evaluation.

The code will process the resumes, calculate the relevance scores, and identify the most suitable candidate based on the keyword matching.

# Examples
The repository includes sample resume files (resume1.docx, resume2.docx, resume3.docx) for testing and demonstration purposes. Feel free to replace them with your own resume files.

# License
This project is licensed under the MIT License. See the LICENSE file for more information.

# Acknowledgments
The code in this repository is a basic implementation of a resume parser and serves as a starting point for more advanced resume parsing and analysis tasks.

# Contributions
Contributions to this project are welcome. If you find any issues or want to add new features, please create a pull request.

# Disclaimer
Please note that this code provides a basic resume parsing functionality and may require customization and further development to meet specific use cases and handle complex resume formats. Test the code thoroughly and adapt it according to your requirements.
