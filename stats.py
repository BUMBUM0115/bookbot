def get_num_words(text):
    words = text.split()
    return len(words)

def sort_on_count(char_count):
    sorted_list = []
    for char, count in char_count.items():
        sorted_list.append({"character": char, "count": count})
    sorted_list.sort(key=lambda x: x["count"], reverse=True)
    return sorted_list