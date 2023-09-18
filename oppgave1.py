print(" ==== Klasser og objekter ==== ")
print("\n=== A ===\n")

class Film:
    def __init__(self, filmtitle, releaseyear, score):
        self.filmtitle = filmtitle
        self.releaseyear = releaseyear
        self.score = score

    def get_description(self):
        return f"{self.filmtitle} was released in {self.releaseyear} and currently has a score of {self.score}"


film_1 = Film("Inception", 2010, 8.8)
film_2 = Film("The Martian", 2015, 8.0)
film_3 = Film("Joker", 2019, 8.4)

print(f"{film_1.filmtitle} was released in {film_1.releaseyear}"
      f" and currently has a score of {film_1.score}")


print("\n=== B ===\n")



print(film_1.get_description())
print(film_2.get_description())
print(film_3.get_description())
