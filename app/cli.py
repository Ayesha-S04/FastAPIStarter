from sqlmodel import Session, select
from app.database import engine
from app.models.models import Game, Listing, Rental, Payment


def view_games():
    with Session(engine) as session:
        games = session.exec(select(Game)).all()

        for game in games:
            print(game.id, game.title, game.platform, game.genre)


def list_game():
    title = input("Game title: ")
    platform = input("Platform: ")
    genre = input("Genre: ")
    price = float(input("Price: "))
    user_id = int(input("User ID: "))

    with Session(engine) as session:
        game = Game(
            title=title,
            platform=platform,
            genre=genre
        )

        session.add(game)
        session.commit()
        session.refresh(game)

        listing = Listing(
            game_id=game.id,
            user_id=user_id,
            price=price
        )

        session.add(listing)
        session.commit()

        print("Game listed successfully")


def rent_game():
    listing_id = int(input("Listing ID: "))
    user_id = int(input("User ID: "))

    with Session(engine) as session:
        rental = Rental(
            listing_id=listing_id,
            user_id=user_id
        )

        session.add(rental)
        session.commit()

        print("Game rented successfully")


def return_game():
    rental_id = int(input("Rental ID: "))
    amount = float(input("Payment amount: "))

    with Session(engine) as session:
        payment = Payment(
            rental_id=rental_id,
            amount=amount
        )

        session.add(payment)
        session.commit()

        print("Game returned and payment recorded")


def menu():
    while True:
        print("\n1. View Games")
        print("2. List Game")
        print("3. Rent Game")
        print("4. Return Game")
        print("5. Exit")

        choice = input("Choose: ")

        if choice == "1":
            view_games()

        elif choice == "2":
            list_game()

        elif choice == "3":
            rent_game()

        elif choice == "4":
            return_game()

        elif choice == "5":
            break


menu()