import json
with open("sample-data.json", "r") as file:
    data = json.load(file)
# print(data)

print("Interface Status")
print("=" * 80)
print(f"{'DN'}{" "*49}{'Description'}{" "*11}{'Speed'}{" "*4}{'MTU'}")
print(f"{"-"*50} {"-"*20}  {"-"*6}  {"-"*6}")

for i in data["imdata"]:
    k = i["l1PhysIf"]["attributes"]
    dn = k.get("dn", "")
    descr = k.get("descr", "")
    speed = k.get("speed", "")
    mtu = k.get("mtu", "")
    # print(item)
    print(f"{dn:<50} {descr:<20} {speed:<8} {mtu:<6}")