# Import necessary libraries
import PyPDF2
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

# Open the PDF file in read mode
with open('steeringwheel.pdf', 'rb') as f:
    pdf_reader = PyPDF2.PdfReader(f)
    text = ''
    for page in pdf_reader.pages:
        text += page.extract_text()


# Close the PDF file
f.close()

# Create a WordCloud object and generate the word cloud
stopwords = set(STOPWORDS)
wordcloud = WordCloud(width = 800, height = 800, 
                background_color ='white', 
                stopwords = stopwords, 
                min_font_size = 10).generate(text)

# Plot the word cloud
plt.figure(figsize = (8, 8), facecolor = None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad = 0)
  
plt.show()