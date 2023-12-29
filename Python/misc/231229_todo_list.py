# utils
welcome_art = """
  _____         _           
 |_   _|__   __| | ___  ___ 
   | |/ _ \ / _` |/ _ \/ __|
   | | (_) | (_| | (_) \__ \\
   |_|\___/ \__,_|\___/|___/
"""

main_prompt = "Enter a command. Type 'h' for help:"

help_msg = """
TODO LIST HELP
Type 'q' to quit
To add a todo to the list, type it and hit enter
To complete a todo enter its number
"""

todos = []

deleted = []


# welcome message
print(welcome_art)

# main program loop
while True:
    # main prompt
    print("*" * len(main_prompt))
    print(main_prompt)
    
    # user input
    user_input = input("> ")

    # process user input
    if user_input == "h":
        print(help_msg)
        continue
    elif user_input == "q":
        if len(deleted) <= 0:
            print("You haven't completed any todo today :(")
        else:
            print(f"Today you completed {len(deleted)} todos:")
            for todo in deleted:
                print(f"{deleted.index(todo) + 1}. {todo}")
        break
    elif user_input.isnumeric():
        idx = int(user_input)
        if idx == 0 or idx > len(todos):
            print("Todo not found. Try Again")
        else:
            done_todo = todos.pop(idx - 1)
            deleted.append(done_todo)
    else:
        todos.append(user_input)

    # print current todos
    for todo in todos:
        print(f"{todos.index(todo) + 1}) {todo}")

    continue
