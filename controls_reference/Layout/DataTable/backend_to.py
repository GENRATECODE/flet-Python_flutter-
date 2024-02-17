import asyncio 

async def add_item(count ):
    count+=1
    sample=dict()
    sample["s.no"]=count
    sample["name"]=input("Enter the name: ")
    sample["age"]=input("Enter the  age in year :")
    sample ["number"] =input ("Enter the phone number : ")
    
    return sample
