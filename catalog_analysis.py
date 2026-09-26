import math

movies = [
    {
        "title": "The Dune Chronicles",
        "year": 2021,
        "genres": {"sci-fi", "drama"},
        "rating": 8.6,
        "duration_min": 155,
        "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"],
    },
    {
        "title": "Kitchen Stories",
        "year": 2019,
        "genres": {"comedy", "drama"},
        "rating": 7.1,
        "duration_min": 98,
        "actors": ["A. Novak", "M. Ferguson"],
    },
    {
        "title": "silent hours",
        "year": 2016,
        "genres": {"thriller", "drama"},
        "rating": 6.4,
        "duration_min": 112,
        "actors": ["J. Bloom", "K. Lee"],
    },
    {
        "title": "Comet Racers",
        "year": 2023,
        "genres": {"sci-fi", "action"},
        "rating": 5.9,
        "duration_min": 101,
        "actors": ["O. Isaac", "P. Diaz"],
    },
    {
        "title": "The Last Bakery",
        "year": 2014,
        "genres": {"comedy"},
        "rating": 7.8,
        "duration_min": 89,
        "actors": ["A. Novak", "T. Chalamet"],
    },
    {
        "title": "midnight in oslo",
        "year": 2020,
        "genres": {"thriller", "mystery"},
        "rating": 8.9,
        "duration_min": 124,
        "actors": ["K. Lee", "R. Ferguson"],
    },
    {
        "title": "Garden of Static",
        "year": 2022,
        "genres": {"drama"},
        "rating": 4.8,
        "duration_min": 137,
        "actors": ["P. Diaz", "J. Bloom"],
    },
    {
        "title": "The Quiet Algorithm",
        "year": 2024,
        "genres": {"sci-fi", "drama"},
        "rating": 9.2,
        "duration_min": 118,
        "actors": ["M. Ferguson", "O. Isaac"],
    },
    {
        "title": "Two Left Shoes",
        "year": 2011,
        "genres": {"comedy"},
        "rating": 6.0,
        "duration_min": 95,
        "actors": ["A. Novak", "K. Lee"],
    },
    {
        "title": "Red Harbor",
        "year": 2018,
        "genres": {"action", "thriller"},
        "rating": 7.3,
        "duration_min": 129,
        "actors": ["P. Diaz", "T. Chalamet"],
    },
]


def average_rating(movies):
    return round(sum(i["rating"] for i in movies) / len(movies), 1)


def catalog_age_stats(movies, current_year=2026):
    sps = [current_year - i["year"] for i in movies]
    return max(sps), min(sps), math.ceil(sum(sps) / len(sps))


def duration_in_hours(minutes):
    return f"{minutes // 60}ч {minutes % 60}м"


def rating_tier(rating):
    otv = None
    if rating < 5:
        otv = "слабо"
    elif rating < 7:
        otv = "средне"
    elif rating < 9:
        otv = "хорошо"
    return otv if otv is not None else "шедевр"


def decade_label(year):
    match year:
        case _ if year < 2015:
            return "старые"
        case _ if year <= 2020:
            return "недавние"
        case _:
            return "новые"


def count_long_movies(movies, threshold=120):
    c = 0
    for i in movies:
        if i["duration_min"] > threshold:
            c += 1
    return c


def normalize_title(title):
    return " ".join([word[0].upper() + word[1:] for word in title.split()])


def make_slug(title):
    return title.lower().replace(" ", "-")


def format_report_line(movie):
    return f'"{normalize_title(movie["title"])}" ({movie["year"]}) — {
        movie["rating"]
    }/10, {duration_in_hours(movie["duration_min"])}, жанры: {
        ", ".join(sorted(movie["genres"]))
    }'


def titles_sorted_by_rating(movies):
    return sorted(
        [(movie["title"], movie["rating"]) for movie in movies],
        key=lambda pair: pair[1],
        reverse=True,
    )


def top_n_by_rating(movies, n=3):
    return titles_sorted_by_rating(movies)[:n]


def count_by_genre(movies):
    res = {}
    for movie in movies:
        for genre in movie["genres"]:
            res[genre] = res.get(genre, 0) + 1
    return res


def actor_filmography(movies):
    res = dict()
    for movie in movies:
        for actor in movie["actors"]:
            if actor in res:
                res[actor].append(movie["title"])
            else:
                res[actor] = [movie["title"]]
    return res


def all_genres(movies):
    s = set()
    for i in movies:
        s.update(set(i["genres"]))
    return s


def common_actors(movie1, movie2):
    return set(movie1["actors"]) & set(movie2["actors"])


def genres_only_in_one(movies_a, movies_b):
    return all_genres(movies_a) - all_genres(movies_b)


def iter_high_rated(movies, min_rating=8.0):
    for movie in movies:
        if movie["rating"] >= min_rating:
            yield movie


def build_report(movies):
    print("ОТЧЕТ ПО КАТАЛОГУ")
    print(f"Средний рейтинг: {average_rating(movies)}")
    print(f"Средний возраст фильмов: {catalog_age_stats(movies)[-1]} лет\n")
    print("Топ-3 фильма:")
    movies_by_title = {movie["title"]: movie for movie in movies}
    for title, _ in top_n_by_rating(movies):
        print(f"    {format_report_line(movies_by_title[title])}")
    print("\nФильмов по жанрам:")
    genre_counts = count_by_genre(movies)
    sorted_genres = sorted(
        genre_counts.items(),
        key=lambda pair: (-pair[1], pair[0]),
    )
    for genre, count in sorted_genres:
        print(f"  {genre} — {count}")
    genres = ", ".join(sorted(all_genres(movies)))
    print(f"\nВсе жанры каталога: {genres}")


if __name__ == "__main__":
    # P.S. я так понял, что здесь без выводов предыдущих этапов
    # (а в некоторых работу надо было сделать внути main)
    # Выполненные полностью предыдущие этапы с выводами
    # можно посмотреть по коммитам, если я неверно понял формат вывода,
    # на последнем 9ом,
    # не думаю, что нужно снижать оценку
    build_report(movies)
