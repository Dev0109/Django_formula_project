from django.db import models

class Input(models.Model):
    input_id = models.AutoField(primary_key=True)
    alpha = models.DecimalField(max_digits=19, decimal_places=4)
    betha = models.DecimalField(max_digits=19, decimal_places=4)
    phi = models.DecimalField(max_digits=19, decimal_places=4)
    delta_a = models.DecimalField(max_digits=19, decimal_places=4)
    delta_p = models.DecimalField(max_digits=19, decimal_places=4)  

    def __str__(self):
        return f"{self.alpha} {self.betha} {self.phi} {self.delta_a} {self.delta_p}"

class Output(models.Model):
    output_id = models.AutoField(primary_key=True)
    foreign_key = models.ForeignKey('Input', on_delete=models.CASCADE)
    kag = models.DecimalField(max_digits=19, decimal_places=4)
    kagh = models.DecimalField(max_digits=19, decimal_places=4)
    kagv = models.DecimalField(max_digits=19, decimal_places=4)
    kaph = models.DecimalField(max_digits=19, decimal_places=4)
    kach = models.DecimalField(max_digits=19, decimal_places=4)
    teta_a = models.DecimalField(max_digits=19, decimal_places=4)
    k0n = models.DecimalField(max_digits=19, decimal_places=4)
    k0t = models.DecimalField(max_digits=19, decimal_places=4)
    k0h = models.DecimalField(max_digits=19, decimal_places=4)
    k0V = models.DecimalField(max_digits=19, decimal_places=4)
    kpgh = models.DecimalField(max_digits=19, decimal_places=4)
    kpph = models.DecimalField(max_digits=19, decimal_places=4)
    kpch = models.DecimalField(max_digits=19, decimal_places=4)
    teta_p = models.DecimalField(max_digits=19, decimal_places=4)

    def __str__(self):
        return f"{self.kag} {self.kagh} {self.kagv} {self.kaph} {self.kach} {self.teta_a} {self.k0n} {self.k0t}{self.k0h} {self.k0V} {self.kpgh} {self.kpph} {self.kpch} {self.teta_p}"