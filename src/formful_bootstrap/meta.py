from formful import widgets
from formful.utils import html_params
from markupsafe import Markup, escape


class Input(widgets.Input):

    def __call__(self, field, **kwargs):
        print(field.id, kwargs)
        kwargs.setdefault("id", field.id)
        kwargs.setdefault("type", self.input_type)
        if "value" not in kwargs:
            kwargs["value"] = field._value()
        flags = getattr(field, "flags", {})
        for k in dir(flags):
            if k in self.validation_attrs and k not in kwargs:
                kwargs[k] = getattr(flags, k)
        kwargs["class"] += " form-control"
        return Markup(
            "<input %s>" % self.html_params(name=field.name, **kwargs)
        )
