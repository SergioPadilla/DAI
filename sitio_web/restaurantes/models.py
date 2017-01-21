from __future__ import unicode_literals

from django.db import models


class Restaurant(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True, unique=True, editable=False)
    cuisine = models.CharField(max_length=200)
    borough = models.CharField(max_length=200)
    name = models.CharField(max_length=200)


# BEGIN;
# --
# -- Create model Restaurant
# --
# CREATE TABLE "restaurantes_restaurant" (
#     "id" integer NOT NULL PRIMARY KEY,
#     "cuisine" varchar(200) NOT NULL,
#     "borough" varchar(200) NOT NULL,
#     "name" varchar(200) NOT NULL
# );
# COMMIT;