from datetime import date
from django.shortcuts import render

posts = [
    {
        "slug": "hike-on-the-mountains",
        "image": "mountain.jpg",
        "author": "Muhlifain",
        "date": date(2023, 3, 8),
        "title": "Journey to Mountains.",
        "excerpt": "Theres nothing like high and coding and i am very glad with this time travel achievements. outstanding view love it love it yeah.",
        "content": """Lorem ipsum dolor sit amet consectetur adipisicing elit. Distinctio natus atque porro. Expedita autem enim quis, sapiente esse, rerum sit reprehenderit officiis eligendi suscipit maiores illo accusamus atque veniam deleniti.
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Distinctio natus atque porro. Expedita autem enim quis, sapiente esse, rerum sit reprehenderit officiis eligendi suscipit maiores illo accusamus atque veniam deleniti.
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Distinctio natus atque porro. Expedita autem enim quis, sapiente esse, rerum sit reprehenderit officiis eligendi suscipit maiores illo accusamus atque veniam deleniti.
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Distinctio natus atque porro. Expedita autem enim quis, sapiente esse, rerum sit reprehenderit officiis eligendi suscipit maiores illo accusamus atque veniam deleniti.
        """
    }
]

# Create view


def starting_page(request):
    return render(request, "blog/index.html")


def posts(request):
    return render(request, "blog/all-posts.html")


def post_detail(request, slug):
    return render(request, "blog/post-detail.html")
