# origames
Fantasy Orienteering League App

### TODO:
- [ ] [models.py](league/models.py): lock team modification after a deadline

notes to self:
to avoid integrity error when loading dumped data:
```
python3 manage.py dumpdata --exclude auth.Permission --exclude contenttypes > fixture.json
```
