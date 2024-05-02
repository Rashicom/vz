from django.db import models
import uuid

# Create your models here.

class BaseModel(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# product Global information
class Products(BaseModel):
    name = models.CharField(max_length=150)
    description = models.TextField()


# multiple images for product, Global feature
class ProductImages(BaseModel):
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to='product_images')


# product price depends on bottle size
class ProductBottles(BaseModel):
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name="bottles")
    bottle_size_ml = models.IntegerField()
    price = models.IntegerField()
    discount_percent = models.IntegerField(default=0)

    @property
    def price_after_discount(self):
        if self.discount_percent != 0:
            return self.price - (self.price * self.discount_percent) / 100
        return self.price


# multiple bottle selles for discounted prices
class ComboProducts(BaseModel):
    bottles = models.ManyToManyField(ProductBottles, related_name="included_combo_offers")
    name = models.CharField(max_length=150)
    discription = models.TextField(null=True, blank=True)
    discounted_price = models.IntegerField()
    free_bottles = models.ManyToManyField(ProductBottles, related_name="included_free_bottles_combo")

    # sub total price fo bottles without bottle discounts
    @property
    def bottle_sub_total_price(self):
        return sum([bottle.price for bottle in self.bottles.all()])
    
    # total price with discounts
    @property
    def bottle_sub_discounted_price(self):
        return sum([bottle.price_after_discount for bottle in self.bottles.all()])
    

# Contact us form submissions
class ContactUs(BaseModel):
    email = models.EmailField(max_length=150)
    message = models.TextField()