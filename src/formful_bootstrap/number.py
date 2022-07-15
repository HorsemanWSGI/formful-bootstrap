from formful import widgets


class NumberInput(widgets.NumberInput):

    def __call__(self, field, **kwargs):
        if self.step is not None:
            kwargs.setdefault("step", self.step)
        if self.min is not None:
            kwargs.setdefault("min", self.min)
        if self.max is not None:
            kwargs.setdefault("max", self.max)
        kwargs['class'] += " form-control"
        return super().__call__(field, **kwargs)


class RangeInput(widgets.RangeInput):

    def __call__(self, field, **kwargs):
        kwargs.setdefault('class', '')
        kwargs['class'] += ' form-control'
        if self.step is not None:
           kwargs.setdefault("step", self.step)
        return super().__call__(field, **kwargs)
