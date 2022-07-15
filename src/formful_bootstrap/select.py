from .meta import Input
from formful import widgets
from markupsafe import Markup


class Select(widgets.Select):

    def __call__(self, field, **kwargs):
        kwargs.setdefault("id", field.id)
        if self.multiple:
            kwargs["multiple"] = True
        flags = getattr(field, "flags", {})
        for k in dir(flags):
            if k in self.validation_attrs and k not in kwargs:
                kwargs[k] = getattr(flags, k)
        kwargs['class'] += ' form-control'
        html = ["<select %s>" % html_params(name=field.name, **kwargs)]
        if field.has_groups():
            for group, choices in field.iter_groups():
                html.append("<optgroup %s>" % html_params(label=group))
                for val, label, selected in choices:
                    html.append(self.render_option(val, label, selected))
                html.append("</optgroup>")
        else:
            for val, label, selected in field.iter_choices():
                html.append(self.render_option(val, label, selected))
        html.append("</select>")
        return Markup("".join(html))


class RadioInput(widgets.RadioInput):

    def __call__(self, field, **kwargs):
        kwargs.setdefault('class', '')
        kwargs['class'] += ' form-check-input'
        canonical = super().__call__(field, **kwargs)
        return Markup(
            '<div class="form-check">' +
            str(canonical) +
            f'<label class="form-check-label" for="{field.id}">' +
            field.label.text +
            '</label></div>'
        )
