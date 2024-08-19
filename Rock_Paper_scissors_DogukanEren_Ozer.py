import random  # Rastgele seçimler yapmak için random modülünü çağırdık.

ACTIONS = ['rock', 'paper', 'scissors']  # Oyunda kullanılacak olan seçenekleri tanımlıyoruz.


def play_round():
    # Bir roundu oynatan fonksiyon. Bu fonksiyon, kullanıcı ve bilgisayarın seçimlerini alır ve roundun sonucunu belirler.

    player1 = input("Choose Rock, Paper, or Scissors (or type 'exit' to quit): ").lower()
    # Kullanıcıdan bir giriş alıyoruz ve küçük harfe çeviriyoruz. Bu sayede kullanıcı büyük harfle veya küçük harfle yazsa da karşılaştırma doğru çalışır.

    if player1 == 'exit':
        return None, None
        # Eğer kullanıcı 'exit' yazarsa, fonksiyon None değerini döndürür ve roundu sonlandırır. None bir değer olmadığını belirtir.

    if player1 not in ACTIONS:
        print('Please choose a valid option: Rock, Paper, or Scissors')
        return None, None
        # Kullanıcı geçersiz bir seçim yaptıysa None döndürülür ve round tekrarlanır

    computer = random.choice(ACTIONS)
    # Bilgisayar için rastgele bir seçim yapıyoruz. Bu bilgisayarın rock, paper veya scissors seçeneklerinden birini seçmesini sağlar.

    print(f'You chose: {player1.capitalize()}')
    # Kullanıcının yaptığı seçimi ekrana yazdırıyoruz. capitalize() stringin ilk harfini büyük yapar.

    print(f'Computer chose: {computer.capitalize()}')
    # Bilgisayarın yaptığı seçimi ekrana yazdırıyoruz. capitalize() stringin ilk harfini büyük yapar

    if player1 == computer:
        print("It's a tie!")
        return 0, 0
        # Eğer seçimler aynıysa roundun berabere olduğunu belirtiriz ve her iki taraf için de 0 puan döneriz

    elif (player1 == 'rock' and computer == 'scissors') or \
            (player1 == 'scissors' and computer == 'paper') or \
            (player1 == 'paper' and computer == 'rock'):
        print("You win this round!")
        return 1, 0
        # Kullanıcının seçimi bilgisayarın seçimini yendiyse kullanıcı için 1 puan ve bilgisayar için 0 puan döneriz.

    else:
        print("Computer wins this round!")
        return 0, 1
        # Bilgisayarın seçimi kullanıcının seçimini yendiyse bilgisayar için 1 puan ve kullanıcı için 0 puan döneriz


def play_game():
    # Bir oyunu başlatan ve oynatan fonksiyon. Bu fonksiyon her iki oyuncu da 2 puana ulaşana kadar roundları oynatır

    player_score = 0  # Kullanıcının skorunu tutmak için bir değişken.
    computer_score = 0  # Bilgisayarın skorunu tutmak için bir değişken.
    round_number = 1  # Round numarasını tutmak için bir değişken.

    while player_score < 2 and computer_score < 2:
        # Kullanıcı veya bilgisayar 2 puana ulaşana kadar roundları oynatır

        print(f"Round {round_number}:")
        # Mevcut round numarasını ekrana yazdırır.

        player_point, computer_point = play_round()
        # Bir round oynatır ve sonucu (kazanılan puanları) alır. Bu değerler, play_round() fonksiyonundan dönen 1 veya 0 olabilir

        if player_point is None:
            print("Exiting game.")
            return
            # Eğer kullanıcı oyunu sonlandırmak istediyse (None döndü) oyun sonlandırılır

        player_score += player_point
        computer_score += computer_point
        # Kazanılan puanları kullanıcının ve bilgisayarın skorlarına ekler

        print(f"Current Score - You: {player_score}, Computer: {computer_score}\n")
        # Mevcut skor durumunu ekrana yazdırır.

        round_number += 1
        # Round numarasını bir artırır böylece bir sonraki roundda doğru numara gösterilir

    if player_score == 2:
        print("Congratulations! You won the game!")
        # Eğer kullanıcı 2 puana ulaştıysa oyunu kazandığını belirten bir mesaj gösterilir

    else:
        print("Computer won the game. Better luck next time!")
        # Eğer bilgisayar 2 puana ulaştıysa bilgisayarın kazandığını belirten bir mesaj gösterilir


def rock_paper_scissors_Dogukan_Eren_Ozer():
    # Oyunu başlatan ve tekrar oynama seçeneği sunan ana fonksiyon. Bu fonksiyon birden fazla oyun oynanmasını sağlar

    game_number = 1  # Oynanan oyunların sayısını tutmak için bir değişken

    while True:
        print(f"Starting Game {game_number}...\n")
        # Kaçıncı oyunun başladığını ekrana yazdırır

        play_game()
        # Bir oyun başlatır ve oynatır.

        play_again = input("Do you want to play another game? (yes/no): ").lower()
        # Oyunu tekrar oynayıp oynamak istemediğini kullanıcıya sorar

        if play_again != 'yes':
            print("Thanks for playing! Goodbye.")
            break
            # Eğer kullanıcı yes dışında bir cevap verdiyse, döngü sonlanır ve program biter

        game_number += 1
        # Eğer kullanıcı tekrar oynamak isterse, oyun numarasını bir artırır ve yeni bir oyun başlar


if __name__ == "__main__":
    rock_paper_scissors_Dogukan_Eren_Ozer()
    # Program, ana fonksiyonu çalıştırır programın çalıştırıldığında hemen başlamasını sağlar

