from .meta import Input
from formful import widgets
from markupsafe import Markup


class TextInput(Input, widgets.TextInput):
    pass


class TextArea(widgets.TextArea):

    def __call__(self, field, **kwargs):
        kwargs.setdefault("id", field.id)
        kwargs['class'] += " form-control"
        flags = getattr(field, "flags", {})
        for k in dir(flags):
            if k in self.validation_attrs and k not in kwargs:
                kwargs[k] = getattr(flags, k)
        return Markup(
            "<textarea {}>\r\n{}</textarea>".format(
                html_params(name=field.name, **kwargs),
                escape(field._value())
            )
        )


class PasswordInput(widgets.PasswordInput):
    def __call__(self, field, **kwargs):
        if self.hide_value:
            kwargs["value"] = ""
        kwargs["class"] += " form-control"
        return super().__call__(field, **kwargs)


class SearchInput(Input, widgets.SearchInput):
    pass


class TelInput(Input, widgets.TelInput):
    pass


class URLInput(Input, widgets.URLInput):
    pass


class EmailInput(Input, widgets.EmailInput):
    pass
