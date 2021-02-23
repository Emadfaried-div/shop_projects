from django.db import models
from django.utils.timezone import datetime
from django.utils.translation import ugettext_lazy as _ #for translation 
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

class Product(models.Model):
    PRDName=models.CharField(max_length=100 , verbose_name=_("product name"))
    PRDCategory=models.ForeignKey('Category', on_delete=models.CASCADE,blank=True, null=True,verbose_name=_("product category"))
    PRDBrand=models.ForeignKey('settings.Brand',on_delete=models.CASCADE,blank=True, null=True,verbose_name=_("product Brand"))
    PRDDesc=models.TextField(verbose_name=_("product description"))
    PRDImage=models.ImageField(upload_to='product/',verbose_name=_(" image"),blank=True, null=True)
    PRDPrice=models.DecimalField(max_digits=5 ,decimal_places=2, verbose_name=_("product price"))
    PRDDiscountPrice=models.DecimalField(max_digits=5 ,decimal_places=2, verbose_name=_("discount Pric"),blank=True, null=True)  # verbose name is to be translated word
    PRDCost=models.DecimalField(max_digits=5 ,decimal_places=2, verbose_name=_("product cost"))
    PRDCreated=models.DateTimeField( verbose_name=_("created_at"))

    PRDSLug= models.SlugField(blank=True, null=True , verbose_name=_("Product URL"))
    PRDISNew = models.BooleanField(default=True , verbose_name=_("New Product "))
    PRDISBestSeller = models.BooleanField(default=False , verbose_name=_("Best Seller"))
    
    
    def save(self , *args , **kwargs):
        if not self.PRDSLug :
            self.PRDSLug = slugify(self.PRDName)
        super(Product , self).save(*args , **kwargs)
    
    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    def get_absolute_url(self):
            return reverse('products:product_detail', kwargs={'slug': self.PRDSLug})


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
    CATName=models.CharField(max_length=50,verbose_name=_("category_name") )
    CATImage=models.ImageField(upload_to="category/",verbose_name=_("Image"))
    CATParent=models.ForeignKey('self',limit_choices_to={'CATParent__isnull':True}, on_delete=models.CASCADE, blank=True, null=True, verbose_name=_("Main_category"))
    CATDesc=models.TextField(verbose_name=_("category_description"))
    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.CATName

class  Product_Alternatives (models.Model):
    PALNProduct=models.ForeignKey(Product,on_delete=models.CASCADE,related_name='main_product',verbose_name=_("product"))
    PALNAlternatives=models.ManyToManyField(Product, related_name='alternative_products',verbose_name=_("product_alternatives"))
    

    class Meta:
        verbose_name = _("Product_Alternative")
        verbose_name_plural = _("Product_Alternatives")
    
    def __str__(self):
        return str(self.PALNProduct) 
   # def get_absolute_url(self):
        #return reverse("_detail", kwargs={"pk": self.pk})


class  Product_Accessories (models.Model):
    
    PACCProduct=models.ForeignKey(Product,on_delete=models.CASCADE,related_name='mainAccessory_product',verbose_name=_("product"))
    PACCAlternatives=models.ManyToManyField(Product, related_name='accessories_products',verbose_name=_("product_accessories"))

    class Meta:
        verbose_name = _(" Product_Accessory")
        verbose_name_plural = _(" Product_Accessories")

    def __str__(self):
        return str(self.PACCProduct)

   # def get_absolute_url(self):
       # return reverse("_detail", kwargs={"pk": self.pk})        

    
        


