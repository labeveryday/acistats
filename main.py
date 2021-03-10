import datetime
from app.aci_conn import iACI
from app.aci_webex import send_webex_message


def main():
    aci = iACI()
    tenants = aci.get_tenant()['imdata']
    tenant_count = len(tenants)
    health = aci.get_aci_health()
    newest_tenants = compare_tenant(tenants)
    current_time = get_date()
    webex_message = create_aci_webex_message(aci.username, tenant_count, tenants,
                                       health, newest_tenants, current_time)
    send_webex_message(webex_message)
    updateLog(tenants)


def create_aci_webex_message(name, tenant_count, tenants, health, newest_tenants,
                             current_time):
    tenant_string = " "
    for i in tenants:
        if i['fvTenant']['attributes']['name'] not in newest_tenants:
            tenant_string = tenant_string + f"        \n           {i['fvTenant']['attributes']['name']}\
            **NEW-TENANT** - {current_time}"
    if len(tenant_string) < 2:
        tenant_string =  tenant_string + f"        \n           NO NEW TENANTS"
    message = (f"# THE AWLAYS ON SANDBOX APIC\n\
       **ACI STATUS UPDATE**\n\
       ✅ Successfully logged with {name}\n\
        FabricOverallHealth:\n\
            healthAvg: {health['imdata'][0]['fabricOverallHealthHist5min']['attributes']['healthAvg']},\n\
            healthMax: {health['imdata'][0]['fabricOverallHealthHist5min']['attributes']['healthMax']},\n\
            healthMin: {health['imdata'][0]['fabricOverallHealthHist5min']['attributes']['healthMin']},\n\
        Tentant Count: {tenant_count}\n\
        Here's a list of New Tenants:\
            {tenant_string}")
    return message

def compare_tenant(tenants):
    new_tenants = []
    with open("tenant_log.txt", "r") as file:
        new_tenants = file.read().splitlines()
    return new_tenants

def updateLog(tenants):
    with open("tenant_log.txt", "w") as file:
        for tenant in tenants:
            file.write(f"{tenant['fvTenant']['attributes']['name']}\n")

def get_date():
    """
    GET Current Date and Time
        return: Date/time '03-05-2021 12:04'
        rtype: str
    """
    return datetime.datetime.now().strftime('%m-%d-%Y %H:%M')

if __name__ == "__main__":
    main()
