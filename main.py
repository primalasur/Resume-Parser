!pip install nltk python-docx
import docx
import nltk

nltk.download('punkt')
nltk.download('stopwords')

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist

def load_resume(file_path):
    doc = docx.Document(file_path)
    text = []
    for paragraph in doc.paragraphs:
        text.append(paragraph.text)
    return ' '.join(text)

def preprocess_resume(resume_text):
    tokens = word_tokenize(resume_text.lower())
    stop_words = set(stopwords.words('english'))
    cleaned_tokens = [token for token in tokens if token.isalnum() and token not in stop_words]
    return cleaned_tokens
def calculate_word_frequency(cleaned_tokens):
    fdist = FreqDist(cleaned_tokens)
    return fdist
def compare_keywords(resume_fdist, keywords):
    score = 0
    for keyword in keywords:
        score += resume_fdist[keyword]
    return score
# Set the keywords to match
keywords = ['python', 'machine learning', 'data analysis']

# Load and preprocess resumes
resume_files = ['resume1', 'resume2', 'resume3',]
resumes = []

for resume_file in resume_files:
    resume_text = load_resume(resume_file)
    cleaned_tokens = preprocess_resume(resume_text)
    resume_fdist = calculate_word_frequency(cleaned_tokens)
    score = compare_keywords(resume_fdist, keywords)
    resumes.append((resume_file, score))

# Sort resumes based on the score
resumes.sort(key=lambda x: x[1], reverse=True)

# Print the most suitable candidate
print("Most Suitable Candidate:")
print(resumes[0][0])
