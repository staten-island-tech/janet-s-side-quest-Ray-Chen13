movie_store = {
    "Inception": {"price": 4, "stock": 3, "genre": "Sci-Fi"},
    "The Conjuring": {"price": 5, "stock": 2, "genre": "Horror"},
    "Titanic": {"price": 3, "stock": 0, "genre": "Romance"},
    "Avengers": {"price": 6, "stock": 5, "genre": "Action"},
    "Joker": {"price": 4, "stock": 4, "genre": "Drama"}

}

rental_request = {
    "Inception": 1,
    "The Conjuring": 1,
    "Titanic": 1,
    "Avengers": 2}


""" for i, values in rental_request.items():
    for x, value in movie_store:
        if values <= value:
            print(f"Movie {x} is out of stock.")
 """
z = 0
a = 0
for i, values in rental_request.items():
    z = z + values
for x, value in movie_store.items():
    a = (a + value["price"])
if ["genre"] == "Horror":
    a = a-2
    print(a)
elif value["stock"] == 0:
    print(f"Movie {x} is out of stock.")
if value["stock"] == 0:
    print(f"Movie {x} is out of stock")
    if z >= 3:
        a * 0.95
print(a*.95)