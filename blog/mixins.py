from django.shortcuts import render
from django.views.generic import View


class ObjectListView(View):
    model = None
    template = None
    queryset = None

    def get(self, slug):
        return render(self.request, self.template, context={self.model.__name__.lower() + 's': self.queryset})
