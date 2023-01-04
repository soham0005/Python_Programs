def word_search(doc_list, keyword):
   
    indices = [] 
    
    for i, doc in enumerate(doc_list):
        tokens = doc.split()
        normalized = [token.rstrip('.,').lower() for token in tokens]
        if keyword.lower() in normalized:
            indices.append(i)
    return indices

ans = word_search(["The Learn Python Challenge Casino.", "They bought a car", "Casinoville"],"casino")
print(ans)