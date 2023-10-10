# authentik is an open-source Identity Provider that emphasizes flexibility and versatility.

# https://github.com/goauthentik/authentik

# Docker Compose installation
# https://goauthentik.io/docs/installation/docker-compose/?utm_source=github


# Example values to get started:
"""
authentik:
  secret_key: "PleaseGenerateA50CharKey"
  # This sends anonymous usage-data, stack traces on errors and
  # performance data to sentry.beryju.org, and is fully opt-in
  error_reporting:
    enabled: true
  postgresql:
    password: "ThisIsNotASecurePassword"

ingress:
  enabled: true
  hosts:
    - host: authentik.domain.tld
      paths:
        - path: "/"
          pathType: Prefix

postgresql:
  enabled: true
  postgresqlPassword: "ThisIsNotASecurePassword"
redis:
  enabled: true
"""
