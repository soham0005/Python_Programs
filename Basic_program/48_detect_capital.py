import string
def detect_capital(word):
    if word == word.lower() or word == word.upper() or word == string.capwords(word):
        return True
    else: 
        return False
ans = detect_capital("FlAg")
# ans = detect_capital("soHam")
print(ans)
