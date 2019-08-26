PORT = 3256

# name -> secret (32 hex chars)
USERS = {
    "tg":  "00000000000000000000000000000001",
}

# Makes the proxy harder to detect
# Can be incompatible with very old clients
SECURE_ONLY = True

# Makes the proxy even more hard to detect
# Compatible only with the recent clients
TLS_ONLY = True

# The domain for TLS, bad clients are proxied there
# Use random existing domain, proxy checks it on start
TLS_DOMAIN = "www.google.com"

# Tag for advertising, obtainable from @MTProxybot
AD_TAG = "2b90a147687a0986d4af9f8d2907d676"
