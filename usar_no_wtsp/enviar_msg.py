importar  pywhatkit

# Envie uma mensagem do WhatsApp para um contato às 13h30 
pywhatkit.sendwhatmsg ( "+910123456789" ,  "Olá" ,  13 ,  30 )

# O mesmo que acima, mas fecha a guia em 2 segundos após enviar a mensagem 
pywhatkit . sendwhatmsg ( "+910123456789" ,  "Hi" ,  13 ,  30 ,  15 ,  True ,  2 )

# Envie uma imagem a um grupo com a legenda como Hello 
pywhatkit . sendwhats_image ( "AB123CDEFGHijklmn" ,  "Images / Hello.png" ,  "Hello" )

# Envie uma imagem para um contato sem o 
pywhatkit sem legenda . sendwhats_image ( "+910123456789" ,  "Images / Hello.png" )

# Envie uma mensagem do WhatsApp para um grupo às 12h 
pywhatkit . sendwhatmsg_to_group ( "AB123CDEFGHijklmn" ,  "Olá, todos!" ,  0 ,  0 )

# Reproduza um vídeo no 
pywhatkit do YouTube . playonyt ( "PyWhatKit" )