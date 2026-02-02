from django.db import models

# Create your models here.
class SecurityIncident(models.Model):
	SEVERITY_CHOICES = [
		('BAIXA', 'Baixa'),
		('MITJANA','Mitjana'),
		('ALTA','Alta'),
	]

	title = models.CharField(max_length=200)
	description = models.TextField()
	severity = models.CharField(max_length=10, choices=SEVERITY_CHOICES, default='BAIXA')
	detected_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title
