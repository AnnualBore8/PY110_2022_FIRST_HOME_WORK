def human_years_cat_years_dog_years(years: int) -> list:
    years = int(years)
    animal_1 = 15
    animal_2 = 9
    cat_other = 4
    dog_other = 5
    ans = []
    humanYears = years

    if years == 1:
        catYears = dogYears = animal_1
    elif 1 < years <= 2:
        catYears = dogYears = animal_1 + animal_2
    elif 3<= years:
        catYears = (years - 2) * cat_other + animal_1 + animal_2
        dogYears = (years - 2) * dog_other + animal_1 + animal_2
    else:
        print('Так не может быть!')

    return [humanYears, catYears, dogYears]

assert human_years_cat_years_dog_years(1) == [1, 15, 15]
assert human_years_cat_years_dog_years(2) == [2, 24, 24]
assert human_years_cat_years_dog_years(10) == [10, 56, 64]