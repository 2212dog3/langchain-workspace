# uv add pypdf
# uv add lanchain_community
from langchain_community.document_loders import PyPDFLoader
import os

file_path = "data\pdf_to_txt\KCI_FI003153549.pdf"

loader = PyPDFLoader(file_path)
pages = loader.load()

# print(pages)

pdf_file_name = os.path.basename(file_path)
pdf_file_name = os.path.splitext(pdf_file_name)[0]

result_txt = ""

for page in pages:
    result_txt += page.page_content

with open(f"out")