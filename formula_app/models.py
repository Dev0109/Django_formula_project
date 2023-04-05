from django.db import models

class Input(models.Model):
    alpha = models.DecimalField(max_digits=19, decimal_places=10)
    betha = models.DecimalField(max_digits=19, decimal_places=10)
    phi = models.DecimalField(max_digits=19, decimal_places=10)
    deltaa = models.DecimalField(max_digits=19, decimal_places=10)
    deltap = models.DecimalField(max_digits=19, decimal_places=10)  

    def __str__(self):
        return f"{self.alpha} {self.betha} {self.phi} {self.deltaa} {self.deltap}"

class Output(models.Model):
    kag = models.ForeignKey("Input", on_delete=models.CASCADE)
    kagh = models.ForeignKey("Input", on_delete=models.CASCADE)
    kagv = models.ForeignKey("Input", on_delete=models.CASCADE)
    kaph = models.ForeignKey("Input", on_delete=models.CASCADE)
    tetaa = models.ForeignKey("Input", on_delete=models.CASCADE)
    k0n = models.ForeignKey("Input", on_delete=models.CASCADE)
    k0t = models.ForeignKey("Input", on_delete=models.CASCADE)
    k0h = models.ForeignKey("Input", on_delete=models.CASCADE)
    k0V = models.ForeignKey("Input", on_delete=models.CASCADE)
    kpgh = models.ForeignKey("Input", on_delete=models.CASCADE)
    kpph = models.ForeignKey("Input", on_delete=models.CASCADE)
    kpch = models.ForeignKey("Input", on_delete=models.CASCADE)
    tetap = models.ForeignKey("Input", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.kag} {self.kagh} {self.kagv} {self.kaph}{self.tetaa} {self.k0n} {self.k0t}{self.k0h} {self.k0V} {self.kpgh} {self.kpph} {self.kpch} {self.tetap}"