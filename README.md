# origames
Fantasy Orienteering League App

### TODO:
no todo

notes to self:
to avoid integrity error when loading dumped data:
```
python3 manage.py dumpdata --exclude auth.Permission --exclude contenttypes > fixture.json
```

query annotating how many times a player is selected by users:
``` models.Participation.objects.annotate(num_selected=Count("team")).order_by("group","-num_selected")
```
