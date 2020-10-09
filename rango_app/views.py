from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from rango_app.models import Category, Page
from rango_app.forms import CategoryForm
from rango_app.forms import PageForm
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.text import slugify


def index(request):
    context_dict = {}
    context_dict['boldmessage'] = 'Crunchy, creamy, cookie, candy, cupcake!'
    category_list = Category.objects.order_by('-likes')[:10]
    context_dict['categories'] = category_list
    # Render the response and send it back!
    for category in category_list:
        category.slug = slugify(category.name)

    return render(request, 'index.html', context=context_dict)


def show_category(request, slug):
    context_dict = {}
    try:
        category = Category.objects.get(slug=slug)

        pages = Page.objects.filter(category=category)

        context_dict['pages'] = pages
        context_dict['category'] = category
    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['pages'] = None

    return render(request, 'category.html', context=context_dict)


def add_category(request):
    form = CategoryForm()
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('/')
        else:
            print(form.errors)
    return render(request, 'add_category.html', {'form': form})


def add_page(request, slug):
    try:
        category = Category.objects.get(slug=slug)
    except Category.DoesNotExist:
        category = None

    if category is None:
        return redirect('/')

    form = PageForm()

    if request.method == 'POST':
        form = PageForm(request.POST)

        if form.is_valid():
            if category:
                page = form.save(commit=False)
                page.category = category
                page.views = 0
                page.save()

                return redirect(reverse('show_category',
                                        kwargs={'slug':
                                                slug}))
        else:
            print(form.errors)

    context_dict = {'form': form, 'category': category}

    return render(request, 'add_page.html', context=context_dict)


def about_us(request):
    return render(request, 'info.html')
