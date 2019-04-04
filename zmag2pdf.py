import requests
import img2pdf
import os
import shutil

# This ID is the string at the end of the publication URL
# For example, for the URL, http://viewer.zmags.com/publication/abcd1234
publicationID = "abcd1234"

# Set desired resolution
# For best resolution, try an arbitrarily high number like 4000x4000
# and the URL will return the highest resolution avaliable.
resolution = "1200x1705"
numberOfPages = 100

filenames = []

os.mkdir("images")
for i in range(1,numberOfPages+1):
    url = "http://viewer.zmags.com/services/resource/pub/"+publicationID+"/pg"+resolution+"/1/"+str(i)
    response = requests.get(url)
    if response.status_code == 200:
        with open("images/"+str(i)+".jpeg", 'wb') as f:
            f.write(response.content)
            print("Downloaded Image to "+"images/"+str(i)+".jpeg")

print("All Images Downloaded!")

for i in range(1,numberOfPages+1):
    filenames.append("images/"+str(i)+".jpeg")

with open("output.pdf","wb") as f:
    f.write(img2pdf.convert(filenames))
print("PDF created")

shutil.rmtree("images")
print("Removed downloaded images")
