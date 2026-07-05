# Architecture — production-cicd-platform

## Vue d'ensemble

3 microservices e-commerce déployés sur Kubernetes avec un pipeline CI/CD complet.

## Microservices

| Service    | Port | Rôle                        |
|------------|------|-----------------------------|
| catalogue  | 8000 | Liste et détail des produits|
| panier     | 8001 | Gestion du panier           |
| paiement   | 8002 | Traitement des paiements    |

## Pipeline CI/CD
## Stack technique

- **CI/CD** : Jenkins + GitHub Actions
- **Sécurité** : Snyk + Trivy + SonarQube
- **Déploiement** : Kubernetes k3s + NGINX + TLS
- **Monitoring** : Prometheus + Grafana + Alertmanager
- **Notifications** : Slack
