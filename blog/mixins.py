from django.shortcuts import render


class ObjectListView:
    model = None
    template = None
    queryset = None

    def get(self, slug):
        print(self.model)
        print(self.template)
        print(self.queryset)
        return render(self.request, self.template, context={self.model.__name__.lower() + 's': self.queryset})
