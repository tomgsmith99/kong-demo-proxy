from dotenv import load_dotenv

import os

from castle.configuration import configuration, DEFAULT_ALLOWLIST

load_dotenv()

# Same as setting it through Castle.api_secret

configuration.api_secret = os.getenv('castle_api_secret')

# For authenticate method you can set failover strategies: allow(default), deny, challenge, throw
configuration.failover_strategy = 'deny'

# Castle::RequestError is raised when timing out in milliseconds (default: 1000 milliseconds)
configuration.request_timeout = 1500

# Base Castle API url
# configuration.base_url = "https://api.castle.io/v1"

# Logger (need to respond to info method) - logs Castle API requests and responses
# configuration.logger = logging.getLogger()

# Allowlisted and Denylisted headers are case insensitive
# and allow to use _ and - as a separator, http prefixes are removed
# By default all headers are passed, but some are automatically scrubbed.
# If you need to apply an allowlist, we recommend using the minimum set of
# standard headers that we've exposed in the `DEFAULT_ALLOWLIST` constant.
# Allowlisted headers
configuration.allowlisted = DEFAULT_ALLOWLIST + ['X_HEADER']

# Denylisted headers take advantage over allowlisted elements. Note that
# some headers are always scrubbed, for security reasons.
configuration.denylisted = ['HTTP-X-header']

# Castle needs the original IP of the client, not the IP of your proxy or load balancer.
# The SDK will only trust the proxy chain as defined in the configuration.
# We try to fetch the client IP based on X-Forwarded-For or Remote-Addr headers in that order,
# but sometimes the client IP may be stored in a different header or order.
# The SDK can be configured to look for the client IP address in headers that you specify.

# Sometimes, Cloud providers do not use consistent IP addresses to proxy requests.
# In this case, the client IP is usually preserved in a custom header. Example:
# Cloudflare preserves the client request in the 'Cf-Connecting-Ip' header.
# It would be used like so: configuration.ip_headers=['Cf-Connecting-Ip']
configuration.ip_headers = []

# If the specified header or X-Forwarded-For default contains a proxy chain with public IP addresses,
# then you must choose only one of the following (but not both):
# 1. The trusted_proxies value must match the known proxy IPs. This option is preferable if the IP is static.
# 2. The trusted_proxy_depth value must be set to the number of known trusted proxies in the chain (see below).
# This option is preferable if the IPs are ephemeral, but the depth is consistent.

# Additionally to make X-Forwarded-For and other headers work better discovering client ip address,
# and not the address of a reverse proxy server, you can define trusted proxies
# which will help to fetch proper ip from those headers

# In order to extract the client IP of the X-Forwarded-For header
# and not the address of a reverse proxy server, you must define all trusted public proxies
# you can achieve this by listing all the proxies ip defined by string or regular expressions
# in the trusted_proxies setting
configuration.trusted_proxies = []
# or by providing number of trusted proxies used in the chain
configuration.trusted_proxy_depth = 0
# note that you must pick one approach over the other.

# If there is no possibility to define options above and there is no other header that holds the client IP,
# then you may set trust_proxy_chain = true to trust all of the proxy IPs in X-Forwarded-For
configuration.trust_proxy_chain = False
# *Warning*: this mode is highly promiscuous and could lead to wrongly trusting a spoofed IP if the request passes through a malicious proxy

# *Note: the default list of proxies that are always marked as "trusted" can be found in: Castle::Configuration::TRUSTED_PROXIES
