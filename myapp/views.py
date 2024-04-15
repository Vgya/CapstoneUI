# myapp/views.py
from django.shortcuts import render
from .forms import FileUploadForm

def file_upload_view(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # Handle uploaded file here
            uploaded_file = request.FILES['file']
            # You can perform operations with the uploaded file
    else:
        form = FileUploadForm()
    return render(request, 'file_upload.html', {'form': form})
