import instaloader
ig=instaloader.Instaloader()
username=input("Enter username:")
profile=instaloader.Profile.from_username(ig.context , username)
print("Username:" , profile.username)
print("Number of posts uploaded :" ,profile.mediacount)
print(profile.username+" is having " +str(profile.followers)+'followers.')
print("Bio : " , profile.biograohy)
instaloader.Instaloader().download_profile(username, prfile_pic_only=True)
