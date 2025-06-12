from .models import Todo

class TodoListView(ListView):
    model = Todo

class TodoCreateView(CreateView):
    model = Todo
    fields = ['title','deadline']
    success_url = reverse_lazy('todo_list')