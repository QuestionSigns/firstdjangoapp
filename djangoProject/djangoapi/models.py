from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from djangoapi.utils import sendTransaction
import hashlib

# Create your models here.
class Post(models.Model):
    #con on_delete=models.CASCADE indichiamo che quando l'utente viene cancellato
    #saranno cancellati anche tutti i posti assegnati a lui
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    author = models.CharField(max_length=50, default="")
    title = models.CharField(max_length=200, default="")
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now())
    published_date = models.DateTimeField(blank=True, null=True)
    hash = models.CharField(max_length=32, default=None, null=True)
    txId = models.CharField(max_length=66, default=None, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self): #Doppi _ prima e dopo il nome del metodo sono chiamati 'dunder'
        return self.title
    
    def writeOnChain(self):
        self.hash = hashlib.sha256(self.content.encode('utf-8')).hexdigest()
        self.txId = sendTransaction(self.hash)