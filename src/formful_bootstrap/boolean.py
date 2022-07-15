from formful import widgets
from markupsafe import Markup


class CheckboxInput(widgets.CheckboxInput):

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
