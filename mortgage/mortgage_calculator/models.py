from django.db import models


class MortgageOffers(models.Model):
    bank_name = models.CharField(max_length=255, verbose_name='Наименование банка')
    term_min = models.IntegerField(verbose_name='Срок ипотеки, ОТ')
    term_max = models.IntegerField(verbose_name='Срок ипотеки, ДО')
    rate_min = models.FloatField(verbose_name='Ипотечная ставка, ОТ, в процентах')
    rate_max = models.FloatField(verbose_name='Ипотечная ставка, ДО, в процентах')
    payment_min = models.IntegerField(verbose_name='Сумма кредита, минимум')
    payment_max = models.IntegerField(verbose_name='Сумма кредита, максимум')
    initial_payment_min = models.IntegerField(verbose_name='Первоначальный взнос, ОТ, в процентах', default=0)
    initial_payment_max = models.IntegerField(verbose_name='Первоначальный взнос, ДО, в процентах', default=0)

    class Meta:
        verbose_name_plural = 'Ипотечные предложения'
        verbose_name = 'Ипотечное предложение'
        ordering = ['bank_name']
