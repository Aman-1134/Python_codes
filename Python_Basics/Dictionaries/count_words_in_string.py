essay = """
Education is an essential part of our lives. We are nothing without knowledge, and education is what separates us from others. The main step to acquire education is enrolling oneself in a school. School serves as the first learning place for most of the people. Similarly, it is the first spark in receiving an education. My school is my second home where I spend most of my time. Above all, it gives me a platform to do better in life and also builds my personality. I feel blessed to study in one of the most prestigious and esteemed schools of the city. In addition, my school has a lot of assets which makes me feel fortunate to be a part of it. In this essay on my school, I will tell you why I love my school and what my school has taught me. 
"""

ctr = 0
word_count = dict()
essay_words = essay.split()
print(essay_words)
for i in essay_words:
    if i.lower() == 'school':
        ctr += 1

print(ctr)
for word in essay_words:
   if word_count.get(word) == None:
       word_count[word] = 0
   else:
       word_count[word] =+ 1
print(word_count)
