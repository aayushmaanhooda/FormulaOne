import fastf1

def main():
    session = fastf1.get_session(2025, 10, "Q")
    print(session)
    print("Hello from f1!")


if __name__ == "__main__":
    main()
