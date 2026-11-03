# Code & Cogito: Reformation — When Authority Crumbles
# Article: https://code-cogito.com/en/reformation-authority-challenged-en/
# All the code blocks of the article, in order. Program output is kept as comments.
# Note: the article shows this code in excerpts, so this file does not run on its own.
import numpy as np

# SIR-style model for idea diffusion via printed pamphlets
# S = unexposed population, I = actively sharing, R = absorbed/moved on

def pamphlet_diffusion(pop=1_000_000, initial_readers=500,
                       beta_no_press=0.02, beta_with_press=0.35,
                       gamma=0.05, days=180):
    """
    Compare idea spread with and without the printing press.
    beta: transmission rate (how fast ideas spread per contact)
    gamma: recovery rate (how fast people stop actively sharing)
    """
    results = {}
    for label, beta in [("Without Press (Wycliffe era)", beta_no_press),
                        ("With Press (Luther era)", beta_with_press)]:
        S, I, R = pop - initial_readers, initial_readers, 0
        history = {"S": [S], "I": [I], "R": [R]}

        for _ in range(days):
            new_infected = beta * S * I / pop
            new_recovered = gamma * I
            S -= new_infected
            I += new_infected - new_recovered
            R += new_recovered
            history["S"].append(S)
            history["I"].append(I)
            history["R"].append(R)

        results[label] = history

    # Plot comparison
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    for ax, (label, hist) in zip(axes, results.items()):
        days_range = range(len(hist["S"]))
        ax.fill_between(days_range, hist["I"], alpha=0.4, label="Actively sharing")
        ax.fill_between(days_range, hist["R"], alpha=0.3, label="Absorbed idea")
        ax.set_title(label, fontsize=13, fontweight="bold")
        ax.set_xlabel("Days")
        ax.set_ylabel("Population")
        ax.legend()
        ax.set_ylim(0, pop)

    plt.suptitle("Pamphlet Diffusion: Why Luther Succeeded Where Wycliffe Failed",
                 fontsize=14, fontweight="bold")
    plt.tight_layout()
    plt.savefig("pamphlet_diffusion.png", dpi=150, bbox_inches="tight")
    plt.show()

pamphlet_diffusion()

import numpy as np

def cascade_failure_simulation(n_institutions=20, n_simulations=500,
                               connection_density=0.3, failure_threshold=0.4):
    """
    Model how questioning one institution cascades to others.
    Each institution has connections; when enough connected
    institutions fail, it fails too (like dominoes).
    """
    np.random.seed(1517)  # The year it all started

    institutions = [
        "Papal Authority", "Indulgences", "Clerical Celibacy",
        "Monasticism", "Church Courts", "Tithes System",
        "Saint Veneration", "Pilgrimages", "Purgatory Doctrine",
        "Sacramental System", "Episcopal Hierarchy", "Canon Law",
        "Church Land Ownership", "Clerical Tax Exemption",
        "Latin Liturgy", "Ecclesiastical Appointments",
        "Religious Orders", "University Theology", "Church Censorship",
        "Feudal Obligations"
    ]

    # Create random adjacency matrix (symmetric)
    adj = np.random.rand(n_institutions, n_institutions) < connection_density
    np.fill_diagonal(adj, False)
    adj = adj | adj.T

    cascade_sizes = []
    for _ in range(n_simulations):
        failed = np.zeros(n_institutions, dtype=bool)
        failed[0] = True  # Papal Authority questioned first

        changed = True
        while changed:
            changed = False
            for i in range(n_institutions):
                if failed[i]:
                    continue
                neighbors = adj[i]
                if neighbors.sum() == 0:
                    continue
                failed_neighbors = (failed & neighbors).sum()
                if failed_neighbors / neighbors.sum() >= failure_threshold:
                    failed[i] = True
                    changed = True

        cascade_sizes.append(failed.sum())

    # Visualize distribution of cascade sizes
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.hist(cascade_sizes, bins=range(1, n_institutions + 2),
            alpha=0.7, color="#c0392b", edgecolor="black")
    ax.axvline(np.mean(cascade_sizes), color="black", linestyle="--",
               label=f"Mean cascade: {np.mean(cascade_sizes):.1f} institutions")
    ax.set_xlabel("Number of Institutions Affected", fontsize=12)
    ax.set_ylabel("Frequency (out of 500 simulations)", fontsize=12)
    ax.set_title("Cascade Failure: How Questioning One Authority Topples Many",
                 fontsize=13, fontweight="bold")
    ax.legend(fontsize=11)
    plt.tight_layout()
    plt.savefig("cascade_failure.png", dpi=150, bbox_inches="tight")
    plt.show()

    print(f"Average institutions affected: {np.mean(cascade_sizes):.1f} / {n_institutions}")
    print(f"Full cascade probability: {sum(1 for s in cascade_sizes if s == n_institutions) / n_simulations:.1%}")

cascade_failure_simulation()
