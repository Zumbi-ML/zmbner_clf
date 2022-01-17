from newspaper import Article
from utils import filehelper as fh

def scrape(input_path):
    """
    """
    urls = fh.read(input_path).split('\n')
    full_content = ""
    for url in urls:
        if (not url):
            continue
        try:
            article = Article(url)
            article.download()
            article.parse()
            full_content += article.text + "\n\n\n"
        except:
            pass
    return full_content

def scrape_n_save(input_file, output_file):
    """
    """
    full_content = scrape(input_file)
    fh.write(output_file, full_content)
