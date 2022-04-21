import googleapiclient.discovery

def check_upgrade(request):
    compute = googleapiclient.discovery.build('compute', 'v1')
    result = compute.instances().start(project='PROJECT_ID', zone='ZONE_NAME', instance='VM_NAME').execute()
return result
