from datetime import date
from django.shortcuts import render

all_posts = [
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
    },
    {
        "slug": "visit-the-bridge",
        "image": "bridge.jpg",
        "author": "Afrishella",
        "date": date(2023, 3, 20),
        "title": "enjoying bridge view",
        "excerpt": "this bridge have history happy and sad life happen here.",
        "content": """Lorem ipsum dolor sit amet consectetur adipisicing elit. Distinctio natus atque porro. Expedita autem enim quis, sapiente esse, rerum sit reprehenderit officiis eligendi suscipit maiores illo accusamus atque veniam deleniti.

        Lorem ipsum dolor sit amet consectetur adipisicing elit. Distinctio natus atque porro. Expedita autem enim quis, sapiente esse, rerum sit reprehenderit officiis eligendi suscipit maiores illo accusamus atque veniam deleniti.

        Lorem ipsum dolor sit amet consectetur adipisicing elit. Distinctio natus atque porro. Expedita autem enim quis, sapiente esse, rerum sit reprehenderit officiis eligendi suscipit maiores illo accusamus atque veniam deleniti.

        Lorem ipsum dolor sit amet consectetur adipisicing elit. Distinctio natus atque porro. Expedita autem enim quis, sapiente esse, rerum sit reprehenderit officiis eligendi suscipit maiores illo accusamus atque veniam deleniti.
        """
    },
    {
        "slug": "camp-on-the-wood",
        "image": "wood.jpg",
        "author": "Yoon He",
        "date": date(2023, 3, 30),
        "title": "Camping on the wood",
        "excerpt": "be the one with nature and feel the fresh air.",
        "content": """Lorem ipsum dolor sit amet consectetur adipisicing elit. Distinctio natus atque porro. Expedita autem enim quis, sapiente esse, rerum sit reprehenderit officiis eligendi suscipit maiores illo accusamus atque veniam deleniti.

        Lorem ipsum dolor sit amet consectetur adipisicing elit. Distinctio natus atque porro. Expedita autem enim quis, sapiente esse, rerum sit reprehenderit officiis eligendi suscipit maiores illo accusamus atque veniam deleniti.

        Lorem ipsum dolor sit amet consectetur adipisicing elit. Distinctio natus atque porro. Expedita autem enim quis, sapiente esse, rerum sit reprehenderit officiis eligendi suscipit maiores illo accusamus atque veniam deleniti.
        
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Distinctio natus atque porro. Expedita autem enim quis, sapiente esse, rerum sit reprehenderit officiis eligendi suscipit maiores illo accusamus atque veniam deleniti.
        """
    }
]

# Create view


def get_date(post):
    return post["date"]


def starting_page(request):
    sorted_post = sorted(all_posts, key=get_date)
    latest_post = sorted_post[-3:]
    return render(request, "blog/index.html", {
        "posts": latest_post
    })


def posts(request):
    return render(request, "blog/all-posts.html", {
        "all_posts": all_posts
    })


def post_detail(request, slug):
    identified_post = next(post for post in all_posts if post["slug"] == slug)
    return render(request, "blog/post-detail.html", {
        "post": identified_post
    })
