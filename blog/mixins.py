from django.shortcuts import render
from django.core.paginator import Paginator


class ObjectListView:
    model = None
    template = None
    queryset = None

    def get(self, slug):
        print(self.request.user)
        pages = Paginator(self.queryset, 1)
        posts = pages.page(self.request.GET.get('page', 1))
        return render(self.request, self.template, context={self.model.__name__.lower() + 's': posts})
