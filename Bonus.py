movies = [
    ("The Shawshank Redemption", 1994, [9, 10, 10, 9, 8, 9]),
    ("The Godfather", 1972, [10, 9, 8, 10, 9, 7]),
    ("Pulp Fiction", 1994, [9, 8, 7, 8, 6, 5]),
    ("The Dark Knight", 2008, [10, 9, 9, 8, 9, 8]),
    ("Schindler's List", 1993, [8, 9, 9, 7, 6, 8]),
    ("The Room", 2003, [1, 2, 3, 4, 5, 1])
]

def calculate_avg_rating():
    movies_avg_rating = []
    for i in range(len(movies)):
        rate = movies[i][2]
        avg_rating = sum(rate)/ len(rate)
        movies_avg_rating.append((movies[i][0], movies[i][1], round(avg_rating, 2)))
    return movies_avg_rating


def display_movies_avg_rating(avg: float):
    # sort_by_rate = int(input('Enter avg rating you want to display movies with: '))
    movies_avg_rating = calculate_avg_rating()
    sorted_data = sorted(movies_avg_rating, key=lambda x: x[2])
    for i in sorted_data:
        print(f'{i[0]} ({i[1]}) - Avergae rating: {i[2]} ★')
