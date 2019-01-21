from django.views.generic.edit import FormView
from django.http.response import HttpResponse
from rescue.forms import ProfileImageForm
from rescue.models import ProfileImage

class ProfileImageView(FormView):
    template_name = 'profile_image_form.html'
    form_class = ProfileImageForm

    def form_valid(self, form):
        profile_image = ProfileImage(
            image=self.get_form_kwargs().get('files')['image'])
        profile_image.save()
        self.id = profile_image.id

        return HttpResponse('File Uploaded')
