`rebase`
==

Команда `rebase` позволяет взять изменения, зафиксированные в одной ветке,
и повторить их в другой.

```
* 2722267 - (3 seconds ago) m3 - alex_shchegretsov (HEAD -> master)
| * b24c309 - (31 seconds ago) f2 - alex_shchegretsov (feature)
| * 48c1c50 - (53 seconds ago) f1 - alex_shchegretsov
|/
* 359c692 - (86 seconds ago) m2 - alex_shchegretsov
* fc01877 - (2 minutes ago) m1 - alex_shchegretsov
```

Здесь для того, что бы в ветке `feature` был доступен функционал из
коммита `m3` - нужно, находясь в `feature`, применить `git rebase master`.
Тем самым, предок f1 будет не m2, а m3!
Т.е мы просто переносим ветку `feature` вверх.
Это искажает историю.

```
# after    git rebase master

* 5f56a0e - (45 minutes ago) f2 - alex_shchegretsov (HEAD -> feature)
* e2f1831 - (46 minutes ago) f1 - alex_shchegretsov
* 2722267 - (45 minutes ago) m3 - alex_shchegretsov (master)
* 359c692 - (46 minutes ago) m2 - alex_shchegretsov
* fc01877 - (46 minutes ago) m1 - alex_shchegretsov
```

- упрощение истории разработки с rebase
- только для приватных веток
- при частом merge в ветку feature образуются "мусорные" коммиты слияния, 
которые не несут ничего полезного, 
кроме желания автора постоянно иметь все изменения из master 
- пока ветка находится у вас на компьютере - её можно как угодно
 перебазировать и делать всё что угодно, но
если она публичная и с ней работают другие люди, 
то любые преписывания истории, включая `rebase`, запрещены
- перебазирование - это по сути один большой обман
