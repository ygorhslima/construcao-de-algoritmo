import pygame

# Inicializa o mixer
pygame.mixer.init()

# Carrega e reproduz o MP3
pygame.mixer.music.load("musica.mp3")
pygame.mixer.music.play()

# Mantém o programa em execução até o som terminar
while pygame.mixer.music.get_busy():
    pass
