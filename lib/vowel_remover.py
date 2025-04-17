# File: lib/vowel_remover.py

class VowelRemover:
    def __init__(self, text):
        self.text = text
        self.vowels = ["a", "e", "i", "o", "u"]
        self.new_text = ""

    def remove_vowels(self):
        i = 0
        while i < len(self.text):
            # We want to iterate over the string and add to a new 
            if self.text[i].lower() not in self.vowels:
                self.new_text += self.text[i]
            i += 1
        return self.new_text