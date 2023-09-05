def build_profile(fname,lname,**userinfo):
    profile={'fname:':fname,'lname:':lname}
    for key,val in userinfo.items():
        profile['key']=val
    return profile
print(build_profile('hamza','ahmed',age=21))
