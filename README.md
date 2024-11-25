# Fetch Cloudflare IPs list and update a Kubernetes resource

This code would fetch the updated Cloudflare owned IP list and use it to rebuild an Envoy Gateway-related Security Policy

References:
- [IP Allowlist/Denylist](https://gateway.envoyproxy.io/docs/tasks/security/restrict-ip-access/)
- [Load Kubernetes context from within the cluster](https://github.com/kubernetes-client/python/blob/master/examples/in_cluster_config.py)
- [Official Python client library for kubernetes - create custom object](https://github.com/kubernetes-client/python/blob/master/kubernetes/docs/CustomObjectsApi.md#create_namespaced_custom_object)
- [Official Python client library for kubernetes - delete custom object](https://github.com/kubernetes-client/python/blob/master/kubernetes/docs/CustomObjectsApi.md#delete_namespaced_custom_object)
- [Cloudflare IPv4 addresses list](https://www.cloudflare.com/ips-v4/#)
- [Cloudflare IPv6 addresses list](https://www.cloudflare.com/ips-v6/#)
- [Elegantly activation a virtual environment in a Dockerfile](https://pythonspeed.com/articles/activate-virtualenv-dockerfile/)

# How to build multiplatform image on Mac M1

```
k8scloudflare git:(master) ✗ docker buildx build --platform linux/amd64,linux/arm64 -t rimmon1971/cfk8s:0.1 --push  .
[+] Building 15.2s (18/18) FINISHED                                                               docker-container:mybuilder
 => [internal] load build definition from Dockerfile                                                                    0.0s
 => => transferring dockerfile: 276B                                                                                    0.0s
 => [linux/arm64 internal] load metadata for docker.io/library/python:3.12-slim-bookworm                                0.9s
 => [linux/amd64 internal] load metadata for docker.io/library/python:3.12-slim-bookworm                                0.9s
 => [auth] library/python:pull token for registry-1.docker.io                                                           0.0s
 => [internal] load .dockerignore                                                                                       0.0s
 => => transferring context: 2B                                                                                         0.0s
 => [linux/arm64 1/5] FROM docker.io/library/python:3.12-slim-bookworm@sha256:2a6386ad2db20e7f55073f69a98d6da2cf9f168e  0.0s
 => => resolve docker.io/library/python:3.12-slim-bookworm@sha256:2a6386ad2db20e7f55073f69a98d6da2cf9f168e05e7487d2670  0.0s
 => [internal] load build context                                                                                       0.0s
 => => transferring context: 65B                                                                                        0.0s
 => [linux/amd64 1/5] FROM docker.io/library/python:3.12-slim-bookworm@sha256:2a6386ad2db20e7f55073f69a98d6da2cf9f168e  0.0s
 => => resolve docker.io/library/python:3.12-slim-bookworm@sha256:2a6386ad2db20e7f55073f69a98d6da2cf9f168e05e7487d2670  0.0s
 => CACHED [linux/amd64 2/5] RUN python3 -m venv /opt/venv                                                              0.0s
 => CACHED [linux/amd64 3/5] COPY requirements.txt .                                                                    0.0s
 => CACHED [linux/amd64 4/5] RUN pip install -r requirements.txt                                                        0.0s
 => CACHED [linux/amd64 5/5] COPY main.py .                                                                             0.0s
 => CACHED [linux/arm64 2/5] RUN python3 -m venv /opt/venv                                                              0.0s
 => CACHED [linux/arm64 3/5] COPY requirements.txt .                                                                    0.0s
 => CACHED [linux/arm64 4/5] RUN pip install -r requirements.txt                                                        0.0s
 => CACHED [linux/arm64 5/5] COPY main.py .                                                                             0.0s
 => exporting to image                                                                                                 14.2s
 => => exporting layers                                                                                                 1.3s
 => => exporting manifest sha256:4208cc199a99739f08715ff06ef2a3355331e399d4a2eeac8908f55427bc4a0e                       0.0s
 => => exporting config sha256:5a297a85519b70254944d0873e641ec3894144022dc41bc11630d16809c6d2e5                         0.0s
 => => exporting attestation manifest sha256:baa6ca577c14225adc52955d44449dc0e7492f269dd97618aec7479e5915a460           0.0s
 => => exporting manifest sha256:0bde3a9574fe8c6fe7ba4ea5c112febd510ddfcb0bbb7a6d2939ab777abf4713                       0.0s
 => => exporting config sha256:59d8da49b1fc23d8b5ac4ab1a04cb7d48908f098d3e3e1451185aeb8ea5c9653                         0.0s
 => => exporting attestation manifest sha256:3c78a86e68a949a4515ca3bef5fb75c46d47343be64965d53d4167fb85ddf8ef           0.0s
 => => exporting manifest list sha256:326181552af024c5b20b26510dc420ad09d3e8637c7259cad7dee6954170e828                  0.0s
 => => pushing layers                                                                                                  10.6s
 => => pushing manifest for docker.io/rimmon1971/cfk8s:0.1@sha256:326181552af024c5b20b26510dc420ad09d3e8637c7259cad7de  2.3s
 => [auth] rimmon1971/cfk8s:pull,push token for registry-1.docker.io                                                    0.0s
```

