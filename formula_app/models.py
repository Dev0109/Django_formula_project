from django.db import models

class Input(models.Model):
    alpha = models.DecimalField(max_digits=19, decimal_places=10)
    betha = models.DecimalField(max_digits=19, decimal_places=10)
    phi = models.DecimalField(max_digits=19, decimal_places=10)
    delta_a = models.DecimalField(max_digits=19, decimal_places=10)
    delta_p = models.DecimalField(max_digits=19, decimal_places=10)  

    def __str__(self):
        return f"{self.alpha} {self.betha} {self.phi} {self.delta_a} {self.delta_p}"

class Output(models.Model):
    kag = models.ForeignKey("Input", on_delete=models.CASCADE, related_name="+")
    kagh = models.ForeignKey("Input", on_delete=models.CASCADE, related_name="+")
    kagv = models.ForeignKey("Input", on_delete=models.CASCADE, related_name="+")
    kaph = models.ForeignKey("Input", on_delete=models.CASCADE, related_name="+")
    teta_a = models.ForeignKey("Input", on_delete=models.CASCADE, related_name="+")
    k0n = models.ForeignKey("Input", on_delete=models.CASCADE, related_name="+")
    k0t = models.ForeignKey("Input", on_delete=models.CASCADE, related_name="+")
    k0h = models.ForeignKey("Input", on_delete=models.CASCADE, related_name="+")
    k0V = models.ForeignKey("Input", on_delete=models.CASCADE, related_name="+")
    kpgh = models.ForeignKey("Input", on_delete=models.CASCADE, related_name="+")
    kpph = models.ForeignKey("Input", on_delete=models.CASCADE, related_name="+")
    kpch = models.ForeignKey("Input", on_delete=models.CASCADE, related_name="+")
    teta_p = models.ForeignKey("Input", on_delete=models.CASCADE, related_name="+")

    def __str__(self):
        return f"{self.kag} {self.kagh} {self.kagv} {self.kaph}{self.teta_a} {self.k0n} {self.k0t}{self.k0h} {self.k0V} {self.kpgh} {self.kpph} {self.kpch} {self.teta_p}"