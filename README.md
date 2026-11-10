# Universitätssystem – Django-Modelle

Übungsaufgabe der Developer Akademie: Datenbankmodelle für ein Universitätssystem.

## Beziehungen

| Beziehung | Feldtyp | Feld |
|---|---|---|
| Student ↔ Studentenausweis (1:1) | `OneToOneField` | `StudentCard.student` |
| Professor → Kurse (1:N) | `ForeignKey` | `Course.professor` |
| Kurse ↔ Studenten (M:N) | `ManyToManyField` | `Course.students` |
| Kurs ↔ Kursbeschreibung (1:1) | `OneToOneField` | `CourseDescription.course` |
| Semester → Kurse (1:N) | `ForeignKey` | `Course.semester` |

Die Modelle stehen in [`university/models.py`](university/models.py).

## Starten

```bash
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
python manage.py migrate
```
