
import re

def clean_resume(resume_text):
    # Remove URLs
    clean_text = re.sub('http\S+\s*', ' ', resume_text)
    # Remove RT and cc
    clean_text = re.sub('RT|cc', ' ', clean_text)
    # Remove hashtags
    clean_text = re.sub('#\S+', '', clean_text)
    # Remove mentions
    clean_text = re.sub('@\S+', '  ', clean_text)
    # Remove special characters
    clean_text = re.sub('[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""), ' ', clean_text)
    # Remove non-ASCII characters
    clean_text = re.sub(r'[^\x00-\x7f]', r' ', clean_text)
    # Remove extra whitespaces and newlines
    clean_text = re.sub(r'\s+', ' ', clean_text).strip()

    return clean_text


