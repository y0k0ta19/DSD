print("3-18")

cats = [
    "Henri",
    "Grumpy",
    "Lucy",
]
animails = {
    "cats": cats,
    "octopi": {},
    "emus": {},
}
life = {
    "animals": animails,
    "plants": {},
    "other": {},
}

print(life["animals"]["cats"])