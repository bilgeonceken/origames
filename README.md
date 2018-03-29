# origames
Fantasy Orienteering League App

### TODO:
- [ ] User agreement
- [ ] Login error text
- [ ] Recover password
- [ ] Create separate view for team selection, just redirect from home.
- [ ] Create "if race, show button" kind of logic on player select so that it can work without a race on the database
- [ ] Create new model for storing old race result data, create a view and write a script for transferring current race data to result data.
- [ ] Fix score calculation mechanism, try to make it more robust and maybe create a view for it so that people can do it without admin panel.


notes to self:
to avoid integrity error when loading dumped data:
```
python3 manage.py dumpdata --exclude auth.Permission --exclude contenttypes > fixture.json
```

query annotating how many times a player is selected by users:
```
 models.Participation.objects.annotate(num_selected=Count("team")).order_by("group","-num_selected")
```
