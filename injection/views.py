from django.shortcuts import render
from .forms import DocumentForm
from .models import Document

# executing uploaded file does not work
def index(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile=request.FILES['docfile'])
            newdoc.save()

            return render(request, 'injection.html')
    else:
        form = DocumentForm()  # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    return render(
        request,
        'injection.html',
        {'documents': documents, 'form': form},
    )
