import json

def lambda_handler(event, context):
    # TODO implement
    if event:
        var = event['replace_string']
        var = str(var)
        var = var.replace('Amazon',"Amazon©")
        var = var.replace('Google','Google©')
        var = var.replace('Oracle','Oracle©')
        var = var.replace('Microsoft','Mircosoft©')
        var = var.replace('Deloitte','Deloitte©')
        var = var.encode('utf8')
    return var
