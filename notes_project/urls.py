from django.contrib import admin
from django.urls import path
from notes.views import home, category_notes, add_note, edit_note, delete_note
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),

    path('python/', category_notes, {'category': 'python'}, name='python_notes'),
    path('html/', category_notes, {'category': 'html'}, name='html_notes'),
    path('css/', category_notes, {'category': 'css'}, name='css_notes'),
    path('javascript/', category_notes, {'category': 'javascript'}, name='javascript_notes'),

    path('add/', add_note, name='add_note'),
    path('edit/<int:note_id>/', edit_note, name='edit_note'),
    path('delete/<int:note_id>/', delete_note, name='delete_note'),
]