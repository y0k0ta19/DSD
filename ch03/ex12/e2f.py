e2f = { "dog" : "chien", "cat" : "chat", "walrus" : "morse"}
f2e = dict([item[::-1] for item in e2f.items()])
print(f2e)

# result
# mbpA1989:ex12 y0k0ta19$ python3 e2f.py                                                                                                             [master]
# {'chien': 'dog', 'chat': 'cat', 'morse': 'walrus'}