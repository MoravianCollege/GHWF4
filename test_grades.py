
from grades import compute_hw_average


def test_zero_grades():
    grades = []
    assert compute_hw_average(grades) == 0


def test_one_grade():
    grades = [42]
    assert compute_hw_average(grades) == 42

# random comment test edition
# random comment test edition
# Para amarte necesito una razón
#Y es difícil creer que no exista
#Una más que este amor

#Sobra tanto dentro de este corazón
#Que a pesar de que dicen
#Que los años son sabios
#Todavía se siente el dolor

#Porque todo el tiempo
#Que pasé junto a tí
#Dejó tejido su hilo dentro de mí

#Y aprendí a quitarle al tiempo los segundos
#Tú mi hiciste ver el cielo aún más profundo
#Junto a tí creo que aumenté más de tres kilos
#Con tus tantos dulces besos repartidos
#Desarollaste mi sentido del olfato
#Y fue por tí que aprendí a querer los gatos
#Despegaste del cemento mis zapatos
#Para escapar los dos volando un rato

#Pero olvidaste una final instrucción
#Porque aún no sé cómo vivir sin tu amor

#Y descubrí lo que significa una rosa
#Me enseñaste decir mentiras piadosas
#Para poder a verte a horas no adecuadas
#Y a reemplazar palabras por miradas
#Y fue por tí que escribí más de cien canciones
#Y hasta perdoné tus equivocaciones
#Y conocí más de mil formas de besar
#Y fue por tí que descubrí lo que es amar
#Lo que es amar
#Lo que es amar
