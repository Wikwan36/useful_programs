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
