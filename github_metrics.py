import urllib.request
import json
import sys
import os

# Paramètre par défaut : le dépot Github
REPO = "alexcmb/simeis-sdv"
if len(sys.argv) > 1:
    REPO = sys.argv[1]

def request_github_api(repo, page):
    """Effectue la requête sur l'API GitHub pour récupérer une page d'issues"""
    url = f"https://api.github.com/repos/{repo}/issues?state=all&per_page=100&page={page}"
    req = urllib.request.Request(url)
    req.add_header('Accept', 'application/vnd.github.v3+json')
    req.add_header('User-Agent', 'Metrics-Script')
    
    # Utilise un token GITHUB_TOKEN s'il est défini pour éviter les limites d'API
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        req.add_header('Authorization', f'token {token}')
        
    try:
        with urllib.request.urlopen(req) as response:
            return json.loads(response.read().decode())
    except urllib.error.HTTPError as e:
        print(f"Erreur HTTP {e.code}: {e.reason}.")
        if e.code == 403 or e.code == 404:
            print("Astuce : Si le dépôt est privé ou que vous êtes limité par l'API (rate limit), exportez une variable GITHUB_TOKEN.")
            print("Exemple: export GITHUB_TOKEN='votre_token_ici'")
        sys.exit(1)
    except Exception as e:
        print(f"Erreur lors de la requête : {e}")
        sys.exit(1)

def get_all_issues(repo):
    """Pagine sur l'API pour récupérer toutes les issues."""
    issues = []
    page = 1
    print(f"[*] Récupération des issues pour {repo} ...")
    
    while True:
        data = request_github_api(repo, page)
        if not data:
            break
            
        issues.extend(data)
        
        # Si la page contient moins de 100 éléments, on a atteint la fin
        if len(data) < 100:
            break
        page += 1
        
    return issues


all_items = get_all_issues(REPO)

total_issues, open_issues, closed_issues = 0, 0, 0
total_prs, open_prs, closed_prs = 0, 0, 0
labels_issues = {}
labels_prs = {}

# Parcourir et extraire les métriques
for item in all_items:
    is_pr = "pull_request" in item
    state = item.get("state")
    
    if is_pr:
        total_prs += 1
        if state == "open":
            open_prs += 1
        else:
            closed_prs += 1
            
        for label in item.get("labels", []):
            name = label["name"]
            labels_prs[name] = labels_prs.get(name, 0) + 1
    else:
        total_issues += 1
        if state == "open":
            open_issues += 1
        else:
            closed_issues += 1
            
        for label in item.get("labels", []):
            name = label["name"]
            labels_issues[name] = labels_issues.get(name, 0) + 1

# Fonction utilitaire pour afficher les labels
def print_labels(counts):
    if not counts:
        print("    (Aucun label utilisé ou trouvé)")
    else:
        for label, count in sorted(counts.items(), key=lambda x: x[1], reverse=True):
            print(f"    - [{label}] : {count}")

# Affichage des métriques
print("\n" + "="*40)
print(f"  MÉTRIQUES POUR : {REPO}")
print("="*40)

print("\n--- 1. ISSUES (Tickets Classiques) ---")
print(f"Total : {total_issues}")
print(f"  - Ouvertes : {open_issues}")
print(f"  - Fermées  : {closed_issues}")
print("  Labels utilisés :")
print_labels(labels_issues)

print("\n--- 2. PULL REQUESTS ---")
print(f"Total : {total_prs}")
print(f"  - Ouvertes : {open_prs}")
print(f"  - Fermées  : {closed_prs}")
print("  Labels utilisés :")
print_labels(labels_prs)

print("\n" + "="*40 + "\n")
