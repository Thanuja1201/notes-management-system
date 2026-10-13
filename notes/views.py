from django.shortcuts import render, redirect
from .models import Note

# Create your views here.

def home(request):
    return render(request, 'home.html')


def category_notes(request, category):
    notes = Note.objects.filter(category=category)

    category_names = {
        'python': 'Python',
        'html': 'HTML',
        'css': 'CSS',
        'javascript': 'JavaScript'
    }

    return render(request, 'category.html', {
        'notes': notes,
        'category': category_names[category]
    })


def add_note(request):

    if request.method == 'POST':

        category = request.POST['category']
        question = request.POST['question']
        answer = request.POST['answer']

        Note.objects.create(
            category=category,
            question=question,
            answer=answer
        )

        return redirect(f'/{category}/')

    return render(request, 'add_note.html')

def edit_note(request, note_id):

    note = Note.objects.get(id=note_id)

    if request.method == 'POST':

        note.category = request.POST['category']
        note.question = request.POST['question']
        note.answer = request.POST['answer']

        note.save()

        return redirect(f'/{note.category}/')

    return render(request, 'edit_note.html', {
        'note': note
    })

def delete_note(request, note_id):

    note = Note.objects.get(id=note_id)

    category = note.category

    note.delete()

    return redirect(f'/{category}/')