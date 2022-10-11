from django import forms


class GetCalculatorArgs(forms.Form):
    cost_estate = forms.IntegerField(min_value=0, required=False,
                                     widget=forms.NumberInput(attrs={'placeholder': 'Стоимость недвижимости'}))
    initial_amount = forms.IntegerField(min_value=0, required=False,
                                        widget=forms.NumberInput(attrs={'placeholder': 'Первоначальный взнос'}))
    payment_term = forms.ChoiceField(choices=((0, 'Любой'), (1, '1 год'), (2, '2 года'), (3, '3 года'),
                                              (4, '4 года'), (5, '5 лет'), (6, '6 лет'), (7, '7 лет'),
                                              (8, '8 лет'), (9, '9 лет'), (10, '10 лет'), (12, '12 лет'),
                                              (15, '15 лет'), (20, '20 лет'), (25, '25 лет'), (30, '30 лет')),
                                     )
    param_sort = forms.ChoiceField(choices=(('empty', 'Случайный порядок'),
                                            ('rate', 'Сортировка по % ставке'),
                                            ('payment', 'Сортировка по платежу')))
