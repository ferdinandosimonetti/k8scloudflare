from kubernetes import client, config, utils
from kubernetes.client.rest import ApiException
from pprint import pprint
import os
import requests

def getCloudflare():
    ipv4 = "https://www.cloudflare.com/ips-v4/#"
    ipv6 = "https://www.cloudflare.com/ips-v6/#"
    try:
        response = requests.get(ipv4)
        response.raise_for_status()
        ipv4list = response.text.splitlines()
    except requests.exceptions.RequestException as e:
        print(f"Error downloading IPv4 Cloudflare file: {e}")
        return None
    try:
        response = requests.get(ipv6)
        response.raise_for_status()
        ipv6list = response.text.splitlines()
    except requests.exceptions.RequestException as e:
        print(f"Error downloading IPv6 Cloudflare file: {e}")
        return None
    combined = ipv4list + ipv6list
    return combined
    

def main():
    khost = "KUBERNETES_SERVICE_HOST"
    if khost in os.environ:
        config.load_incluster_config()
    else:
        config.load_kube_config()
    k8s_client = client.ApiClient()
    api_instance = client.CustomObjectsApi(k8s_client)

    group = 'gateway.envoyproxy.io'
    plural = 'securitypolicies'
    version = 'v1alpha1'
    apiversion = group + "/" + version
    namespace = os.environ.get("POLICYNAMESPACE","balancers")
    name = os.environ.get("POLICYNAME","from-cloudflare")
    gateway = os.environ.get("GATEWAYNAME","gateway-public")
    pretty = True
    iplist = getCloudflare()
    if iplist:
        data = {
            "apiVersion": apiversion,
            "kind": "SecurityPolicy",
            "metadata": {
                "name": name,
                "namespace": namespace
            },
            "spec": {
                "targetRefs": [
                    {
                        "group": "gateway.networking.k8s.io",
                        "kind": "Gateway",
                        "name": gateway
                    }
                ],
                "authorization": {
                    "defaultAction": "Deny",
                    "rules": [
                        {
                            "action": "Allow",
                            "principal": {
                                "clientCIDRs": iplist
                            }
                        }
                    ]
                }
            }
        }
        try:
            api_response = api_instance.delete_namespaced_custom_object(group, version, namespace, plural, name)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CustomObjectsApi->delete_namespaced_custom_object: %s\n" % e)
        try:
            api_response = api_instance.create_namespaced_custom_object(group, version, namespace, plural, data, pretty=pretty)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CustomObjectsApi->create_namespaced_custom_object: %s\n" % e)
        #utils.create_from_dict(k8s_client,data)
    # example nginx deployment
    #example_dict = {'apiVersion': 'apps/v1', 'kind': 'Deployment', 'metadata': {'name': 'k8s-py-client-nginx', 'namespace': 'default'}, 'spec': {'selector': {'matchLabels': {'app': 'nginx'}}, 'replicas': 1, 'template': {'metadata': {'labels': {'app': 'nginx'}}, 'spec': {'containers': [{'name': 'nginx', 'image': 'nginx:1.14.2', 'ports': [{'containerPort': 80}]}]}}}}
    #utils.create_from_dict(k8s_client, example_dict)

if __name__ == '__main__':
    main()