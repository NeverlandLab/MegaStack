from django.contrib import admin
from import_export.admin import ImportExportModelAdmin


class BaseAdmin(ImportExportModelAdmin):
    def changelist_view(self, request, extra_context=None):
        try:
            action = self.get_actions(request)[request.POST['action']][0]
            action_acts_on_all = action.acts_on_all
        except (KeyError, AttributeError):
            action_acts_on_all = False

        if action_acts_on_all:
            post = request.POST.copy()
            post.setlist(admin.helpers.ACTION_CHECKBOX_NAME,
                         self.model.objects.values_list('id', flat=True))
            request.POST = post

        return super(BaseAdmin, self).changelist_view(request, extra_context)
