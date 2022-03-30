from pytube import YouTube, streams

url = input(str('Cole aqui o URL para download: '))
video = YouTube(url)
stream = video.streams.get_highest_resolution()

stream.download(output_path=r'C:\Users\pedro\OneDrive\Área de Trabalho')

print("Download realizado com sucesso!")