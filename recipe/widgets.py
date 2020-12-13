from django import forms

class PreviewFileWidget(forms.ClearableFileInput):
    template_name = "/widgets/preview_file.html"

    class Media:
        js = [
            "//code.jquery.com/jquery-3.4.1.min.js",
        ]
