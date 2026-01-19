shelpek_count = input("How many shelpeks to fry? ")  # Asking the user how many shelpeks need frying
try:
    shelpek_count = int(shelpek_count)
    shelpeks = [["raw", "raw"] for _ in range(shelpek_count)]
    time = 0

    while True:
        frying = 0
        for i in range(len(shelpeks)):
            if frying == 2:
                break
            if shelpeks[i][0] == "raw":
                shelpeks[i][0] = "fried"
                print(f"Shelpek {i+1} (side 1) is frying...")
                frying += 1
            elif shelpeks[i][1] == "raw":
                shelpeks[i][1] = "fried"
                print(f"Shelpek {i+1} (side 2) is frying...")
                frying += 1

        time += 10
        if all(side == "fried" for pair in shelpeks for side in pair):
            break

    print("All shelpeks are ready!")
    print("Total frying time:", time, "minutes")
except ValueError:
    print("Please enter a valid integer.")

