import subprocess as sp

GREEN="\033[92m"
RESET="\033[0m"

def runCMD():
    while True:
        try:
            command=input('SnakeShell$ ')
            if command.lower()=="exit":
                break
            if command=='ls':
                command='dir'
            if command=='cd':
                command='cd..'
            if command.lower()=='snakeshell -version':
                print(".                                                                                                   \n.                                                                                                   .\n.                                                                                                  .\n                                                ..                                                .\n.                                                --                                                .\n.                                               .=-                                                 \n.                                              :%@@%:                                              .\n.                                              *@@@@*.                                             .\n.                                             :@@@@@@:                                             .\n.                                            .@@@@@@@%                                             .\n.                                            .%@@@@@@#                                              \n.                                             .%@@@@#.                                             .\n.                                              :@@@%:      .......                                 .\n.                                              :%@@@-. .:+#@@@@@@@#-.                               \n.                                              .#@@@@@@@@@@@@@@@@@@@@=.                            .\n.                                   ..:::::...  -%@@@@@@@@@%+==*@@@@@@=                            .\n.                               .:+#@@@@@@@@@@#+-.-*%@@%*-.      +@@@@%                            .\n.                              .#@@@@@@@@@@@@@@@@@@#-.           -@@@@@                            .\n.                            .-@@@@@@@@@@@@@@@@@@@@@@@@#-:... ..-@@@@@#                             \n.                            :#@@@@@@+:.  .:-+#@@@@@@@@@@@@@@@@@@@@@@@-                             \n.                            -@@@@@%.          ..-#@@@@@@@@@@@@@@@@@@:.                            .\n.                            =@@@@@#.         ..:+%@@@@@@@@@@@@@@@#:                               .\n.                            :@@@@@@#:.   .:=*@@@@@@@@@@@@@@@@@=.                                  .\n.                            .+@@@@@@@@@@@@@@@@@@@@@@@%#*#@@@@@@=                                  .\n.                              =@@@@@@@@@@@@@@@@@@*:.      :@@@@@.                                 .\n.                               .=#@@@@@@@@@@#+-.           =@@@@-                                 .\n.                                  ..:----#@@@@@@%#+:.     .%@@@@.                                 .\n.                                      .+@@@@@@@@@@@@@@@@@@@@@@@:                                   \n.                                      =@@@-.   .-+#@@@@@@@@@@+.                                    \n.                                      *@@=         ..::---:..                                     .\n.                                      :@@@..                                                       \n.                                       -%@@#=.                                                     \n.                                        .:*@@@%+.                                                 .\n.                                             :*@@#..                                               \n.                                               .-%%:.                                              \n.                                                 .##.                                              \n.                                                  -%.                                              \n.                                                 .=*.                                              \n.                                                 :#:.                                              \n.                                               .:%.                                                \n.                                              .--                                                  \n.                                                                                                  .\n.                                                                                                   \n")
                print('SnakeShell reporting:\nVersion 1.0\nDev Codingsnail80')
                command=''
            if command.lower()=='snakeshell':
                print('snakeshell use:\n-help gives commands help\n-version get version')
                command=''
            if command.lower()=='snakeshell -help':
                command='help'
            sp.run(command,shell=True)
        except KeyboardInterrupt:
            print('\nuse "exit" to quit')
        except EOFError:
            break


runCMD()