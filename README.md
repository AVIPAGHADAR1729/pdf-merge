# PDF-MERGE API Using Flask and PyPDF
## In This Project Use API to Merge Multiple PDFs into Single PDF

### **Usage Description**

### API Link **https://pdf-merger-easily.herokuapp.com/pdfmerge**


<div class="termy">

```console

import requests


URL = "https://pdf-merger-easily.herokuapp.com/pdfmerge"


print(URL)

files = (
    ("file", open("1.pdf", "rb")),
    ("file", open("2.pdf", "rb")),
    ("file", open("3.pdf", "rb")),
)


print(files, sep="\n")

resp = requests.post(URL, files=files)

print(resp)

with open("out-merged.pdf", "wb") as fw:
    fw.write(resp.content)

print("Complete")


```
