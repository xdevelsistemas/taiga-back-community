# Copyright (C) 2014 Andrey Antukh <niwi@niwi.be>
# Copyright (C) 2014 Jesús Espino <jespinog@gmail.com>
# Copyright (C) 2014 David Barragán <bameda@dbarragan.com>
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from django.contrib import admin
from django.contrib.contenttypes import generic

from . import models


class AttachmentAdmin(admin.ModelAdmin):
    list_display = ["id", "attached_file", "project", "owner", "content_type", "content_object"]
    list_display_links = ["id", "attached_file",]
    list_filter = ["content_type"]
    search_fields = ["id", "name", "project__name", "project__slug", "object_id"]
    readonly_fields = ["project", "owner", "content_type", "content_object"]

    def has_add_permission(self, request):
        return False


class AttachmentInline(generic.GenericTabularInline):
     model = models.Attachment
     fields = ("attached_file", "owner", "is_deprecated", "order", "description")
     extra = 0


admin.site.register(models.Attachment, AttachmentAdmin)
