from django.db import models

# Create your models here.


JOP_TYPE = (
    ('Full time','Full time'),
    ('part time','part time'),
)

class Job(models.Model) :
    title= models.CharField(max_length=100,null=True)
    # location =
    jop_type  = models.CharField(max_length=20,choices=JOP_TYPE)
    description = models.TextField(max_length=300)
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default = 1 )
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)

    def __str__(self) :
        return self.title
