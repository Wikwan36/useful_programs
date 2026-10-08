# Jakiś ciekawy tytuł 
## Nabój ##* LM 
### .338 Lapua Magnum (8,6 × 70 mm lub 8,58 × 70 mm) – jest nabojem karabinowym centralnego zapłonu, bez kryzy wystającej przeznaczonym dla karabinów wyborowych. Z uwagi na wysokie parametry balistyczne zdobywa także dużą popularność jako nabój do broni myśliwskiej. Projektantem naboju jest fińskie przedsiębiorstwo Lapua.

### Nabój .338 Lapua Magnum jest kompromisem pomiędzy standardowymi nabojami NATO o kalibrach 7,62 mm NATO i 12,7 mm NATO pozwalającym zbudować karabin wyborowy o zasięgu skutecznym powyżej 1000 m, a jednocześnie wymiarach i masie mniejszej niż wkbw. Obecnie produkowana jest szeroka gama pocisków kalibru .338 przeznaczonych dla tego naboju. W wojsku najczęściej stosowany jest klasyczny nabój pełnopłaszczowy, rzadziej przeciwpancerny pocisk posiadający przebijalność 20 mm RHA z dystansu 200 m. Snajperzy policyjni i myśliwi używają dodatkowo amunicji o zwiększonej zdolności obalającej. 
*W świetle przedstawionych informacji zasadne **jest dalsze monitorowanie omawianych zagadnień** oraz analiza ich potencjalnych konsekwencji. ~~Należy również uwzględnić, że skuteczne wdrażanie rekomendowanych działań wymaga zachowania odpowiednich procedur i standardów organizacyjnych.~~*

- **7,62×51 mm NATO (.308 Winchester)** – jeden z najpopularniejszych kalibrów wyborowych i sportowych.
- **.300 Winchester Magnum (7,62×67 mm)** – ceniony za większy zasięg i energię pocisku.
- **.338 Lapua Magnum (8,6×70 mm)** – powszechnie stosowany do strzelań długodystansowych powyżej 1000 m.

1. **5,56×45 mm NATO** – standardowy kaliber pośredni używany m.in. w karabinkach M4 i HK416.
2
2. **7,62×39 mm** – klasyczny nabój pośredni stosowany w rodzinie karabinków AK-47 i AKM.
3
3. **5,45×39 mm** – radziecki/rosyjski kaliber pośredni wykorzystywany m.in. w karabinkach AK-74.

- [x] **7,62×51 mm NATO (.308 Winchester)** – jeden z najpopularniejszych kalibrów wyborowych i sportowych.
- [x] **.300 Winchester Magnum (7,62×67 mm)** – ceniony za większy zasięg i energię pocisku.
- [ ] **.338 Lapua Magnum (8,6×70 mm)** – powszechnie stosowany do strzelań długodystansowych powyżej 1000 m.
- [ ] **5,56×45 mm NATO** – standardowy kaliber pośredni używany m.in. w karabinkach M4 i HK416.
- [ ] **7,62×39 mm** – klasyczny nabój pośredni stosowany w rodzinie karabinków AK-47 i AKM.
- [ ] **5,45×39 mm** – radziecki/rosyjski kaliber pośredni wykorzystywany m.in. w karabinkach AK-74.

Poniżej tabela w formacie Markdown. Podane zasięgi są orientacyjnymi skutecznymi zasięgami bojowymi i zależą od broni, amunicji oraz umiejętności strzelca. Dla 5,56×45 mm NATO przyjmuje się ok. 500 m dla celu punktowego z karabinka M4.

| Kaliber | Typ | Typowy skuteczny zasięg |
|----------|----------|----------|
| 5,56×45 mm NATO | Pośredni | 500 m |
| 7,62×39 mm | Pośredni | 300-400 m |
| 5,45×39 mm | Pośredni | 500 m |
| 7,62×51 mm NATO (.308 Win) | Snajperski / pełnej mocy | 800-1000 m |
| .300 Winchester Magnum | Snajperski | 1000-1200 m |
| .338 Lapua Magnum | Snajperski dalekiego zasięgu | 1200-1500+ m |


Jeżeli Twój edytor obsługuje Markdown, możesz też użyć bardziej rozbudowanej tabeli:

| Kaliber | Średnica pocisku | Typ naboju | Typowy skuteczny zasięg |
|----------|----------|----------|----------|
| 5,56×45 mm NATO | 5,56 mm | Pośredni | 500 m |
| 7,62×39 mm | 7,62 mm | Pośredni | 300-400 m |
| 5,45×39 mm | 5,45 mm | Pośredni | 500 m |
| 7,62×51 mm NATO (.308 Win) | 7,62 mm | Pełnej mocy | 800-1000 m |
| .300 Winchester Magnum | 7,62 mm | Magnum | 1000-1200 m |
| .338 Lapua Magnum | 8,6 mm | Magnum | 1200-1500+ m |

[link](http://colab.research.google.com)

### Prosty kalkulator energii kinetycznej dla .338 Lapua Magnum

Założenia:
- masa pocisku: **16,2 g** (250 gr)
- prędkość wylotowa: **900 m/s**

Wzór:

E = ½ · m · v²

```python
# .338 Lapua Magnum - uproszczone obliczenie energii kinetycznej

masa_g = 16.2          # masa pocisku [g]
predkosc = 900         # prędkość [m/s]

masa_kg = masa_g / 1000

energia = 0.5 * masa_kg * predkosc**2

print(f"Energia pocisku: {energia:.0f} J")


Przykładowy wynik:

Energia pocisku: 6561 J

Szacunkowy czas lotu do celu
# Przybliżony czas lotu na dystansie 1000 m

dystans = 1000      # m
predkosc = 900      # m/s

czas_lotu = dystans / predkosc

print(f"Czas lotu: {czas_lotu:.2f} s")


Wynik:

Czas lotu: 1.11 s
```
### Energia kinetyczna pocisku
2
 
3
$E = \frac{1}{2}mv^2$
4
 
5
### Pęd pocisku
6
 
7
$p = mv$
8
 
9
### Opad pocisku (bez uwzględnienia oporu powietrza)
10
 
11
$h = \frac{1}{2}gt^2$

### Zasięg maksymalny (rzut ukośny bez oporu powietrza)

$$
R = \frac{v_0^2 \sin(2\theta)}{g}
$$

### Wysokość maksymalna toru lotu

$$
H = \frac{v_0^2 \sin^2(\theta)}{2g}
$$

### Czas lotu pocisku

$$
T = \frac{2v_0 \sin(\theta)}{g}
$$


Te trzy wzory będą wyświetlane jako wycentrowane równania matematyczne, jeśli Twój podgląd Markdown obsługuje MathJax lub KaTeX i renderuje bloki $$ ... $$.

![Wykres](wykres.png)

