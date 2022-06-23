import instaloader

ig = instaloader.Instaloader()
dp = input("Kullanici adini giriniz : ")

ig.download_profile(dp , profile_pic_only=True)