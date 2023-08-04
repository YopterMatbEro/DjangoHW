from django.http import HttpResponse
from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты;)
}

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }


def dish(request, recipe):
    if DATA[recipe]:
        subject_to_serving = DATA[recipe].copy()
        servings = int(request.GET.get("servings", 1))
        for ingredient, amount in DATA[recipe].items():
            subject_to_serving[ingredient] = round(amount * servings, 2)
        context = {
            'recipe': subject_to_serving
        }
        return render(request, 'calculator/index.html', context)
    else:
        return HttpResponse(f"Проверьте правильность введенных данных:"
                            f"\nrecipe: {recipe}/")
