from django.shortcuts import render


def index(request):
    return render(request, "coffee/index.html", {
        "page": "index",
        "heading": "Кофены төгс ертөнц",
    })


def about(request):
    steps = [
        {"number": "01", "title": "Алсын хараа",
         "text": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Ipsum quasi maiores, sapiente itaque provident error consequuntur. Cumque delectus voluptatem ea temporibus ipsa aut laudantium aspernatur!"},
        {"number": "02", "title": "Зорилго",
         "text": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Ipsum quasi maiores, sapiente itaque provident error consequuntur. Cumque delectus voluptatem ea temporibus ipsa aut laudantium aspernatur! Excepturi laudantium tempore, nam eaque, voluptas corrupti laborum."},
    ]
    return render(request, "coffee/about.html", {"page": "about", "steps": steps})


def menu(request):
    items = [
        {"name": "Mocha", "price": "9 500.00₮"},
        {"name": "Espresso", "price": "9 900.00₮"},
        {"name": "Americano", "price": "8 500.00₮"},
        {"name": "Cafe Latte", "price": "9 600.00₮"},
        {"name": "Frappuccino", "price": "9 800.00₮"},
        {"name": "Ice Coffee", "price": "8 800.00₮"},
    ]
    return render(request, "coffee/menu.html", {
        "page": "menu",
        "items": items,
        "description": "Lorem ipsum, dolor sit amet, consectetur, & adipiscing elit",
    })
