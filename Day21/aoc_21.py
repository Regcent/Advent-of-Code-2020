import time
from typing import Union

class Recipe:

    def __init__(self, ingredients: list, allergens: list):
        self.ingredients = ingredients
        self.allergens = allergens

def run_script(filepath: str) -> Union[int, str, float, bool]:
    with open(filepath, "r") as f:
        raw_data = f.read()
    return main_function(raw_data)

def main_function(raw_data: str) -> Union[int, str, float, bool]:
    start_time = time.time()
    
    result = your_script(raw_data)

    elapsed_time = time.time() - start_time
    print(f"Time elapsed : {elapsed_time}s")
    return result

def your_script(raw_data: str) -> Union[int, str, float, bool]:
    """
    Time to code! Write your code here to solve today's problem
    """
    lines = raw_data.split("\n")
    all_ingredients = []
    all_allergens = []
    candidates = {}
    recipes = {}
    for i in range(len(lines)):
        ingredients, allergens = lines[i].split(" (")
        ingredient_list = ingredients.split(" ")
        allergens = allergens.replace("contains ", "").replace(")", "")
        allergens = allergens.split(", ")
        recipes[i] = Recipe(ingredient_list, allergens)
        for ingredient in ingredient_list:
            if ingredient in all_ingredients:
                continue
            all_ingredients.append(ingredient)
        for allergen in allergens:
            update_candidates(allergen, ingredient_list, candidates)
            if allergen in all_allergens:
                continue
            all_allergens.append(allergen)
            
    non_allergen_ingredients = []
    for ingredient in all_ingredients:
        non_allergen_ingredients.append(ingredient)
    for allergen in all_allergens:
        for ingredient in candidates[allergen]:
            if ingredient in non_allergen_ingredients:
                non_allergen_ingredients.remove(ingredient)
    print(non_allergen_ingredients)
    total = 0
    for recipe_id in recipes:
        for ingredient in recipes[recipe_id].ingredients:
            if ingredient in non_allergen_ingredients:
                total += 1
    print(f"Part 1 answer : {total}")
    clean_candidates(candidates)
    sorted_allergens = list(candidates.keys())
    sorted_allergens.sort()
    return ",".join([candidates[allergen][0] for allergen in sorted_allergens])

def clean_candidates(candidates: dict):
    used_singleton_allergens = []
    singleton_allergen = ""
    singleton_ingredient = ""
    while True:
        for allergen in candidates:
            if allergen in used_singleton_allergens:
                continue
            if len(candidates[allergen]) == 1:
                singleton_allergen = allergen
                singleton_ingredient = candidates[allergen][0]
                break
        if singleton_allergen == "":
            break
        for allergen in candidates:
            if allergen == singleton_allergen:
                continue
            if singleton_ingredient in candidates[allergen]:
                candidates[allergen].remove(singleton_ingredient)
        used_singleton_allergens.append(singleton_allergen)
        singleton_allergen = ""

def update_candidates(allergen: str, ingredient_list: list, candidates: dict):
    if allergen not in candidates:
        candidates[allergen] = []
        for ingredient in ingredient_list:
            candidates[allergen].append(ingredient)
    else:
        to_remove = []
        for ingredient in candidates[allergen]:
            if ingredient not in ingredient_list:
                to_remove.append(ingredient)
        for ingredient in to_remove:
            candidates[allergen].remove(ingredient)

if __name__ == "__main__":
    print(run_script("input.txt"))