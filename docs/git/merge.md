`merge`
=


```
# before merge

* d8a24ba - (1 second ago) m3 - alex_shchegretsov (HEAD -> master)
| * f360584 - (20 seconds ago) f2 - alex_shchegretsov (feature)
| * 601ea08 - (31 seconds ago) f1 - alex_shchegretsov
|/
* 89262fd - (53 seconds ago) m2 - alex_shchegretsov
* def6e8a - (64 seconds ago) m1 - alex_shchegretsov
```
Находясь в ветке master `git merge feature`

```
*   83d0c01 - (7 seconds ago) Merge branch 'feature' - alex_shchegretsov (HEAD -> master)
|\
| * f360584 - (3 minutes ago) f2 - alex_shchegretsov (feature)
| * 601ea08 - (4 minutes ago) f1 - alex_shchegretsov
* | d8a24ba - (3 minutes ago) m3 - alex_shchegretsov
|/
* 89262fd - (4 minutes ago) m2 - alex_shchegretsov
* def6e8a - (4 minutes ago) m1 - alex_shchegretsov
```
- Алгоритм слияния найдёт где ветки разделились - общий коммит-предок m2
# проверка общего предка у двух веток
- `git merge-base master feature`
- Дальше для каждого файла сравниваются его 3 версии:
- Первая версия - которая была в их общем предке до разделения - base
- Вторая - та, которая на текущей ветке(master) - т.н ours
- Третья версия - из feature, называется theirs
- `base + (ours changes) + (theirs changes) -> merge` - так мы получаем новую версию с изменениями из обеих веток,
если мы изменяли одну и ту же область - нужно будет решить 
`merge conflict`
- если в одной из веток файл менялся, а в другой - нет, то, 
очевидно, в результат слияния должна попасть более новая,
изменённая версия
- `git merge --abort` - отменить слияние и откатиться в начальное состояние(до слияния)
В случае когда есть конфликты слияния - создатся `MERGE_HEAD` с 
которого можно откатиться в состояние до слияния, если слияние 
прошло успешно - то `MERGE_HEAD` - отсутствует и откат невозможен.
