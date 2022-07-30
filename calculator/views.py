from django.shortcuts import render, reverse

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
}


def home_view(request):
    template_name = 'home.html'
    pages = {
        'Омлет': reverse('omlet'),
        'Паста': reverse('pasta'),
        'Бутерброд': reverse('buter')
    }

    context = {
        'pages': pages
    }
    return render(request, template_name, context)



def omlet(request):
    servings = request.GET.get('servings', 1)
    recipe = DATA.get('omlet')
    context = {
        'recipe': {key: value * int(servings) for key, value in recipe.items()}
    }
    return render(request, 'calculator.html', context)


def pasta(request):
    servings = request.GET.get('servings', 1)
    recipe = DATA.get('pasta')
    context = {
        'recipe': {key: value * int(servings) for key, value in recipe.items()}
    }
    return render(request, 'calculator.html', context)


def buter(request):
    servings = request.GET.get('servings', 1)
    recipe = DATA.get('buter')
    context = {
        'recipe': {key: value * int(servings) for key, value in recipe.items()}
    }
    return render(request, 'calculator.html', context)

