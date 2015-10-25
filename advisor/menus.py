__author__ = 'arkaaito'

from menu import Menu, MenuItem
from django.core.urlresolvers import reverse

Menu.add_item("main", MenuItem("Login",
              "/login/",
              #reverse("accounts.views.login"),
              weight=90,
              separator=True,
              icon="user"))