# Rzut ukośny bez oporu i z oporem powietrza

## Cel i założenia

Rzut ukośny jest ruchem ciała, któremu nadano prędkość początkową pod kątem do poziomu. W polu grawitacyjnym tor jest parabolą, jeśli pominiemy opór powietrza. Po uwzględnieniu oporu tor przestaje być parabolą, a prędkość i przyspieszenie trzeba wyznaczyć z równań ruchu.

W raporcie porównano oba modele dla tej samej prędkości początkowej i kąta:

$$
v_0=36\ \mathrm{m/s}, \qquad
\alpha=11^\circ=\frac{11\pi}{180}\ \mathrm{rad}
\approx 0{,}191986\ \mathrm{rad}.
$$

Przyjmujemy poziomą oś $x$ i pionową oś $y$ skierowaną w górę. Początek układu jest punktem wyrzutu, a lądowanie następuje na tej samej wysokości ($y=0$). Przyspieszenie grawitacyjne jest stałe i wynosi $g=9{,}81\ \mathrm{m/s^2}$. Pomijamy obrót Ziemi, wiatr i zmianę gęstości powietrza z wysokością.

Do modelu z oporem przyjęto parametry przykładowej piłki:

| Wielkość | Symbol | Wartość | Jednostka SI |
|---|---:|---:|---|
| masa ciała | $m$ | $0{,}145$ | $\mathrm{kg}$ |
| średnica | $d$ | $0{,}100$ | $\mathrm{m}$ |
| gęstość powietrza | $\rho$ | $1{,}225$ | $\mathrm{kg/m^3}$ |
| współczynnik oporu kuli | $C_D$ | $0{,}47$ | bezwymiarowy |
| pole przekroju | $A=\pi(d/2)^2$ | $0{,}007854$ | $\mathrm{m^2}$ |
| przyspieszenie grawitacyjne | $g$ | $9{,}81$ | $\mathrm{m/s^2}$ |

Parametry ciała i powietrza są założeniami modelowymi, a nie pomiarami. Dzięki temu wynik dla oporu jest jednoznaczny i odtwarzalny.

## 1. Rozkład prędkości początkowej

Wektor prędkości początkowej rozkładamy na składowe:

$$
v_{x0}=v_0\cos\alpha,\qquad v_{y0}=v_0\sin\alpha.
$$

Po podstawieniu danych:

$$
v_{x0}=36\cos(11^\circ)\approx35{,}339\ \mathrm{m/s},
\qquad
v_{y0}=36\sin(11^\circ)\approx6{,}869\ \mathrm{m/s}.
$$

Kontrola: $v_{x0}^2+v_{y0}^2=v_0^2$, zatem początkowa wartość prędkości wynosi $36\ \mathrm{m/s}$.

## 2. Rzut bez oporu powietrza

### 2.1. Równania ruchu

Na ciało działa tylko siła ciężkości. Z drugiej zasady Newtona, osobno dla obu osi:

$$
m\ddot{x}=0,\qquad m\ddot{y}=-mg.
$$

Po podzieleniu przez masę otrzymujemy przyspieszenia:

$$
\ddot{x}=0,\qquad \ddot{y}=-g.
$$

Całkujemy pierwsze równanie, korzystając z warunków początkowych $x(0)=0$ i $\dot{x}(0)=v_{x0}$:

$$
v_x(t)=v_{x0},\qquad x(t)=v_{x0}t.
$$

Analogicznie dla osi pionowej, z $y(0)=0$ i $\dot{y}(0)=v_{y0}$:

$$
v_y(t)=v_{y0}-gt,\qquad
y(t)=v_{y0}t-\frac{1}{2}gt^2.
$$

Są to równania parametryczne toru. Eliminując czas $t=x/v_{x0}$ z równania wysokości, dostajemy:

$$
y(x)=x\tan\alpha-\frac{g x^2}{2v_0^2\cos^2\alpha}.
$$

Równanie ma postać funkcji kwadratowej, więc tor w modelu idealnym jest parabolą.

