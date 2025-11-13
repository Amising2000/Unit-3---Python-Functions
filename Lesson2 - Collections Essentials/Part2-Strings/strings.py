# Starting with messy user input:
announcment = " BERGEN TECH robotics meeting TODAY! "


# we'll clean it up together
def format_course_code(code):
    # strip = code.strip()
    # upper = strip.upper()
    # return upper
    return code.strip().upper()


print(format_course_code("Hwllo123   "))


def count_hashtags(post):
    # count = 0
    # for char in post:
    #     if char == "#":
    #         count += 1
    # return count
    words = post.split()
    count = 0

    for word in words:
        if word.startswith("#"):
            count = count + 1
    return count

print(count_hashtags("Great game today! #BergenTech #GoGamrz #Pride"))
print(count_hashtags("Meeting tomorrow in room 205"))
print(count_hashtags("#Robotics team wins #StateChampionship! #STEM #BergenTech"))