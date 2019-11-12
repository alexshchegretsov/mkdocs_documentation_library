`default_related_name`
=

Название, которое будет использоваться для обратных связей с этой моделью.

```
class Song(CommonInfo):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    duration = models.DurationField()

    class Meta:
        # определим имя обратной связи со стороны artist и album
        default_related_name = "composition"

```
