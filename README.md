# Fetch Cloudflare IPs list and update a Kubernetes resource

This code would fetch the updated Cloudflare owned IP list and use it to rebuild an Envoy Gateway-related Security Policy

References:
- [IP Allowlist/Denylist](https://gateway.envoyproxy.io/docs/tasks/security/restrict-ip-access/)
- [Official Python client library for kubernetes](https://github.com/kubernetes-client/python/blob/master/examples/apply_from_dict.py)
- [Cloudflare IPv4 addresses list](https://www.cloudflare.com/ips-v4/#)
- [Cloudflare IPv6 addresses list](https://www.cloudflare.com/ips-v6/#)
