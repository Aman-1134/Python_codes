text = """
Education is an essential part of our lives. We are nothing without knowledge, and education is what separates us from others. The main step to acquire education is enrolling oneself in a school. School serves as the first learning place for most of the people. Similarly, it is the first spark in receiving an education. My school is my second home where I spend most of my time. Above all, it gives me a platform to do better in life and also builds my personality. I feel blessed to study in one of the most prestigious and esteemed schools of the city. In addition, my school has a lot of assets which makes me feel fortunate to be a part of it. In this essay on my school, I will tell you why I love my school and what my school has taught me. 
"""
text_s = text.split()
text_count = dict()
for text in text_s:
    text_count[text] = 0
for text in text_s:
    text_count[text] += 1

print(text_count)
sorted_items = sorted(text_count.items(), key=lambda x: x[1], reverse=True)
print(sorted_items[:10])