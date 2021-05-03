
def plain(text):
    input_text = input("Text: ")
    text += input_text
    return text

def bold(text):
    input_text = input("Text: ")
    text += f"**{input_text}**"
    return text

def italic(text):
    input_text = input("Text: ")
    text += f"*{input_text}*"
    return text

def inline_code(text):
    input_text = input("Text: ")
    text += f"`{input_text}`"
    return text

def link(text):
    label = input("Label: ")
    url = input("URL: ")

    return f"[{label}]({url})"

def header(text):
    level = 0
    while level not in range(1,6):
        level = int(input("level: "))
        if level > 6:
            print("The level should be within the range of 1 to 6")
    input_text = input("Text: ")
    text += ("#" * level) + " " + input_text + "\n"
    return text


def new_line(text):
    text += "\n"
    return text

def ordered_list(text):
    while True:
        row_num = int(input("Number of rows: "))
        if row_num <= 0:
            print("The number of rows should be greater than zero")
        elif row_num:
            break
    i = 1
    while i <= row_num:
        row_text = input(f"Row #{i}: ")
        text += f"{i}. {row_text}\n"
        i += 1
    return text

def unordered_list(text):
    while True:
        row_num = int(input("Number of rows: "))
        if row_num <= 0:
            print("The number of rows should be greater than zero")
        elif row_num:
            break
    i = 1
    while i <= row_num:
        row_text = input(f"Row #{i}: ")
        text += f"* {row_text}\n"
        i += 1
    return text

def conv_txt_file(text):
    f = open('output.md', 'w+')
    f.write(text)
    f.close()

def markdown_editor():
    choice = None
    output_text = ""
    while True:
        choice = input("Choose a formatter: ")
        if choice not in ['italic', '!help', 'header', 'ordered-list', 'unordered-list', 'link', '!done', 'inline-code', 'plain', 'bold', 'new-line']:
            print("Unknown formatting type or command. Please try again")
        else:
            if choice == "header":
                output_text = header(output_text)
                print(output_text)
            if choice == "plain":
                output_text = plain(output_text)
                print(output_text)
            if choice == "bold":
                output_text = bold(output_text)
                print(output_text)
            if choice == "italic":
                output_text = italic(output_text)
                print(output_text)
            if choice == "inline-code":
                output_text = inline_code(output_text)
                print(output_text)
            if choice == "link":
                output_text = link(output_text)
                print(output_text)
            if choice == "new-line":
                output_text = new_line(output_text)
                print(output_text)
            if choice == "ordered-list":
                output_text = ordered_list(output_text)
                print(output_text)
            if choice == "unordered-list":
                output_text = unordered_list(output_text)
                print(output_text)
        if choice == "!help":
            print("Available formatters: plain bold italic link inline-code header ordered-list unordered-list line-break\nSpecial commands: !help !done")
        if choice == "!done":
            conv_txt_file(output_text)
            return


markdown_editor()
