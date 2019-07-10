surprise = ["Groucho", "Chico", "Harpo"]
# surprise[-1] = "Harpo".lower()
# print("Harpo".lower())
surprise[-1] = surprise[-1].lower()
print(surprise)
surprise = surprise[::-1]
print(surprise)
surprise[0] = surprise[0].capitalize()
print(surprise)

# result
# ['Groucho', 'Chico', 'harpo']
# ['harpo', 'Chico', 'Groucho']
# ['Harpo', 'Chico', 'Groucho']