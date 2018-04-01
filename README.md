# origames
Fantasy Orienteering League App

<img src="https://github.com/bilgeonceken/origames/blob/master/screenshots/welcome.png" width="82"> <img src="https://github.com/bilgeonceken/origames/blob/master/screenshots/login.png" width="82"> <img src="https://github.com/bilgeonceken/origames/blob/master/screenshots/signup.png" width="82"> <img src="https://github.com/bilgeonceken/origames/blob/master/screenshots/results.png" width="82"> <img src="https://github.com/bilgeonceken/origames/blob/master/screenshots/rules.png" width="82"> <img src="https://github.com/bilgeonceken/origames/blob/master/screenshots/stages.png" width="82">

<img src="https://github.com/bilgeonceken/origames/blob/master/screenshots/playerdraft.png" width="520">

### TODO:
- [ ] User agreement
- [ ] Login error text
- [ ] Recover password
- [ ] Create separate view for team selection, just redirect from home.
- [ ] Create "if race, show button" kind of logic on player select so that it can work without a race on the database
- [ ] Create new model for storing old race result data, create a view and write a script for transferring current race data to result data.
- [ ] Fix score calculation mechanism, try to make it more robust and maybe create a view for it so that people can do it without admin panel.
- [ ] currently, static files for league app sits in /static/league. However it must be /league/static/league. This is intentional since I don't have to define a separate location for static files in nginx conf. and run "python3 manage.py collectstatic" on every update on the repository. Consider doing these things the right way.


#### notes to myself:  
to avoid integrity error when loading dumped data:
```
python3 manage.py dumpdata --exclude auth.Permission --exclude contenttypes > fixture.json
```

query annotating how many times a player is selected by users:
```
 models.Participation.objects.annotate(num_selected=Count("team")).order_by("group","-num_selected")
```
