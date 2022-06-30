full_name = "Luis Mendoza Ramirez"
nickname = "Luis"
age = 19
has_used_python = True

hobbies = [
  "working out", "watching anime", "playing video games", "running", "playing soccer"
]

favorites = {
  "movie": "Interstellar",
  "number": 21,
  "food": "chicken sandwich",
  "hobby": hobbies[0],
  "anime": "One Piece",
  "game" : "Ghost of Tsushima"
}

print(f"Hello world! My name is {full_name}, but many of my friends call me {nickname}. I am {age} years old.")
print()
print(f"Has Python Experience: {has_used_python}")
print()

for key in favorites.keys():
    print(f"My favorite {key} is {favorites[key]}.")
  
print()
print(f"Here are some of my other hobbies: {hobbies}")

all_vars = dict(vars())