### 2.2. Czas lotu, wysokość maksymalna i zasięg

Chwila osiągnięcia wierzchołka toru wynika z warunku $v_y=0$:

$$
0=v_{y0}-gt_{\mathrm{w}},\qquad
t_{\mathrm{w}}=\frac{v_{y0}}{g}.
$$

Wysokość maksymalną otrzymujemy, podstawiając ten czas do $y(t)$:

$$
H=y(t_{\mathrm{w}})
=v_{y0}\frac{v_{y0}}{g}
-\frac{g}{2}\left(\frac{v_{y0}}{g}\right)^2
=\frac{v_{y0}^2}{2g}
=\frac{v_0^2\sin^2\alpha}{2g}.
$$

Przy lądowaniu na wysokości startu $y(T)=0$. Nietrywialnym rozwiązaniem równania
$v_{y0}T-\frac12gT^2=0$ jest:

$$
T=\frac{2v_{y0}}{g}=\frac{2v_0\sin\alpha}{g}.
$$

Zasięg poziomy to $R=x(T)$:

$$
R=v_{x0}T
=\frac{v_0^2\sin(2\alpha)}{g}.
$$

Dla zadanych danych otrzymujemy:

| Wynik bez oporu | Wartość |
|---|---:|
| czas wznoszenia $t_{\mathrm{w}}$ | $0{,}7002\ \mathrm{s}$ |
| czas całego lotu $T$ | $1{,}4004\ \mathrm{s}$ |
| wysokość maksymalna $H$ | $2{,}4049\ \mathrm{m}$ |
| zasięg $R$ | $49{,}4893\ \mathrm{m}$ |

Przyspieszenie jest stałe: $a_x=0\ \mathrm{m/s^2}$ i $a_y=-9{,}81\ \mathrm{m/s^2}$.
W najwyższym punkcie $v_y=0$, ale prędkość całkowita nie jest zerowa, ponieważ
$v_x$ pozostaje równe $35{,}339\ \mathrm{m/s}$.

## 3. Rzut z oporem powietrza

### 3.1. Model siły oporu

Dla ciała poruszającego się w powietrzu przyjmujemy kwadratowy model oporu:

$$
\vec{F}_D=-\frac12\rho C_D A\,|\vec{v}|\,\vec{v}.
$$

Znak minus oznacza, że siła jest skierowana przeciwnie do wektora prędkości. Moduł
siły wynosi $F_D=\frac12\rho C_D A v^2$ i rośnie z kwadratem szybkości. Wprowadzamy
współczynnik

$$
k=\frac12\rho C_D A
=\frac12(1{,}225)(0{,}47)(0{,}00785398)
\approx0{,}00226096\ \mathrm{kg/m}.
$$

Wtedy $F_D=k v^2$. Jednostka $k$ wynika z $[\rho A]=\mathrm{kg/m}$, a iloczyn
$k v^2$ ma jednostkę $\mathrm{kg\,m/s^2}=\mathrm{N}$.

Ponieważ $|\vec v|=\sqrt{v_x^2+v_y^2}$, równania ruchu wynikające z drugiej zasady
Newtona są następujące:

$$
\begin{aligned}
\dot{x}&=v_x, & \dot{y}&=v_y,\\
\dot{v}_x&=-\frac{k}{m}\sqrt{v_x^2+v_y^2}\,v_x, &
\dot{v}_y&=-g-\frac{k}{m}\sqrt{v_x^2+v_y^2}\,v_y.
\end{aligned}
$$

Warunki początkowe są takie same jak w modelu idealnym:

$$
x(0)=y(0)=0,\qquad
v_x(0)=35{,}339\ \mathrm{m/s},\qquad
v_y(0)=6{,}869\ \mathrm{m/s}.
$$

### 3.2. Dlaczego rozwiązanie jest numeryczne?

W równaniach przyspieszenia składowe $v_x$ i $v_y$ są sprzężone przez
$\sqrt{v_x^2+v_y^2}$. Nie można więc osobno rozwiązać dwóch prostych równań
stałego przyspieszenia ani użyć parabolicznego wzoru na tor. Układ całkujemy
numerycznie metodą Rungego–Kutty (`solve_ivp` z adaptacyjnym krokiem). Obliczenie
kończy się przy pierwszym ponownym przejściu przez $y=0$ w kierunku w dół.

