import matplotlib.pyplot as plt
from wordcloud import WordCloud
import nltk
from nltk.corpus import stopwords
from collections import Counter

# Sample text data
text = "The question of whether UFOs (Unidentified Flying Objects) are real is a subject of debate and investigation. UFOs, in the literal sense, refer to objects or phenomena that are observed flying in the sky but cannot be immediately identified or explained. While many UFO sightings turn out to have mundane explanations, some remain unexplained or mysterious.Government agencies, military organizations, and scientific groups around the world have investigated UFO sightings to determine if they represent a potential threat or if they have scientific significance. In some cases, UFOs have been associated with natural phenomena, misidentified aircraft or celestial objects, or even classified military technology. It's important to note that the term UFO does not necessarily imply that these objects are of extraterrestrial origin or proof of alien life. Most UFO sightings have alternative explanations grounded in science and technology. In recent years, there has been increased attention and disclosure from government sources about previously classified UFO-related information. This has sparked further interest and discussion on the topic. Whether or not UFOs represent evidence of extraterrestrial life or advanced technology beyond human understanding is a question that remains open, and scientific investigation continues. It's important to approach the topic with a critical and evidence-based perspective, as well as an understanding of the difference between an unidentified object and one that is definitively extraterrestrial. Ultimately, opinions on this matter may vary widely, but scientific inquiry and critical analysis remain crucial in understanding the nature of UFOs and their potential implications."
words = nltk.word_tokenize(text)
# Convert to lowercase
words = [word.lower() for word in words]
# Remove stopwords and punctuation
stop_words = set(stopwords.words('english'))
words = [word for word in words if word.isalnum() and word not in stop_words]
text = " ".join(words)
wordcloud = WordCloud(max_words=20,width=800, height=400, background_color='white').generate(text)

# Display the word cloud
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.title("Word Cloud")
#plt.show()
plt.savefig("Before.png")


# First extract the words from the actual word cloud.
exactwords = list(wordcloud.words_.keys())

words = nltk.word_tokenize(text)
words = [word.lower() for word in words]

stop_words = set(stopwords.words('english'))
filtered_words = [word for word in words if word.lower() not in stop_words]

word_freq = Counter(filtered_words)
ww = []
ff = []
tt = []
for word, freq in word_freq.items():
    if word in exactwords:
        print(f"{word}: {freq}")
        #ff.append(int(freq))
        #ww.append(word)
        for l in range(0,freq):
            tt.append(str(freq)+"_"+word)
            


text= " ".join(tt)

print(text)

wordcloud = WordCloud(max_words=20,width=800, height=400, background_color='white').generate(text)

# Display the word cloud
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.title("Word Cloud")
#plt.show()
plt.savefig("After.png")