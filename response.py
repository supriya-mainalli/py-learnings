response = {
    "nodes": [
        {
            "name": "cephid01",
            "networks": [
                {
                    "name": "nic0",
                    "speed": "1G",
                    "mac": "xx:aa:bb:cc:88:ca",
                    "addresses": [
                        "10.64.0.20"
                    ]
                },
                {
                    "name": "nic1",
                    "speed": "1G",
                    "mac": "xx:aa:bb:cc:88:cb",
                    "addresses": []
                }
            ]
        },
        {
            "name": "cephid02",
            "networks": [
                {
                    "name": "nic0",
                    "speed": "1G",
                    "mac": "xx:aa:bb:cc:90:ca",
                    "addresses": [
                        "10.64.0.22"
                    ]
                },
                {
                    "name": "nic1",
                    "speed": "1G",
                    "mac": "xx:aa:bb:cc:88:cb",
                    "addresses": []
                }
            ]
        }
    ]
}

nodes = response["nodes"]


my_dict = {}
for node in nodes:
    name = node["name"]
    for network in node["networks"]:
        a = network["addresses"]
        address = [x for x in a]
        if address!=[]:
            print(address)
my_dict[name] = address
print(my_dict)