W modelu z oporem pozioma składowa prędkości maleje, a pionowa składowa
przyspieszenia zależy od kierunku ruchu. Podczas wznoszenia opór zmniejsza
przyspieszenie w dół, natomiast podczas opadania działa w górę i zwiększa
przyspieszenie skierowane ku górze względem samej grawitacji.

### 3.3. Wyniki obliczeń

| Wielkość | Bez oporu | Z oporem kwadratowym |
|---|---:|---:|
| czas lotu | $1{,}4004\ \mathrm{s}$ | $1{,}2555\ \mathrm{s}$ |
| wysokość maksymalna | $2{,}4049\ \mathrm{m}$ | $1{,}9474\ \mathrm{m}$ |
| zasięg | $49{,}4893\ \mathrm{m}$ | $33{,}6641\ \mathrm{m}$ |

W tych założeniach opór skraca zasięg o około $15{,}83\ \mathrm{m}$, czyli o
$32{,}0\%$ w stosunku do modelu bez oporu. Wartości te dotyczą wyłącznie
przyjętej masy, średnicy, gęstości powietrza i współczynnika $C_D$; nie są
uniwersalnymi wynikami dla dowolnego pocisku.

## 4. Wykresy

Poniższe rysunki zostały wygenerowane z kodu Pythona zamieszczonego w dalszej
części raportu. Osie i wielkości fizyczne są podane w jednostkach SI.

![Porównanie torów rzutu bez oporu i z oporem kwadratowym](files/rzut_ukosny/tory_ruchu.png)

*Rysunek 1. Tor idealny jest parabolą. Przy oporze kwadratowym tor jest niższy i
ma krótszy zasięg.*

![Położenie poziome i pionowe w czasie dla obu modeli](files/rzut_ukosny/polozenie_czas.png)

*Rysunek 2. Położenie poziome $x(t)$ przestaje rosnąć jednostajnie po
uwzględnieniu oporu. W obu modelach ruch pionowy kończy się na poziomie
$y=0$.*

![Składowe prędkości poziomej i pionowej w czasie](files/rzut_ukosny/predkosc.png)

*Rysunek 3. Bez oporu $v_x$ jest stałe, a $v_y$ zmienia się liniowo. Z oporem
maleją obie składowe prędkości.*

![Wartość prędkości w czasie](files/rzut_ukosny/wartosc_predkosci.png)

*Rysunek 4. W modelu idealnym wartość prędkości jest najmniejsza w wierzchołku
toru. Opór rozprasza energię i szybkość maleje w porównaniu z lotem idealnym.*

![Składowe przyspieszenia w czasie](files/rzut_ukosny/przyspieszenie.png)

*Rysunek 5. Bez oporu działa wyłącznie stałe przyspieszenie grawitacyjne. Przy
oporze pojawia się także pozioma składowa przyspieszenia.*

![Energia mechaniczna w czasie dla obu modeli](files/rzut_ukosny/energia.png)

*Rysunek 6. Bez oporu suma energii kinetycznej i potencjalnej jest stała. Przy
oporze energia mechaniczna maleje, ponieważ siła oporu wykonuje ujemną pracę.*

## 5. Energia i kontrola fizyczna

Energia mechaniczna względem poziomu wyrzutu wynosi:

$$
E_{\mathrm{mech}}=\frac12m(v_x^2+v_y^2)+mgy.
$$

W modelu bez oporu nie ma sił rozpraszających, więc $E_{\mathrm{mech}}$ jest
stała. Początkowa energia kinetyczna wynosi
$E_0=\frac12mv_0^2\approx94{,}0\ \mathrm{J}$.

Siła oporu zawsze działa przeciwnie do prędkości, zatem jej moc jest
nie dodatnia:

