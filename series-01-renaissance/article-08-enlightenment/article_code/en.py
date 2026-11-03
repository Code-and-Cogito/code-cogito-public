# Code & Cogito: Enlightenment — When Reason Becomes the New God
# Article: https://code-cogito.com/en/enlightenment-age-of-reason-en/
# All the code blocks of the article, in order. Program output is kept as comments.
# Note: the article shows this code in excerpts, so this file does not run on its own.
import numpy as np

# Define thinkers and their primary intellectual influences
thinkers = {
    "Locke":          {"born": 1632, "country": "England",  "domain": "political"},
    "Newton":         {"born": 1643, "country": "England",  "domain": "science"},
    "Voltaire":       {"born": 1694, "country": "France",   "domain": "political"},
    "Montesquieu":    {"born": 1689, "country": "France",   "domain": "political"},
    "Hume":           {"born": 1711, "country": "Scotland",  "domain": "philosophy"},
    "Rousseau":       {"born": 1712, "country": "France",   "domain": "political"},
    "Diderot":        {"born": 1713, "country": "France",   "domain": "philosophy"},
    "Smith":          {"born": 1723, "country": "Scotland",  "domain": "economics"},
    "Kant":           {"born": 1724, "country": "Prussia",  "domain": "philosophy"},
    "Franklin":       {"born": 1706, "country": "America",  "domain": "political"},
    "Jefferson":      {"born": 1743, "country": "America",  "domain": "political"},
    "Wollstonecraft": {"born": 1759, "country": "England",  "domain": "political"},
}

# Directed edges: (source_of_influence -> influenced_by)
influences = [
    ("Locke", "Voltaire"), ("Locke", "Montesquieu"), ("Locke", "Rousseau"),
    ("Locke", "Jefferson"), ("Locke", "Hume"), ("Locke", "Franklin"),
    ("Newton", "Voltaire"), ("Newton", "Hume"), ("Newton", "Kant"),
    ("Newton", "Smith"), ("Newton", "Diderot"),
    ("Voltaire", "Diderot"), ("Voltaire", "Franklin"),
    ("Montesquieu", "Jefferson"), ("Montesquieu", "Smith"),
    ("Hume", "Kant"), ("Hume", "Smith"),
    ("Rousseau", "Kant"), ("Rousseau", "Wollstonecraft"),
    ("Rousseau", "Jefferson"),
    ("Smith", "Jefferson"),
    ("Locke", "Wollstonecraft"), ("Voltaire", "Wollstonecraft"),
]

# Layout: x = birth year, y = grouped by country
country_y = {"England": 4, "Scotland": 3, "France": 2,
             "Prussia": 1, "America": 0}
domain_colors = {"political": "#e74c3c", "science": "#3498db",
                 "philosophy": "#2ecc71", "economics": "#f39c12"}

# Draw influence arrows
for src, tgt in influences:
    x0, y0 = thinkers[src]["born"], country_y[thinkers[src]["country"]]
    x1, y1 = thinkers[tgt]["born"], country_y[thinkers[tgt]["country"]]
    ax.annotate("", xy=(x1, y1), xytext=(x0, y0),
                arrowprops=dict(arrowstyle="->", color="#bdc3c7",
                                alpha=0.5, connectionstyle="arc3,rad=0.1"))

# Draw thinker nodes
for name, info in thinkers.items():
    x = info["born"]
    y = country_y[info["country"]]
    color = domain_colors[info["domain"]]
    # Count influence connections (in + out degree)
    degree = sum(1 for s, t in influences if s == name or t == name)
    size = 80 + degree * 40
    ax.scatter(x, y, s=size, c=color, edgecolors="black",
               linewidths=1.5, zorder=5)
    ax.annotate(name, (x, y), textcoords="offset points",
                xytext=(0, 12), ha="center", fontsize=9, fontweight="bold")

# Labels and legend

patches = [mpatches.Patch(color=c, label=d.capitalize())
           for d, c in domain_colors.items()]

import numpy as np

# Three revolutions inspired by Enlightenment ideas
revolutions = {
    "American (1775-1783)": {
        "duration_years": 8,
        "deaths_estimate": 37_000,
        "population": 2_500_000,
        "outcome_democracy_years": 248,  # still ongoing
        "key_documents": ["Declaration of Independence", "Constitution",
                          "Bill of Rights"],
        "terror_deaths": 0,
        "color": "#3498db"
    },
    "French (1789-1799)": {
        "duration_years": 10,
        "deaths_estimate": 600_000,
        "population": 28_000_000,
        "outcome_democracy_years": 0,  # ended in Napoleon
        "key_documents": ["Declaration of Rights of Man",
                          "Civil Constitution of the Clergy"],
        "terror_deaths": 16_594,
        "color": "#e74c3c"
    },
    "Haitian (1791-1804)": {
        "duration_years": 13,
        "deaths_estimate": 350_000,
        "population": 500_000,
        "outcome_democracy_years": 0,  # cycles of instability
        "key_documents": ["Declaration of Independence (1804)"],
        "terror_deaths": 5_000,
        "color": "#2ecc71"
    }
}

# Chart 1: Deaths as % of population
names = list(revolutions.keys())
death_pcts = [revolutions[r]["deaths_estimate"] / revolutions[r]["population"] * 100
              for r in names]
colors = [revolutions[r]["color"] for r in names]
axes[0].barh(names, death_pcts, color=colors, edgecolor="black")
axes[0].set_xlabel("Deaths as % of Population")
axes[0].set_title("Human Cost", fontweight="bold")

# Chart 2: Duration
durations = [revolutions[r]["duration_years"] for r in names]
axes[1].barh(names, durations, color=colors, edgecolor="black")
axes[1].set_xlabel("Years")
axes[1].set_title("Duration", fontweight="bold")

# Chart 3: Terror deaths (state-sponsored executions)
terror = [revolutions[r]["terror_deaths"] for r in names]
axes[2].barh(names, terror, color=colors, edgecolor="black")
axes[2].set_xlabel("Executed by Revolutionary Government")
axes[2].set_title("State Terror", fontweight="bold")
