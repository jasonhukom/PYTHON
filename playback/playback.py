def main():
    usr_inp = str(input())
    playback(usr_inp)

def playback(play):
    print(play.replace(' ', '...'))
main()
