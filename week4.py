import random

def coin_toss():
    return random.choice(["Heads", "Tails"])

def multiple_tosses(num_flips):
    heads_count = 0
    tails_count = 0

    for _ in range(num_flips):
        result = coin_toss()
        print(f"Result: {result}")
        if result == "Heads":
            heads_count += 1
        else:
            tails_count += 1

    return heads_count, tails_count

def main():
    while True:
        try:
            num_flips = int(input("Enter the number of coin flips: "))
            if num_flips <= 0:
                print("Please enter a positive integer.")
                continue

            heads, tails = multiple_tosses(num_flips)
            total = heads + tails

            print("\nResults Summary:")
            print(f"Heads: {heads} ({(heads / total) * 100:.2f}%)")
            print(f"Tails: {tails} ({(tails / total) * 100:.2f}%)")

            repeat = input("Do you want to flip again? (yes/no): ").strip().lower()
            if repeat != 'yes':
                print("Thank you for using the Virtual Coin Toss program!")
                break

        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()