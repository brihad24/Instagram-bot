from instagrapi import Client

# Not including the credentials for privacy reasons
username = "" 
password = ""

client = Client()
client.login(username, password)

hashtag = input("Enter the hashtags you want to search for: ")
no_of_posts = int(input("Enter how many posts you want to perform actions on: "))

medias = client.hashtag_medias_recent(hashtag, no_of_posts)

for i,media in enumerate(medias):
    client.media_like(media.id)
    print(f"Liked post number {i+1} of hashtag {hashtag}")

    if i % 5 == 0:
        client.media_comment(media.id, "Very informative")
        print(f"Commented on the {i + 1}th post")