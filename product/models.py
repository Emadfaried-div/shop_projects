from django.db import models
from django.utils.timezone import datetime
from django.utils.translation import ugettext_lazy as _ #for translation 

# Create your models here.

class Product(models.Model):
    PRDName=models.CharField(max_length=100 , verbose_name=_("product name"))
    #category=models.ForeignKey()
    PRDDesc=models.TextField(verbose_name=_("product description"))
    PRDPrice=models.DecimalField(max_digits=5 ,decimal_places=2, verbose_name=_("product price")) # verbose name is to be translated word
    PRDCost=models.DecimalField(max_digits=5 ,decimal_places=2, verbose_name=_("product cost"))
    PRDCreated=models.DateTimeField( verbose_name=_("created_at"))
    

    def __str__(self):
        return self.PRDName

## Category 
## Images 
# alternatives
# accessories        
class ProductImage (models.Model):
    PRDIProduct=models.ForeignKey(Product,on_delete=models.CASCADE, verbose_name=_("product"))
    PRDIImage=models.ImageField(upload_to='product/',verbose_name=_("product image"))

    def __str__(self):
        return str (self.PRDIProduct)

class Category(models.Model):
    CATName=models.CharField(max_length=50)
    CATImage=models.ImageField(upload_to="category/")
    CATPartent=models.ForeignKey('self', on_delete=models.CASCADE)
    CATDesc=models.TextField()


