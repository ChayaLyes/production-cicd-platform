# 🚀 production-cicd-platform

> Pipeline CI/CD production-grade pour une plateforme e-commerce — Jenkins + GitHub Actions + Kubernetes + NGINX + TLS + Monitoring complet

## 🎯 Problème résolu

Automatisation complète du cycle de vie applicatif : zéro déploiement manuel, détection des failles de sécurité avant production, monitoring 24h/24 avec alertes Slack.

## 🏗 Architecture
## 🛠 Stack technique

| Catégorie | Outils |
|-----------|--------|
| CI/CD | Jenkins, GitHub Actions |
| Sécurité | Snyk, Trivy, SonarQube |
| Déploiement | Kubernetes k3s, Helm |
| Réseau | NGINX Ingress, cert-manager, Let's Encrypt |
| Monitoring | Prometheus, Grafana, Blackbox Exporter |
| Notifications | Slack |
| Registry | GitHub Container Registry (GHCR) |

## 📦 Microservices

| Service | Port | Description |
|---------|------|-------------|
| catalogue | 8000 | Liste et détail des produits |
| panier | 8001 | Gestion du panier d'achat |
| paiement | 8002 | Traitement des paiements |

## 🚦 Pipeline CI/CD

1. **Jenkins** — build Docker + analyse SonarQube
2. **Snyk** — scan vulnérabilités dépendances
3. **Trivy** — scan image Docker (CVE HIGH/CRITICAL)
4. **Push GHCR** — image signée et versionnée
5. **Deploy k3s** — déploiement automatique Kubernetes
6. **Slack** — notification succès/échec

## 📊 Monitoring

- **Prometheus** scrape les métriques toutes les 15s
- **Grafana** dashboard temps réel (latence, erreurs, trafic)
- **Blackbox Exporter** surveille les endpoints /health
- **Alertmanager** envoie une alerte Slack si service down > 30s

## 🏃 Lancer en local

```bash
# Cloner le repo
git clone https://github.com/ChayaLyes/production-cicd-platform.git
cd production-cicd-platform

# Lancer tous les services
docker-compose up -d

# Vérifier
curl http://localhost:8000/health
curl http://localhost:8001/health
curl http://localhost:8002/health
```

## 👤 Auteur

**Lyes Chaya** — DevOps Engineer
- GitHub : [@ChayaLyes](https://github.com/ChayaLyes)
- LinkedIn : [lyes-chaya](https://linkedin.com/in/lyes-chaya-b12065208)