$$
P_D=\vec{F}_D\cdot\vec{v}
=-\frac12\rho C_D A|\vec{v}|^3\leq0.
$$

W konsekwencji energia mechaniczna maleje w czasie w modelu z oporem, co
potwierdza wykres energii. W punkcie najwyższym toru nadal zachodzi $v_y=0$,
ale z powodu oporu prędkość pozioma jest już mniejsza niż początkowa.

## 6. Kod i odtwarzanie wyników

Pełny, wykonywalny skrypt znajduje się w pliku
[generuj_wykresy.py](generuj_wykresy.py). Zapisuje sześć wykresów w katalogu
`files/rzut_ukosny/` i wypisuje wartości wykorzystane w tabelach. Do uruchomienia
potrzebne są pakiety `numpy`, `scipy` i `matplotlib`:

```bash
python -m pip install numpy scipy matplotlib
python pages/solutions/04_sol_vscode/generuj_wykresy.py
```

Najważniejszy fragment kodu modelu numerycznego pokazano poniżej:

```python
def rhs(t, stan):
    x, y, vx, vy = stan
    speed = np.hypot(vx, vy)
    ax = -(k / m) * speed * vx
    ay = -g - (k / m) * speed * vy
    return vx, vy, ax, ay


def ladowanie(t, stan):
    return stan[1]  # y = 0


ladowanie.terminal = True
ladowanie.direction = -1

stan_poczatkowy = (
    0.0,
    0.0,
    v0 * np.cos(alpha),
    v0 * np.sin(alpha),
)
rozwiazanie = solve_ivp(
    rhs,
    (0.0, 20.0),
    stan_poczatkowy,
    events=ladowanie,
    dense_output=True,
    rtol=1e-10,
    atol=1e-12,
)
if not rozwiazanie.success:
    raise RuntimeError(rozwiazanie.message)


W tym fragmencie `k = 0.5 * rho * C_D * A`, `m` jest masą, a `g` przyspieszeniem
grawitacyjnym. Pełny skrypt zawiera również obliczenia rozwiązania analitycznego,
generowanie wykresów i kontrolę poprawności obliczeń numerycznych.
"""Generate plots for the oblique projectile motion report.

Run from the repository root with:
    python pages/solutions/04_sol_vscode/generuj_wykresy.py
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp


OUT = Path(__file__).parent / "files" / "rzut_ukosny"
OUT.mkdir(parents=True, exist_ok=True)

G = 9.81
V0 = 36.0
ALPHA_DEG = 11.0
ALPHA = np.deg2rad(ALPHA_DEG)
RHO = 1.225
CD = 0.47
DIAMETER = 0.10
MASS = 0.145
AREA = np.pi * (DIAMETER / 2) ** 2
DRAG_FACTOR = 0.5 * RHO * CD * AREA

BLUE, ORANGE, GREEN, PURPLE, INK = (
    "#2463A6",
    "#D47722",
    "#168578",
    "#8455A4",
    "#233044",
)
plt.rcParams.update(
    {
        "font.family": "DejaVu Sans",
        "font.size": 10,
        "axes.titlesize": 12,
        "axes.titleweight": "bold",
        "axes.labelcolor": INK,
        "text.color": INK,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.grid": True,
        "grid.alpha": 0.2,
        "lines.linewidth": 2.2,
        "figure.facecolor": "white",
        "savefig.facecolor": "white",
    }
)


def bez_oporu(t):
    vx = V0 * np.cos(ALPHA)
    vy = V0 * np.sin(ALPHA)
    x = vx * t
    y = vy * t - 0.5 * G * t**2
    return x, y, np.full_like(t, vx), vy - G * t


def rhs(_t, stan):
    x, y, vx, vy = stan
    speed = np.hypot(vx, vy)
    ax = -(DRAG_FACTOR / MASS) * speed * vx
    ay = -G - (DRAG_FACTOR / MASS) * speed * vy
    return vx, vy, ax, ay


def zdarzenie_ladowania(_t, stan):
    return stan[1]


zdarzenie_ladowania.terminal = True
zdarzenie_ladowania.direction = -1


czas_bez_oporu = 2 * V0 * np.sin(ALPHA) / G
rozwiazanie = solve_ivp(
    rhs,
    (0.0, 20.0),
    (0.0, 0.0, V0 * np.cos(ALPHA), V0 * np.sin(ALPHA)),
    events=zdarzenie_ladowania,
    dense_output=True,
    rtol=1e-10,
    atol=1e-12,
)
if not rozwiazanie.success:
    raise RuntimeError(rozwiazanie.message)
if len(rozwiazanie.t_events[0]) != 1:
    raise RuntimeError("Nie znaleziono chwili lądowania w przedziale symulacji.")

czas_opor = rozwiazanie.t_events[0][0]
czas = np.linspace(0.0, max(czas_bez_oporu, czas_opor), 1000)
t_opor = czas[czas <= czas_opor]
stan_opor = rozwiazanie.sol(t_opor)
x_opor, y_opor, vx_opor, vy_opor = stan_opor
x0, y0, vx0, vy0 = bez_oporu(czas)

zasieg_bez_oporu = V0**2 * np.sin(2 * ALPHA) / G
wysokosc_bez_oporu = (V0 * np.sin(ALPHA)) ** 2 / (2 * G)
zasieg_opor = rozwiazanie.y_events[0][0, 0]
wysokosc_opor = np.max(y_opor)


def zapisz(fig, nazwa):
    fig.savefig(OUT / f"{nazwa}.png", dpi=180, bbox_inches="tight")
    plt.close(fig)


print(f"v0 = {V0:.2f} m/s; alpha = {ALPHA_DEG:.2f} deg")
print(f"vx0 = {V0*np.cos(ALPHA):.6f} m/s")
print(f"vy0 = {V0*np.sin(ALPHA):.6f} m/s")
print(f"Bez oporu: czas = {czas_bez_oporu:.6f} s")
print(f"Bez oporu: zasieg = {zasieg_bez_oporu:.6f} m")
print(f"Bez oporu: wysokosc maks. = {wysokosc_bez_oporu:.6f} m")
print(f"Z oporem: czas = {czas_opor:.6f} s")
print(f"Z oporem: zasieg = {zasieg_opor:.6f} m")
print(f"Z oporem: wysokosc maks. = {wysokosc_opor:.6f} m")
print(f"Pole przekroju = {AREA:.8f} m^2; k = {DRAG_FACTOR:.8f} kg/m")

fig, ax = plt.subplots(figsize=(9, 4.8), layout="constrained")
ax.plot(x0, y0, color=BLUE, label="Bez oporu powietrza")
ax.plot(x_opor, y_opor, color=ORANGE, label="Z oporem kwadratowym")
ax.scatter([0], [0], color=INK, s=35, zorder=4, label="Punkt startu")
ax.scatter(
    [zasieg_bez_oporu, zasieg_opor],
    [0, 0],
    color=[BLUE, ORANGE],
    s=35,
    zorder=4,
)
ax.set(
    xlabel="Położenie poziome x [m]",
    ylabel="Wysokość y [m]",
    title="Tory ruchu: model idealny i opór powietrza",
)
ax.set_ylim(bottom=0)
ax.legend()
zapisz(fig, "tory_ruchu")

fig, axes = plt.subplots(2, 1, figsize=(9, 6), sharex=True, layout="constrained")
axes[0].plot(czas, x0, color=BLUE, label="Bez oporu")
axes[0].plot(t_opor, x_opor, color=ORANGE, label="Z oporem")
axes[0].set_ylabel("x [m]")
axes[0].set_title("Współrzędne położenia w czasie", loc="left")
axes[0].legend()
axes[1].plot(czas, y0, color=BLUE, label="Bez oporu")
axes[1].plot(t_opor, y_opor, color=ORANGE, label="Z oporem")
axes[1].axhline(0, color=INK, lw=0.8)
axes[1].set(xlabel="Czas t [s]", ylabel="y [m]")
zapisz(fig, "polozenie_czas")

fig, axes = plt.subplots(2, 1, figsize=(9, 6), sharex=True, layout="constrained")
axes[0].plot(czas, vx0, color=BLUE, label="Bez oporu")
axes[0].plot(t_opor, vx_opor, color=ORANGE, label="Z oporem")
axes[0].set_ylabel("$v_x$ [m/s]")
axes[0].set_title("Składowe prędkości", loc="left")
axes[0].legend()
axes[1].plot(czas, vy0, color=BLUE, label="Bez oporu")
axes[1].plot(t_opor, vy_opor, color=ORANGE, label="Z oporem")
axes[1].axhline(0, color=INK, lw=0.8)
axes[1].set(xlabel="Czas t [s]", ylabel="$v_y$ [m/s]")
zapisz(fig, "predkosc")

fig, ax = plt.subplots(figsize=(9, 4.5), layout="constrained")
ax.plot(czas, np.hypot(vx0, vy0), color=BLUE, label="Bez oporu")
ax.plot(t_opor, np.hypot(vx_opor, vy_opor), color=ORANGE, label="Z oporem")
ax.set(
    xlabel="Czas t [s]",
    ylabel="Wartość prędkości |v| [m/s]",
    title="Zmiana wartości prędkości",
)
ax.legend()
zapisz(fig, "wartosc_predkosci")

fig, ax = plt.subplots(figsize=(9, 4.5), layout="constrained")
ax.plot(czas, np.full_like(czas, -G), color=BLUE, label="Bez oporu: $a_y$")
ax.plot(
    t_opor,
    -G - (DRAG_FACTOR / MASS) * np.hypot(vx_opor, vy_opor) * vy_opor,
    color=ORANGE,
    label="Z oporem: $a_y$",
)
ax.plot(
    t_opor,
    -(DRAG_FACTOR / MASS) * np.hypot(vx_opor, vy_opor) * vx_opor,
    color=GREEN,
    label="Z oporem: $a_x$",
)
ax.axhline(0, color=INK, lw=0.8)
ax.set(
    xlabel="Czas t [s]",
    ylabel="Przyspieszenie [m/s²]",
    title="Przyspieszenie: grawitacja i siła oporu",
)
ax.legend()
zapisz(fig, "przyspieszenie")

energia_kin_bez = 0.5 * MASS * (vx0**2 + vy0**2)
energia_kin_opor = 0.5 * MASS * (vx_opor**2 + vy_opor**2)
energia_pot_bez = MASS * G * y0
energia_pot_opor = MASS * G * y_opor
fig, ax = plt.subplots(figsize=(9, 4.5), layout="constrained")
ax.plot(czas, energia_kin_bez + energia_pot_bez, color=BLUE, label="Bez oporu: E")
ax.plot(
    t_opor,
    energia_kin_opor + energia_pot_opor,
    color=ORANGE,
    label="Z oporem: E mechaniczna",
)
ax.set(
    xlabel="Czas t [s]",
    ylabel="Energia mechaniczna [J]",
    title="Energia mechaniczna a praca siły oporu",
)
ax.legend()
zapisz(fig, "energia")
```


## 7. Wnioski

1. Bez oporu ruch poziomy jest jednostajny, pionowy jednostajnie przyspieszony,
   a tor jest parabolą. Czas lotu, wysokość maksymalną i zasięg można wyprowadzić
   bezpośrednio z równań kinematycznych.
2. Opór kwadratowy zależy od całego wektora prędkości, dlatego sprzęga ruch w
   obu osiach. Dla przyjętego modelu trzeba rozwiązać układ równań numerycznie.
3. Dla $v_0=36\ \mathrm{m/s}$ i $\alpha=11^\circ$ model idealny daje zasięg
   $49{,}4893\ \mathrm{m}$, a model z oporem kuli o masie $0{,}145\ \mathrm{kg}$
   i średnicy $0{,}100\ \mathrm{m}$ daje $33{,}6641\ \mathrm{m}$.
4. W modelu idealnym energia mechaniczna jest zachowana. Opór powietrza wykonuje
   ujemną pracę i powoduje jej spadek.
